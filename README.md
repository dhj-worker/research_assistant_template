# Paper Notes for Codex

VS Code Codex extension으로 논문 PDF를 읽고 Markdown 요약 파일을 만드는 작업 공간입니다. 별도 API 키나 Python 스크립트는 사용하지 않습니다.

## 사용법

PDF는 `papers/`에 넣고, 요약 결과는 `summary/`에 저장합니다.

새 논문을 정리하려면:

```text
새 논문 정리
```

이미 정리된 논문과 대화하려면:

```text
Pixal3D 논문 대화
```

세부 동작 규칙은 [skills/paper-notes/SKILL.md](skills/paper-notes/SKILL.md)에 있습니다. `AGENTS.md`는 Codex가 이 프로젝트 스킬을 사용하도록 안내하는 얇은 진입점입니다.

커스텀 스킬은 전역 로컬 스킬 폴더에 설치하지 않고, 항상 이 저장소의 `skills/` 폴더 안에 둡니다.

## 폴더 구조

- `AGENTS.md`: Codex가 이 프로젝트에서 어떤 스킬을 써야 하는지 알려주는 진입점
- `skills/paper-notes/`: 논문 정리와 대화 규칙의 단일 원본
- `papers/`: 논문 PDF 폴더
- `summary/`: Markdown 요약 파일 폴더
- `templates/paper_summary.md`: 새 요약 파일의 기본 형태
