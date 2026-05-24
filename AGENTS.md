# Project Instructions for Codex

이 프로젝트는 VS Code Codex extension으로 논문 PDF를 읽고 Markdown 연구 노트를 만드는 작업 공간이다.

논문 정리와 논문 대화 작업의 세부 규칙은 `skills/paper-notes/SKILL.md`를 단일 source of truth로 삼는다.

이 프로젝트의 커스텀 스킬은 전역 로컬 스킬 폴더(`~/.codex/skills`)에 설치하지 않는다. 앞으로 관련 스킬을 만들거나 수정할 때는 반드시 이 저장소의 `skills/` 폴더 안에 둔다.

## 기본 폴더

- 입력 PDF: `papers/`
- 요약 Markdown: `summary/`
- 템플릿: `templates/paper_summary.md`
- 프로젝트 스킬: `skills/paper-notes/`

`papers/`는 로컬 연동 폴더라 git remote repository에 push되지 않는다.

## 프로젝트 Markdown 수식 규칙

이 저장소의 모든 Markdown 파일은 같은 수식 표기 규칙을 따른다.

- Inline 수식, 변수, 짧은 표현은 `$...$`로 감싼다. 예: `$x_t$`, `$T_g$`, `$N$`, `$r=0.1$`
- 수학 변수나 수식에는 code span을 쓰지 않는다. Code span은 파일 경로, 명령어, literal identifier, 코드/텍스트 값에만 사용한다.
- 중요한 식, 여러 줄 유도, aligned expression, inline으로 읽기 어려운 식은 block math로 작성한다.
- Block math는 `$$ ... $$`를 사용하고, 여는 `$$`와 닫는 `$$`는 각각 독립된 줄에 둔다.
- Block math에 `\[ ... \]`는 사용하지 않는다.
- Inline math에 `\( ... \)`는 사용하지 않는다.
- `$`와 `\[`를 섞지 않는다.
- `=`만 단독 줄에 남기지 말고, 필요하면 `aligned`를 사용한다.
- 수식은 Markdown code block 안에 넣지 않는다.
- LaTeX backslash는 한 번만 쓴다.
- 벡터와 행렬은 가능하면 표준 LaTeX 표기, 예를 들어 `\mathbf{x}`와 `\begin{bmatrix} ... \end{bmatrix}`를 사용한다.

## 대화창 수식 표시 규칙

위 Markdown 수식 규칙은 저장소에 저장되는 `.md` 파일에 적용한다. Codex가 사용자와 대화창에서 설명할 때는 렌더링 호환성을 위해 다른 표기를 사용한다.

- 대화창의 inline 수식, 변수, 짧은 표현은 `\(...\)`로 감싼다. 예: `\(x_t\)`, `\(T_g\)`, `\(N\)`, `\(r=0.1\)`
- 대화창의 block math는 `\[ ... \]`를 사용한다.
- 대화창에서는 `$...$`와 `$$ ... $$`를 쓰지 않는다.
- 저장소 Markdown 파일을 만들거나 수정할 때는 여전히 위의 프로젝트 Markdown 수식 규칙을 따른다.

## 작업 규칙

사용자가 다음과 같은 요청을 하면 `paper-notes` 스킬을 사용한다.

- `새 논문 정리`
- `논문 정리`
- `PDF 정리`
- `새 PDF`
- `요약해줘`
- `papers 처리`
- `<keyword> 논문 대화`

스킬이 현재 세션에서 자동 로드되지 않는 경우, 이 저장소의 `skills/paper-notes/SKILL.md`를 직접 읽고 그 절차를 따른다.

사용자가 다음과 같은 요청을 하면 `research-map` 스킬을 사용한다.

- `research-map`
- `리서치맵`
- `연구 지도`
- `연구 흐름`
- `관계 그래프`
- `<keyword> 관계 추적`
- `<keyword> 연구 흐름`
- `논문 카드 추가`
- `누락 카드 추가`

논문 요약이 완료되면 `paper-notes` 스킬은 자동으로 `research-map` 스킬을 이어서 실행하여 `summary/RESEARCH_MAP.md`를 갱신한다.

스킬이 현재 세션에서 자동 로드되지 않는 경우, 이 저장소의 `skills/research-map/SKILL.md`를 직접 읽고 그 절차를 따른다.



파일을 만들거나 수정한 뒤에는 변경한 파일 경로를 사용자에게 알려준다.
