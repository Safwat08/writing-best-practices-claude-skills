#!/usr/bin/env python3
"""Enumerate venue folders under a Knowledge/ directory.

A "venue folder" is any immediate subdirectory of Knowledge/ that contains at
least one per-paper note (Writing-Best-Practices-{Author}-{Year}.md).

Usage:
    list_venues.py /path/to/Knowledge

Output (JSON to stdout):
{
  "knowledge_dir": "...",
  "venues": [
    {
      "name": "NeurIPS",
      "path": ".../Knowledge/NeurIPS",
      "per_paper_count": 11,
      "has_master": true,
      "master_stale": false,
      "master_mtime": "ISO" | null,
      "newest_per_paper_mtime": "ISO" | null
    }, ...
  ],
  "cross_venue_master": {"exists": true|false, "path": "...", "mtime": "ISO"|null}
}

Exit code:
    0 — at least one venue folder found
    1 — Knowledge dir missing, or no venue folders found
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


def iso(epoch):
    return dt.datetime.fromtimestamp(epoch).isoformat() if epoch else None


def is_per_paper(name):
    if name == MASTER_NAME:
        return False
    if name.endswith(".bak.md") or ".bak." in name:
        return False
    return bool(PER_PAPER_RE.match(name))


def scan_venue(path):
    per_paper = []
    for name in os.listdir(path):
        if is_per_paper(name):
            per_paper.append(os.path.getmtime(os.path.join(path, name)))
    if not per_paper:
        return None
    master_path = os.path.join(path, MASTER_NAME)
    has_master = os.path.isfile(master_path)
    master_mtime = os.path.getmtime(master_path) if has_master else None
    newest_pp = max(per_paper)
    stale = bool(has_master and master_mtime < newest_pp)
    return {
        "name": os.path.basename(path.rstrip("/")),
        "path": path,
        "per_paper_count": len(per_paper),
        "has_master": has_master,
        "master_stale": stale,
        "master_mtime": iso(master_mtime),
        "newest_per_paper_mtime": iso(newest_pp),
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("knowledge_dir")
    args = p.parse_args()

    kdir = args.knowledge_dir
    if not os.path.isdir(kdir):
        print(json.dumps({"venues": [], "error": f"not a directory: {kdir}"}))
        sys.exit(1)

    venues = []
    for entry in sorted(os.listdir(kdir)):
        sub = os.path.join(kdir, entry)
        if not os.path.isdir(sub) or entry.startswith("."):
            continue
        info = scan_venue(sub)
        if info:
            venues.append(info)

    cross_path = os.path.join(kdir, CROSS_VENUE_NAME)
    cross = {
        "exists": os.path.isfile(cross_path),
        "path": cross_path,
        "mtime": iso(os.path.getmtime(cross_path)) if os.path.isfile(cross_path) else None,
    }

    out = {"knowledge_dir": kdir, "venues": venues, "cross_venue_master": cross}
    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    sys.exit(0 if venues else 1)


if __name__ == "__main__":
    main()
