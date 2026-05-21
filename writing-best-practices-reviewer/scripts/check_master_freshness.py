#!/usr/bin/env python3
"""Verify a writing-best-practices master is present and fresh.

Two modes:

VENUE MODE (default)
    check_master_freshness.py /path/to/Knowledge/{Venue}/
  Checks that {Venue}/Writing-Best-Practices.md exists, that the venue folder
  holds >= 2 per-paper notes, and that the master is >= the newest per-paper note.

CROSS-VENUE MODE
    check_master_freshness.py --cross-venue /path/to/Knowledge/
  Checks that Knowledge/Writing-Best-Practices-CROSS-VENUE.md exists, that >= 2
  venue folders have per-venue masters, and that the cross-venue master is
  >= the newest per-venue master.

Output: JSON to stdout (see fields below).

Exit code:
    0 — master present, enough sources, and fresh
    1 — master missing
    2 — fewer than 2 source units (per-paper notes / per-venue masters)
    3 — master is stale
"""
import argparse
import datetime as dt
import json
import os
import re
import sys

MASTER_NAME = "Writing-Best-Practices.md"
CROSS_VENUE_NAME = "Writing-Best-Practices-CROSS-VENUE.md"
PER_PAPER_RE = re.compile(r"^Writing-Best-Practices-(.+)\.md$")


def isoformat(epoch):
    return dt.datetime.fromtimestamp(epoch).isoformat() if epoch else None


def is_per_paper(name):
    if name == MASTER_NAME:
        return False
    if name.endswith(".bak.md") or ".bak." in name:
        return False
    return bool(PER_PAPER_RE.match(name))


def check_venue(venue_dir):
    """Venue mode: master + per-paper notes inside one venue folder."""
    master_path = os.path.join(venue_dir, MASTER_NAME)
    master_exists = os.path.isfile(master_path)

    per_paper = []
    for name in os.listdir(venue_dir):
        if is_per_paper(name):
            per_paper.append((name, os.path.getmtime(os.path.join(venue_dir, name))))
    per_paper.sort(key=lambda x: x[1], reverse=True)
    newest_name, newest_mtime = (per_paper[0] if per_paper else (None, None))

    messages, ok = [], True
    if not master_exists:
        ok = False
        messages.append(f"Venue master missing: {master_path}. Run writing-best-practices-comparator (within-venue mode).")
    if len(per_paper) < 2:
        ok = False
        messages.append(f"Only {len(per_paper)} per-paper note(s) in {venue_dir}. Need >= 2.")

    master_mtime = os.path.getmtime(master_path) if master_exists else None
    stale = bool(master_exists and per_paper and master_mtime < newest_mtime)
    if stale:
        ok = False
        messages.append(f"Venue master is older than newest per-paper note ({newest_name}). Re-run the comparator.")

    return {
        "mode": "venue",
        "ok": ok,
        "exists": master_exists,
        "source_count": len(per_paper),
        "source_kind": "per-paper notes",
        "master_mtime": isoformat(master_mtime),
        "newest_source_mtime": isoformat(newest_mtime),
        "newest_source": newest_name,
        "stale": stale,
        "messages": messages,
    }, (1 if not master_exists else 2 if len(per_paper) < 2 else 3 if stale else 0)


def check_cross_venue(knowledge_dir):
    """Cross-venue mode: cross-venue master vs. per-venue masters."""
    cross_path = os.path.join(knowledge_dir, CROSS_VENUE_NAME)
    cross_exists = os.path.isfile(cross_path)

    venue_masters = []
    for entry in sorted(os.listdir(knowledge_dir)):
        sub = os.path.join(knowledge_dir, entry)
        if not os.path.isdir(sub) or entry.startswith("."):
            continue
        vm = os.path.join(sub, MASTER_NAME)
        if os.path.isfile(vm):
            venue_masters.append((entry, os.path.getmtime(vm)))
    venue_masters.sort(key=lambda x: x[1], reverse=True)
    newest_name, newest_mtime = (venue_masters[0] if venue_masters else (None, None))

    messages, ok = [], True
    if not cross_exists:
        ok = False
        messages.append(f"Cross-venue master missing: {cross_path}. Run writing-best-practices-comparator (cross-venue mode).")
    if len(venue_masters) < 2:
        ok = False
        messages.append(f"Only {len(venue_masters)} venue folder(s) have a per-venue master. Need >= 2 for a cross-venue comparison.")

    cross_mtime = os.path.getmtime(cross_path) if cross_exists else None
    stale = bool(cross_exists and venue_masters and cross_mtime < newest_mtime)
    if stale:
        ok = False
        messages.append(f"Cross-venue master is older than the {newest_name} venue master. Re-run the cross-venue comparator.")

    return {
        "mode": "cross-venue",
        "ok": ok,
        "exists": cross_exists,
        "source_count": len(venue_masters),
        "source_kind": "per-venue masters",
        "master_mtime": isoformat(cross_mtime),
        "newest_source_mtime": isoformat(newest_mtime),
        "newest_source": newest_name,
        "stale": stale,
        "messages": messages,
    }, (1 if not cross_exists else 2 if len(venue_masters) < 2 else 3 if stale else 0)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("path", help="Venue folder (venue mode) or Knowledge dir (--cross-venue)")
    p.add_argument("--cross-venue", action="store_true", help="Check the cross-venue master instead of a venue master")
    args = p.parse_args()

    if not os.path.isdir(args.path):
        print(json.dumps({"ok": False, "messages": [f"not a directory: {args.path}"]}))
        sys.exit(1)

    result, code = check_cross_venue(args.path) if args.cross_venue else check_venue(args.path)
    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")
    sys.exit(code)


if __name__ == "__main__":
    main()
