# Git·GitHub 기초 (데스크탑에서 레포 쓰기)

- **Git** = 내 컴퓨터에서 파일의 변경 기록을 남기는 프로그램. **GitHub** = 그 기록을 올려 두는 웹사이트(원본 보관소).
- **repository(레포)** = 기록이 붙은 프로젝트 폴더 하나. 이 공부 레포가 `kdi0420/HF_AI_STUDY`.
- **clone** = GitHub 레포를 내 컴퓨터로 처음 통째로 복사 (`git clone 주소`, 한 번만).
- **pull** = GitHub에 새로 올라온 변경을 내 복사본으로 받아오기 (`git pull`, 매번).
- **commit** = "여기까지 저장" 스냅샷 + 메모. **push** = 내 커밋을 GitHub에 올리기.
- **branch** = 원본(`main`)을 건드리지 않고 따로 작업하는 갈래. AI는 `claude/...` 브랜치에서 일하고, 마무리 때 `main`에 합친다(merge).
- 우리 흐름: AI(클라우드)가 commit·push → 데스크탑은 `git pull`로 받아서 실행만. 데스크탑에서 파일을 고치면 충돌이 날 수 있으니, 고칠 게 있으면 AI에게 말하기.
- 공개 레포라 clone·pull은 로그인 없이 됨. push는 로그인 필요.
