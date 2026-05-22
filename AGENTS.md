# Project Instructions for Codex

이 프로젝트는 VS Code Codex extension으로 논문 PDF를 읽고 Markdown 연구 노트를 만드는 작업 공간이다.

논문 정리와 논문 대화 작업의 세부 규칙은 `skills/paper-notes/SKILL.md`를 단일 source of truth로 삼는다.

이 프로젝트의 커스텀 스킬은 전역 로컬 스킬 폴더(`~/.codex/skills`)에 설치하지 않는다. 앞으로 관련 스킬을 만들거나 수정할 때는 반드시 이 저장소의 `skills/` 폴더 안에 둔다.

## 기본 폴더

- 입력 PDF: `papers/`
- 요약 Markdown: `summary/`
- 템플릿: `templates/paper_summary.md`
- 프로젝트 스킬: `skills/paper-notes/`

PDF 파일은 드라이브로 따로 관리하므로 Git에 포함하지 않는다.

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

파일을 만들거나 수정한 뒤에는 변경한 파일 경로를 사용자에게 알려준다.
