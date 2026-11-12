# 현재 상태

> 세션 간 인계 문서. **매 세션 자동으로 로드된다.** AI는 의미 있는 진행이 있을 때마다 이 파일을 덮어써서 최신으로 유지한다.
> 사용자가 "이어서" / "계속"이라고만 하면 아래 "다음 할 일"의 첫 항목부터 진행한다.

- 마지막 업데이트: 2026-11-12
- 작업 브랜치: 세션마다 작업 브랜치에서 하고 마무리 때 `main`에 반영

## 지금 초점

- **Unit 0 + Unit 1**, 목표 **11/15** (Todoist 마감은 11/12로 잡혀 있음). Unit 1 끝나면 기초 인증서.
- 노트 틀만 있고 내용은 아직 비어 있음 → 사용자가 공부하며 같이 채우는 단계.

## 다음 할 일

- [ ] Unit 0 체크리스트: HF 계정 · 코스 등록 · HF 토큰 발급(`.env`의 `HF_TOKEN`) · Discord · 라이브 1 → `units/unit0-onboarding/notes.md`
- [ ] Unit 1 섹션 순서대로 `units/unit1-intro-agents/notes.md` 채우기 (목차·링크는 원문과 대조 완료)
- [ ] Unit 1 실습: dummy agent → smolagents로 Alfred 만들기 → HF Space 배포 → 최종 퀴즈
- [ ] (환경) 2026-11-12에 개인 환경 "기본값"에 `huggingface.co`·`router.huggingface.co` 허용함(접속 200 확인). 실습 시작할 때 HF 토큰은 `request_credential`로 환경 비밀(huggingface.co용)에 저장 — 컨테이너가 매번 새로 만들어져서 `.env`는 세션마다 사라짐

## 사용자 결정 대기

- Unit 2~4 목표일(11/22 · 11/29 · 12/6)은 "1주 1유닛" 계산값 → 현준과 확정 필요
- 이 레포를 현준과 공유할지 (공유하면 GitHub collaborator 초대)

## 최근 세션 (최신 3개, 전체는 SESSION-LOG.md)

- 2026-11-12: AI_playground에서 HF 공부 폴더 설계 → 이 저장소로 독립
