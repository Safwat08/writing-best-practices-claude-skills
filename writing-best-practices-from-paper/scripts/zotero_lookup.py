#!/usr/bin/env python3
"""Resolve a Zotero paper reference to a PDF path on disk.

Fallback for when the Zotero MCP is unavailable. Reads ~/Zotero/zotero.sqlite
by copying it to a temp file first (zotero.sqlite is locked when the desktop
app is running).

Usage:
    zotero_lookup.py collection <name>            List items + PDFs in a collection
    zotero_lookup.py item-key <KEY>               Resolve PDF path for an item key
    zotero_lookup.py title <substring>            Search by title substring

Output (TSV): item_key<TAB>title<TAB>pdf_path_or_(no PDF)

Examples:
    zotero_lookup.py collection award_papers
    zotero_lookup.py item-key UP8X6SK3
    zotero_lookup.py title "artificial hivemind"
"""
import argparse
import os
import shutil
import sqlite3
import sys
import tempfile

ZOTERO_DB = os.path.expanduser("~/Zotero/zotero.sqlite")
ZOTERO_STORAGE = os.path.expanduser("~/Zotero/storage")


def open_db():
    if not os.path.exists(ZOTERO_DB):
        sys.exit(f"Zotero DB not found at {ZOTERO_DB}")
    tmp_fd, tmp_path = tempfile.mkstemp(suffix=".sqlite")
    os.close(tmp_fd)
    shutil.copy(ZOTERO_DB, tmp_path)
    return sqlite3.connect(tmp_path)


def pdf_for_item(conn, item_id):
    cur = conn.execute(
        """
        SELECT i.key, ia.path
        FROM itemAttachments ia
        JOIN items i ON i.itemID = ia.itemID
        WHERE ia.parentItemID = ? AND ia.contentType = 'application/pdf'
        """,
        (item_id,),
    )
    row = cur.fetchone()
    if not row:
        return None
    key, path = row
    if path and path.startswith("storage:"):
        filename = path.split(":", 1)[1]
        candidate = os.path.join(ZOTERO_STORAGE, key, filename)
        return candidate if os.path.exists(candidate) else None
    if path and os.path.exists(path):
        return path
    return None


def print_row(item_key, title, pdf):
    title = (title or "").replace("\t", " ").replace("\n", " ").strip()
    print(f"{item_key}\t{title}\t{pdf or '(no PDF)'}")


def cmd_collection(args):
    conn = open_db()
    cur = conn.execute(
        """
        SELECT i.itemID, i.key, idv.value
        FROM collections c
        JOIN collectionItems ci ON ci.collectionID = c.collectionID
        JOIN items i ON i.itemID = ci.itemID
        LEFT JOIN itemData idata ON idata.itemID = i.itemID
            AND idata.fieldID = (SELECT fieldID FROM fields WHERE fieldName='title')
        LEFT JOIN itemDataValues idv ON idv.valueID = idata.valueID
        WHERE LOWER(c.collectionName) = LOWER(?)
        """,
        (args.collection,),
    )
    rows = cur.fetchall()
    if not rows:
        sys.exit(f"No collection named '{args.collection}'")
    for item_id, key, title in rows:
        print_row(key, title, pdf_for_item(conn, item_id))


def cmd_item_key(args):
    conn = open_db()
    cur = conn.execute("SELECT itemID FROM items WHERE key = ?", (args.item_key,))
    row = cur.fetchone()
    if not row:
        sys.exit(f"No item with key {args.item_key}")
    pdf = pdf_for_item(conn, row[0])
    if not pdf:
        sys.exit(f"No PDF attachment for item {args.item_key}")
    print(pdf)


def cmd_title(args):
    conn = open_db()
    cur = conn.execute(
        """
        SELECT i.itemID, i.key, idv.value
        FROM items i
        JOIN itemData idata ON idata.itemID = i.itemID
            AND idata.fieldID = (SELECT fieldID FROM fields WHERE fieldName='title')
        JOIN itemDataValues idv ON idv.valueID = idata.valueID
        WHERE LOWER(idv.value) LIKE LOWER(?)
        """,
        (f"%{args.title}%",),
    )
    rows = cur.fetchall()
    if not rows:
        sys.exit(f"No item title matching '{args.title}'")
    for item_id, key, title in rows:
        print_row(key, title, pdf_for_item(conn, item_id))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    pc = sub.add_parser("collection", help="List items + PDFs in a Zotero collection by name")
    pc.add_argument("collection")
    pc.set_defaults(func=cmd_collection)

    pi = sub.add_parser("item-key", help="Resolve PDF path for a single Zotero item key")
    pi.add_argument("item_key")
    pi.set_defaults(func=cmd_item_key)

    pt = sub.add_parser("title", help="Search items by title substring (case-insensitive)")
    pt.add_argument("title")
    pt.set_defaults(func=cmd_title)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
