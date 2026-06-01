#!/usr/bin/env bash
# 검색 API 4종 — 환경변수에 키 설정 후 실행. 필요한 블록만 주석 해제.
set -euo pipefail

# --- Tavily (AI/RAG 특화) : export TAVILY_API_KEY=tvly-...
curl -X POST https://api.tavily.com/search \
  -H "Authorization: Bearer ${TAVILY_API_KEY:?set TAVILY_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"query":"latest LLM agent research","search_depth":"basic","max_results":5}'

# --- Exa (시맨틱) : export EXA_API_KEY=...
# curl -X POST https://api.exa.ai/search -H "x-api-key: $EXA_API_KEY" \
#   -H "Content-Type: application/json" \
#   -d '{"query":"LLM agents","numResults":5,"contents":{"text":true}}'

# --- Brave Search (저렴·자체인덱스) : export BRAVE_API_KEY=...
# curl -s "https://api.search.brave.com/res/v1/web/search?q=AI+news&count=5" \
#   -H "Accept: application/json" -H "X-Subscription-Token: $BRAVE_API_KEY"

# --- SerpAPI (Google SERP 원본) : export SERPAPI_KEY=...
# curl "https://serpapi.com/search.json?q=AI+news&engine=google&api_key=$SERPAPI_KEY"
