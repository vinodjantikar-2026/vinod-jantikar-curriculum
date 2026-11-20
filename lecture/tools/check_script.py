#!/usr/bin/env python3
"""Deterministic checker for a lecture script (format v2).

Usage:
    python3 check_script.py <lecture_script.md> [--los "LO 1;LO 2;..."] [--announcements yes|no]
                            [--module "Module name"] [--session "Session name"]

Exit code 0 = no FAIL. Prints one line per finding: FAIL (must fix) or WARN (look at it).
It checks structure, numbers and wording rules only. It cannot judge accuracy; the verifier does that.
"""
import os, re, sys

BANNED = [  # (label, regex, apply_to_code)
    ("synthetic", r"(?i)\bsynthetic\b"),
    ("facilitator", r"(?i)\bfacilitator"),
    ("I Do / We Do / You Do", r"\b(I|We|You) Do\b"),
    ("Recap", r"(?i)\brecap\b"),
    ("Break", r"\bBreak\b"),
    ("Time plan", r"(?i)\btime plan\b"),
    ("[Script:]", r"\[Script:"),
    ("Spine", r"(?i)\bspine\b"),
    ("Exit Ticket", r"(?i)\bexit ticket"),
    ("Appendix", r"(?i)\bappendix\b"),
    ("Connects To", r"(?i)\bconnects to\b"),
    ("Builds on", r"(?i)\bbuilds on\b"),
    ("Format: line", r"(?m)^\**Format:"),
    ("Step N (lecture part)", r"\bSteps? \d\b"),
    ("unfilled placeholder", r"\{\{\s*[A-Za-z_]"),
]
ORDER = ["Agenda", "Scenario", "Problem Statement", "What We Will Use", "How:",
         "Topic 1:", "Topic 2:", "Topic 3:", "Topic 4:", "Closing: Outcome & Summary"]


