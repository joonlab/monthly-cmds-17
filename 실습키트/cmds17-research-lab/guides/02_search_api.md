# 02. 2순위 — 검색 API로 우회 (Tavily · Exa · Brave · SerpAPI)

> **준비물**: 아래 4종 중 **최소 1개** API 키
> - `TAVILY_API_KEY` (`tvly-...`, 가입 크레딧)
> - `EXA_API_KEY` (무료 1,000 req/월 — 가장 넉넉)
> - `BRAVE_API_KEY` (월 $5 크레딧 ≈ 1k)
> - `SERPAPI_KEY` (250/월)
> **예상시간**: 15분 · **난이도**: ★★☆☆☆

---

## 이 단계의 한 줄

> 공식 API가 없으면, **일반 웹을 LLM이 먹기 좋은 형태**로 바꿔주는 검색 API로 우회한다.

| | Tavily | Exa | Brave Search | SerpAPI |
|--|--------|-----|--------------|---------|
| 성격 | AI/RAG 특화 검색+요약 | 임베딩 시맨틱 검색 | 자체 웹 인덱스 | Google SERP 미러 |
| 무료 | 가입 크레딧 | **1,000 req/월** | 월 $5 크레딧(≈1k) | 250/월 |
| 인증 헤더 | `Authorization: Bearer tvly-` | `x-api-key` | `X-Subscription-Token` | `api_key` 쿼리 |

---

## STEP 1 — 키를 .env에 넣기

발급받은 키를 프로젝트 루트 `.env`에 둔다(키 발급 절차는 키 발급 가이드 참조).

```bash
# .env  (커밋 금지 — .gitignore에 포함됨)
TAVILY_API_KEY=tvly-xxxxx
EXA_API_KEY=xxxxx
```

> 🔐 `.env`와 키는 절대 git에 커밋하지 않는다. 이 키트의 `.gitignore`가 막아준다.

---

## STEP 2 — 검색 한 번 돌려보기

가진 키에 맞는 줄을 골라 실행한다. 4종 전부 [`code/search_apis.sh`](../code/search_apis.sh)에 들어 있다.

**붙여넣기 (Tavily — RAG에 바로):**
```bash
curl -X POST https://api.tavily.com/search \
  -H "Authorization: Bearer $TAVILY_API_KEY" -H "Content-Type: application/json" \
  -d '{"query":"latest LLM agent research","search_depth":"basic","max_results":5}'
```

**Exa (시맨틱) / Brave (저렴) / SerpAPI (Google 원본):**
```bash
curl -X POST https://api.exa.ai/search -H "x-api-key: $EXA_API_KEY" -H "Content-Type: application/json" \
  -d '{"query":"LLM agents","numResults":5,"contents":{"text":true}}'

curl -s "https://api.search.brave.com/res/v1/web/search?q=AI+news&count=5" \
  -H "Accept: application/json" -H "X-Subscription-Token: $BRAVE_API_KEY"

curl "https://serpapi.com/search.json?q=AI+news&engine=google&api_key=$SERPAPI_KEY"
```

### ✅ 체크포인트 1
- [ ] 검색 결과 JSON(제목/URL/요약)이 돌아왔다
- [ ] 어떤 상황에 어떤 API를 쓸지 한 줄로 말할 수 있다

**선택 가이드**: RAG/요약 즉시 → **Tavily** · 시맨틱/연구 발견 → **Exa**(무료 넉넉) · 저비용+Claude 친화 → **Brave** · Google 결과 원본 → **SerpAPI**(비쌈).

---

## STEP 3 — 검색 API를 MCP로 (모델이 직접 웹검색)

Tavily·Exa·Brave 모두 공식 MCP가 있다. Exa는 Smithery 최상위.

**붙여넣기 (Tavily 예):**
```bash
claude mcp add tavily --env TAVILY_API_KEY=$TAVILY_API_KEY -- npx -y tavily-mcp
claude mcp list
```

**입력 프롬프트:**
```
2026년 소형 LLM 동향을 검색해서 핵심 5줄 + 출처 URL로 정리해줘.
```

> 💡 만들기 전에 **Smithery / mcp.so에 이미 있는지 검색**한다 — 바퀴 재발명 금지.

### ✅ 체크포인트 2
- [ ] MCP 등록 후 모델이 검색 도구를 자동 호출했다
- [ ] 결과에 출처 URL이 붙어 있다

---

## 이 단계의 산출물
- 검색 API 1종 동작 확인
- 등록된 MCP 1개(tavily/exa/brave 중)

➡️ 사이트 구조가 복잡하거나 본문을 통째로 긁어야 하면 → [`03_crawling_saas.md`](03_crawling_saas.md)
