# Unit 1 실습 환경 안내 (데스크탑)

Dummy Agent Library부터 코드를 **한 칸씩 실행하고 확인**하는 방식(Jupyter 노트북)으로 실습한다. 2026-11-16 작성.

## 어디서 실행하나

| 선택지 | 판단 | 이유 |
|---|---|---|
| **데스크탑 + Jupyter 노트북(브라우저)** | ✅ 추천 | 파이썬이 이미 깔려 있음(Unit 0에서 venv 만들고 실행 성공). `pip` 한 줄만 더 설치하면 됨. Ollama가 같은 PC에 있어서 바로 연결됨 |
| 데스크탑 + VS Code | 괜찮음(나중에) | 같은 노트북 파일을 열 수 있음. 다만 VS Code와 확장 2개(Python, Jupyter)를 새로 깔아야 함 |
| Google Colab | ❌ 이번엔 안 맞음 | Colab은 구글의 컴퓨터라서 **내 데스크탑의 Ollama(`localhost`)에 접속할 수 없음**. 원문처럼 HF 서버를 쓰려면 크레딧이 필요한데 무료 계정은 0 |

- 파이썬을 **새로 깔 필요는 없다.** 아래 1번에서 버전만 확인한다.
- `.py` vs `.ipynb`: `.py`는 위에서 아래까지 **한 번에** 실행되는 대본. `.ipynb`(노트북)는 대본을 **칸으로 잘라서** 한 칸씩 실행하고, 결과가 칸 바로 아래에 남는다. 코스 실습이 노트북인 이유 = 배우면서 중간 결과를 보기 좋아서.

## 처음 한 번만: 준비 (PowerShell)

시작 메뉴에서 **PowerShell**을 연다 (cmd 말고). 한 줄씩 붙여 넣고 Enter.

1. 파이썬 확인: `python --version` → `Python 3.10` 이상이면 OK
2. 레포 폴더로 이동 + 최신 받기:
   - `cd $HOME\Documents\HF_AI_STUDY` (탐색기의 "문서" = `Documents`. 안 되면 Unit 0 때 clone한 위치로)
   - `git pull`
3. Unit 1 실습 폴더로 이동: `cd units\unit1-intro-agents\code`
4. 이 폴더 전용 가상환경(venv) 만들기: `python -m venv .venv` (venv = 이 폴더에서만 쓰는 파이썬 공구함. 다른 폴더와 안 섞임)
5. 가상환경 켜기: `.venv\Scripts\Activate.ps1` → 줄 앞에 `(.venv)`가 붙으면 성공
6. Jupyter 설치: `pip install notebook` (1~2분)

## 매번: 노트북 열기

1. **Ollama 앱이 켜져 있는지** 확인 (작업 표시줄 오른쪽 아래 라마 아이콘)
2. PowerShell에서:
   - `cd $HOME\Documents\HF_AI_STUDY\units\unit1-intro-agents\code`
   - `.venv\Scripts\Activate.ps1`
   - `jupyter notebook dummy_agent_ollama.ipynb`
3. 브라우저가 자동으로 열리고 노트북이 보인다. 맨 위 칸부터 `Shift + Enter`
4. 끝낼 때: 브라우저 메뉴 **File → Shut Down**, 또는 PowerShell 창에서 `Ctrl + C`

PowerShell 창은 Jupyter가 돌아가는 동안 **닫지 않는다** (닫으면 노트북 실행이 멈춤).

## 자주 나는 문제

| 증상 | 원인 → 해결 |
|---|---|
| `python`을 찾을 수 없다 / Microsoft Store가 열림 | 파이썬 경로 문제. `py --version`이 되면 위 명령의 `python`을 `py`로 바꿔서 |
| `Activate.ps1` 실행 시 "스크립트를 실행할 수 없습니다" | PowerShell 보안 설정. `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` 한 번 실행 후 다시 |
| `jupyter`를 찾을 수 없다 | 가상환경이 꺼져 있음(`(.venv)` 없음) → 5번 다시 |
| 노트북 0단계에서 `ConnectionRefusedError` | Ollama 꺼짐 → 앱 켜고 그 칸 다시 실행 |
| Jupyter를 끄려고 `Ctrl + C`를 눌러도 안 멈춤 | 창 안을 클릭하면 PowerShell이 **글자 선택 모드**가 되어 키를 안 받음 → `Esc`를 누르고 `Ctrl + C`를 **두 번 빠르게**. 그래도 안 되면 PowerShell 창을 **X로 닫아도 됨** (서버만 꺼짐. 노트북을 고쳤다면 닫기 전에 브라우저에서 `Ctrl + S`로 저장) |
| `No such file or directory: ...ipynb` | 파일이 아직 내 PC에 없음 → `git pull`. 그래도 없으면 AI에게 "main에 올라갔는지" 확인 요청 |
| 첫 모델 호출이 오래 걸림 | 모델을 GPU에 올리는 중. 수십 초까지 정상 |

## 실습 파일

- `code/dummy_agent_ollama.ipynb` — 단계별 실습 노트북 (0~7단계, 단계마다 ✅ 확인할 것)
- `code/dummy_agent_ollama.py` — 같은 내용(1~6단계)을 한 번에 실행하는 버전: `python dummy_agent_ollama.py`