def is_emoji(ch):
    o = ord(ch)
    if ch == "\U0001F3AF":
        return False
    return (0x1F300 <= o <= 0x1FAFF) or (0x2600 <= o <= 0x27BF) or (0x2B00 <= o <= 0x2BFF) or o == 0xFE0F


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    path = argv[1]
    opt = {}
    i = 2
    while i < len(argv):
        if argv[i].startswith("--") and i + 1 < len(argv):
            opt[argv[i][2:]] = argv[i + 1]
            i += 2
        else:
            i += 1
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    base = os.path.dirname(os.path.abspath(path))
    out = []

    def fail(m): out.append("FAIL " + m)
    def warn(m): out.append("WARN " + m)

    # split prose and code
    prose, blocks, cur, in_code, lang, start = [], [], [], False, "", 0
    for n, ln in enumerate(lines, 1):
        if ln.startswith("```"):
            if not in_code:
                in_code, lang, cur, start = True, ln[3:].strip(), [], n
            else:
                blocks.append((lang, cur, start, n))
                in_code = False
            continue
        if in_code:
            cur.append(ln)
        else:
            prose.append((n, ln))
    if in_code:
        fail(f"unclosed code fence starting at line {start}")

    # headings and order
    heads = [(n, re.sub(r"<[^>]+>", "", ln).lstrip("# ").strip()) for n, ln in prose if re.match(r"^##\s", ln)]
    pos = []
    for key in ORDER:
        hit = [n for n, h in heads if h.startswith(key)]
        if len(hit) != 1:
            fail(f"section '{key}' found {len(hit)} times (need exactly 1)")
            pos.append(None)
        else:
            pos.append(hit[0])
    seq = [p for p in pos if p]
    if seq != sorted(seq):
        fail("sections are out of order: " + ", ".join(ORDER))
    ann = [n for n, h in heads if h.startswith("Announcements")]
    poll = [n for n, ln in prose if re.match(r"^#\s", ln) and "Launch the Feedback Poll" in ln]
    if len(poll) != 1:
        fail("the red H1 'Launch the Feedback Poll' must appear once")
    want = opt.get("announcements", "").lower()
    if want == "yes" and len(ann) != 1:
        fail("Announcements = Yes but the Announcements section is missing")
    if want == "no" and ann:
        fail("Announcements = No but the Announcements section is present")
    if ann and pos[-1] and ann[0] < pos[-1]:
        fail("Announcements must come after the Closing")
    topic_heads = [h for n, h in heads if re.match(r"Topic \d", h)]
    if len(topic_heads) != 4:
        fail(f"need exactly 4 Topic sections, found {len(topic_heads)}")
    for n, h in heads:
        if re.match(r"(Step|Block|Part) \d", h):
            fail(f"line {n}: use 'Topic N', not '{h[:20]}'")

    # agenda
    minutes = []
    for n, ln in prose:
        m = re.match(r"^\|\s*(\d|—)\s*\|(.*)\|\s*(\d+)\s*\|\s*$", ln)
        if m:
            minutes.append(int(m.group(3)))
    if len(minutes) != 5:
        fail(f"Agenda should have 4 topic rows and a Closing row with minutes; found {len(minutes)}")
    elif sum(minutes) != 120:
        fail(f"Agenda minutes add up to {sum(minutes)}, not 120")
    if not any("**120**" in ln for _, ln in prose):
        fail("Agenda needs a Total row with **120**")
    head_min = []
    for n, ln in prose:
        if re.match(r"^##\s.*(Topic \d|Closing: Outcome)", ln):
            m = re.search(r"`(\d+) min`", ln)
            head_min.append(int(m.group(1)) if m else None)
    if len(minutes) == 5 and head_min and head_min != minutes:
        fail(f"heading minutes {head_min} do not match Agenda minutes {minutes}")

    agenda_txt = ""
    if pos[0] and pos[1]:
        agenda_txt = "\n".join(lines[pos[0]:pos[1] - 1])
    if "los" in opt:
        for lo in [x.strip() for x in opt["los"].split(";") if x.strip()]:
            c = agenda_txt.count(lo)
            if c != 1:
                fail(f"LO not verbatim exactly once in the Agenda ({c} times): {lo[:70]}")

    # quizzes
    qpos = [n for n, ln in prose if re.match(r"^###\s.*Quiz \d", ln)]
    if len(qpos) != 4:
        fail(f"need exactly 4 quizzes, found {len(qpos)}")
    for qi, q in enumerate(qpos):
        end = qpos[qi + 1] if qi + 1 < len(qpos) else len(lines)
        seg = "\n".join(lines[q:min(end, q + 40)])
        if not re.search(r"\*\*Question:\*\*", seg): fail(f"Quiz {qi+1}: no **Question:**")
        if len(re.findall(r"^- [A-D]\) ", seg, re.M)) < 4: fail(f"Quiz {qi+1}: needs options A to D")
        if not re.search(r"\*\*Correct Answer:\*\* [A-D]\b", seg): fail(f"Quiz {qi+1}: no **Correct Answer:** letter")
        if len(re.findall(r"^- \*\*[A-D]\)\*\*", seg, re.M)) != 4: fail(f"Quiz {qi+1}: needs 4 explanation lines")
    if len(qpos) == 4 and len(topic_heads) == 4:
        tp = [n for n, h in heads if re.match(r"Topic \d", h)]
        tp.append(pos[-1] or len(lines))
        for k in range(4):
            c = sum(1 for q in qpos if tp[k] < q < tp[k + 1])
            if c != 1:
                fail(f"Topic {k+1} contains {c} quizzes (need 1)")
    for n, ln in prose:
        if re.match(r"^#{3,4}\s.*>(Why|What|How)<", ln):
            fail(f"line {n}: no per-topic Why/What/How headings")

    # banned terms (prose and code), module and emoji
    for n, ln in enumerate(lines, 1):
        for label, rx in BANNED:
            if re.search(rx, ln):
                fail(f"line {n}: banned term '{label}'")
        for ch in ln:
            if is_emoji(ch):
                fail(f"line {n}: emoji {ch!r} (only the target emoji is allowed)")
                break
    if opt.get("module") and opt["module"].lower() in text.lower():
        fail("the Module Name must never be printed")
    if opt.get("session") and opt["session"].lower() not in lines[0].lower():
        warn("title line does not contain the session name")

    # instructor notes: 1-2 lines
    i = 0
    while i < len(lines):
        if "Instructor Note" in lines[i] and lines[i].startswith(">"):
            j = i + 1
            while j < len(lines) and lines[j].startswith(">"):
                j += 1
            if j - i > 2:
                fail(f"line {i+1}: Instructor Note is {j-i} lines (max 2)")
            i = j
        else:
            i += 1

    # code blocks
    n_code = 0
    for lang, body, s, e in blocks:
        if lang in ("python", "sql", "py", "r", "bash"):
            n_code += 1
            if len(body) > 10:
                fail(f"line {s}: {lang} block has {len(body)} lines (max 10)")
            nxt = "\n".join(lines[e:e + 4])
            if "**Output**" not in nxt:
                warn(f"line {s}: {lang} block is not followed by **Output**")
    for n, ln in prose:
        if ln.strip() == "**Output**":
            pass
    for lang, body, s, e in blocks:
        if lang == "mermaid":
            src = "\n".join(body)
            nodes = set(re.findall(r"\b(\w+)\[", src))
            styled = set(re.findall(r"^\s*style (\w+) [^\n]*color:#(?:fff|ffffff)\b", src, re.M | re.I))
            if nodes - styled:
                fail(f"line {s}: Mermaid nodes {sorted(nodes - styled)} need a style line with color:#ffffff (white text)")
    if n_code == 0:
        warn("no code blocks (fine for a no-code session)")
    for n, ln in prose:
        if "Code Explanation" in ln or "Logic Explanation" in ln:
            break
    else:
        if n_code:
            fail("no Code Explanation heading found")

    # images
    for n, ln in prose:
        for m in re.finditer(r'<img\s+[^>]*>', ln):
            tag = m.group(0)
            src = re.search(r'src="([^"]+)"', tag)
            if not src or not os.path.exists(os.path.join(base, src.group(1))):
                fail(f"line {n}: image missing: {src.group(1) if src else tag[:40]}")
            if 'alt="' not in tag: fail(f"line {n}: image has no alt text")
            if 'width="900"' not in tag: fail(f"line {n}: image should use width=\"900\"")
    if re.search(r"!\[", text):
        fail("use <img ... width=\"900\"> instead of markdown images")

    # closing-section pieces
    for needle in ("Outcome", "Summary", "Therefore"):
        if needle not in text:
            fail(f"Closing needs '{needle}'")
    if "30 seconds to respond in chat" not in text:
        warn("no 'Give learners 30 seconds to respond in chat.' prompt found")
    if "Practical value" not in text:
        fail("Summary needs a 'Practical value' row")

    for m in out:
        print(m)
    nf = sum(1 for m in out if m.startswith("FAIL"))
    print(f"\n{'PASS' if nf == 0 else 'FAIL'}: {nf} fail, {len(out) - nf} warn  ({path})")
    return 0 if nf == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
