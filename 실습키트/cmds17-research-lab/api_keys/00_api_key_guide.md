# API 키 발급 가이드 (CMDS 17회차 Research Lab)

> 이 문서는 수강생이 **그대로 따라 하면 키를 발급받을 수 있도록** 작성되었습니다.
> 모든 절차·버튼명·무료티어는 **2026-06-01 직접 방문 확인** 기준입니다.
> 가격/무료 한도는 각 서비스가 수시로 바꾸므로, 발급 시점에 화면을 한 번 더 확인하세요.

---

## 0. 먼저: 무엇부터 발급할까? (필수 vs 선택)

실습을 굴리는 데 **꼭 필요한 키 3개**만 먼저 받으면 됩니다. 모두 **무료 + 신용카드 불필요**라 5분이면 끝납니다. 나머지는 더 깊은 검색/스크래핑/한국 법령 실습을 할 때 선택적으로 추가하세요.

| 구분 | 서비스 | .env 변수 | 무료티어(2026-06-01) | 카드 필요? | 용도 |
|------|--------|-----------|----------------------|-----------|------|
| **필수** | Google AI Studio (Gemini) | `GEMINI_API_KEY` | 무료티어 있음(모델별 분당/일일 한도) | ❌ | LLM 추론·요약·합성의 핵심 |
| **필수** | Tavily | `TAVILY_API_KEY` | 1,000 크레딧/월 | ❌ | 에이전트용 실시간 웹 검색 |
| **필수** | Firecrawl | `FIRECRAWL_API_KEY` | Free 플랜(소량 크레딧/월) | ❌ | 웹페이지 스크래핑→마크다운 |
| 선택 | Apify | `APIFY_TOKEN` | $5 크레딧/월 | ❌ | 대규모 스크래퍼(Actor) 실행 |
| 선택 | Brave Search API | `BRAVE_API_KEY` | $5 무료 크레딧/월 | ✅(무료 플랜도 카드 등록) | 독립 검색 인덱스 |
| 선택 | Exa | `EXA_API_KEY` | 가입 시 무료 크레딧 제공 | ❌(시작 시) | 시맨틱/신경망 웹 검색 |
| 선택 | SerpAPI | `SERPAPI_KEY` | 100 검색/월(무료 플랜) | ❌ | 구글 SERP 구조화 결과 |
| 선택 | 법제처 OPEN API (OC키) | `LAW_OC` | 완전 무료 | ❌ | 한국 법령·판례 조회 |

> **권장 순서**: Gemini → Tavily → Firecrawl 까지 받고 바로 실습 시작 → 필요할 때 나머지 추가.

---

## 1. Google AI Studio — Gemini API 키 (필수)

- **발급 URL**: https://aistudio.google.com/apikey
- **무료티어(2026-06-01)**: 무료티어 제공. 모델별로 분당 요청수(RPM)·일일 요청수(RPD)·분당 토큰수(TPM) 한도가 있으며, Google 계정만 있으면 카드 없이 사용 가능. 정확한 한도는 https://ai.google.dev/gemini-api/docs/rate-limits 에서 확인.
- **키 형식**: `AIza...` 로 시작하는 39자 내외 문자열
- **.env 변수**: `GEMINI_API_KEY`

### 발급 절차
1. 브라우저에서 https://aistudio.google.com/apikey 접속 (Google 로그인 필요 — 로그인 안 했으면 계정 선택 화면으로 이동)
2. 처음이면 약관(Terms of Service) 동의 체크 후 **Continue**
3. 화면의 **"Create API key"**(또는 **"API 키 만들기"**) 버튼 클릭
4. 기존 Google Cloud 프로젝트를 선택하거나 **"Create API key in new project"** 선택
5. 생성된 키 옆 **복사 아이콘** 클릭 → 키 복사
6. `.env`의 `GEMINI_API_KEY=` 뒤에 붙여넣기

> 참고: 키 발급 화면은 로그인 상태에서만 보입니다(로그인 전에는 Google 계정 선택 페이지로 리다이렉트됨).

