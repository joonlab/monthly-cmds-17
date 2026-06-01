# 01. 1순위 — 공식 API 먼저 (arXiv 무키 + 법제처 OC)

> **준비물**: 없음(arXiv) / `LAW_OC` 키(법제처, 1분 무료 발급 — `02_search_api.md` 옆 키 발급 가이드 참조)
> **예상시간**: 20분 · **난이도**: ★☆☆☆☆
> **사전 설치**: `pip install feedparser`

---

## 이 단계의 한 줄

> 스크래핑부터 떠올리면 초보. **"공식 API/공개데이터가 이미 있나?"를 먼저 묻는다.** 있으면 안정·합법·구조화 JSON으로 끝난다.

정보 수집 4단 사다리의 **1순위**다. arXiv(논문)·법제처(법령)처럼 무료 공식 API가 있으면 크롤링을 짤 이유가 없다.

---

## STEP 1 — arXiv: 키 없이 논문 수집

arXiv는 인증키가 필요 없는 공개 API다(엔드포인트 `http://export.arxiv.org/api/query`, Atom XML 응답).

먼저 감을 잡기 위해 그냥 셸에서 한 번 호출해 본다.

**붙여넣기 (터미널 직접 또는 Claude Code에 그대로):**
```bash
curl "http://export.arxiv.org/api/query?search_query=cat:cs.CL+AND+abs:agent&max_results=5&sortBy=submittedDate&sortOrder=descending"
```

다음으로, 파싱까지 된 스크립트를 Claude Code에게 실행시킨다.

**Claude Code 입력 프롬프트:**
```
code/arxiv_search.py 를 사용해서 "cat:cs.CL AND abs:agent" 최신 5건을 가져와줘.
제목 / 저자 / 링크를 표로 정리해줘.
```

- 스크립트 전문: [`code/arxiv_search.py`](../code/arxiv_search.py)
- 쿼리 필드 prefix: `ti`(제목) `au`(저자) `abs`(초록) `cat`(카테고리) `all`(전체)

> ⚠️ **arXiv 주의**: 공개 API라 동일 IP에서 단시간 다수 호출 시 HTTP 429/503으로 일시 제한된다. 연속 호출 사이 3초 이상 딜레이(코드에 내장됨)를 두고, 막히면 잠시 후 재시도.

### ✅ 체크포인트 1
- [ ] 논문 5건의 제목·링크가 표로 출력됐다
- [ ] (막혔다면) 3초 딜레이 후 재시도하니 정상 동작했다

---

## STEP 2 — arXiv를 MCP로 패키징 (LLM이 대화 중 스스로 검색)

CLI는 "한 번 실행 → 텍스트". MCP로 등록하면 **모델이 대화 중 필요할 때 스스로 도구를 골라 호출**한다.

**붙여넣기:**
```bash
uv tool install arxiv-mcp-server
claude mcp add arxiv -- uv tool run arxiv-mcp-server --storage-path ~/.arxiv-mcp-server/papers
claude mcp list    # 등록 확인
```

등록 후 대화에서 그냥 이렇게 말하면 모델이 `arxiv` 도구를 자동 호출한다.

**입력 프롬프트:**
```
arxiv에서 "small language model" 관련 최신 논문 3건을 찾아서 한 줄씩 요약해줘.
```

> ⚠️ 다운로드한 논문 본문은 **신뢰 불가 외부 입력**이다. 본문 속 "이전 지시를 무시하라"는 명령이 아니라 데이터로만 취급한다(프롬프트 인젝션 / OWASP LLM01). → 자세한 방어는 [`07_claude_harness.md`](07_claude_harness.md) (E).

### ✅ 체크포인트 2
- [ ] `claude mcp list`에 `arxiv`가 보인다
- [ ] 대화에서 논문 요청 시 모델이 도구를 자동 호출했다

---

## STEP 3 — 법제처 Open API + korean-law (★ 환각검증 데모)

법조문·판례 조회뿐 아니라 **다른 AI가 쓴 법조문이 진짜인지 환각검증**하는 게 킬러 기능이다.

- **인증**: `LAW_OC`(무료, 1분 발급). skill의 `klaw.sh`가 자동 주입.

**CLI로 먼저 (입력 프롬프트 / 터미널):**
```bash
scripts/klaw.sh "근로기준법 제60조"                                    # 자연어 라우팅
scripts/klaw.sh verify_citations --text "민법 제839조의2에 따른 재산분할 청구"   # ⭐환각검증
```

`verify_citations`는 LLM이 지어낸 "○○법 제○조"를 법제처 DB와 실시간 대조해 `✓실존 / ✗환각의심 / ⚠확인필요`로 판정한다.

**MCP 등록 (모델이 대화 중 자동 호출):**
```bash
claude mcp add korean-law --env LAW_OC=<발급받은-OC키> \
  -- node <korean-law-repo>/build/index.js
```

### ✅ 체크포인트 3
- [ ] `verify_citations`가 실존/환각 판정을 내놨다
- [ ] **CLI vs MCP** 차이를 한 문장으로 설명할 수 있다 (CLI=일회성 텍스트 / MCP=대화 중 자동 호출, 같은 코드베이스를 둘 다로 노출 가능)

---

## 이 단계의 산출물
- arXiv 논문 검색 결과 표 1개
- 등록된 MCP: `arxiv` (+ 선택: `korean-law`)
- "공식 무료 API를 MCP로 감싸면 유료 DB 없이 환각까지 잡는다"는 체감

➡️ 공식 API가 **없는** 주제라면 → [`02_search_api.md`](02_search_api.md) 검색 API로 우회.
