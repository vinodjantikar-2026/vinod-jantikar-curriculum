#!/usr/bin/env python3
"""Read a batch curriculum CSV and report what the batch has completed before a target session.

Usage:
    python3 curriculum_context.py <curriculum.csv> "<Session name>" [--json] [--last N]
    python3 curriculum_context.py <curriculum.csv> --columns      (show the column mapping only)

Columns are mapped by name aliases, so different CSV layouts work. If a needed column
cannot be found, the script prints lines starting with "ASK:" and exits with code 2.
The creator agent must then ask the user which column to use. It must never guess.
"""
import csv, difflib, json, re, sys

ALIASES = {
    "title":      ["session title", "session name", "session_name", "title", "lecture title", "lecture"],
    "topics":     ["topics covered", "topics", "subtopics", "concepts", "topic", "description"],
    "objectives": ["learning objectives", "learning objective", "lo_statement", "los", "objectives", "objective"],
    "module":     ["module", "module name", "module number", "module_name"],
    "week":       ["week", "week number", "week no.", "week no", "week_number"],
    "session":    ["session", "session number", "session no", "session_no", "#"],
    "date":       ["date", "session date"],
    "status":     ["status", "coverage status", "state"],
}
REQUIRED = ["title", "topics"]
DONE_WORDS = {"done", "completed", "complete", "covered", "delivered", "yes", "taught"}


def norm(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def map_columns(header):
    cols = {norm(h): h for h in header}
    found = {}
    for key, names in ALIASES.items():
        for n in names:
            if n in cols:
                found[key] = cols[n]
                break
    return found


def read_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rd = csv.DictReader(f)
        header = [h for h in (rd.fieldnames or []) if h is not None]
        rows = [r for r in rd]
    return header, rows


def find_target(rows, tcol, name):
    want = norm(name)
    titles = [norm(r.get(tcol, "")) for r in rows]
    for i, t in enumerate(titles):
        if t == want:
            return i
    for i, t in enumerate(titles):
        if want and (want in t or (t and t in want)):
            return i
    m = difflib.get_close_matches(want, titles, n=1, cutoff=0.6)
    return titles.index(m[0]) if m else None


def split_items(text):
    return [x.strip() for x in re.split(r"[;\n]", text or "") if x.strip()]


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 1
    path = argv[1]
    as_json = "--json" in argv
    last = 8
    if "--last" in argv:
        last = int(argv[argv.index("--last") + 1])
    header, rows = read_rows(path)
    colmap = map_columns(header)
    if argv[2] == "--columns":
        print(json.dumps({"header": header, "mapping": colmap}, indent=2))
        return 0
    missing = [k for k in REQUIRED if k not in colmap]
    if missing:
        for k in missing:
            print(f"ASK: no column found for '{k}'. Columns present: {header}. Which column holds the {k}?")
        return 2
    target = argv[2]
    idx = find_target(rows, colmap["title"], target)
    if idx is None:
        print(f"ASK: session '{target}' is not in the CSV. Is it a new row, or is it named differently?")
        print("Sessions in the CSV (first 15): " + "; ".join(r[colmap['title']] for r in rows[:15]))
        return 2
    status_col = colmap.get("status")
    before = rows[:idx]
    if status_col and any(norm(r.get(status_col, "")) for r in before):
        completed = [r for r in before if norm(r.get(status_col, "")) in DONE_WORDS]
        basis = f"rows before the target with {status_col} marked done"
    else:
        completed = before
        basis = "all rows before the target, in CSV order"
    nxt = rows[idx + 1] if idx + 1 < len(rows) else None

    def brief(r):
        d = {"title": r.get(colmap["title"], "").strip(), "topics": split_items(r.get(colmap["topics"], ""))}
        for k in ("module", "week", "session", "date"):
            if k in colmap:
                d[k] = (r.get(colmap[k]) or "").strip()
        if "objectives" in colmap:
            d["objectives"] = split_items(r.get(colmap["objectives"], ""))
        return d

    recent = [brief(r) for r in completed[-last:]]
    all_tools = []
    for r in completed:
        for t in split_items(r.get(colmap["topics"], "")):
            if t not in all_tools:
                all_tools.append(t)
    report = {
        "target": brief(rows[idx]),
        "completed_count": len(completed),
        "completed_basis": basis,
        "most_recent_completed": recent,
        "all_completed_topics": all_tools,
        "next_session": brief(nxt) if nxt else None,
        "column_mapping": colmap,
        "notes": ([] if "objectives" in colmap else ["No objectives column found; bridges use topics only."]),
    }
    if as_json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0
    print(f"Target session: {report['target']['title']}")
    print(f"Completed sessions ({basis}): {len(completed)}")
    print("\nMost recent completed:")
    for b in recent:
        print(f"- {b['title']}: " + "; ".join(b["topics"][:8]))
    print("\nAll completed topics (usable for bridges):")
    print("; ".join(all_tools) if all_tools else "(none)")
    if nxt:
        print(f"\nNext session: {report['next_session']['title']}")
    for n in report["notes"]:
        print("NOTE:", n)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
