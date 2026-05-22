---
name: paper-notes
description: Manage a local paper-reading workspace for VS Code Codex. Use when the user asks Korean paper-work commands such as "새 논문 정리", "논문 정리", "PDF 정리", "새 PDF", "요약해줘", "papers 처리", "업데이트", or "<keyword> 논문 대화"; list unprocessed PDFs in papers/, create Markdown summaries in summary/, infer target papers from keywords, and append follow-up Q&A to existing paper notes.
---

# Paper Notes

Use this skill for a local research-paper workspace with:

- PDF inputs in `papers/`
- Markdown summaries in `summary/`
- Paper overview/index in `summary/INDEX.md`
- Extracted PDF text cache in `extracted_text/`
- Optional template at `templates/paper_summary.md`

Do not create API scripts, servers, or file watchers. Work directly as the Codex agent.

## Encoding Rules

- Treat this skill file, project Markdown files, and YAML metadata files as UTF-8 text.
- When using PowerShell to read Korean text, explicitly specify UTF-8 instead of relying on the shell default encoding.
- Prefer:

```powershell
Get-Content -Raw -Encoding UTF8 .\skills\paper-notes\SKILL.md
```

- If PowerShell output still appears garbled, verify the file through a UTF-8-aware reader such as Node `fs.readFileSync(path, 'utf8')` before assuming the file content is corrupted.
- Do not rewrite Korean text just because one terminal output path displays mojibake; first confirm the actual file bytes/encoding.

## User and Writing Profile

- The user is a Ph.D.-level researcher in AI and robotics.
- Do not oversimplify technical content.
- Write the document body primarily in Korean.
- Preserve English technical terms when they improve precision.
- Base all claims on the PDF content. Mark unknown information as `확인 필요` instead of guessing.
- Keep this `SKILL.md`'s instructional prose in English. Use Korean only for literal command triggers, fixed output labels, required placeholders, or exact phrases that should appear in generated notes.

## PDF Reading Priority

Codex in VS Code should treat PDFs as local files. Do not assume ChatGPT-style server-side PDF reading is available for arbitrary files in `papers/`; Codex normally needs a local extraction route or an explicitly attached file.

Before reading or parsing a PDF, always check whether extracted text already exists.

- The extracted text cache root is `extracted_text/`.
- For each paper, store extracted text under `extracted_text/<stem>/`, where `<stem>` is the PDF filename without `.pdf` and matches the summary filename stem.
- The canonical full-text file is `extracted_text/<stem>/full.txt`.
- If page-range or table-oriented extraction files are useful, store them in the same folder with descriptive names such as `head_pages_1-3.txt`, `tables_pages_5-8.txt`, or `raw_tables_pages_5-8.txt`.
- Do not add `extracted_text/` to `.gitignore`; extracted text is allowed to be committed and pushed.
- If PDF text extraction is performed, commit and push the extracted text files under `extracted_text/<stem>/...` immediately after saving them.
- If `extracted_text/<stem>/full.txt` exists, use it as the primary paper source instead of re-parsing the PDF. Re-open the PDF only when the cached text is incomplete, corrupted, or insufficient for a specific figure/table.
- If extracted text does not exist, parse the PDF and save the extracted text into `extracted_text/<stem>/` before writing or updating the summary.

When cached text is unavailable or insufficient and PDF parsing is needed, try methods in this order:

1. Use installed local PDF CLI tools if available.
   - Prefer `pdftotext -layout` for full-text extraction.
   - On Windows, also check common bundled locations such as `C:\Program Files\Git\mingw64\bin\pdftotext.exe`.
   - Use page ranges first for orientation, e.g. title/abstract/introduction, then extract the full text if needed.
   - Be aware that `pdftotext -layout` preserves page geometry, columns, and tables, but two-column papers may interleave paragraph order or split sentences awkwardly. Use `-layout` as the canonical `full.txt` because it is useful for headings, tables, captions, and page-local structure.
   - If `-layout` output has mixed reading order, also extract `pdftotext -raw` to `extracted_text/<stem>/raw_full.txt` and use it to cross-check abstract/prose order. Do not replace `full.txt` solely because `-raw` reads more smoothly; keep both when both are useful.
   - For orientation, a good default set is `head_pages_1-3.txt` from `-layout`, `full.txt` from `-layout`, and optionally `raw_full.txt` from `-raw` when reading order matters.
