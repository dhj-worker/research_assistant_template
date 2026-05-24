---
name: research-map
description: Maintain this project's cross-paper research map in summary/RESEARCH_MAP.md and per-paper cards in summary/research_cards/. Use after a paper summary is completed, or for Korean commands such as "research-map", "리서치맵", "연구 지도", "연구 흐름", "관계 그래프", "<keyword> 관계 추적", "<keyword> 연구 흐름", "논문 카드 추가", or "누락 카드 추가"; add paper card files, track relationships between summarized papers, and accumulate themes, gaps, and research questions without forcing a full comparison of every paper.
---

# Research Map

Use this skill for maintaining `summary/RESEARCH_MAP.md` and the per-paper card files under `summary/research_cards/` in this local paper-reading workspace.

Work directly as Codex. Do not create API scripts, servers, or file watchers.

## Paths

- Paper summaries: `summary/*.md`
- Index: `summary/INDEX.md`
- Research map: `summary/RESEARCH_MAP.md`
- Paper cards: `summary/research_cards/<summary-stem>.md`
- Paper source cache when needed: `extracted_text/<stem>/full.txt`

Exclude `summary/INDEX.md` and `summary/RESEARCH_MAP.md` from the set of paper summaries.
Do not treat files under `summary/research_cards/` as paper summaries.

## Writing Profile

- Write primarily in Korean, keeping English technical terms when precise.
- Treat the user as a Ph.D.-level AI/robotics researcher.
- Use `확인 필요` instead of guessing.
- Follow the project Markdown math rules in root `AGENTS.md`.
- Keep `RESEARCH_MAP.md` as a thin index and relation map, not a finished survey.
- Keep detailed per-paper analysis in separate card files so future tasks can load only the relevant cards.

## Map Structure

If `summary/RESEARCH_MAP.md` does not exist, create it with this structure:

```markdown
# Research Map

Last updated: YYYY-MM-DD HH:mm

## Purpose

이 문서는 개별 논문 summary 사이의 관계, 반복되는 문제의식, 연구 흐름, robotics 관점의 gap을 누적 기록한다.

## Paper Cards

| Paper | Summary | Card | Status | Main Themes |
|---|---|---|---|---|

## Relations

| Source | Relation | Target | Confidence | Evidence / Note |
|---|---|---|---|---|

## Themes

### Image-Grounded 3D Reconstruction

### Structured 3D Latents

### Geometry Extraction / Mesh Optimization

### Robotics Deployment Gaps

## Research Questions
```

Preserve existing user-written notes. Update sections in place instead of rewriting the whole file when possible.
In `RESEARCH_MAP.md`, the `## Paper Cards` section should contain only a compact table of links and status metadata. Do not paste full paper cards into `RESEARCH_MAP.md`.

Use `Status` values `up-to-date`, `needs-refresh`, or `missing-card`. Use `Main Themes` as a short comma-separated list, not a full abstract.

## Paper Card Format

Create or update one separate card file per summarized paper at `summary/research_cards/<summary-stem>.md`. Create the `summary/research_cards/` directory if it does not exist.
Use the exact summary stem for the card filename so `summary/<stem>.md` maps to `summary/research_cards/<stem>.md`. Percent-encode spaces only in Markdown link targets when needed; do not percent-encode filesystem paths.

```markdown
# <Paper Title>

## Source

- Summary file: [`<summary filename>`](../<summary filename>)
- PDF: `<pdf filename or 확인 필요>`

## Paper Card

- Core problem: <one concise technical sentence>
- Core method: <main method / architecture / training idea>
- Representation: <latent, mesh, voxel, Gaussian, point/depth, material, etc.>
- Input / output: <input conditions and produced 3D artifacts>
- Claimed improvement: <what limitation this paper claims to improve>
- Main baselines: <methods explicitly compared or discussed>
- Limitations: <paper-stated or evidence-based limitations>
- Robotics relevance: <perception, simulation asset, manipulation, deployment implication>
- Related papers: <links to summaries when already in this workspace; otherwise names>
- Open questions: <research questions raised by this paper>

## Local Relations

| Relation | Target | Confidence | Evidence / Note |
|---|---|---|---|
```

Rules:

