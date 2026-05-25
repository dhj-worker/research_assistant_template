---
name: research-start
description: Start a focused research analysis from this paper-reading workspace. Use for Korean commands such as "연구 시작", "<keyword> 연구 시작", "<keyword>로 연구하자", "연구 방향 찾자", "아이디어 발굴", "연구 질문 만들자", "실험 계획 세우자", or when the user wants to analyze a specific paper/topic using the existing research map; update or consult summary/RESEARCH_MAP.md and summary/research_cards/ as needed, then derive a local subgraph, comparison axes, tensions, research questions, and a concrete mini-project plan. If the first prompt lacks the necessary focus, ask concise clarification questions before proceeding.
---

# Research Start

Use this skill to begin a focused research analysis from the summarized papers, research map, and paper cards in this workspace.

Work directly as the user's research assistant. Do not create API scripts, servers, or file watchers.

## Paths

- Research map: `summary/RESEARCH_MAP.md`
- Paper cards: `summary/research_cards/<summary-stem>.md`
- Paper summaries: `summary/*.md`
- Index: `summary/INDEX.md`
- Research threads: `summary/research_threads/<topic-slug>.md`
- Paper source cache: `extracted_text/<summary-stem>/full.txt`
- Original PDFs: `papers/<paper filename>.pdf`
- Project research-map skill: `skills/research-map/SKILL.md`

Exclude `summary/INDEX.md`, `summary/RESEARCH_MAP.md`, files under `summary/research_cards/`, and files under `summary/research_threads/` from the set of paper summaries.

## Source Priority

This is a local paper-reading workspace. Prefer local sources before any external lookup.

Use sources in this order:

1. `summary/RESEARCH_MAP.md` for already confirmed cross-paper relations.
2. `summary/research_cards/<summary-stem>.md` for compact per-paper facts.
3. `summary/<summary-stem>.md` for detailed local notes and extracted evidence.
4. `extracted_text/<summary-stem>/full.txt` when exact claims, baselines, limitations, equations, or relation evidence need confirmation.
5. `papers/<paper filename>.pdf` only when the text cache is missing, incomplete, or a figure/table must be checked from the original paper.

Do not browse the web for papers that already have local summaries, cards, extracted text, or PDFs unless the user explicitly asks for external checking, the task requires the latest post-summary status such as code/model release availability, or a local source is missing/stale and the gap matters. If external lookup is used, label it as external metadata and keep it secondary to local evidence.

## Writing Profile

- Write primarily in Korean, keeping English technical terms when precise.
- Treat the user as a Ph.D.-level AI/robotics researcher.
- Use `확인 필요` instead of guessing.
- Follow the project Markdown math rules in root `AGENTS.md` when writing files.
- In chat, follow the root `AGENTS.md` conversation math rules.

## Clarify or Proceed

Proceed immediately if the user's first prompt gives enough information to identify:

- A center paper, method, lineage, or topic.
- A research goal, such as survey, gap finding, idea generation, experiment planning, implementation direction, or paper-writing support.
- A perspective or constraint when relevant, such as robotics deployment, simulation-ready assets, 3D reconstruction, generation prior, metric geometry, physical validity, or available code/data.

Ask concise clarification questions when key information is missing and the choice would change the analysis. Ask at most three questions. Prefer these:

1. 중심 논문/주제는 무엇인가?
2. 목표는 survey, 연구 아이디어 발굴, 실험 계획, 구현 방향, 논문 작성 중 무엇인가?
3. 관점은 robotics, representation, reconstruction accuracy, generation prior, physical validity 중 어디에 둘까?

If the user gives only a broad command such as `연구 시작`, first inspect `summary/RESEARCH_MAP.md` and ask the user to choose among likely starting points from available cards/themes.

## Dependency on Research Map

Before deeper analysis, make sure the relevant research-map state is usable:

1. Read `summary/RESEARCH_MAP.md` if it exists.
2. If the center paper/topic has no card or stale/missing links, invoke the project `research-map` skill from `skills/research-map/SKILL.md` to add/update only the needed cards and relations.
3. Do not run a full corpus update unless the user asks for it.
4. Load only the map, target cards, directly related cards, and summaries needed for the current question.

## Research Thread File

For a substantive research-start task, create or update `summary/research_threads/<topic-slug>.md` unless the user explicitly asks for a chat-only analysis.

