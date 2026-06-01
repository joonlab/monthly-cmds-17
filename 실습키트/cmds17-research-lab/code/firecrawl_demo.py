#!/usr/bin/env python3
"""Firecrawl — URL → LLM-ready 마크다운. pip install firecrawl-py
키 발급: https://firecrawl.dev/app/api-keys (fc-...). 무료 1,000 credits/월."""
import os
from firecrawl import Firecrawl

fc = Firecrawl(api_key=os.environ.get("FIRECRAWL_API_KEY", "fc-YOUR-KEY"))

# 단일 페이지 → 마크다운
doc = fc.scrape("https://firecrawl.dev", formats=["markdown"])
print(doc)

# 웹 검색 + 본문
print(fc.search(query="AI agents", limit=3))