2. Use other installed PDF tools only if `pdftotext` is unavailable, such as `mutool`, `qpdf`, or `gswin64c`, when they are already present.
3. Use model/browser-visible PDF content only when the PDF is explicitly attached or otherwise available to the current interface in a readable form.
4. Avoid local Python package workflows by default.
   - Do not assume Python exists.
   - Do not install or rely on Python PDF packages unless the user approves and CLI extraction is unavailable.
5. If no PDF extraction path is available, explain the blocker and ask the user to provide extracted text, install a PDF extraction tool, or attach the PDF in a readable way.

Do not treat extracted text as a temporary artifact. Keep it under `extracted_text/<stem>/` after creating or updating the summary, and report the changed extracted-text paths along with the summary path.

## Incremental Summary Writing

When creating a new summary, make the Markdown file visible early so the user can start reading from the top while work continues.

- After the target PDF is confirmed and before doing long analysis, create `summary/<stem>.md` if it does not exist.
- Start with an empty file or a minimal skeleton using the `Summary Format` headings.
- As soon as the PDF text cache is available, extract the abstract from the paper source and write the sentence-by-sentence English/Korean abstract translation into the skeleton before doing long-form summary analysis.
- Do not wait for the full detailed summary before saving the abstract. The user should be able to read the translated abstract while the rest of the summary is still being prepared.
- Fill the remaining document top-down as information becomes reliable: metadata, table of contents, then detailed summary sections.
- Save useful partial progress rather than waiting until every section is complete.
- If a section is still pending, use a short placeholder such as `작성 중` or `확인 필요`, then replace it before the final report.
- Do not leave the final summary in a partial state unless the user explicitly stops the work or a blocker prevents completion.
- When a paper summary is complete, commit and push the completed `summary/<stem>.md` and updated `summary/INDEX.md` immediately.
- Stage only the completed summary and index files for that commit unless the user explicitly asks to include other changes. Do not include unrelated working-tree changes.

## Papers Index

Maintain an overview file at `summary/INDEX.md` for all PDFs in `papers/`.

Purpose:

- Show which PDFs already have matching summaries.
- Provide a compact status table with topic tags.
- Keep longer three-line summaries in a separate table so the status table stays readable.
- Help choose the next paper and speed up follow-up paper selection.

Recommended structure:

```markdown
# Papers Index

Last updated: YYYY-MM-DD HH:mm

## Paper Status

| # | PDF | Summary | Status | Tags |
|---:|---|---|---|---|
| 1 | [`example.pdf`](../papers/example.pdf) | [`summary/example.md`](example.md) | summarized | `3D reconstruction`, `robotics` |
| 2 | [`new-paper.pdf`](../papers/new-paper.pdf) | 없음 | pending | 요약 후 작성 |

## Summaries

| # | PDF | 3-line summary |
|---:|---|---|
| 1 | [`example.pdf`](../papers/example.pdf) | 1. ...<br>2. ...<br>3. ... |
| 2 | [`new-paper.pdf`](../papers/new-paper.pdf) | 요약 전 |
```

Rules:

- Include every PDF currently in `papers/`.
- Keep the same stable `#` index for a PDF across both tables during each index update.
- Sort PDFs consistently, preferably by filename unless the existing index already uses another clear order.
- The first table is for selection and status: `#`, `PDF`, `Summary`, `Status`, and `Tags`.
- The second table is only for `#`, `PDF`, and `3-line summary`.
- In both tables, the `PDF` cell should be a Markdown link to the file under `papers/`, relative to `summary/INDEX.md`, e.g. [`example.pdf`](../papers/example.pdf).
- When a summary exists, the `Summary` cell should be a Markdown link to `summary/<stem>.md`, relative to `summary/INDEX.md`, e.g. [`summary/example.md`](example.md).
- Percent-encode spaces in link targets when needed, while keeping the displayed filename readable.
- `Status` should be one of `summarized`, `pending`, `in-progress`, or `needs-refresh`.
- `Summary` should point to `summary/<stem>.md` when it exists; otherwise write `없음`.
- Tags must be written only after the paper summary is complete, using the full summary and extracted text as context.
- Do not invent tags from filename or title alone for unsummarized papers. For `pending` papers, write `요약 후 작성`.
- If a summary exists but is too incomplete to support tags, write `확인 필요` and mark the status as `needs-refresh` when appropriate.
- The three-line summary should be exactly three short lines when the paper has been read. If the paper has not been read yet, write `요약 전`.
- Update `summary/INDEX.md` after creating or refreshing a paper summary.
- When listing unprocessed PDFs for `새 논문 정리`, consult or refresh `summary/INDEX.md` so the user sees summary status and topic context together.

