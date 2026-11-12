# 현재 상태

> 세션 간 인계 문서. **매 세션 자동으로 로드된다.** AI는 의미 있는 진행이 있을 때마다 이 파일을 덮어써서 최신으로 유지한다.
> 사용자가 "이어서" / "계속"이라고만 하면 아래 "다음 할 일"의 첫 항목부터 진행한다.

- 마지막 업데이트: 2026-11-12 (Unit 0 진행 중)
- 작업 브랜치: 세션마다 작업 브랜치에서 하고 마무리 때 `main`에 반영

## 지금 초점

- **Unit 0** 마무리 → **Unit 1**, 목표 **11/15** (Todoist 마감은 11/12로 잡혀 있음). Unit 1 끝나면 기초 인증서.
- Unit 0: 계정·Org 팔로우·Discord 완료, Onboarding 페이지 Step 5(Ollama)까지 읽고 노트 정리함.

## 다음 할 일

- [ ] Unit 0 남은 것: HF 토큰 발급(Settings → Access Tokens → Read, Unit 1 실습 전 필수) · 친구와 요일 정하기 · 라이브 1은 앞 15~20분만 훑기(선택)
- [ ] Unit 0 "코스 구조 메모"(인증서 2종 조건·권장 진도·필요 도구) 사용자 답 받아 채우기
- [ ] Unit 1 섹션 순서대로 `units/unit1-intro-agents/notes.md` 채우기 (목차·링크는 원문과 대조 완료)
- [ ] Unit 1 실습: dummy agent → smolagents로 Alfred 만들기 → HF Space 배포 → 최종 퀴즈
- [ ] (선택, Unit 0 완료 조건 아님) Ollama 로컬 실행은 **집 데스크탑**에서 (설치 안내 받음, 진행 중). 사양 확인 → 설치 → `ollama pull qwen2:7b` → `units/unit0-onboarding/code/ollama_check.py` 실행. 결과(OS·사양·성공 여부) 받아서 노트에 기록
- [ ] (환경) 개인 환경 "기본값"에 `huggingface.co`·`router.huggingface.co` 허용됨(2026-11-12, 200 확인). 실습 시작할 때 HF 토큰은 `request_credential`로 환경 비밀(huggingface.co용)에 저장 — 컨테이너가 매번 새로 만들어져서 `.env`는 세션마다 사라짐

## 사용자 결정 대기

- Unit 2~4 목표일(11/22 · 11/29 · 12/6)은 "1주 1유닛" 계산값 → 친구와 확정 필요
- 이 레포를 친구와 공유할지 (공유하면 GitHub collaborator 초대)

## 최근 세션 (최신 3개, 전체는 SESSION-LOG.md)

- 2026-11-12: Unit 0 온보딩 진행 (계정·팔로우·Discord), Ollama(Step 5) 정리
- 2026-11-12: AI_playground에서 HF 공부 폴더 설계 → 이 저장소로 독립
