---
description: 실습 환경 점검. Python 버전·필수 패키지 설치 여부·.env API 키 존재를 확인하고 부족한 것을 안내한다. "환경 점검", "셋업 확인", "키 확인", "잘 깔렸나" 등에 사용.
allowed-tools: Bash, Read
---

## Python 버전
!`python3 --version 2>&1 || python --version 2>&1`

## 설치된 핵심 패키지
!`pip list 2>/dev/null | grep -iE "feedparser|firecrawl|apify|playwright|google-genai|mcp|httpx|dotenv" || echo "(관련 패키지 미설치 — pip install -r requirements.txt 필요)"`

## .env 키 존재 확인 (값은 노출 안 함, 키 이름만)
!`test -f .env && grep -oE "^[A-Z_]+=" .env | tr -d '=' || echo ".env 파일 없음"`

## 지시

위 결과를 보고 수강생 환경을 점검해 보고하라.

1. **Python**: 3.10 이상인지 확인. 낮거나 없으면 설치/업그레이드 안내.
2. **패키지**: `requirements.txt`의 항목 중 빠진 것이 있으면 `pip install -r requirements.txt` 실행을 권하라(원하면 직접 실행해줘도 됨).
3. **API 키**: `.env`에 어떤 키가 들어있는지(이름만) 보고. 최소 1개(예: `TAVILY_API_KEY`)가 있으면 검색 API 실습 가능. 키가 없으면 `api_keys/00_api_key_guide.md`를 보라고 안내.
4. **결론 한 줄**: "지금 바로 실습 가능 / 무엇을 보완하면 됨"을 명확히. 보완 후 `/step 1` 또는 `/start` 로 돌아가라고.

⚠️ `.env`의 키 **값**은 절대 출력하지 마라. 키 이름만 다룬다.
