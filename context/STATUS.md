# 현재 상태

> 세션 간 인계 문서. **매 세션 자동으로 로드된다.** AI는 의미 있는 진행이 있을 때마다 이 파일을 덮어써서 최신으로 유지한다.
> 사용자가 "이어서" / "계속"이라고만 하면 아래 "다음 할 일"의 첫 항목부터 진행한다.

- 마지막 업데이트: 2026-11-16 (Dummy Agent Library 완료, 세션 마무리)
- 작업 브랜치: 세션마다 작업 브랜치에서 하고 마무리 때 `main`에 반영. **데스크탑에서 실행할 파일은 만들자마자 main에 반영**(사용자 승인 하에)해야 `git pull`로 받아짐

## 지금 초점

- **Unit 1** 진행 중 (14개 중 11개 완료). Dummy Agent Library 끝: 데스크탑 Jupyter 노트북(`code/dummy_agent_ollama.ipynb`)으로 0~6단계 실습 성공. 6-A(원문의 assistant 이어 쓰기)는 막히고 **6-B(관찰을 user 메시지로)**로 환각 없는 답을 얻음. 7단계 보너스 루프는 원래 노트북(6-A 방식)으로 돌려서 실패 → 6-B로 고친 `code/dummy_agent_loop.ipynb`는 **다음 섹션 때 같이** 하기로 함(사용자 결정)
- 다음: **First Agent with smolagents**
- Unit 0 완료(2026-11-12). 집 데스크탑에 Ollama + `qwen3.5:9b`(100% GPU)

## 다음 할 일

- [ ] **First Agent with smolagents**: 사용자가 원문을 붙여 주면 → 입문자용으로 처음부터 자세히 설명 → Ollama용 실습 노트북 준비 → **main에 바로 반영** → 데스크탑 실행 안내.
  - 실습 노트북에 **6-B 루프(`dummy_agent_loop.ipynb` 내용)를 먼저 넣어** "손으로 짠 루프 vs smolagents" 비교로 시작 (사용자 요청: "다음에 할 때 이 내용 고친 거 추가로"). 손 루프에서 에러 관찰을 "JSON을 ```json 블록으로 다시 써라"처럼 **고칠 방법을 알려 주는 말**로 바꾸는 것도 같이
  - 모델: `LiteLLMModel(model_id="ollama_chat/qwen3.5:9b")` (Space 대신 데스크탑 로컬 실행, HF 크레딧 0이라 구매 안 함). 이미지 생성 도구(`agents-course/text-to-image`)는 HF 서버를 쓸 수 있어 빼거나 대체(미확인). `load_tool(..., trust_remote_code=True)`는 실행 전 승인표 필요(`docs/ai-workflow.md`)
  - 데스크탑 안내는 **PowerShell 창 열기부터 한 줄씩**(USER.md): `cd $HOME\Documents\HF_AI_STUDY\units\unit1-intro-agents\code` → `.venv\Scripts\Activate.ps1` → `git pull` → (처음이면 `pip install -r requirements.txt`, smolagents 등) → `jupyter notebook 파일이름.ipynb`
- [ ] 그다음 Final Quiz → Conclusion(한 페이지 요약) → README 진도표·결과 갱신
- [ ] 노트의 "내 말로:" 칸 채우기 (What is an Agent? · Messages · Tools · TAO · ReAct · Actions · Observe, 사용자 말로). Dummy Agent는 사용자 복습 말을 이미 기록함
- [ ] (필요할 때만) HF 토큰 발급(Settings → Access Tokens → **Read**): 퀴즈 제출·Space 등 HF 사이트 작업에 필요하면. 데스크탑은 `.env`, 클라우드 세션은 `request_credential`
- [ ] (낮은 우선순위) Meta Llama 접근 신청: What are LLMs? 끝 노트북에만 필요
- [ ] (선택) 라이브 1 앞 15~20분 훑기 · `gemma4:12b`와 비교 · `ollama launch`로 로컬 코딩 에이전트 체험

## 사용자 결정 대기

- Unit 1 목표일 11/15가 지남 → 새 목표일 (Todoist "Unit 1" 할 일 날짜도 같이)

- Unit 2~4 목표일(11/22 · 11/29 · 12/6)은 "1주 1유닛" 계산값 → 친구와 편하게 연락해서 확정 (AI가 챙길 일 아님)
- 이 레포를 친구와 공유할지 (공유하면 GitHub collaborator 초대)

## 데스크탑 메모

- 레포 위치: `문서\HF_AI_STUDY` = `$HOME\Documents\HF_AI_STUDY` (clone 완료). 쓸 때마다 `git pull`. 데스크탑에서는 실행만, 파일 수정은 AI에게. 평소 `main` 브랜치 (한 번 `claude/...` 브랜치로 checkout했을 수 있음 → 그렇다면 `git checkout main`)
- Unit 1 실습 venv: `units\unit1-intro-agents\code\.venv` (2026-11-16 만듦, `notebook` 설치됨. smolagents는 아직 → `pip install -r requirements.txt`)
- Unit 0 실습 venv: `units\unit0-onboarding\code\.venv`
- **`dummy_agent_ollama.ipynb`는 데스크탑에서 실행 결과가 저장돼 로컬 변경이 있음 → 클라우드에서 이 파일을 고치지 말 것**(`git pull` 충돌). 고칠 게 있으면 새 파일로. `git pull`이 이 파일 때문에 막히면 `git checkout -- units\unit1-intro-agents\code\dummy_agent_ollama.ipynb`로 되돌린 뒤 pull
- Jupyter 끄기: `Esc` → `Ctrl + C` 두 번, 안 되면 PowerShell 창을 X로 닫아도 됨

## 최근 세션 (최신 3개, 전체는 SESSION-LOG.md)

- 2026-11-16: Dummy Agent Library 읽기·설명 → 데스크탑 Jupyter 노트북으로 0~6단계 실습 성공(6-A 막힘, 6-B 성공). 7단계 루프는 실패 분석만, 6-B 루프는 다음 섹션 때
- 2026-11-15 (3): Thought (ReAct) · Actions · Observe 공부 = TAO 이론 끝. 입문자용 상세 설명 + 데모 2개(`stop_and_parse_demo.py`, `observe_adapt_demo.py`)
- 2026-11-15 (2): Messages and Special Tokens · What are Tools? · Quick Quiz 2(5/5) · Thought–Action–Observation 사이클
