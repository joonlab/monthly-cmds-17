#!/usr/bin/env python3
"""Gemini Google Search Grounding — 실시간 검색+인용. pip install google-genai
키: export GEMINI_API_KEY=...  (AI Studio 무료 티어 가능)"""
from google import genai
from google.genai import types

client = genai.Client()  # GEMINI_API_KEY 자동 사용
cfg = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)
r = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="2026년 소형 LLM(SLM) 최신 동향 요약",
    config=cfg,
)
print(r.text)

# 인용(각주) 추출
gm = r.candidates[0].grounding_metadata
if gm and gm.grounding_supports:
    print("\n--- 출처 매핑 ---")
    for s in gm.grounding_supports:
        srcs = [gm.grounding_chunks[i].web.uri for i in s.grounding_chunk_indices]
        print(s.segment.text, "→", srcs)
