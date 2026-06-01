#!/usr/bin/env bash
# 수집 도구를 MCP로 패키징 → Claude Code가 대화 중 자동 호출.
# 필요한 줄만 실행. 확인: claude mcp list / 제거: claude mcp remove <name>

# arXiv (논문 검색·다운로드·읽기)
uv tool install arxiv-mcp-server
claude mcp add arxiv -- uv tool run arxiv-mcp-server --storage-path ~/.arxiv-mcp-server/papers

# 법제처 korean-law (로컬 빌드)
claude mcp add korean-law --env LAW_OC=<발급받은-OC키> \
  -- node ~/Desktop/10_프로젝트/날짜별/2026/20260601_korean-law-mcp-tutorial/repo/build/index.js

# Firecrawl (URL→마크다운/크롤/검색)
claude mcp add firecrawl --env FIRECRAWL_API_KEY=fc-YOUR-KEY -- npx -y firecrawl-mcp
# hosted 대안: claude mcp add --transport http firecrawl https://mcp.firecrawl.dev/fc-YOUR-KEY/v2/mcp

# Apify (34K+ Actor를 도구로)
claude mcp add --transport http apify https://mcp.apify.com/

# 탐색: smithery.ai / mcp.so 에서 키워드(search/scrape/arxiv/docs) 검색 후 카드의 add 명령 복사