- Prefer evidence from the paper summary. Use extracted text only when the summary is too thin or a relationship requires confirmation.
- Do not infer tags or relations from filename alone.
- If a card already exists, update it rather than duplicating it.
- In card files, link local summaries with `../<summary filename>`.
- In `RESEARCH_MAP.md`, link cards with `research_cards/<card filename>`.
- In the global `## Relations` table, prefer linking `Source` and `Target` to card files when the cards exist.
- Keep `## Local Relations` in each card as the target-centered view, and keep `## Relations` in `RESEARCH_MAP.md` as the global table.

## Relation Types

Use a small controlled vocabulary unless the paper clearly needs another phrase:

- `extends`
- `improves`
- `replaces`
- `uses-prior-from`
- `provides-prior-to`
- `addresses-limitation-of`
- `complements`
- `contrasts-with`
- `shares-baseline-with`
- `same-lineage-as`

Use `high`, `medium`, or `low` confidence:

- `high`: explicitly stated in the summary/paper, or direct successor/use relation.
- `medium`: supported by method/baseline overlap, but not explicitly framed as dependency.
- `low`: plausible research-map hint; mark with `확인 필요`.

Keep evidence notes short and grounded. Avoid adding speculative relations as facts.

## After Paper Summary Completion

When called by `paper-notes` after a completed summary:

1. Read the completed `summary/<stem>.md` and `summary/INDEX.md`.
2. Create `summary/RESEARCH_MAP.md` if missing.
3. Create `summary/research_cards/` if missing.
4. Add or update `summary/research_cards/<stem>.md` for this paper.
5. Add or update the compact card link row in `RESEARCH_MAP.md`.
6. Add only high-confidence relations directly supported by the summary, such as explicit prior work, baseline comparisons, successor claims, or methods used as priors.
7. Mirror those target-centered relations in the card's `## Local Relations` table.
8. Add at most 1-3 theme or research-question bullets when the paper clearly introduces a reusable gap.
9. Update `Last updated`.
10. Report both `summary/RESEARCH_MAP.md` and the changed card file.

Do not attempt to compare every summary in the workspace during this automatic update.

## Direct Command: Research Map Update

For commands such as `research-map`, `리서치맵`, `연구 지도`, `연구 흐름`, or `관계 그래프`:

1. Read `summary/INDEX.md` and list summarized papers.
2. Read `summary/RESEARCH_MAP.md` if it exists.
3. If the user gave a `<keyword>`, fuzzy-match it against summary filenames, titles, index rows, tags, and existing card titles.
4. If no keyword was given and multiple reasonable targets exist, ask which paper or whether to add missing cards first.
5. If the user explicitly asks for all missing cards, add card files for every summary missing from `summary/research_cards/` and add their compact link rows to `RESEARCH_MAP.md`.

## Direct Command: `<keyword>` Relation Tracking

For commands such as `<keyword> 관계 추적`, `<keyword> 연구 흐름`, or `<keyword> 관계 그래프`:

1. Select the target paper by fuzzy matching.
2. Read the target summary and its card file if present.
3. Search existing summaries for the target title, method names, baselines, datasets, and named priors using `rg` when useful.
4. Read only the relevant candidate summaries and card files needed to verify relations.
5. Add or update relations involving the target paper.
6. Add missing paper card files for the target and directly related summarized papers if absent.
7. Update themes or research questions only when a new cross-paper pattern is clear.

If several papers match, ask the user to choose 2-5 candidates. If no relation is supported by the summaries, say so and leave a short `확인 필요` note only if it helps future analysis.

## Direct Command: Missing Paper Cards

For commands such as `논문 카드 추가`, `누락 카드 추가`, or `<keyword> 논문 카드 추가`:

1. Compare paper summaries in `summary/*.md` with card files in `summary/research_cards/` and card link rows in `summary/RESEARCH_MAP.md`.
2. If `<keyword>` is present, add or update only that paper's card.
3. If no keyword is present and more than one card is missing, ask which one to add unless the user explicitly asks to add all missing cards.
4. Build each card from the summary first, then consult extracted text only when the summary lacks essential fields.

## Output Discipline

- Keep updates concise and local to the requested paper or missing cards.
- Preserve manual notes and unresolved questions.
- Do not overwrite the map with a generated full survey unless the user explicitly asks for a full rewrite.
- Do not load every card file unless the user explicitly asks for a full corpus pass.
- After modifying files, report changed paths.
