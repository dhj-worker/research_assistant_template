# Project Instructions for Codex

이 프로젝트는 VS Code Codex extension으로 논문 PDF를 읽고, 사용자의 기존 `guide.txt` 방식에 맞춰 Markdown 연구 노트를 생성하고 이어 쓰기 위한 작업 공간이다.

별도 OpenAI API 호출 스크립트, 서버, 자동 감시 프로세스를 만들지 않는다. Codex 에이전트가 사용자의 요청을 받으면 직접 PDF를 읽고, Markdown 파일을 생성하거나 수정한다.

## 사용자 프로필

- 사용자는 AI 및 robotics 분야의 Ph.D. 수준 연구자다.
- 기술 용어를 과도하게 단순화하지 않는다.
- 답변과 문서 본문은 기본적으로 한국어로 작성하되, technical term은 영어를 적절히 보존한다.

## 폴더 규칙

- 입력 PDF는 `papers/`에 둔다.
- 출력 Markdown은 `outputs/`에 둔다.
- 새 논문 요약 파일 이름은 원칙적으로 PDF 파일명과 같은 stem을 사용한다.
  - 예: `papers/example.pdf` -> `outputs/example.md`
- 기존 md 파일이 있으면 덮어쓰기 전에 내용을 확인한다.
- 후속 질문 답변은 기존 md 파일의 `## 추가 질문과 답변` 아래에 이어서 작성한다.
- `guide.txt`는 기존 규칙의 원문이다. 인코딩이 깨져 보이는 부분이 있어도, 이 `AGENTS.md`의 정규화된 규칙을 우선 적용한다.

## 새 PDF 처리 절차

사용자가 "papers 폴더의 논문을 정리해줘", "새 PDF 요약해줘", "이 논문 abstract/목차/요약 만들어줘"처럼 요청하면 다음 절차를 따른다.

아래와 같은 짧은 요청도 모두 같은 의미로 해석한다.

- `새 논문 정리`
- `논문 정리`
- `PDF 정리`
- `새 PDF`
- `요약해줘`
- `papers 처리`
- `업데이트`

별도 대상이 지정되지 않으면 `papers/`에서 아직 `outputs/`에 같은 stem의 Markdown 파일이 없는 PDF를 우선 처리한다. 새 PDF가 여러 개 있으면 모두 처리한다. 이미 Markdown이 있는 PDF만 있으면, 어떤 파일을 갱신할지 사용자에게 짧게 확인한다.

1. `papers/`에서 대상 PDF를 찾는다.
2. 같은 stem의 `outputs/<stem>.md`가 있는지 확인한다.
3. PDF의 title, abstract, section/subsection 구조, method, experiments, conclusion을 읽는다.
4. 아래 Markdown 구조로 `outputs/<stem>.md`를 생성한다.
5. 파일 생성 후 사용자에게 생성 파일 경로와 간단한 작업 요약을 알려준다.

## Markdown 구조

새 요약 파일은 다음 순서를 지킨다.

```markdown
# <논문 제목>

## 메타데이터

## Abstract

## 목차

## 요약

## 추가 질문과 답변
```

`## 메타데이터`에는 가능한 경우 다음을 적는다.

- PDF 파일
- 논문 제목
- 저자
- venue 또는 arXiv 정보
- 연도
- DOI 또는 URL
- 작업 일시

정보를 PDF에서 확인할 수 없으면 억지로 채우지 말고 `확인 필요`라고 적는다.

## Abstract 작성 규칙

Abstract는 요약하지 않는다. 전체 abstract를 sentence-by-sentence로 번역한다.

각 문장마다 다음 형식을 지킨다.

```markdown
Original English sentence.
**한국어 번역문.**
```

- 원문 영어 문장은 bold 처리하지 않는다.
- 한국어 번역문만 Markdown bold로 작성한다.
- 문장을 생략하지 않는다.
- 한 문장 안의 수식, 변수, 용어는 최대한 보존한다.