## Command: 새 논문 정리

Also treat these as the same command:

- `논문 정리`
- `PDF 정리`
- `새 PDF`
- `요약해줘`
- `papers 처리`
- `업데이트`
- `papers index`
- `index 업데이트`

### Selection Rules

1. List PDF files in `papers/`.
2. For each PDF, compare its stem with `summary/<stem>.md`.
3. Refresh or consult `summary/INDEX.md` so the paper list includes index numbers, summary status, tags for completed summaries, and separate three-line summaries when available.
4. Build a list of PDFs that do not yet have a matching summary file.
5. Show that unprocessed list to the user and ask which file to summarize.
6. Do not automatically summarize every new PDF without asking.
7. If a matching summary already exists, do not overwrite it without checking with the user.
8. If no unprocessed PDF exists, say so and ask whether the user wants to refresh an existing summary.

### Execution Checklist

After the user chooses a PDF, show a short checklist and update it during the work. Include more than file discovery; show reading and writing stages too.

Recommended checklist:

- [ ] Confirm the target PDF
- [ ] Create an empty `summary/<stem>.md` file or summary skeleton
- [ ] Check the extracted-text cache
- [ ] If no cache exists, extract PDF text and save it under `extracted_text/<stem>/`
- [ ] Extract and translate the abstract sentence by sentence
- [ ] Write the translated abstract to the skeleton immediately after PDF parsing/cache loading
- [ ] Check metadata such as title, authors, venue, arXiv, and URL
- [ ] Write metadata to the summary
- [ ] Reconstruct the table of contents from body headings
- [ ] Write the table of contents to the summary
- [ ] Organize the method, equations, and algorithmic flow
- [ ] Check experiment setup, metrics, quantitative results, and ablations
- [ ] Separate contributions, assumptions, limitations, and failure cases
- [ ] Write robotics relevance and deployment implications
- [ ] Complete the detailed `summary/<stem>.md` summary
- [ ] Update `summary/INDEX.md`
- [ ] Commit and push the completed summary and index files
- [ ] Report the changed summary and extracted-text files

Update the checklist in user-facing progress messages as major stages complete.

### Required Summary Rules

When executing `새 논문 정리`, explicitly follow all of these rule sections:

- `PDF Reading Priority`
- `Incremental Summary Writing`
- `Papers Index`
- `Summary Format`
- `Abstract Rules`
- `Table of Contents Rules`
- `Summary Rules`
- `Math Rules`
- `Work Attitude`

Do not treat these as optional background instructions. They are part of the command.

## Command: `<keyword> 논문 대화`

Examples:

- `Pixal3D 논문 대화`
- `pixel aligned 논문 대화`
- `trellis 논문 대화`

Procedure:

1. Treat `<keyword>` as a fuzzy paper selector.
2. Search `papers/` and `summary/INDEX.md` for PDF filenames, titles, tags, and representative terms matching the keyword by prefix, abbreviation, hyphen/space variation, or case-insensitive containment.
3. If one clear PDF matches, select it.
4. If multiple PDFs plausibly match, show 2-5 candidates and ask the user which one they mean.
5. Check for `summary/<stem>.md`.
6. If the summary does not exist, ask whether to summarize it first.
7. If the summary exists, check `extracted_text/<stem>/full.txt` before reading the paper source.
   - If it exists, read the extracted text and the summary, then tell the user you are ready to discuss that paper.
   - If it does not exist, parse the PDF following `PDF Reading Priority`, save the extracted text under `extracted_text/<stem>/`, then read the extracted text and summary.

## Command: `papers index` / `index 업데이트`

Use this command when the user asks to update the paper overview without necessarily summarizing a new paper.

