# 04. 4순위 — 브라우저 자동화 직접 (Playwright · cmux · DevTools Recorder)

> **준비물**: 없음(데모 사이트) / 로그인 시연 시 **본인 계정**
> **예상시간**: 20분 · **난이도**: ★★★☆☆
> **사전 설치**: `pip install playwright && playwright install`

---

## ⚠️ 코드 짜기 전에 — 스크래핑 윤리·합법 (반드시 먼저 읽기)

기술적으로 "가능"한 것과 "해도 되는" 것은 다르다.

1. **robots.txt 확인** — `https://사이트/robots.txt`의 `Disallow`는 자동 수집 비권장 신호.
2. **ToS 확인** — X(트위터)·쿠팡 등은 자동 수집을 ToS에서 **명시적으로 금지**. 위반 시 계정 정지·법적 분쟁.
3. **개인정보·저작권** — 공개 게시물이라도 무단 재배포는 별개 문제(개인정보보호법·저작권법).
4. **부하/매너** — 요청 간 지연·동시성 제한. 짧은 간격 대량 요청은 DDoS로 간주될 수 있음.
5. **로그인 사이트** — 본인 계정·본인 권한 범위 내 데이터만.
6. **우선순위** — 공식 API > 공개데이터(CSV/RSS) > 스크래핑(최후 수단).

> 🎓 **교육 시연은 `demo.playwright.dev` 또는 본인 소유 페이지로만 한다.**

---

## STEP 1 — Playwright: 범용 표준 + 로그인 세션 재사용

로그인이 필요한 사이트는 **한 번 로그인 → 상태 저장 → 재사용**한다. 전문은 [`code/playwright_auth.py`](../code/playwright_auth.py).

**붙여넣기 (저장 → 재사용):**
```bash
python code/playwright_auth.py save     # (1) 브라우저 떠서 본인 로그인 → state.json 저장
python code/playwright_auth.py          # (2) state.json 재사용해 로그인 단계 건너뜀
```

```python
ctx = b.new_context(storage_state="state.json")   # ★ 로그인 단계 건너뜀
```

> 🚨 `state.json`은 본인 사칭 가능한 쿠키를 포함한다 → **`.gitignore` 필수, 절대 커밋 금지** (이 키트에 이미 포함).

### ✅ 체크포인트 1
- [ ] 데모 사이트 페이지 제목이 출력됐다
- [ ] `state.json`이 `.gitignore`에 들어 있다

---

## STEP 2 — Playwright Codegen: 클릭하면 코드가 나온다

```bash
playwright codegen demo.playwright.dev/todomvc   # 시연→Python 초안 자동생성
```

→ 생성된 코드를 Claude Code에 붙여 **"반복 처리·CSV 저장 추가"** 를 요청한다 = 초안→완성.

---

## STEP 3 — Chrome DevTools Recorder: 코드 0줄로 녹화

1. DevTools > More tools > **Recorder** → Start → 플로우 수행 → End → Replay 검증.
2. **Export** → Puppeteer / `@puppeteer/replay` / (확장 설치 시) Playwright 스크립트.
3. 그 코드를 Claude Code에 붙여:

**입력 프롬프트:**
```
아래는 DevTools Recorder로 녹화한 플로우야. Playwright Python으로 변환하고,
결과 데이터를 CSV로 저장하는 코드까지 추가해줘.
<여기에 export한 코드 붙여넣기>
```

비개발자도 녹화만으로 자동화 초안을 얻는다.

---

## STEP 4 — cmux browser CLI (박준 표준 · 병렬 조사)

이 강의 자료 자체가 cmux browser 4명 병렬 조사로 만들어졌다.

```
open → wait → eval/get → (interact) → verify
cmux browser open <url> → surface:XX → wait --load-state complete → eval "document.body.innerText"
```

- 로그인/세션: `state save/load <path>` (Playwright storage_state와 동일 개념)
- **병렬 조사**: 백그라운드 서브에이전트마다 독립 surface(최대 5)

> cmux-browser는 skill로 활성화한다 (`Skill("cmux-browser")`). 활성화 후 모든 웹 상호작용을 cmux 명령으로 수행.

---

## 대표 시나리오 3선 (ToS 준수 전제 · 코드는 [`code/`](../code/) 참조)

| 시나리오 | 왜 브라우저인가 | 핵심 기법 |
|---------|----------------|----------|
| ① X(트위터) 게시물 | 공식 API 유료·제한 | storage_state 로그인 + 무한스크롤(지연 필수) |
| ② 쿠팡류 상품정보 | 공식 검색 API 미제공 | user-agent/locale 설정 + 셀렉터 추출 |
| ③ 로그인 사이트 데이터 | 본인 계정에만 보임 | storage_state 재사용 → 표 추출 → CSV |

> [`code/playwright_scrape.py`](../code/playwright_scrape.py) 가 ②③의 골격이다(데모 사이트 대상).

---

## 이 단계의 산출물
- Playwright/cmux로 추출한 데이터 1건
- `state.json` 재사용 흐름 체득

➡️ "도구를 내가 고르는" 1~4단을 넘어, **AI가 검색·읽기·종합을 통째로** 하게 하려면 → [`05_gemini.md`](05_gemini.md)
