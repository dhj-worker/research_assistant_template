---
name: paper-notes
description: Manage this local paper-reading workspace. Use for Korean commands such as "논문 정리", "새 논문 정리", "<keyword> 논문 정리", "논문 요약", "<keyword> 논문 요약", "논문 업데이트", "<keyword> 논문 공부", "<keyword> 논문 토의", or "<keyword> 논문 대화"; select PDFs from papers/, create summaries in summary/, maintain summary/INDEX.md, and append follow-up Q&A.
---

# Paper Notes

Use this skill for the local workspace:

- PDFs: `papers/`
- Summaries: `summary/`
- Index: `summary/INDEX.md`
- Extracted text cache: `extracted_text/<stem>/full.txt`
- Optional template: `templates/paper_summary.md`

Work directly as Codex. Do not create API scripts, servers, or file watchers.

## Encoding

- Treat this file and project Markdown/YAML files as UTF-8.
- In PowerShell, read Korean text with `Get-Content -Raw -Encoding UTF8 ...`.
- If terminal output is mojibake, verify bytes with a UTF-8-aware reader before rewriting text.

## Writing Profile

- The user is a Ph.D.-level AI/robotics researcher; do not oversimplify.
- Write generated paper notes primarily in Korean, keeping English technical terms when precise.
- Base claims on the paper source. Use `확인 필요` instead of guessing.
- Keep this `SKILL.md`'s prose in English except literal Korean triggers, labels, and required note text.

## Paper Source and Extraction

Always check the extracted-text cache before parsing a PDF.

- Cache path: `extracted_text/<stem>/full.txt`, where `<stem>` matches the PDF and summary stem.
- If cache exists, use it as the primary paper source. Re-open the PDF only when the cache is incomplete, corrupted, or insufficient for a specific figure/table.
- If cache is missing, parse the PDF, save useful outputs under `extracted_text/<stem>/`, then use the cache for summary or Q&A work.
- Keep extracted text as a project artifact; do not add `extracted_text/` to `.gitignore`. Report changed extracted-text paths, and commit/push extracted text immediately after creating it.

Extraction priority:

1. Use installed local CLI tools. Prefer `pdftotext -layout`; also check `C:\Program Files\Git\mingw64\bin\pdftotext.exe` on Windows.
2. For orientation, extract pages 1-3 first when useful; then create canonical `full.txt`.
3. If reading order is poor, also save `raw_full.txt` from `pdftotext -raw` for cross-checking prose. Keep `full.txt` as canonical unless unusable.
4. If `pdftotext` is unavailable, use already-installed alternatives such as `mutool`, `qpdf`, or `gswin64c`.
5. Use browser/model-visible PDF content only when the PDF is explicitly available in the interface.
6. Avoid Python package workflows unless the user approves and CLI extraction is unavailable.
7. If no extraction route exists, explain the blocker and ask for extracted text, a readable attachment, or a PDF extraction tool.

## Index

Maintain `summary/INDEX.md` for every PDF in `papers/`.

Required structure:

- `# Papers Index`
- `Last updated: YYYY-MM-DD HH:mm`
- `## Paper Status`: columns `#`, `PDF`, `Summary`, `Status`, `Tags`
- `## Summaries`: columns `#`, `PDF`, `3-line summary`

Rules:

- Include every PDF and keep the same stable `#` across both tables.
- Sort consistently, preferably by filename unless the existing index clearly uses another order.
- Link PDFs as `../papers/<filename>` and summaries as `<stem>.md`; percent-encode spaces in targets.
- `Status` is one of `summarized`, `pending`, `in-progress`, or `needs-refresh`.
- If no summary exists: `Summary` = `없음`, `Status` = `pending`, `Tags` = `요약 후 작성`, `3-line summary` = `요약 전`.
- Write tags only after reading the paper summary/full text. Do not infer tags from filename/title alone.
- If an existing summary is too incomplete for tags or a three-line summary, use `확인 필요` and mark `needs-refresh` when appropriate.
- When a summary is complete, update `summary/INDEX.md`, then commit and push only the completed summary and index unless the user asks otherwise.

## Command: 논문 정리

Examples:

- `논문 정리`, `새 논문 정리`, `논문 요약`, `새 논문 요약`
- `<keyword> 논문 정리`, `<keyword> 논문 요약`
- `PDF 정리`, `새 PDF`, `정리해줘`, `요약해줘`, `papers 처리`, `논문 업데이트`, `업데이트`

Selection rules:

1. Decide whether the command has a real `<keyword>`.
   - Keyword-less: `논문 정리`, `새 논문 정리`, `논문 요약`, `새 논문 요약`, `PDF 정리`, `새 PDF`, `정리해줘`, `요약해줘`, `papers 처리`.
   - Keyword: `Pixal3D 논문 정리`, `ReconViaGen 논문 요약`, `pixel aligned 논문 정리`.
