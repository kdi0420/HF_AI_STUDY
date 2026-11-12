---
name: wrap-up
description: 공부 세션을 마무리하고 다음 세션에 인계한다. 유닛 노트·README 진도표를 정리하고, context/STATUS.md와 SESSION-LOG.md를 갱신하고, main에 반영해 푸시한다. 사용자가 "오늘 공부 끝", "정리해줘", "마무리", "오늘 여기까지" 라고 할 때 사용.
---

# 마무리 & 인계

목표: **다음 세션이 아무 설명 없이 이어서 공부할 수 있게** 만든다.

## 1. 공부 기록 정리
1. 이번 세션에서 다룬 유닛을 확인한다 (`git status`, 대화 내용).
2. `units/unitN-*/notes.md`: 진도 표의 완료 체크, 대화에서 나온 내용 중 아직 안 적힌 것 반영.
3. `glossary.md`(새 용어), `questions.md`(새 질문 / 해결된 질문 이동), `quiz.md`(오답)를 확인한다.
4. 유닛이 끝났으면: "한 페이지 요약" 작성, `README.md` 진도표 상태 `완료`, "결과"에 한 줄(인증서·Space 링크·퀴즈 결과).

## 2. 인계 문서
5. `context/STATUS.md`를 덮어쓴다: 마지막 업데이트, 지금 초점(현재 유닛·섹션), 다음 할 일(우선순위 순), 사용자 결정 대기, 최근 세션 3개.
6. `context/SESSION-LOG.md` 맨 위(템플릿 주석 아래)에 항목 추가: 날짜·제목, 브랜치, 한 일, 남은 일.
7. 새로 알게 된 사용자 선호는 `context/USER.md`에, AI 실수 교정은 `AGENTS.md` "교훈"에.

## 3. 커밋 & main 반영
8. 남은 변경을 `study(unitN): <요약>` 등으로 커밋한다.
9. main에 반영한다:
    ```bash
    git fetch origin main
    git merge origin/main          # 충돌 나면 해결하고 커밋
    git push origin HEAD:main
    git push origin HEAD
    ```
    - push가 거절되면 fetch·merge부터 다시. 강제 푸시 금지.
    - 권한 문제로 main 푸시가 막히면 사용자에게 알리고 PR 생성을 제안한다.
10. 사용자에게 3줄 이내로 보고: 오늘 한 것, main 반영 여부, 다음에 이어질 첫 작업.