Use a stable ASCII slug derived from the center paper/topic, for example `trellis-robotics-assets.md` or `vggt-reconviagen.md`. If a matching thread already exists, append a dated section rather than creating a duplicate.

Suggested structure:

```markdown
# <Research Topic>

Last updated: YYYY-MM-DD HH:mm

## Focus

- Center:
- Goal:
- Perspective:
- Scope:

## Local Subgraph

## Comparison Axes

## Claim-Evidence-Limitation Table

| Paper | Claim | Evidence | Limitation | Relevance |
|---|---|---|---|---|

## Repeating Tensions

## Candidate Research Questions

## Candidate Mini-Projects

## Next Actions
```

Keep this file as a working note. Preserve user-written notes and earlier dated analyses.

## Workflow

Follow this order once the focus is clear.

### 1. Define Focus

State the interpreted center, goal, perspective, and scope. If scope is too large, narrow it to a manageable first pass.

Examples:

- Center paper: `ReconViaGen`
- Topic: `simulation-ready image-to-3D assets`
- Goal: `research question generation`
- Perspective: `robotics deployment`

### 2. Update or Consult Research Map

Use `research-map` only as much as needed:

- Add or refresh the center paper card if missing.
- Add or refresh directly related cards if needed.
- Update high-confidence relations required for the current analysis.
- Avoid reading every card unless the user asks for a full corpus pass.

### 3. Extract a Local Subgraph

Build a small subgraph around the center:

- `1-hop`: directly used priors, explicit baselines, successor/predecessor, direct comparison targets.
- `2-hop`: priors or successors of those papers when they affect the current research question.
- `side branch`: same benchmark, representation, or failure mode, but different methodological family.

Represent the subgraph as a concise list or Mermaid graph when useful. Do not over-expand.

### 4. Choose Comparison Axes

Choose only axes relevant to the user's goal. Typical axes:

- Input condition: single-view, multi-view, pose-free, text-conditioned, image-conditioned.
- Representation: mesh, voxel, sparse latent, Gaussian, point map, depth, material/PBR.
- Prior type: reconstruction prior, generation prior, visual feature prior, geometry extraction prior.
- Output validity: visual fidelity, metric accuracy, physical plausibility, simulation readiness.
- Robotics risk: scale, contact, watertightness, material validity, uncertainty, temporal consistency, calibration robustness.

State what is intentionally out of scope for this pass.

### 5. Build Claim-Evidence-Limitation Table

For the selected papers, extract:

- Main claim.
- Evidence actually shown.
- Limitation or unsupported assumption.
- Relevance to the current research goal.

Prefer paper cards first, then summaries. Use extracted text when the summary/card is too thin, when exact evidence matters, or when a relation/limitation should be verified against the paper. Use the original PDF only if the text cache cannot answer the question.

### 6. Identify Repeating Tensions

Look for cross-paper patterns, not isolated limitations:

- visible fidelity vs invisible plausibility
- feed-forward speed vs optimization-level accuracy
- generative completion vs measurement-grounded reconstruction
- visual asset quality vs simulation-ready physical asset
- compact latent vs editability/control
- benchmark generality vs robot deployment reliability

Add only tensions supported by at least two papers or by one paper plus a strong deployment requirement.

### 7. Convert Gaps to Research Questions

Generate 3-5 research questions. Each question should make clear:

- What variable or assumption is being tested.
- Which prior line of work it extends, combines, or challenges.
- What evidence would make the answer convincing.

Avoid vague questions such as "Can we improve performance?" Prefer testable questions.

### 8. Evaluate Candidate Directions

Score or rank each question qualitatively on:

- Novelty
- Feasibility
- Evidence path
- Robotics value
- Risk of being mere engineering integration

Keep the evaluation compact and candid.

### 9. Reduce to Mini-Project

Select the most promising direction and turn it into a small first project:

- Hypothesis
- Minimal method idea
- Required papers/models/data
- Baselines
- Metrics
- Ablations
- Expected failure cases
- First 3 next actions

If no direction is clearly best, present 2-3 candidates and ask the user to choose.

## Output Discipline

- Ground claims in `RESEARCH_MAP.md`, paper cards, summaries, extracted text, or local PDFs, following the local source priority above.
- Separate confirmed relations from hypotheses.
- Do not force all summarized papers into the analysis.
- Do not update paper summaries unless the user asks.
- Do not use web sources as primary evidence for papers that are already present locally.
- When files are created or modified, report changed paths.