---

## 2. Tavily — 웹 검색 API (필수)

- **가입 URL**: https://app.tavily.com/home  (랜딩: https://www.tavily.com/)
- **무료티어(2026-06-01, 공식 문서 확인)**: **1,000 크레딧/월, 신용카드 불필요**. 초과 시 Pay-as-you-go $0.008/크레딧.
- **키 형식**: `tvly-` 로 시작
- **.env 변수**: `TAVILY_API_KEY`

### 발급 절차
1. https://app.tavily.com/home 접속 → **Sign Up**(Google/GitHub/이메일 중 선택)
2. 로그인하면 대시보드(Overview/Home) 진입
3. 대시보드 메인 또는 **API Keys** 메뉴에 기본 키가 이미 생성되어 있음 → 키 우측 **복사** 클릭
4. (없으면) **"+ Create Key"** / **"Generate API Key"** 클릭 후 복사
5. `.env`의 `TAVILY_API_KEY=` 뒤에 붙여넣기

---

## 3. Firecrawl — 웹 스크래핑 API (필수)

- **가입 URL**: https://www.firecrawl.dev/  → 우측 상단 **Sign Up**
- **무료티어(2026-06-01)**: **Free 플랜** 제공(소량 크레딧/월, 카드 불필요). 유료는 Hobby 5,000 크레딧/월부터. 크레딧 소비: Scrape 1크레딧/페이지, Search 2크레딧/10건.
- **키 형식**: `fc-` 로 시작
- **.env 변수**: `FIRECRAWL_API_KEY`

### 발급 절차
1. https://www.firecrawl.dev/ 접속 → **Sign Up**(Google/GitHub/이메일)
2. 로그인 후 대시보드 진입 → 좌측/상단 **API Keys** 메뉴 클릭
3. 기본 생성된 키(`fc-...`)의 **복사 아이콘** 클릭, 또는 **"Create API Key"** 후 복사
4. `.env`의 `FIRECRAWL_API_KEY=` 뒤에 붙여넣기

---

## 4. Apify — 토큰 (선택)

- **가입 URL**: https://apify.com/  → **Sign up** / 가격: https://apify.com/pricing
- **무료티어(2026-06-01)**: **Free 플랜 — $5 상당 사용량/월, 신용카드 불필요**("No credit card required").
- **토큰 형식**: `apify_api_...`
- **.env 변수**: `APIFY_TOKEN`

### 발급 절차
1. https://apify.com/ 접속 → **Sign up**(Google/GitHub/이메일)
2. 로그인 후 Console 진입 → 좌측 메뉴 **Settings → API & Integrations**(또는 우측 상단 프로필 → **Settings**)
3. **Personal API tokens** 섹션에서 기본 토큰의 **Copy** 클릭, 또는 **"+ Create a new token"** 후 복사
4. `.env`의 `APIFY_TOKEN=` 뒤에 붙여넣기

---

## 5. Brave Search API (선택)

- **가입/구독 URL**: https://api-dashboard.search.brave.com/  (안내: https://brave.com/search/api/)
- **무료티어(2026-06-01)**: **매월 $5 무료 크레딧** 제공. 무료 "Free" 플랜은 **1 query/sec** 한도. ⚠️ **무료 플랜이라도 구독 시 신용카드 등록이 필요**합니다.
- **키 형식**: 영숫자 토큰(예 `BSA...`)
- **.env 변수**: `BRAVE_API_KEY`

### 발급 절차
1. https://api-dashboard.search.brave.com/ 접속 → **Sign up** / 로그인
2. **Subscriptions**에서 **Free** 플랜 선택 → **Subscribe**(신용카드 정보 등록)
3. 좌측 **API Keys** 메뉴 → **"Add API key"** / **Generate** 클릭 후 키 복사
4. `.env`의 `BRAVE_API_KEY=` 뒤에 붙여넣기

---

## 6. Exa — 시맨틱 검색 API (선택)

