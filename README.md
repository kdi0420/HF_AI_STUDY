# hf_ai_study

친구와 같이 듣는 [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction)의 **공부 저장소**.
진도·노트·코드·질문을 전부 여기에 남긴다. AI(Claude Code 등)와 같이 공부하는 것을 전제로 설계했다. AI 작업 규칙은 [`AGENTS.md`](AGENTS.md).

> 출신: `kdi0420/AI_playground`의 `experiments/2026-11-12-hf-agents-course/`에서 2026-11-12에 독립 ([결정 기록](docs/decisions/0001-separate-repo.md))

## 목표

- 에이전트의 기본 구조(LLM + 도구 + Thought→Action→Observation 루프)를 **남에게 설명할 수 있을 만큼** 이해한다.
- 코스를 끝내면 직접 쓸 에이전트(리서치 자동화, 교차 검증 등)를 만들 수 있게 된다.
- 1차 목표: **Unit 1 기초 인증서** → 최종 목표: **수료 인증서**(Unit 1 + 활용 과제 1개 + 최종 과제)

## 진행 방식 (친구와 합의, 2026-11-11)

- 유닛 1개 = 1주, 주 3~4시간. 마감은 없지만 Todoist("🤗 개인 › AI 공부") 날짜를 기준으로 삼는다.
- 준비물: Python 기초, HF 계정, Discord(권장)

## 진도표

| 유닛 | 내용 | 목표일 | 상태 | 노트 |
|---|---|---|---|---|
| Unit 0 | 온보딩: 계정·Discord·라이브 1 | 11/15 | 완료 (11/12) | [unit0-onboarding](units/unit0-onboarding/notes.md) |
| Unit 1 | 에이전트 기초 + 첫 에이전트(Alfred) + 퀴즈 → **기초 인증서** | 11/15 | 진행중 | [unit1-intro-agents](units/unit1-intro-agents/notes.md) |
| Unit 2 | 에이전트 프레임워크 (smolagents · LlamaIndex · LangGraph) | 11/22 | 예정 | — |
| Unit 3 | 활용 사례: Agentic RAG | 11/29 | 예정 | — |
| Unit 4 | 최종 과제: GAIA 벤치마크 문제 푸는 에이전트 → **수료 인증서** | 12/6 | 예정 | — |
| Bonus 1 | Function-calling용 LLM 파인튜닝 | 선택 | — | — |
| Bonus 2 | 에이전트 관측성·평가 | 선택 | — | — |
| Bonus 3 | 게임 속 에이전트 (Pokemon) | 선택 | — | — |

> Unit 2~4 목표일은 "1주 1유닛" 규칙으로 계산한 값이다(친구와 확정한 날짜 아님).
> 유닛 구성은 코스 원문과 대조함(2026-11-12). Unit 2는 2.1 smolagents · 2.2 LlamaIndex · 2.3 LangGraph, Unit 4는 GAIA 벤치마크 기반 최종 과제.
> 한국어판도 있다: https://huggingface.co/learn/agents-course/ko/unit1/introduction (영어판보다 늦게 갱신될 수 있음)

## 폴더 구조

```
hf_ai_study/
├── README.md            # 이 파일: 진도표, 결과, 배운 점
├── glossary.md          # 용어집 (유닛 넘나들며 누적)
├── questions.md         # 질문·막힌 점 → 해결되면 답까지 기록 (친구와 공유용)
├── units/
│   ├── unit0-onboarding/notes.md
│   └── unit1-intro-agents/
│       ├── notes.md     # 섹션별 노트
│       ├── quiz.md      # 퀴즈 오답 노트
│       └── code/        # 실습 코드 (의존성은 유닛 폴더 안에만)
├── notes/til/           # 짧은 팁 (YYYY-MM-DD-topic.md)
├── context/             # AI 세션 간 기억: USER · STATUS · SESSION-LOG
├── docs/decisions/      # 구조·방식 결정 기록
└── AGENTS.md, CLAUDE.md # AI 작업 규칙
```

## AI와 같이 공부하는 법

이렇게 말하면 AI가 아래 위치에 기록한다.

| 이렇게 말하면 | AI가 하는 일 | 기록 위치 |
|---|---|---|
| "유닛1 ○○ 섹션 읽었어, 내 이해는 …" | 이해한 내용을 점검·보충하고 정리 | `units/unitN-*/notes.md` 해당 섹션 |
| "○○가 뭐야?" | 설명 + 예시 | 답은 `notes.md`, 용어는 `glossary.md` |
| "이거 모르겠어 / 막혔어" | 같이 풀고, 해결 과정 기록 | `questions.md` |
| "퀴즈 틀렸어: …" | 왜 틀렸는지 설명 | `units/unitN-*/quiz.md` |
| "실습 코드 돌려보자" | 코드 작성·실행 (HF 토큰은 `.env`) | `units/unitN-*/code/` |
| "유닛2 시작하자" | `/new-unit`으로 유닛 폴더 생성, 진도표 갱신 | `units/unit2-*/` |
| "오늘 공부 끝" | `/wrap-up`: 진도표·STATUS 갱신, main 반영 | 이 README, `context/STATUS.md` |

- HF 토큰(`HF_TOKEN`)은 루트 `.env`에만 둔다. 노트북·코드에 붙여넣지 않는다.

## 결과

- (유닛이 끝날 때마다 한 줄씩: 인증서, 만든 Space 링크, 퀴즈 점수 등)
- Unit 0 (2026-11-12): 온보딩 완료. 덤으로 데스크탑에 Ollama + `qwen3.5:9b` 로컬 실행 환경 구축(100% GPU, smolagents 연결 확인)

## 배운 점

-
