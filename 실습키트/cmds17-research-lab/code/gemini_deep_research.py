#!/usr/bin/env python3
"""Gemini Deep Research Agent — 자율 다단계 리서치(Preview). pip install google-genai
generate_content가 아니라 Interactions API. background=True + 폴링."""
import time
from google import genai

client = genai.Client()
it = client.interactions.create(
    input="소형 LLM 상용화 동향을 조사해 인용 포함 보고서로 정리",
    agent="deep-research-preview-04-2026",
    background=True,
)
print("started:", it.id)
while True:
    it = client.interactions.get(it.id)
    if it.status == "completed":
        print(it.output_text); break
    if it.status == "failed":
        print("failed:", it.error); break
    time.sleep(10)
