#!/usr/bin/env python3
"""research-ladder 수집 스크립트 — 4단 사다리의 ① 공식 API(arXiv) 단계.

arXiv는 무료·무인증 공식 API다. pip install feedparser

사용법:
    python3 collect.py arxiv "cat:cs.CL AND abs:small language model"
    python3 collect.py arxiv "agent" 10      # 결과 개수 지정(기본 5)
"""
import sys
import time
import urllib.parse
import urllib.request

try:
    import feedparser
except ImportError:
    sys.exit("feedparser 가 필요합니다:  pip install feedparser")

ARXIV_API = "http://export.arxiv.org/api/query?"


def arxiv(query, n=5):
    """arXiv 최신 논문 n건을 검색해 제목/저자/링크/날짜를 출력한다."""
    params = urllib.parse.urlencode({
        "search_query": query,
        "start": 0,
        "max_results": n,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    raw = urllib.request.urlopen(ARXIV_API + params, timeout=20).read()
    feed = feedparser.parse(raw)
    if not feed.entries:
        print(f"(결과 없음) query={query!r}")
    for e in feed.entries:
        authors = ", ".join(a.name for a in getattr(e, "authors", []))
        print(f"- {e.title.strip()}")
        print(f"    저자: {authors}")
        print(f"    {e.link} | {e.published}")
    time.sleep(3)  # 공식 권장 연속 호출 딜레이


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    cmd = argv[1]
    if cmd == "arxiv":
        query = argv[2] if len(argv) > 2 else "cat:cs.CL AND abs:agent"
        n = int(argv[3]) if len(argv) > 3 else 5
        arxiv(query, n)
    else:
        sys.exit(f"알 수 없는 명령: {cmd!r} (지원: arxiv)")


if __name__ == "__main__":
    main(sys.argv)
