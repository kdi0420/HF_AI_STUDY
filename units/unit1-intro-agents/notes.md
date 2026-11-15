# Unit 1 — Introduction to Agents

- 링크: [Unit 1 소개](https://huggingface.co/learn/agents-course/unit1/introduction)
- 목표일: 11/15 · 끝나면 **기초 인증서**
- 이 유닛의 결과물: smolagents로 만든 에이전트 **Alfred**를 HF Space에 올리기 + 최종 퀴즈 통과
- 실습 전 준비: **HF Access Token 발급**(Settings → Access Tokens → Read). 클라우드 세션에선 `request_credential`로 환경 비밀에 저장, 데스크탑에선 `.env`. HF 크레딧이 떨어지면 데스크탑 Ollama(`qwen3.5:9b`)로 교체 — Unit 0 노트 Step 5

## 진도

목차는 코스 원문과 대조함 (2026-11-12). 한국어판: https://huggingface.co/learn/agents-course/ko/unit1/introduction

| # | 섹션 | 끝나면 설명할 수 있어야 하는 것 | 완료 |
|---|---|---|---|
| 1 | [What is an Agent?](https://huggingface.co/learn/agents-course/unit1/what-are-agents) | 에이전트 = 무엇이 무엇을 하는 시스템인가? 챗봇과 뭐가 다른가? | [x] |
| 2 | [Quick Quiz 1](https://huggingface.co/learn/agents-course/unit1/quiz1) | 틀린 문제 → `quiz.md` | [x] |
| 3 | [What are LLMs?](https://huggingface.co/learn/agents-course/unit1/what-are-llms) | LLM이 "다음 토큰 예측기"라는 게 에이전트에 어떤 의미인가? | [ ] |
| 4 | [Messages and Special Tokens](https://huggingface.co/learn/agents-course/unit1/messages-and-special-tokens) | 채팅 메시지(system/user/assistant)가 실제로 모델에 어떻게 들어가나? 채팅 템플릿은 왜 필요한가? | [ ] |
| 5 | [What are Tools?](https://huggingface.co/learn/agents-course/unit1/tools) | 도구는 어떻게 정의하고, LLM은 도구를 어떻게 "아는가"? (system prompt에 도구 설명) | [ ] |
| 6 | [Quick Quiz 2](https://huggingface.co/learn/agents-course/unit1/quiz2) | 틀린 문제 → `quiz.md` | [ ] |
| 7 | [Thought–Action–Observation 사이클](https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure) | 루프가 한 바퀴 도는 과정을 예시로 말할 수 있나? | [ ] |
| 8 | [Thought (ReAct)](https://huggingface.co/learn/agents-course/unit1/thoughts) | ReAct가 뭐고, 왜 "생각하고 행동하기"가 성능을 올리나? | [ ] |
| 9 | [Actions](https://huggingface.co/learn/agents-course/unit1/actions) | JSON 액션 vs 코드 액션(code agent)의 차이와 장단점은? 멈추고 파싱하는 방식은? | [ ] |
| 10 | [Observe](https://huggingface.co/learn/agents-course/unit1/observations) | 도구 실행 결과가 어떻게 다시 모델 입력으로 들어가나? | [ ] |
| 11 | [Dummy Agent Library](https://huggingface.co/learn/agents-course/unit1/dummy-agent-library) | 프레임워크 없이 에이전트 루프를 손으로 짜면 어떤 모양인가? | [ ] |
| 12 | [First Agent with smolagents](https://huggingface.co/learn/agents-course/unit1/tutorial) | `CodeAgent` + 도구 + 모델로 Alfred 만들고 Space에 올리기 | [ ] |
| 13 | [Final Quiz](https://huggingface.co/learn/agents-course/unit1/final-quiz) | 통과 → 기초 인증서 | [ ] |
| 14 | [Conclusion](https://huggingface.co/learn/agents-course/unit1/conclusion) | 유닛 1 한 페이지 요약 쓰기 | [ ] |

## 섹션별 노트

<!-- 각 섹션: "내 말로 정리" 3~5줄 + 예시. 모르는 건 ../../questions.md, 용어는 ../../glossary.md -->

### 0. 소개 (로드맵) — 2026-11-15 읽음

- 유닛 1에서 배우는 것 4덩어리: ① 에이전트란 무엇이고 어떻게 판단하나(추론·계획) ② LLM = 에이전트의 "뇌", 대화는 Messages로 구조화 ③ 도구(Tools)로 바깥 세계에 작용 ④ Think → Act → Observe 루프
- 실습: `smolagents`로 **Alfred** 만들기 → HF Spaces에 공개 → 최종 퀴즈 통과 시 기초 인증서
- 큰 유닛이니 천천히, 여러 번 다시 와서 볼 것 (원문 권고)

### 1. What is an Agent? — 2026-11-15 읽음

- 원문 정의: AI 모델로 **환경과 상호작용**해 **사용자가 정한 목표**를 이루는 시스템. 추론 + 계획 + 행동(주로 도구로) 실행
- 구조: **뇌**(AI 모델, 무엇을 할지 결정) + **몸**(도구·능력, 할 수 있는 행동의 범위를 정함. 날개 없으면 "날기" 불가)
- Agency(행위 능력) 스펙트럼: LLM 출력이 프로그램 흐름을 얼마나 좌우하나 → 단순 처리기 ☆☆☆ → 라우터(분기) ★☆☆ → 도구 호출자 ★★☆ → 멀티스텝(반복 여부까지 결정) ★★★ → 멀티 에이전트(다른 에이전트를 실행) ★★★
- LLM은 **텍스트만** 생성 → ChatGPT가 이미지를 만드는 건 개발자가 붙인 **이미지 생성 도구**를 LLM이 호출하기 때문
- **Action ≠ Tool**: 행동 하나에 도구 여러 개를 쓸 수 있음 (커피 내오기 = 주방 이동 + 커피머신 + 가져오기). 도구 설계가 에이전트 품질을 크게 좌우
- 예시: 개인 비서(Siri 등), 고객센터 챗봇, 게임 NPC
- Q. reasoning과 planning은 뭐가 다른가? → reasoning = 상황을 따져 결론 내기("원두가 없네 → 먼저 사야 함"), planning = 그 결론으로 단계 순서 짜기. 관찰 결과가 예상과 다르면 다시 추론해서 계획을 고침 (2026-11-15)
- 내 말로:

### 2. What are LLMs? — 2026-11-15 읽음

- LLM = 대량의 텍스트로 학습해 사람 말을 이해·생성하는 모델. 대부분 **Transformer**(Attention 기반) 구조
- Transformer 3종: 인코더(BERT, 텍스트 → 의미 벡터, 분류·검색) / **디코더**(Llama, 토큰을 하나씩 생성, 챗봇·코드) / Seq2Seq(T5·BART, 번역·요약). **LLM은 보통 수십억 파라미터의 디코더**
- 핵심 원리: **앞 토큰들이 주어졌을 때 다음 토큰 예측**. 토큰 = 단어보다 작은 조각(`interest` + `ing`). Llama 2 어휘는 약 3.2만 토큰
- **Autoregressive**: 이번 출력이 다음 입력에 붙음 → **EOS 토큰**이 나오면 멈춤. 특수 토큰 모양은 모델마다 다름(`<|im_end|>`, `<|eot_id|>` …)
- 다음 토큰 고르기(디코딩): 점수 최댓값만 고르기(greedy) / beam search(후보 문장 여러 개의 총점 비교)
- Attention: 다음 토큰에 중요한 단어에 집중("The capital of **France** is …"). context length = 한 번에 볼 수 있는 최대 토큰 수
- 프롬프트가 중요: LLM이 하는 일은 입력을 보고 다음 토큰을 고르는 것뿐이라 입력 문구가 출력을 좌우
- 학습: 사전학습(pre-training, 다음 토큰 맞히기로 언어 패턴 습득) → 파인튜닝(대화·도구 사용 등 특정 작업)
- 쓰는 법: 로컬 실행 vs 클라우드/API. 코스는 주로 HF API 사용 (나는 데스크탑 Ollama도 있음)
- 에이전트에서: LLM = **뇌**. 지시 해석, 대화 맥락 유지, 계획, 도구 선택
- 노트북 실습엔 HF 토큰 + **Meta Llama 모델 접근 신청** 필요
- Q. Transformer·인코더·디코더·Seq2Seq가 뭔가? → Transformer = 모든 토큰이 서로를 보고 "누가 중요한지" 가중치를 매기는(Attention) 신경망 설계도. 인코더 = 문장 전체를 앞뒤로 다 보고 의미 벡터로 요약(독해 담당), 디코더 = 앞 토큰만 보고 다음 토큰 생성(이어쓰기 담당), Seq2Seq = 인코더가 입력을 다 읽고 디코더가 그걸 참고해 새 문장 생성(통역사). 큰 디코더는 프롬프트만으로 번역·요약도 해서 LLM은 대부분 디코더 (2026-11-15)
- 내 말로:

### 3. Messages and Special Tokens

-

### 4. What are Tools?

-

### 5. Thought–Action–Observation 사이클

-

### 6. Thought (ReAct)

-

### 7. Actions

-

### 8. Observe

-

### 9. Dummy Agent Library

- 코드: `code/` 에 따라 친 것 저장

### 10. First Agent with smolagents

- 만든 Space 링크:
- 추가한 도구:
- 막혔던 점:

## 유닛 1 한 페이지 요약

<!-- 유닛 끝나고 "에이전트란?"을 친구에게 3분 안에 설명한다고 생각하고 쓴다 -->

-