2. List PDFs in `papers/`, compare each stem with `summary/<stem>.md`, and consult or refresh `summary/INDEX.md`.
3. For keyword-less commands, show unprocessed PDFs with index/status/tag/three-line context and ask which one to summarize. Do not summarize all new PDFs automatically. If none are unprocessed, ask whether to refresh an existing summary.
4. For keyword commands, use `<keyword>` as a fuzzy selector over PDF filenames, index entries, titles, tags, and representative terms. Match by prefix, abbreviation, hyphen/space variation, or case-insensitive containment.
5. If one PDF clearly matches, select it. If several match, show 2-5 candidates and ask. If none match, say so and fall back to the unprocessed list.
6. After a target PDF is selected, check `summary/<stem>.md`. If it exists, ask before overwriting and offer refresh/update. If it does not exist, proceed.

Summary workflow:

1. Show a short progress checklist and update it during major stages.
2. Confirm the target PDF.
3. Create `summary/<stem>.md` early, empty or with the summary skeleton.
4. Load or create `extracted_text/<stem>/full.txt`.
5. Extract the abstract and write sentence-by-sentence English/Korean translation immediately.
6. Fill the summary top-down: metadata, reconstructed table of contents, technical summary, experiments, limitations, robotics relevance.
7. Update `summary/INDEX.md`.
8. Commit and push the completed summary and index. Report changed summary, index, and extracted-text paths.

Do not leave the final summary partial unless the user stops the work or a blocker prevents completion. Use temporary placeholders such as `작성 중` or `확인 필요` only while work is in progress.

## Command: `<keyword> 논문 대화`

Use `<keyword>` as the same fuzzy paper selector described above.

1. Search `papers/` and `summary/INDEX.md`.
2. If one PDF clearly matches, select it; if several match, ask with 2-5 candidates.
3. If `summary/<stem>.md` is missing, ask whether to summarize first.
4. If the summary exists, read it and load `extracted_text/<stem>/full.txt` before re-opening the PDF.
5. If extracted text is missing or insufficient, follow `Paper Source and Extraction`, save the cache, then continue.
6. Tell the user when you are ready to discuss the paper.

## Command: `papers index` / `index 업데이트`

Use when the user wants the overview updated without necessarily summarizing.

1. List all PDFs in `papers/`.
2. Check for matching `summary/<stem>.md`.
3. Use stable numbering across both index tables.
4. For complete summaries, infer tags and three-line summaries from the summary first, then extracted text if needed.
5. For incomplete summaries, use `needs-refresh` or `in-progress` and `확인 필요` where needed.
6. For missing summaries, use the pending placeholders from `Index`.
7. Write `summary/INDEX.md` and report its path.

## Summary Format

Create summaries with this structure:

```markdown
# <paper title>

## 메타데이터

## Abstract

## 목차

## 요약

## 추가 질문과 답변
```

Metadata should include PDF filename, title, authors, venue/arXiv, year, DOI/URL, and work timestamp when available. Use `확인 필요` for unknowns.

## Abstract

- Translate the abstract sentence by sentence; do not summarize it.
- Use original English sentences from the paper. Paraphrase only if extraction is corrupted/incomplete, and mark that as `확인 필요`.
- Format each sentence as:

```markdown
Original English sentence.

**Korean translation.**
```

- Put blank lines between English, Korean, and the next sentence.
- Keep English plain; bold only the Korean translation.
- Preserve equations, variables, symbols, and important terms.
- Do not insert legal, policy, or assistant-process disclaimers.

## Table of Contents

- Extract the full table of contents when present; otherwise reconstruct from body headings.
- Include sections and subsections.
- If reconstructed, include this note: `본문 heading 기반으로 재구성했으며, section/subsection 누락 여부를 다시 확인했다`.
- After extraction/reconstruction, briefly state that omissions were rechecked.

## Summary Content

Write a technical note for a Ph.D.-level AI/robotics reader. Include:

- Section-by-section structure and how sections connect
- Core claims, evidence, contributions, assumptions, limitations, and failure cases
- Robotics novelty, applicability, and deployment implications
- Comparison table against prior methods/baselines, explaining why each baseline matters
- Implementation idea, algorithmic flow, and mathematical background when available
- Experiment setup, metrics, quantitative results, and ablations
- Conclusion and future work
- If evidence is weak or a claim is under-supported, say so explicitly.

Avoid shallow compression; use headings, bullets, and tables when they clarify the paper.

## Math

Follow the project-wide Markdown math rules in root `AGENTS.md`. This skill does not override them.

## Follow-up Q&A

When the user asks about a summarized paper:

1. Read `summary/<stem>.md`.
2. Load `extracted_text/<stem>/full.txt` before re-opening the PDF.
3. If cache is missing/insufficient, extract and save text following `Paper Source and Extraction`.
4. Answer from the summary and paper source.
5. Append useful exchanges to `## 추가 질문과 답변` without rewriting the whole summary unless asked.

Append format:

```markdown
### YYYY-MM-DD HH:mm - <short question title>

**질문**

<user question>

**답변**

<answer>
```
