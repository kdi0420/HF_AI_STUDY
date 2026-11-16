# 현재 상태

> 세션 간 인계 문서. **매 세션 자동으로 로드된다.** AI는 의미 있는 진행이 있을 때마다 이 파일을 덮어써서 최신으로 유지한다.
> 사용자가 "이어서" / "계속"이라고만 하면 아래 "다음 할 일"의 첫 항목부터 진행한다.

- 마지막 업데이트: 2026-11-16 (smolagents 노트북 데스크탑 7단계까지 실행, 8단계 선택)
- 작업 브랜치: 세션마다 작업 브랜치에서 하고 마무리 때 `main`에 반영. **데스크탑에서 실행할 파일은 만들자마자 main에 반영**(사용자 승인 하에)해야 `git pull`로 받아짐

## 지금 초점

- **Unit 1** 진행 중 (14개 중 11개 완료). Dummy Agent Library 끝: 데스크탑 Jupyter 노트북(`code/dummy_agent_ollama.ipynb`)으로 0~6단계 실습 성공. 6-A(원문의 assistant 이어 쓰기)는 막히고 **6-B(관찰을 user 메시지로)**로 환각 없는 답을 얻음. 7단계 루프는 6-A 방식으로 10바퀴 실패 → **6-B + 친절한 에러 관찰로 고쳐 3바퀴 만에 성공**(London 8°C → Paris 14°C → "Paris가 더 따뜻"). `dummy_agent_ollama` 완전히 끝
- **First Agent with smolagents**: 원문 설명 끝, `code/smolagents_first_agent.ipynb`(0~8단계, Ollama판) 만들어 가짜 서버로 전 칸 검증 → **main 반영**. 데스크탑에서 **0~7단계 실행**(7단계 웹 검색: 에러 2번 → 검색어 줄여 4바퀴 성공, 노트 기록). 6단계 결과는 아직 못 받음. 남은 것: 8단계(Gradio, 선택)
- Unit 0 완료(2026-11-12). 집 데스크탑에 Ollama + `qwen3.5:9b`(100% GPU)

## 다음 할 일

- [ ] **smolagents 노트북 데스크탑 실행** (`code/smolagents_first_agent.ipynb`): 사용자가 4·6·7단계 결과를 붙여 주면 → 노트 10번 "실행 결과" 칸에 기록. 결과가 실패면 원인 같이 보기
  - 데스크탑 안내(2026-11-16 이미 함): 레포 폴더에서 `git checkout -- units\unit1-intro-agents\code\dummy_agent_ollama.ipynb` → `git pull` → `code` 폴더 → venv → `pip install -r requirements.txt`(처음) → `jupyter notebook smolagents_first_agent.ipynb`
  - (선택) HF Space에 올리기: 크레딧이 없어 Space 안 모델은 못 씀 → 하려면 사용자 결정 필요(크레딧 구매 or 생략). 인증서와는 무관
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
- **`dummy_agent_ollama.ipynb`**: 2026-11-16 마지막에 레포 쪽 7단계를 고쳤고, 데스크탑 쪽은 사용자가 같은 코드를 직접 붙여 넣음 → 다음 `git pull`은 이 파일 때문에 막힘. 그때 먼저 `git checkout -- units\unit1-intro-agents\code\dummy_agent_ollama.ipynb`(로컬 실행 결과 버리기, 코드는 레포와 같음) → `git pull`. 앞으로 데스크탑에서 실행한 노트북은 클라우드에서 고치지 말고 새 파일로
- `dummy_agent_loop.ipynb`: 고친 7단계만 따로 떼어 낸 독립 실행판(내용은 노트북 7단계와 같음)
- Jupyter 끄기: `Esc` → `Ctrl + C` 두 번, 안 되면 PowerShell 창을 X로 닫아도 됨

## 최근 세션 (최신 3개, 전체는 SESSION-LOG.md)

- 2026-11-16: Dummy Agent Library 읽기·설명 → 데스크탑 Jupyter 노트북으로 0~6단계 실습 성공(6-A 막힘, 6-B 성공). 7단계 루프 6-A 실패 → 6-B + 친절한 에러 관찰로 고쳐 3바퀴 성공
- 2026-11-15 (3): Thought (ReAct) · Actions · Observe 공부 = TAO 이론 끝. 입문자용 상세 설명 + 데모 2개(`stop_and_parse_demo.py`, `observe_adapt_demo.py`)
- 2026-11-15 (2): Messages and Special Tokens · What are Tools? · Quick Quiz 2(5/5) · Thought–Action–Observation 사이클
