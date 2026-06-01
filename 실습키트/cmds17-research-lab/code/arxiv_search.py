#!/usr/bin/env python3
"""arXiv 논문 검색 — 공식 API(무료·무인증). pip install feedparser"""
import urllib.request, urllib.parse, feedparser, time, sys

def arxiv_search(query, n=5):
    p = urllib.parse.urlencode({
        "search_query": query, "start": 0, "max_results": n,
        "sortBy": "submittedDate", "sortOrder": "descending",
    })
    raw = urllib.request.urlopen("http://export.arxiv.org/api/query?" + p).read()
    feed = feedparser.parse(raw)
    for e in feed.entries:
        print("•", e.title.strip())
        print("   ", ", ".join(a.name for a in e.authors))
        print("   ", e.link, "|", e.published)
    time.sleep(3)  # 공식 권장 연속 호출 딜레이

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else "cat:cs.CL AND abs:agent"
    arxiv_search(q, 5)
