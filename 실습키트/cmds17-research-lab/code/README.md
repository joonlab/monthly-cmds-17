# 17회차 박준 파트 — 실행코드 모음

강의 마스터 자료 `../00_강의자료_MASTER.md`의 코드를 단독 실행 파일로 분리.

## 사전 준비
```bash
pip install feedparser firecrawl-py apify-client playwright google-genai "mcp[cli]" httpx
playwright install
```

## 파일별 실행법
| 파일 | 사다리 | 실행 | 필요 키 |
|------|--------|------|---------|
| `arxiv_search.py` | ① 공식API | `python arxiv_search.py "cat:cs.CL AND abs:agent"` | 없음 |
| `search_apis.sh` | ② 검색API | `TAVILY_API_KEY=tvly-... bash search_apis.sh` | Tavily/Exa/Brave/SerpAPI |
| `firecrawl_demo.py` | ③ 크롤링SaaS | `FIRECRAWL_API_KEY=fc-... python firecrawl_demo.py` | Firecrawl(무료 1k/월) |
| `apify_demo.py` | ③ 크롤링SaaS | `APIFY_TOKEN=... python apify_demo.py` | Apify(무료 $5/월) |
| `playwright_scrape.py` | ④ 브라우저 | `python playwright_scrape.py` | 없음(데모 사이트) |
| `playwright_auth.py` | ④ 브라우저 | `python playwright_auth.py save` → `python playwright_auth.py` | 본인 계정 |
| `gemini_grounding.py` | ⑤ Gemini | `GEMINI_API_KEY=... python gemini_grounding.py` | Gemini(무료 5k/월) |
| `gemini_deep_research.py` | ⑤ Gemini | `GEMINI_API_KEY=... python gemini_deep_research.py` | Gemini(Preview) |
| `research_mcp.py` | ⭐MCP 제작 | `claude mcp add research-tools -- python $PWD/research_mcp.py` | 없음 |
| `mcp_add_commands.sh` | ⭐MCP 등록 | 필요한 줄만 복사 실행 | 도구별 상이 |

## ⚠️ 주의
- `state.json`(Playwright 인증상태)은 **절대 커밋 금지** → `.gitignore` 추가.
- 스크래핑은 robots.txt·ToS·개인정보 확인 후, 본인 권한 범위·저빈도로만.
- 법제처 korean-law는 로컬 repo 빌드 필요(미빌드 시 `cd repo && npm i && npm run build`).

> ⚠️ arXiv 주의: 공개 API라 동일 IP 단시간 다수 호출 시 HTTP 429/503으로 일시 제한됩니다. 연속 호출 사이 3초 이상 딜레이(코드에 반영됨)를 두고, 막히면 잠시 후 재시도하세요. 문법/로직은 검증 완료.