## 목차 작성 규칙

- 논문의 full table of contents를 가능한 정확히 추출한다.
- section과 subsection을 포함한다.
- PDF에 명시적 목차가 없으면 본문 heading을 기반으로 추론하고, "본문 heading 기반으로 재구성"이라고 표시한다.
- 추출 후 한 번 더 검토한 결과라는 점을 간단히 명시한다.

권장 형식:

```markdown
## 목차

> 본문 heading 기반으로 재구성했으며, section/subsection 누락 여부를 재검토했다.

1. Introduction
2. Related Work
   1. ...
3. Method
   1. ...
```

## 요약 작성 규칙

요약은 짧게 끝내지 않는다. robotics 및 AI 연구자의 관점에서 기술적으로 깊게 작성한다.

반드시 다음 내용을 포함한다.

1. 목차 기반 전체 구조 설명
2. 각 section이 서로 어떻게 연결되는지
3. 핵심 주장과 그 근거
4. robotics 관점에서 novelty와 relevance
5. previous methods 또는 baselines와의 비교 표
6. implementation idea와 algorithmic flow
7. 가능한 경우 mathematical background
8. experimental setup, metrics, results 분석
9. limitations, assumptions, failure cases
10. conclusion과 future work

표, bullet, 소제목을 적극적으로 사용하되, 논문 내용을 과도하게 압축해서 핵심이 사라지지 않게 한다.

## 수식 작성 규칙

- VS Code Markdown Preview 호환성을 우선한다.
- Inline math는 가능하면 `\( ... \)`를 사용한다.
- Block math는 반드시 `$$ ... $$`를 사용한다.
- Block math에 `\[ ... \]`를 사용하지 않는다.
- `$`와 `\[`를 섞어 쓰지 않는다.
- 수식 블록의 시작과 끝 marker는 각각 별도 줄에 둔다.
- 여러 줄 수식에서 `=`만 단독 줄에 두지 않는다. alignment가 필요하면 `aligned` 환경을 사용한다.
- 코드 블록 안에 수식을 넣지 않는다.
- LaTeX backslash는 하나만 쓴다.
  - 올바름: `\alpha`
  - 틀림: `\\alpha`
- 벡터와 행렬은 가능한 표준 LaTeX 표기를 사용한다.
  - 예: `\mathbf{x}`, `\begin{bmatrix} ... \end{bmatrix}`

권장 block math 형식:

```markdown
$$
\begin{aligned}
\mathbf{c}_{\mathrm{mv}}(\mathbf{x})
&= \frac{1}{N} \sum_{i=1}^{N} \mathbf{c}_i(\mathbf{x})
\end{aligned}
$$
```

## 후속 질문과 답변 기록 규칙

사용자가 이미 요약된 논문에 대해 추가 질문을 하면:

1. 대상 `outputs/<stem>.md` 파일을 연다.
2. 필요하면 원본 PDF도 다시 확인한다.
3. 답변을 생성한다.
4. 같은 md 파일의 `## 추가 질문과 답변` 아래에 다음 형식으로 append한다.

```markdown
### YYYY-MM-DD HH:mm - <짧은 질문 제목>

**질문**

<사용자 질문 원문>

**답변**

<답변 내용>
```

기존 요약 본문을 무단으로 크게 갈아엎지 않는다. 보강이 필요한 경우에는 사용자의 의도에 맞춰 관련 section만 수정하거나, Q&A에 보강 답변으로 추가한다.

## 작업 태도

- PDF 내용에 근거해서 작성한다.
- 확인할 수 없는 정보는 추측하지 않고 `확인 필요`라고 표시한다.
- 논문의 contribution, assumption, limitation을 분리해서 쓴다.
- 특히 robotics 적용 가능성, 실험 세팅, real-world deployment 관점의 의미를 따로 짚는다.
- 파일을 만들거나 수정한 뒤에는 어떤 파일을 만들었는지 명확히 알려준다.
