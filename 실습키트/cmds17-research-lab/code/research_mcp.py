#!/usr/bin/env python3
"""공식 API를 감싸는 최소 MCP 서버. pip install "mcp[cli]" httpx
등록: claude mcp add research-tools -- python /절대경로/research_mcp.py"""
from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("research-tools")

@mcp.tool()
def arxiv_search(query: str, max_results: int = 5) -> str:
    """arXiv에서 논문을 검색해 Atom XML(제목/링크/날짜)을 반환한다."""
    r = httpx.get(
        "http://export.arxiv.org/api/query",
        params={"search_query": query, "max_results": max_results,
                "sortBy": "submittedDate", "sortOrder": "descending"},
        timeout=20,
    )
    return r.text

if __name__ == "__main__":
    mcp.run()  # stdio
