---
name: new-unit
description: Hugging Face Agents Course의 새 유닛(또는 보너스 유닛) 공부 폴더를 만들고 진도표에 등록한다. 사용자가 "유닛2 시작", "다음 유닛", "보너스 유닛 해보자" 라고 할 때 사용.
---

# 새 유닛 시작

1. 슬러그를 정한다: `unitN-주제` 또는 `bonusN-주제` (kebab-case). 예: `unit2-frameworks`, `unit3-agentic-rag`, `bonus1-fine-tuning`.
2. 이미 `units/`에 같은 유닛이 있으면 새로 만들지 않고 이어간다.
3. 폴더를 만든다 — `units/unit1-intro-agents/`와 같은 모양:
   - `notes.md`: 제목, 코스 링크, 목표일, **진도 표**(# · 섹션 · 끝나면 설명할 수 있어야 하는 것 · 완료), 섹션별 노트 칸, 끝에 "한 페이지 요약"
   - `quiz.md`: 오답 노트 표 (퀴즈가 있는 유닛만)
   - `code/requirements.txt`: 실습이 있는 유닛만. 주석에 venv 만드는 법, `HF_TOKEN`은 루트 `.env`에서 읽는다고 적는다.
4. 섹션 목록은 코스 원문(huggingface.co/learn/agents-course/unitN)을 확인해 채운다. 접속이 안 되면 기억 기반으로 채우고 "원문 대조 필요"라고 적는다.
5. `README.md` 진도표에서 해당 유닛 상태를 `진행중`으로, 노트 링크를 채운다. 이전 유닛이 끝났으면 `완료`로.
6. `context/STATUS.md` "지금 초점"·"다음 할 일"을 새 유닛 기준으로 갱신한다.
7. 사용자에게 만든 경로와 첫 섹션을 짧게 알려준다.
