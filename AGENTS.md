# Project Instructions for AI Agents

> [!NOTE]
> This file is intentionally ASCII-only so an AI agent can read the bootstrap instructions before any UTF-8-sensitive project content is loaded. Read all other Markdown (`.md`) and skill files in this repository with UTF-8 encoding.

This project is a research assistant workspace. An AI agent should act as the user's research assistant: read research paper PDFs, create Markdown research notes, maintain cross-paper maps, and help start research analysis from accumulated notes.

Keep `AGENTS.md` as a thin bootstrap file. Do not duplicate Korean command triggers or detailed workflows here; those belong in the project skill files listed below.

## Skill Sources of Truth

- Paper summarization and paper discussion workflows: `skills/paper-notes/SKILL.md`
- Cross-paper relationship maps and research-flow notes: `skills/research-map/SKILL.md`
- Starting research analysis from a specific paper or topic: `skills/research-start/SKILL.md`

If a relevant skill is not automatically loaded in the current session, read the corresponding `SKILL.md` file directly with UTF-8 encoding and follow its procedure.

After a paper summary is completed, the paper-notes workflow should continue with the research-map workflow so `summary/RESEARCH_MAP.md` and the relevant paper card stay up to date.

## Default Folders

- Input PDFs: `papers/`
- Summary Markdown files: `summary/`
- Research map: `summary/RESEARCH_MAP.md`
- Paper cards: `summary/research_cards/`
- Research thread notes: `summary/research_threads/`
- Template: `templates/paper_summary.md`
- Project skills: `skills/paper-notes/`, `skills/research-map/`, `skills/research-start/`

PDF files under `papers/` are local inputs and should not be pushed to the git remote repository.

Do not install this project's custom skills into any global or tool-specific skills directory. When creating or modifying related skills, always keep them inside this repository's `skills/` directory.

## Project Markdown Math Rules

All Markdown files in this repository follow the same math notation rules.

- Wrap inline math, variables, and short expressions with `$...$`. Examples: `$x_t$`, `$T_g$`, `$N$`, `$r=0.1$`
- Do not use code spans for mathematical variables or equations. Use code spans only for file paths, commands, literal identifiers, and code/text values.
- Use block math for important equations, multi-line derivations, aligned expressions, or equations that are hard to read inline.
- Use `$$ ... $$` for block math, with opening `$$` and closing `$$` each on their own line.
- Do not use `\[ ... \]` for block math.
- Do not use `\( ... \)` for inline math.
- Do not mix `$` notation with `\[` notation.
- Do not leave `=` alone on its own line; use `aligned` when needed.
- Do not put equations inside Markdown code blocks.
- Use a single LaTeX backslash.
- Prefer standard LaTeX notation for vectors and matrices, such as `\mathbf{x}` and `\begin{bmatrix} ... \end{bmatrix}`.

## Chat Math Display Rules

The Markdown math rules above apply to `.md` files saved in this repository. When acting as the research assistant in chat, use different notation for rendering compatibility.

- Wrap inline math, variables, and short expressions in chat with `\(...\)`. Examples: `\(x_t\)`, `\(T_g\)`, `\(N\)`, `\(r=0.1\)`
- Use `\[ ... \]` for block math in chat.
- Do not use `$...$` or `$$ ... $$` in chat.
- When creating or editing repository Markdown files, still follow the project Markdown math rules above.

## Reporting

After creating or modifying files, report the changed file paths to the user.
