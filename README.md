# Paper Notes for Codex

이 폴더는 VS Code Codex extension에서 논문 PDF를 읽고 Markdown 요약 파일을 만들기 위한 작업 공간입니다. 별도 API 키나 Python 스크립트를 사용하지 않습니다.

## 사용 방법

1. `papers/` 폴더에 논문 PDF를 넣습니다.
2. VS Code Codex에게 짧게 요청합니다.

```text
새 논문 정리
```

3. Codex는 PDF를 읽고 `outputs/<논문 파일명>.md`를 생성합니다.
4. 이후 추가 질문을 하면 Codex가 같은 Markdown 파일의 `## 추가 질문과 답변` 아래에 대화를 이어서 기록합니다.

## 폴더 구조

- `AGENTS.md`: Codex 에이전트가 이 프로젝트에서 따라야 할 작업 지시문
- `guide.txt`: 기존 작업 방식 원문
- `papers/`: 논문 PDF를 넣는 폴더
- `outputs/`: 생성된 Markdown 요약 파일이 저장되는 폴더
- `templates/paper_summary.md`: 새 요약 파일의 기본 형태

## 권장 요청 예시

```text
새 논문 정리
```

```text
PDF 정리
```

```text
요약해줘
```

```text
outputs/<논문명>.md에 이어서, 이 논문의 method를 수식 중심으로 다시 설명해줘.
```

```text
이 논문의 related work와 baseline 비교를 더 촘촘하게 보강해서 md에 추가해줘.
```
