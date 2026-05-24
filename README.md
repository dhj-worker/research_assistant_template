# Paper Notes for Codex

VS Code Codex extension으로 논문 PDF를 읽고 Markdown 요약 파일을 만드는 작업 공간입니다. 별도 API 키나 Python 스크립트는 사용하지 않습니다.

## 사용법

PDF는 `papers/`에 넣고, 요약 결과는 `summary/`에 저장합니다(`papers/`는 로컬 연동 폴더라 git remote repository에 push되지 않습니다).

### 1. 논문 PDF 추가

정리할 논문 PDF를 `papers/` 폴더에 넣습니다.

### 2. 논문 정리 실행

새 논문을 정리하려면 Codex에게 다음처럼 요청합니다.

```text
새 논문 정리
```

특정 논문을 지정할 수도 있습니다.

```text
Pixal3D 논문 정리
```

이미 정리된 논문과 대화하려면:

```text
Pixal3D 논문 대화
```

논문 정리가 끝나면 Codex는 요약 파일과 인덱스를 갱신하고, 연구 관계 지도에 사용할 논문 카드도 함께 갱신합니다.

### 3. 관련 논문이 쌓인 뒤 연구 시작

여러 관련 논문이 정리되면 특정 논문, 방법론, 또는 주제를 중심으로 연구 분석을 시작할 수 있습니다.

```text
TRELLIS 계열 연구 시작
```

```text
simulation-ready 3D asset 관점에서 연구 방향 찾자
```

이때 Codex는 `summary/RESEARCH_MAP.md`와 `summary/research_cards/`를 필요한 만큼만 읽고 갱신한 뒤, 중심 주제 주변의 local subgraph, 비교 축, 반복되는 tension, 연구 질문, mini-project 계획을 정리합니다.

### 4. 만들어지는 결과물

- `summary/<paper>.md`: 논문별 상세 요약과 후속 Q&A
- `summary/INDEX.md`: PDF와 요약 상태 인덱스
- `summary/RESEARCH_MAP.md`: 논문 카드 링크, 전역 관계, 주요 theme, 연구 질문
- `summary/research_cards/<paper>.md`: 논문별 연구 카드
- `summary/research_threads/<topic>.md`: 특정 논문/주제 기반 연구 진행 노트
- `extracted_text/<paper>/full.txt`: PDF에서 추출한 텍스트 캐시

세부 동작 규칙은 [skills/paper-notes/SKILL.md](skills/paper-notes/SKILL.md), [skills/research-map/SKILL.md](skills/research-map/SKILL.md), [skills/research-start/SKILL.md](skills/research-start/SKILL.md)에 있습니다. `AGENTS.md`는 Codex가 이 프로젝트 스킬을 사용하도록 안내하는 얇은 진입점입니다.

커스텀 스킬은 전역 로컬 스킬 폴더에 설치하지 않고, 항상 이 저장소의 `skills/` 폴더 안에 둡니다.

## 폴더 구조

- `AGENTS.md`: Codex가 이 프로젝트에서 어떤 스킬을 써야 하는지 알려주는 진입점
- `skills/paper-notes/`: 논문 정리와 대화 규칙의 단일 원본
- `skills/research-map/`: 논문 카드와 연구 관계 지도 갱신 규칙
- `skills/research-start/`: 특정 논문/주제로 연구 분석을 시작하는 규칙
- `papers/`: 논문 PDF 폴더
- `summary/`: Markdown 요약 파일 폴더
- `summary/research_cards/`: 논문별 연구 카드 폴더
- `summary/research_threads/`: 연구 주제별 진행 노트 폴더
- `extracted_text/`: PDF 추출 텍스트 캐시
- `templates/paper_summary.md`: 새 요약 파일의 기본 형태
