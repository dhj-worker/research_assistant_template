# Research Assistant Workspace

이 저장소는 AI 에이전트를 연구 조수로 활용해 사용자와 함께 논문을 읽고, 연구 노트를 만들고, 논문 간 관계와 연구 방향을 발전시키는 작업 공간입니다. 특정 AI 에이전트나 편집기 확장을 전제로 하지 않으며, 별도 API 키나 Python 스크립트 없이 로컬 파일과 Markdown을 중심으로 사용할 수 있습니다.

> [!NOTE]
> 이 템플릿의 기본 워크플로와 질문 관점은 robotics 연구 주제에 맞춰져 있습니다.
> 다른 분야나 문제 설정에 맞게 사용하려면 AI 에이전트에게 이 `README.md`와 `skills/` 안의 프로젝트 스킬들을 함께 수정하도록 요청하세요.

## 권장 편집 환경

VS Code로 Markdown 연구 노트를 볼 때는 `Markdown Preview Mermaid Support` 확장 설치를 권장합니다. 연구 지도나 연구 스레드 노트에서 Mermaid 그래프를 사용하면 논문 간 관계와 연구 흐름을 Markdown 안에서 바로 시각화할 수 있습니다.

## 주요 사용 방식

### 논문 정리

새 PDF를 읽고 논문별 연구 노트를 만들 때 사용합니다. 먼저 정리할 PDF를 `papers/` 폴더에 넣은 뒤 연구 조수에게 다음처럼 요청합니다.

```text
새 논문 정리
```

```text
<논문 키워드> 논문 정리
```

`papers/*.pdf`는 git에 올리지 않도록 설정되어 있습니다. 원본 PDF는 repository에 포함되지 않으므로, OneDrive, Google Drive 같은 드라이브 연동 폴더로 관리하는 것을 권장합니다.

논문 정리가 끝나면 연구 조수는 요약, 인덱스, 연구 지도, 논문 카드 등 필요한 산출물을 갱신하고 git에 commit/push합니다.

주요 산출물:

- `summary/<paper>.md`: 논문별 상세 요약과 후속 Q&A
- `summary/INDEX.md`: PDF와 요약 상태 인덱스
- `summary/RESEARCH_MAP.md`: 논문 카드 링크, 전역 관계, 주요 theme, 연구 질문
- `summary/research_cards/<paper>.md`: 논문별 연구 카드
- `extracted_text/<paper>/full.txt`: PDF에서 추출한 텍스트 캐시

### 논문 대화

이미 정리된 논문을 다시 펼쳐 놓고, 특정 개념, 수식, 실험, 한계, robotics 관점 등을 함께 파고들 때 사용합니다.

```text
<논문 키워드> 논문 대화
```

논문 대화는 새 논문 정리 산출물 생성과 분리된 사용 방식입니다. 기존 요약과 추출 텍스트를 참고해 대화를 이어가며, 유용한 후속 Q&A는 필요할 때 해당 요약 파일에 누적합니다.

남을 수 있는 기록:

- `summary/<paper>.md`: 유용한 후속 Q&A가 `추가 질문과 답변` 섹션에 누적될 수 있음
- `extracted_text/<paper>/full.txt`: 대화 중 필요하면 PDF 추출 텍스트 캐시를 생성하거나 보완할 수 있음

### 연구 시작

여러 논문이 어느 정도 쌓인 뒤, 특정 논문, 방법론, 또는 연구 주제를 중심으로 연구 방향을 잡고 싶을 때 사용합니다.

```text
<주제 키워드> 연구 시작
```

연구 시작은 기존 요약, 연구 지도, 논문 카드를 필요한 만큼 읽고 특정 주제 주변의 비교 축, 반복되는 tension, 연구 질문, mini-project 계획을 정리합니다.

주요 산출물:

- `summary/research_threads/<topic>.md`: 특정 논문/주제 기반 연구 진행 노트
- `summary/RESEARCH_MAP.md`: 필요할 때 새 theme, gap, 연구 질문이 갱신될 수 있음

## 폴더 구조

- `AGENTS.md`: AI 에이전트가 연구 조수 역할과 프로젝트 작업 규칙을 찾기 위한 진입점
- `skills/paper-notes/`: 논문 정리와 논문 대화 규칙
- `skills/research-map/`: 논문 카드와 연구 관계 지도 갱신 규칙
- `skills/research-start/`: 특정 논문/주제로 연구 분석을 시작하는 규칙
- `papers/`: 논문 PDF 폴더
- `summary/`: Markdown 요약 파일 폴더
- `summary/research_cards/`: 논문별 연구 카드 폴더
- `summary/research_threads/`: 연구 주제별 진행 노트 폴더
- `extracted_text/`: PDF 추출 텍스트 캐시
- `templates/paper_summary.md`: 새 요약 파일의 기본 형태

세부 동작 규칙은 [skills/paper-notes/SKILL.md](skills/paper-notes/SKILL.md), [skills/research-map/SKILL.md](skills/research-map/SKILL.md), [skills/research-start/SKILL.md](skills/research-start/SKILL.md)에 있습니다. 프로젝트별 커스텀 스킬은 전역 로컬 스킬 폴더가 아니라 이 저장소의 `skills/` 폴더 안에 둡니다.