Procedure:

1. List all PDFs in `papers/`.
2. For each PDF, check whether `summary/<stem>.md` exists.
3. Assign a stable numeric index to each PDF and use the same index in both index tables.
4. If a summary exists and is complete, infer tags and the three-line summary from the summary file first, then from extracted text if needed.
5. If a summary exists but is incomplete, mark status as `needs-refresh` or `in-progress`, and write `확인 필요` for tags and three-line summary if needed.
6. If a summary does not exist, mark status as `pending`; write `요약 후 작성` for tags and `요약 전` for the three-line summary.
7. Do not infer tags from filename or title alone for unsummarized papers.
8. Write or update `summary/INDEX.md` following `Papers Index`.
9. Report the changed index path.

## Summary Format

Create Markdown summaries with this structure:

```markdown
# <paper title>

## 메타데이터
## Abstract

## 목차

## 요약

## 추가 질문과 답변
```

In metadata, include PDF filename, title, authors, venue/arXiv, year, DOI/URL, and work timestamp when available. Use `확인 필요` for unknown fields.

## Abstract Rules

Translate the abstract sentence by sentence. Do not summarize it.

Use the original abstract sentences from the PDF as the English source text. Do not paraphrase the English abstract unless the extracted text is corrupted or incomplete, and explicitly mark any such case as `확인 필요`.

Do not insert legal, policy, or assistant-process disclaimers into the generated summary. The summary is a private local research note for the user.

Format each sentence as:

```markdown
Original English sentence.

**Korean translation.**
```

Put one blank line between the original English sentence and the Korean translation. Put another blank line before the next English sentence.

Keep the English sentence plain. Bold only the Korean translation.

Do not skip sentences. Preserve equations, variables, symbols, and important terms inside each sentence.

## Table of Contents Rules

- Extract the full table of contents as accurately as possible.
- Include sections and subsections.
- If the PDF does not contain an explicit table of contents, reconstruct it from body headings and state `본문 heading 기반으로 재구성했으며, section/subsection 누락 여부를 다시 확인했다`.
- After extraction, briefly state that section/subsection omissions were rechecked.

Recommended format:

```markdown
## 목차

> 본문 heading 기반으로 재구성했으며, section/subsection 누락 여부를 다시 확인했다.

1. Introduction
2. Related Work
   1. ...
3. Method
   1. ...
```

## Summary Rules

Write for a Ph.D.-level AI/robotics researcher. Include:

1. Table-of-contents-based structure
2. How sections connect
3. Core claims and evidence
4. Robotics novelty and relevance
5. Comparison table against previous methods or baselines
6. Implementation idea and algorithmic flow
7. Mathematical background when available
8. Experimental setup, metrics, and results
9. Limitations, assumptions, and failure cases
10. Conclusion and future work

Avoid shallow summaries.

Use headings, bullets, and tables where they improve readability, but do not compress the paper so much that the core technical idea disappears.

## Math Rules

Follow the project-wide Markdown math rules in the repository root `AGENTS.md`.

This skill must not duplicate or override those rules. When writing paper summaries, apply the project rules for inline math, block math, LaTeX notation, and code span usage.

## Follow-up Q&A

When the user asks follow-up questions about a summarized paper:

1. Read `summary/<stem>.md`.
2. Check `extracted_text/<stem>/full.txt` before re-opening the source PDF.
3. If extracted text exists, use it as the primary paper source.
4. If extracted text does not exist or is insufficient, parse/re-open the PDF following `PDF Reading Priority` and save any newly extracted text under `extracted_text/<stem>/`.
5. Answer using both sources.
6. Append useful conversation to `## 추가 질문과 답변`.

Append format:

```markdown
### YYYY-MM-DD HH:mm - <short question title>

**질문**

<user question>

**답변**

<answer>
```

Do not rewrite large parts of the summary unless the user asks for revision.

## Work Attitude

- Separate contribution, assumption, limitation, and failure cases.
- Pay special attention to robotics applicability, experiment setup, and real-world deployment implications.
- When comparing methods, explain why each baseline matters, not only which score is higher.
- If the paper's evidence is weak or a claim is under-supported, say so explicitly.
- After creating or editing files, clearly report the changed paths.
