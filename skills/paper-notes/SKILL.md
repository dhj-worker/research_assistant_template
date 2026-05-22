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

## PDF Reading Priority

Codex in VS Code should treat PDFs as local files. Do not assume ChatGPT-style server-side PDF reading is available for arbitrary files in `papers/`; Codex normally needs a local extraction route or an explicitly attached file.

Before reading or parsing a PDF, always check whether extracted text already exists.

- The extracted text cache root is `extracted_text/`.
- For each paper, store extracted text under `extracted_text/<stem>/`, where `<stem>` is the PDF filename without `.pdf` and matches the summary filename stem.
- The canonical full-text file is `extracted_text/<stem>/full.txt`.
- If page-range or table-oriented extraction files are useful, store them in the same folder with descriptive names such as `head_pages_1-3.txt`, `tables_pages_5-8.txt`, or `raw_tables_pages_5-8.txt`.
- Do not add `extracted_text/` to `.gitignore`; extracted text is allowed to be committed and pushed.
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
- Fill the document top-down as information becomes reliable: metadata, abstract, table of contents, then detailed summary sections.
- Save useful partial progress rather than waiting until every section is complete.
- If a section is still pending, use a short placeholder such as `작성 중` or `확인 필요`, then replace it before the final report.
- Do not leave the final summary in a partial state unless the user explicitly stops the work or a blocker prevents completion.

## Papers Index

Maintain an overview file at `summary/INDEX.md` for all PDFs in `papers/`.

Purpose:

- Show which PDFs already have matching summaries.
- Provide a fast overview of topic tags and a very short three-line summary.
- Help choose the next paper and speed up follow-up paper selection.

Recommended structure:

```markdown
# Papers Index

Last updated: YYYY-MM-DD HH:mm

| PDF | Summary | Status | Tags | 3-line summary |
|---|---|---|---|---|
| `example.pdf` | `summary/example.md` | summarized | `3D reconstruction`, `robotics` | 1. ...<br>2. ...<br>3. ... |
```

Rules:

- Include every PDF currently in `papers/`.
- `Status` should be one of `summarized`, `pending`, `in-progress`, or `needs-refresh`.
- `Summary` should point to `summary/<stem>.md` when it exists; otherwise write `없음`.
- Tags should be concise topical labels inferred from the title, abstract, and summary when available. If unknown, write `확인 필요`.
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
3. Refresh or consult `summary/INDEX.md` so the paper list includes summary status, tags, and three-line summaries when available.
4. Build a list of PDFs that do not yet have a matching summary file.
5. Show that unprocessed list to the user and ask which file to summarize.
6. Do not automatically summarize every new PDF without asking.
7. If a matching summary already exists, do not overwrite it without checking with the user.
8. If no unprocessed PDF exists, say so and ask whether the user wants to refresh an existing summary.

### Execution Checklist

After the user chooses a PDF, show a short checklist and update it during the work. Include more than file discovery; show reading and writing stages too.

Recommended checklist:

- [ ] 대상 PDF 확정
- [ ] `summary/<stem>.md` 빈 파일 또는 skeleton 생성
- [ ] 추출 텍스트 캐시 확인
- [ ] 캐시가 없으면 PDF 텍스트 추출 및 `extracted_text/<stem>/` 저장
- [ ] title/authors/venue/arXiv/URL 등 메타데이터 확인
- [ ] 메타데이터를 summary에 먼저 기록
- [ ] Abstract 문장 단위 추출 및 번역
- [ ] Abstract를 summary에 기록
- [ ] 본문 heading 기반 목차 재구성
- [ ] 목차를 summary에 기록
- [ ] 방법론, 수식, 알고리즘 흐름 정리
- [ ] 실험 설정, metric, quantitative result, ablation 확인
- [ ] contribution, assumption, limitation, failure case 분리
- [ ] robotics relevance와 deployment implication 작성
- [ ] `summary/<stem>.md` 상세 요약 완성
- [ ] `summary/INDEX.md` 업데이트
- [ ] 변경된 summary 및 extracted text 파일 보고

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
3. If a summary exists, infer tags and the three-line summary from the summary file first, then from extracted text if needed.
4. If a summary does not exist, mark status as `pending`; infer only obvious title-level tags when safe, otherwise use `확인 필요`.
5. Write or update `summary/INDEX.md` following `Papers Index`.
6. Report the changed index path.

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

Format each sentence as:

```markdown
Original English sentence.
**Korean translation.**
```

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

Prioritize VS Code Markdown Preview compatibility.

- Prefer block math over inline math.
- Avoid inline LaTeX such as `\( ... \)` or `$...$` in prose because it may fail to render in VS Code Markdown Preview.
- For simple inline variables or symbols, use code spans, e.g. `x_t`, `T_g`, `N`, `PSNR`.
- If an inline expression is mathematically meaningful, move it to a block equation instead of keeping it inline.
- Block math: use `$$ ... $$`.
- Do not use `\[ ... \]` for block math.
- Do not mix `$` with `\[`.
- Put opening and closing `$$` markers on separate lines.
- Do not leave `=` alone on its own line; use `aligned` when needed.
- Do not put equations inside Markdown code blocks.
- Use one LaTeX backslash, not doubled backslashes.
- Use standard LaTeX notation for vectors and matrices when possible, such as `\mathbf{x}` and `\begin{bmatrix} ... \end{bmatrix}`.

Recommended:

```markdown
본문에서는 `x_t`처럼 code span으로 짧게 언급한다.

$$
\begin{aligned}
\mathbf{c}_{\mathrm{mv}}(\mathbf{x})
&= \frac{1}{N} \sum_{i=1}^{N} \mathbf{c}_i(\mathbf{x})
\end{aligned}
$$
```

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
