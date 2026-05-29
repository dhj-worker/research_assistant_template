#!/usr/bin/env python3
r"""Normalize selected LaTeX commands in Markdown files.

With no arguments, this script is intended for a Git pre-commit hook and only
touches staged Markdown files. With path arguments, it rewrites every Markdown
file under those files or directories.

It rewrites patterns that some web Markdown previews handle poorly:

  \mathbb{ABC}  ->  \mathbb ABC
  \mathrm{Frustum}  ->  \mathrm Frustum
  \mathbf{x}  ->  \mathbf x
  \mathcal{L}  ->  \mathcal L
  =
    inside $$...$$ blocks -> {}=
  + x
    inside $$...$$ blocks -> {}+ x

In pre-commit mode, if a staged Markdown file also has unstaged changes, the
script stops instead of accidentally staging unrelated work.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


PATTERNS = (
    (re.compile(r"\\mathbb\{([^{}\r\n]+)\}"), lambda m: f"\\mathbb {m.group(1)}"),
    (re.compile(r"\\mathrm\{([^{}\r\n]+)\}"), lambda m: f"\\mathrm {m.group(1)}"),
    (re.compile(r"\\mathbf\{([^{}\r\n]+)\}"), lambda m: f"\\mathbf {m.group(1)}"),
    (re.compile(r"\\mathcal\{([^{}\r\n]+)\}"), lambda m: f"\\mathcal {m.group(1)}"),
)

DISPLAY_MATH_MARKER = "$$"
STANDALONE_MATH_OPERATOR = re.compile(r"^(\s*)([=-])(\s*)$")
LEADING_PLUS_IN_MATH = re.compile(r"^(\s*)\+")


def git(args: list[str], *, cwd: Path, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    result = subprocess.run(
        ["git", *args],
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and result.returncode != 0:
        sys.stderr.buffer.write(result.stderr)
        raise SystemExit(result.returncode)
    return result


def decode_paths(raw: bytes) -> list[str]:
    if not raw:
        return []
    return [item.decode("utf-8", errors="surrogateescape") for item in raw.split(b"\0") if item]


def staged_markdown_files(repo_root: Path) -> list[str]:
    result = git(
        ["diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z", "--", "*.md"],
        cwd=repo_root,
    )
    return decode_paths(result.stdout)


def has_unstaged_changes(repo_root: Path, path: str) -> bool:
    result = git(["diff", "--quiet", "--", path], cwd=repo_root, check=False)
    return result.returncode == 1


def markdown_files_under(repo_root: Path, paths: list[str]) -> list[str]:
    files: list[str] = []
    for raw_path in paths:
        path = (repo_root / raw_path).resolve()
        if not path.exists():
            sys.stderr.write(f"Skipping missing path: {raw_path}\n")
            continue

        if path.is_file():
            candidates = [path] if path.suffix.lower() == ".md" else []
        else:
            candidates = sorted(item for item in path.rglob("*.md") if item.is_file())

        for candidate in candidates:
            try:
                relative = candidate.relative_to(repo_root)
            except ValueError:
                sys.stderr.write(f"Skipping path outside repository: {candidate}\n")
                continue
            files.append(str(relative).replace("\\", "/"))

    return sorted(dict.fromkeys(files))


def rewrite_text(text: str) -> str:
    lines = text.splitlines(keepends=True)
    rewritten: list[str] = []
    in_fence = False
    in_display_math = False
    fence = ""

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence = marker
            elif marker == fence:
                in_fence = False
                fence = ""
            rewritten.append(line)
            continue

        if stripped.strip() == DISPLAY_MATH_MARKER:
            in_display_math = not in_display_math
            rewritten.append(line)
            continue

        if in_fence:
            rewritten.append(line)
            continue

        updated = line
        if in_display_math and not stripped.startswith("{}"):
            updated = STANDALONE_MATH_OPERATOR.sub(r"\1{}\2\3", updated)
            updated = LEADING_PLUS_IN_MATH.sub(r"\1{}+", updated)

        for pattern, replacement in PATTERNS:
            updated = pattern.sub(replacement, updated)
        rewritten.append(updated)

    return "".join(rewritten)


def rewrite_files(repo_root: Path, files: list[str]) -> list[str]:
    changed: list[str] = []
    for relative_path in files:
        file_path = repo_root / relative_path
        if not file_path.exists():
            continue

        original_bytes = file_path.read_bytes()
        original = original_bytes.decode("utf-8")
        updated = rewrite_text(original)
        if updated != original:
            file_path.write_bytes(updated.encode("utf-8"))
            changed.append(relative_path)

    return changed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize selected LaTeX commands in Markdown files.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Markdown files or directories to rewrite. Omit for pre-commit staged-file mode.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root_result = git(["rev-parse", "--show-toplevel"], cwd=Path.cwd())
    repo_root = Path(root_result.stdout.decode("utf-8", errors="surrogateescape").strip())

    if args.paths:
        files = markdown_files_under(repo_root, args.paths)
        changed = rewrite_files(repo_root, files)
        if changed:
            sys.stderr.write(
                "Normalized Markdown math preview patterns in:\n"
                + "\n".join(f"  {path}" for path in changed)
                + "\n"
            )
        return 0

    files = staged_markdown_files(repo_root)
    if not files:
        return 0

    dirty_files = [path for path in files if has_unstaged_changes(repo_root, path)]
    if dirty_files:
        joined = "\n  ".join(dirty_files)
        sys.stderr.write(
            "pre-commit: staged Markdown files also have unstaged changes.\n"
            "Stage or stash those changes first so the hook does not stage unrelated work:\n"
            f"  {joined}\n"
        )
        return 1

    changed = rewrite_files(repo_root, files)
    if changed:
        git(["add", "--", *changed], cwd=repo_root)
        sys.stderr.write(
            "pre-commit: normalized Markdown math preview patterns in:\n"
            + "\n".join(f"  {path}" for path in changed)
            + "\n"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
