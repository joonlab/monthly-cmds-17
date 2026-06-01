# 03. 3순위 — 크롤링 SaaS에 위임 (Firecrawl · Apify)

> **준비물**: `FIRECRAWL_API_KEY` (`fc-...`, 무료 1,000 credits/월, 카드 불필요) 또는 `APIFY_TOKEN` (무료 $0 플랜 + 매월 $5 크레딧)
> **예상시간**: 15분 · **난이도**: ★★☆☆☆
> **사전 설치**: `pip install firecrawl-py apify-client`

---

## 이 단계의 한 줄

> 사이트 구조·안티봇·JS 렌더링을 **신경 쓰기 싫을 때.** "URL만 던지면 끝."

검색 API로는 부족하고(본문 전체가 필요), 직접 브라우저 자동화(4순위)를 짜기는 부담스러울 때의 중간 지점이다.

---

## STEP 1 — Firecrawl: URL → LLM-ready 마크다운

엔드포인트: Scrape(단일) · Crawl(사이트 전체) · Map(URL 발견) · Search(검색+본문) · Interact(클릭/폼). 페이지당 1 credit.

**입력 프롬프트 (Claude Code):**
```
code/firecrawl_demo.py 패턴으로 https://firecrawl.dev 를 markdown으로 긁어줘.
FIRECRAWL_API_KEY는 .env에 있어.
```

핵심은 한 줄이다 — 스크립트 전문은 [`code/firecrawl_demo.py`](../code/firecrawl_demo.py):
```python
from firecrawl import Firecrawl
fc = Firecrawl(api_key="fc-YOUR-KEY")
print(fc.scrape("https://firecrawl.dev", formats=["markdown"]))   # URL→마크다운 한 줄
```

**MCP 등록:**
```bash
claude mcp add firecrawl --env FIRECRAWL_API_KEY=fc-YOUR-KEY -- npx -y firecrawl-mcp
# 또는 hosted: claude mcp add --transport http firecrawl https://mcp.firecrawl.dev/fc-YOUR-KEY/v2/mcp
```

### ✅ 체크포인트 1
- [ ] 임의 URL이 깨끗한 마크다운으로 변환됐다

---

## STEP 2 — Apify: 사이트 전용 스크래퍼 "앱스토어"(Actor)

**Actor** = 서버리스 스크래퍼. Store에 34K+ 개(인스타·링크드인·구글맵·X 전용 등)를 빌려 쓴다. 대표 Actor `apify/website-content-crawler`(RAG 피딩).

**입력 프롬프트:**
```
code/apify_demo.py 패턴으로 apify/website-content-crawler 를 써서
https://example.com 의 본문을 긁어줘. APIFY_TOKEN은 .env에 있어.
```

스크립트 전문: [`code/apify_demo.py`](../code/apify_demo.py)

**MCP 등록 (34K Actor를 도구로):**
```bash
claude mcp add --transport http apify https://mcp.apify.com/
```

### ✅ 체크포인트 2
- [ ] Actor 실행 결과(URL+본문)가 돌아왔다

---

## 언제 무엇을 (의사결정)
- **URL → 깨끗한 본문 + RAG** → **Firecrawl**
- **특정 플랫폼(인스타/링크드인/구글맵/X)의 정형 데이터** or 클라우드 스케줄 운영 → **Apify**
- **완전 통제·내부망·초대량(SaaS 비용 부담)·로그인 미묘 제어** → **직접 크롤링([`04_browser.md`](04_browser.md))**

> ⚠️ SaaS도 결국 남의 사이트를 긁는다. robots.txt·ToS·개인정보를 먼저 확인하고, 본인 권한 범위에서 저빈도로만. → 윤리 체크리스트는 [`04_browser.md`](04_browser.md) 상단.

---

## 이 단계의 산출물
- Firecrawl 또는 Apify로 긁은 본문 마크다운 1개
- 등록된 MCP 1개

➡️ 로그인·전용 제어·완전 통제가 필요하면 → [`04_browser.md`](04_browser.md)