- **가입 URL**: https://exa.ai/  → **API Dashboard**(https://dashboard.exa.ai/)
- **무료티어(2026-06-01)**: 가입 시 무료 크레딧 제공(시작 시 카드 불필요). 과금: Search $5/1k requests, Contents $1/1k pages 등 사용량 기반.
- **키 형식**: 영숫자 토큰(대시 포함)
- **.env 변수**: `EXA_API_KEY`

### 발급 절차
1. https://exa.ai/ 접속 → 우측 상단 **API**(또는 **Try API for free**) → **Sign Up**
2. 로그인 후 https://dashboard.exa.ai/ (API Dashboard) 진입
3. **API Keys** 메뉴 → **"Create API Key"** 클릭 후 복사
4. `.env`의 `EXA_API_KEY=` 뒤에 붙여넣기

---

## 7. SerpAPI — 구글 SERP 구조화 API (선택)

- **가입 URL**: https://serpapi.com/users/sign_up  (가격: https://serpapi.com/pricing)
- **무료티어(2026-06-01)**: 무료 플랜 **100 검색/월**. 유료는 Starter $25/월(1,000 검색)부터.
- **키 형식**: 64자 hex 문자열
- **.env 변수**: `SERPAPI_KEY`

### 발급 절차
1. https://serpapi.com/users/sign_up 접속 → 이메일/Google로 가입(가입 시 휴대폰 인증 요구될 수 있음)
2. 로그인 후 대시보드 좌측 **"Api Key"** 메뉴 클릭
3. **Your Private API Key** 값을 **Copy** 클릭
4. `.env`의 `SERPAPI_KEY=` 뒤에 붙여넣기

---

## 8. 법제처 OPEN API — OC키 (선택, 한국 법령 실습용)

- **사이트**: https://open.law.go.kr/  (OPEN API 안내: https://open.law.go.kr/LSO/openApi/guideList.do)
- **무료티어**: **완전 무료**. 별도 결제 없음.
- **OC키 정체**: 회원가입 시 입력한 **이메일 아이디(@ 앞부분)** 가 그대로 OC(기관코드) 값입니다. 예: 이메일이 `hong@gmail.com` 이면 OC = `hong`.
- **.env 변수**: `LAW_OC`

### 발급 절차
1. https://open.law.go.kr/ 접속 → 우측 상단 **로그인 → 사용자 가입**
2. 이메일 주소로 회원가입(이때 정한 **아이디가 곧 OC값**)
3. 로그인 후 상단 **OPEN API → 사용 신청**(또는 마이페이지에서 API 활용 신청) → 활용 목적 입력 후 신청
4. 승인되면 `.env`의 `LAW_OC=` 뒤에 **이메일 아이디(@ 앞부분)** 입력
   - 예: `LAW_OC=hong`

> 호출 예시: `https://www.law.go.kr/DRF/lawSearch.do?OC=<아이디>&target=law&type=XML&query=도로교통법`

---

## 9. .env 작성 예시

키를 다 받았으면 키트 루트의 `.env.example`을 복사해 `.env`로 만들고 값을 채웁니다.

```bash
cp .env.example .env
```

`.env` 내용 예시(따옴표 없이, = 뒤에 바로 값):

```dotenv
# 필수 3종
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
TAVILY_API_KEY=tvly-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
FIRECRAWL_API_KEY=fc-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# 선택 (필요 시)
APIFY_TOKEN=apify_api_XXXXXXXXXXXXXXXXXXXXXXXXXXXX
BRAVE_API_KEY=BSAXXXXXXXXXXXXXXXXXXXXXXXXXXXX
EXA_API_KEY=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
SERPAPI_KEY=0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
LAW_OC=hong
```

> ⚠️ **주의**: `.env`는 절대 GitHub 등에 커밋하지 마세요(키트 `.gitignore`에 포함). 값에 따옴표를 붙이지 마세요. 키가 노출되면 각 서비스 대시보드에서 즉시 재발급(rotate)하세요.
