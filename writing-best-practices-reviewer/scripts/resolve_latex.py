#!/usr/bin/env python3
"""Flatten a LaTeX project by recursively resolving \\input{} and \\include{} chains.

Usage:
    resolve_latex.py /path/to/main.tex > /tmp/manuscript-flat.tex

Behaviour:
- Reads the root .tex file.
- Replaces each \\input{X} or \\include{X} with the contents of X.tex (or X if it
  already has a .tex extension), resolved relative to the root file's directory.
- Recurses into included files (depth-bounded to 8 to avoid runaway loops).
- Emits a banner comment marking the start/end of each inlined file so the
  reviewer can cite the original file in findings.
- Preserves line-level fidelity inside each file so line numbers within an
  inlined file still make sense.

Notes:
- Does NOT resolve \\subfile{}, \\import{}, or bibliography commands. These are
  rarer; add them if needed.
- Does NOT execute the LaTeX. The output is concatenated source, not compiled.
- If an included file is missing, prints a warning to stderr and leaves the
  original \\input{...} line untouched in the output (so the reviewer can still
  see the structure).
- Comment lines (starting with %) are preserved — they reveal author TODOs and
  draft alternatives, which are valuable diagnostic signals.

Exit code:
    0 — success (one or more files concatenated)
    1 — root file missing or unreadable
    2 — too-deep recursion (likely an \\input loop)
"""
import argparse
import os
import re
import sys

MAX_DEPTH = 8
INCLUDE_RE = re.compile(r"^(\s*)\\(input|include)\{([^}]+)\}\s*$")


def resolve_file(path: str, depth: int, visited: set, root_dir: str, warnings: list):
    """Yield lines for `path`, recursively expanding \\input/\\include."""
    if depth > MAX_DEPTH:
        warnings.append(f"max depth exceeded at {path}; not expanding further")
        return
    abs_path = os.path.realpath(path)
    if abs_path in visited:
        warnings.append(f"already-visited file skipped: {path} (possible cycle)")
        return
    visited.add(abs_path)

    if not os.path.exists(path):
        warnings.append(f"missing file: {path}")
        return

    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
    except OSError as e:
        warnings.append(f"cannot read {path}: {e}")
        return

    rel_path = os.path.relpath(path, root_dir)
    yield f"%%%%%% BEGIN INLINED FILE: {rel_path}\n"
    for line_num, line in enumerate(lines, start=1):
        m = INCLUDE_RE.match(line.rstrip("\n"))
        if m:
            indent, _cmd, target = m.group(1), m.group(2), m.group(3)
            # Try with and without .tex extension; search relative to current file's dir
            current_dir = os.path.dirname(path)
            candidates = [
                os.path.join(current_dir, target),
                os.path.join(current_dir, target + ".tex"),
                os.path.join(root_dir, target),
                os.path.join(root_dir, target + ".tex"),
            ]
            found = next((c for c in candidates if os.path.exists(c)), None)
            if found:
                yield f"{indent}%% [resolve_latex] inlined from {os.path.relpath(found, root_dir)} (was \\{_cmd}{{{target}}} at {rel_path}:{line_num})\n"
                yield from resolve_file(found, depth + 1, visited, root_dir, warnings)
                yield f"{indent}%% [resolve_latex] end inlined from {os.path.relpath(found, root_dir)}\n"
            else:
                warnings.append(
                    f"could not resolve \\{_cmd}{{{target}}} at {rel_path}:{line_num} "
                    f"(tried: {', '.join(candidates)})"
                )
                yield line  # keep the original line for visibility
        else:
            yield line
    yield f"%%%%%% END INLINED FILE: {rel_path}\n"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("root_tex", help="Path to the root .tex file")
    args = p.parse_args()

    if not os.path.exists(args.root_tex):
        sys.exit(f"Root file not found: {args.root_tex}")

    root_dir = os.path.dirname(os.path.realpath(args.root_tex)) or "."
    visited = set()
    warnings = []

    try:
        for line in resolve_file(args.root_tex, 0, visited, root_dir, warnings):
            sys.stdout.write(line)
    except RecursionError:
        sys.exit(2)

    if warnings:
        sys.stderr.write("\n=== resolve_latex warnings ===\n")
        for w in warnings:
            sys.stderr.write(f"  {w}\n")
        sys.stderr.write(f"  ({len(warnings)} total)\n")


if __name__ == "__main__":
    main()
