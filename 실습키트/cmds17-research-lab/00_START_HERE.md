# 🚀 START HERE — 월간 CMDS 17회차 실습 키트

> **이 키트가 뭔가요?** 👉 Claude Code 하나로 *"원하는 정보를 AI가 알아서 찾아오게"* 만드는 실습장입니다. 압축만 풀면 하네스(CLAUDE.md·슬래시커맨드·권한)가 **이미 다 세팅된 상태**라, 여러분은 따라가기만 하면 됩니다.

---

## ✅ 준비물 (3개만 확인)

| 준비물 | 확인 명령 | 없으면 |
|--------|-----------|--------|
| 🤖 Claude Code | `claude --version` | 설치: https://docs.claude.com/en/docs/claude-code/setup |
| 🐍 Python 3.10+ | `python3 --version` | https://www.python.org/downloads/ |
| 🔑 API 키 (최소 1개) | 아래 4번 참고 | `api_keys/00_api_key_guide.md` |

> 설치/버전은 위 한 줄 링크면 충분합니다. **이 키트는 Claude Code와 Python이 이미 준비돼 있다고 가정**합니다.

---

## 🏁 3스텝으로 시작하기

```
① 이 zip 압축을 풀고
② 이 폴더(cmds17-research-lab)에서 터미널을 열어 claude 를 실행하고
③ Claude에게  /start  라고 입력하세요.
```

끝입니다. `/start`가 **지금 어디까지 했는지 파악하고, 다음 할 일을 안내**합니다. 막히면 언제든 다시 `/start`.

> 💡 터미널 여는 법: 이 폴더를 Finder/탐색기에서 우클릭 → "터미널에서 열기" (또는 `cd`로 이 폴더 경로로 이동).

---

## 🔑 API 키 넣기 (.env 만들기)

자료조사용 키(Tavily·Firecrawl·Gemini 등) 발급 절차는 👉 **`api_keys/00_api_key_guide.md`** 에 단계별로 정리돼 있습니다. (전부 무료 티어로 실습 가능)

키를 받았으면 `.env` 파일에 넣습니다. **두 가지 방법 중 택1:**

**방법 A — 직접 편집**
```bash
cp .env.example .env      # 템플릿 복사
# .env 를 열어 발급받은 키를 붙여넣기
```

**방법 B — Claude에게 맡기기 (추천 🙆)**
```
내 키를 .env에 넣어줘:  TAVILY_API_KEY 는 tvly-xxxx ...
```
라고 말하면 Claude가 `.env`를 만들어 줍니다. (`.env`는 `.gitignore`에 등록돼 있어 커밋되지 않습니다.)

> 키가 제대로 들어갔는지 확인하려면 Claude에게 `/setup-check` 라고 입력하세요.

---

## 🗺️ 전체 커리큘럼 (가이드 01~08)

`guides/` 폴더에 단계별 실습이 있습니다. `/step 1`, `/step 2` … 로 하나씩 진행하세요.

| # | 가이드 | 한 줄 요약 | 슬래시커맨드 |
|---|--------|-----------|-------------|
| 01 | 정보 수집 4단 사다리 | 공식API→검색API→크롤링SaaS→브라우저 (위에서부터!) | `/step 1` |
| 02 | 공식 API 먼저 | arXiv(무키)·법제처 — 안정·합법·구조화 | `/step 2` |
| 03 | 검색 API로 우회 | Tavily·Exa·Brave·SerpAPI 비교/선택 | `/step 3` |
| 04 | 크롤링 SaaS 위임 | Firecrawl(URL→마크다운)·Apify | `/step 4` |
| 05 | 브라우저 자동화 | Playwright·cmux·DevTools Recorder | `/step 5` |
| 06 | AI에게 통째로 위임 | Gemini grounding / Deep Research | `/step 6` |
| 07 | ★ Claude Code 하네스 | CLAUDE.md·서브에이전트·command·MCP·검증 | `/step 7` |
| 08 | ★ 캡스톤: 나만의 LLM Wiki | Karpathy 패턴 실제 볼트(`LLMWiki/`)에 /ingest→/query→/lint | `/step 8` |

**자주 쓰는 슬래시커맨드**
- `/start` — 어디까지 했는지 + 다음 할 일
- `/setup-check` — Python·패키지·키 점검
- `/step [번호]` — 해당 가이드를 함께 진행
- `/research-ladder [주제]` — 4단 사다리로 조사해 `research/`에 저장
- `/wiki-build [주제]` — 캡스톤 위키 파이프라인 실행

---

## 🆘 자주 막히는 점 FAQ

**Q. `claude`를 쳤는데 명령을 못 찾아요.**
→ Claude Code가 설치 안 됐거나 PATH 문제입니다. `claude --version`이 동작하는지 먼저 확인하세요.

**Q. `/start`를 입력해도 반응이 없어요.**
→ 이 폴더(`cmds17-research-lab`) **안에서** `claude`를 실행했는지 확인하세요. 슬래시커맨드는 `.claude/commands/`가 있는 폴더에서만 보입니다.

**Q. 패키지가 없다고 나와요 (ModuleNotFoundError).**
→ `pip install -r requirements.txt` 를 실행하거나, Claude에게 `/setup-check` 후 "부족한 패키지 설치해줘"라고 하세요.

**Q. API 키 에러(401/403)가 나요.**
→ `.env`에 키가 올바른지 `/setup-check`로 확인. 키 앞뒤 공백·따옴표를 빼세요.

**Q. 권한을 묻는 프롬프트가 자꾸 떠요.**
→ 실습 편의를 위해 `.claude/settings.json`에 자주 쓰는 명령은 허용해 뒀지만, 처음 보는 명령은 물어볼 수 있습니다. 안전하면 허용하세요. (`rm`, `git push`는 막혀 있습니다.)

**Q. 브라우저 자동화(05)에서 cmux가 없어요.**
→ cmux는 강사 환경 도구입니다. 수강생은 Playwright(`requirements.txt`에 포함)로 동일 개념을 실습합니다. 가이드 05가 안내합니다.

---

준비됐으면 — 이 폴더에서 `claude` 실행 → `/start` 🎬
