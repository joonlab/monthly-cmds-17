#!/usr/bin/env python3
"""Apify — Actor(서버리스 스크래퍼) 실행. pip install apify-client
토큰: apify.com > Settings > API & Integrations. 무료 $5 크레딧/월."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ.get("APIFY_TOKEN", "YOUR_APIFY_TOKEN"))
run = client.actor("apify/website-content-crawler").call(
    run_input={"startUrls": [{"url": "https://example.com"}], "maxCrawlDepth": 1}
)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("url"), "|", item.get("text", "")[:160])
