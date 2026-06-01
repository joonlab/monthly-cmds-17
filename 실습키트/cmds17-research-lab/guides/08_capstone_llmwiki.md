# 08. 캡스톤 — 나만의 LLM Wiki (Karpathy 패턴, cmds-llm-wiki v1.3.0)

> **준비물**: Claude Code · (권장) Obsidian · 검색/수집 키 1개 이상(앞 단계에서 발급) · (선택) qmd
> **예상시간**: 60분 · **난이도**: ★★★★★
> **작업 폴더**: 이 키트의 [`LLMWiki/`](../LLMWiki/) — **실제 프로덕션 볼트 v1.3.0**가 들어 있습니다
> 🧭 먼저 읽기: [`LLMWiki/00_실습_안내_READ_ME_FIRST.md`](../LLMWiki/00_실습_안내_READ_ME_FIRST.md)

---

## 캡스톤 한 줄

> **"AI가 사다리(0→4단)로 모아 교차검증한 자료를 → `/ingest` 한 줄로 → 복리로 자라는 검증된 나만의 위키 백과로 컴파일한다."**
> *RAG = 질문마다 매번 재검색. LLM Wiki = 한 번 읽어 위키로 컴파일하고 계속 갱신 → compounding knowledge.*
> *"Obsidian은 IDE, LLM은 프로그래머, Wiki는 코드베이스." — Andrej Karpathy*

```
01~06 수집/검증 ─▶ 00. Inbox/ ─/ingest─▶ 10. Raw Sources/(원문보존) ─컴파일─▶ 20. Wiki/(합성지식)
                                                                          /query  ▲   │ 역피드백
                                                                                  └── 30. Queries/
```

> 이 캡스톤은 수집 기법을 다시 가르치지 않는다. 01~07의 사다리·검증·하네스를 **Karpathy LLM Wiki 시스템 하나로 엮는 법**을 다룬다.

---

## STEP 0 — 볼트 열기 & 구조 이해 (10분)

앞 실습은 상위 폴더에서 했지만, **캡스톤은 `LLMWiki/` 폴더 안에서** Claude Code를 연다 (그래야 이 볼트 전용 7개 슬래시커맨드가 활성화됨).

```bash
cd LLMWiki        # 키트 안의 이 폴더로 이동
claude            # 여기서 Claude Code 실행
```

**3계층 아키텍처** (이 시스템의 심장):
- `10. Raw Sources/` — 원본을 **그대로(verbatim) 보존**하는 불변 계층. (소스코드)
- `20. Wiki/` — LLM이 만드는 합성 지식: `21.Concepts`/`22.Entities`/`23.Guides`/`24.Maps(MOC)`. (실행파일)
- 루트 `CLAUDE.md` — 볼트 규칙서(스키마). `Core Context.md` — 사용자 맥락.

**입력 프롬프트:**
```
이 볼트의 CLAUDE.md(스키마)와 index.md, LLM-Wiki-Starter-Kit.md를 읽고,
이 LLM Wiki가 어떻게 동작하는지(3계층, ingest-query-lint) 1단락으로 설명해줘.
```

### ✅ 체크포인트 0
- [ ] `LLMWiki/` 안에서 `claude`를 열었고, 슬래시커맨드 `/ingest /query /lint /status /inbox /reindex /refresh-context`가 보인다
- [ ] 3계층(Raw Sources→Wiki, 규칙서 CLAUDE.md)을 한 줄로 설명할 수 있다

---

## STEP 1 — Core Context 채우기 (10분) · "왜 수집하는가"

이 시스템의 차별점: 수집 전에 **"미래의 내가 이걸 왜 다시 볼까"**(재활용 축)를 먼저 정한다. `Core Context.md`가 그 맥락이고, LLM이 ingest/query 전에 반드시 먼저 읽는다.

**입력 프롬프트 (직접 채우기):**
```
Core Context.md 를 열어서 §1 정체성, §2 재활용 축(5~9개: 예 학술/저술/강의/컨설팅/제품/에세이/커뮤니티)을
내 상황에 맞게 채워줘. 다 채우면 frontmatter status를 active로, snapshot_date를 오늘로 바꿔줘.
```
> 💡 블로그·노트가 이미 있으면: "내 글 OO를 읽고 Core Context의 정체성·철학을 추론해서 채워줘"라고 시켜도 된다.

### ✅ 체크포인트 1
- [ ] `Core Context.md` §1·§2가 채워지고 `status: active`
- [ ] (Standalone) §5 Mothership 섹션은 비우거나 삭제했다

---

## STEP 2 — 현재 상태 확인 `/status` (2분)

```
/status
```
Raw Sources·Wiki·MOC·Inbox 수, collectionPurpose 커버리지, Core Context 나이를 한눈에 보여준다. (처음엔 Karpathy 원문 ingest 예시만 있음)

### ✅ 체크포인트 2
- [ ] `/status`가 볼트 통계를 출력했다

---

## STEP 3 — 자료 수집해서 Inbox에 넣기 (10분) · 01~06 재활용

앞 단계에서 배운 방법으로 자료를 모아 `00. Inbox/`에 넣는다. 세 가지 길:

1. **Web Clipper (가장 편함 — 사다리 0순위)** — Web Clipper는 별도 서비스·키 없이 브라우저에서 바로 쓰는 **0순위 수집 도구**다. `90. Settings/Sharing/clipper-*.json` 17종을 Obsidian Web Clipper에 등록하면, 브라우저에서 기사·논문·X·유튜브를 버튼 한 번으로 `00. Inbox/`에 카테고리별 저장. (`90. Settings/Sharing/Setup Guide.md` 참고)
2. **앞 단계 스크립트** — arXiv/Tavily/Firecrawl(01~03)로 모은 결과를 `00. Inbox/01. Articles/` 등에 `.md`로 저장.
   ```
   code/firecrawl_demo.py 패턴으로 <블로그 URL>을 마크다운으로 긁어서
   LLMWiki/00. Inbox/01. Articles/ 에 저장해줘.
   ```
3. **URL 직접** — `/ingest`에 URL을 바로 줘도 된다(아래 STEP 4).

### ✅ 체크포인트 3
- [ ] `00. Inbox/`(또는 하위 카테고리)에 자료 1건 이상이 들어왔다 (또는 ingest할 URL을 준비했다)

---

## STEP 4 — `/ingest` — 원본 보존 + 위키 컴파일 (15분) ★핵심

```
/ingest <URL 또는 Inbox 파일명>      # 예: /ingest https://arxiv.org/abs/2404.xxxxx
/ingest all                          # Inbox 전체 일괄
```

`/ingest`가 자동으로 수행하는 것:
1. **수집 목적 1회 질문** ("미래의 나에게 보내는 편지" — §2 재활용 축 중 어디에 쓸지). → `collectionPurpose`에 기록.
2. **Raw Source 저장** — `10. Raw Sources/`에 **원문 그대로(`## Original Content`)** 보존. (요약으로 대체 금지 — 훅이 차단)
3. **Wiki 페이지 10~15개** 생성/갱신 — Concepts·Entities·Guides. 기존 페이지는 **업데이트 우선**.
4. **연결** — `[[위키링크]]` + MOC + `index.md`/`log.md` 갱신.

> 🔒 **하네스 안전장치**: `10. Raw Sources/`에 `## Original Content`(원문)가 없으면 `validate-raw-source.sh` 훅이 **쓰기를 차단**한다 → "요약으로 원본을 대체"하는 환각/유실을 시스템이 막는다. 이게 단순 프롬프트보다 강한 이유.
> ⚠️ 외부 본문 속 "이전 지시 무시" = 데이터로만 취급(인젝션 방지, `CLAUDE.md` 규칙).

### ✅ 체크포인트 4
- [ ] `/ingest`가 수집 목적을 물었고, 답이 `collectionPurpose`에 기록됐다
- [ ] `10. Raw Sources/`에 `## Original Content`가 보존됐다
- [ ] `20. Wiki/`에 새 페이지가 생기고 `index.md`가 갱신됐다

---

## STEP 5 — `/query` — 쌓인 위키로 답하고 역피드백 (10분)

```
/query 소형 LLM이 온디바이스에서 갖는 한계는?
```
- 위키 페이지를 읽어 **출처(`[[위키링크]]`) 인용** 답변을 합성.
- 답이 충실하면 `30. Queries/`에 저장 → **다음 질문의 재료**가 됨(복리).
- 답하다 발견한 **지식 갭·모순**을 위키에 피드백(`> [!warning]`).
- 답이 어느 **재활용 축**에 쓸모인지 한 줄로 연결.

### ✅ 체크포인트 5
- [ ] `/query` 답변에 위키 페이지 인용이 달렸다
- [ ] (충실한 답이면) `30. Queries/`에 결과가 저장됐다

---

## STEP 6 — `/lint` + Obsidian 시각화 (8분)

```
/lint
```
고아 페이지·끊긴 링크·모순·stale·index 동기화·MOC 커버리지·**검증 프론트매터(collectionPurpose/explored/Bias Check)** 까지 health check.

**Obsidian으로 열기**: 이 `LLMWiki/` 폴더를 Obsidian에서 "폴더를 볼트로 열기" → **그래프뷰**에서 위키링크가 연결된 지식망이 보인다.

### ✅ 체크포인트 6
- [ ] `/lint`가 health 리포트를 냈다 (고아/끊긴링크/커버리지)
- [ ] (Obsidian) 그래프뷰에서 페이지 연결을 확인했다

---

## STEP 7 — 자동화로 "스스로 자라게" (5분)

- **반복 수집**: Web Clipper로 평소 관심 자료를 Inbox에 쌓아두고, 모이면 `/inbox`로 일괄 `/ingest`.
- **주기 갱신(cron)**:
  ```
  매주 월요일 오전 9시 즈음(정각 피해서) Inbox에 쌓인 자료를 /inbox로 일괄 ingest하고
  /lint로 health check하는 루틴을 만들어줘. (recurring은 7일 후 자동 만료 — 재설정 필요)
  ```
- **qmd(선택)**: 위키가 커지면 `90. Settings/qmd-config-template.yml`을 `~/.config/qmd/index.yml`로 복사 → `qmd update && qmd embed` → `/query`가 의미 기반 검색으로 업그레이드. (없으면 Grep 폴백 — 실습엔 불필요)

> 💡 Web Clipper(입력) + `/ingest`(컴파일) + `/query`(복리) + `/lint`(건강) = **AI한테 모아두라 시켜놓으면, 교차검증을 통과한 사실만 쌓이는 나만의 검증된 백과사전.**

---

## STEP 8 — 완성 체크리스트

- [ ] `LLMWiki/` 안에서 `claude`로 7개 커맨드 사용
- [ ] `Core Context.md` §1·§2 채움 + `status: active`
- [ ] `/ingest`로 자료 1건 이상: Raw Source 원문 보존 + Wiki 페이지 생성 + `collectionPurpose` 기록
- [ ] `/query`로 출처 인용 답변 (충실하면 `30. Queries/` 저장)
- [ ] `/lint` health 리포트 통과 (고아/끊긴 링크 정리)
- [ ] (권장) Obsidian 그래프뷰로 지식망 확인
- [ ] (선택) Web Clipper 등록 / cron 주기 갱신 / qmd 시맨틱 검색
- [ ] `.env`·키 등 비밀정보 `.gitignore` 제외 (볼트 `.gitignore` 확인)

---

## 마무리 한 줄

> 17회차 전체가 여기서 만난다: **(01~06) AI에게 정보를 모으게 하는 법 + (07) Claude Code를 하네스로 굳히는 법 + (08) 그 결과를 Karpathy LLM Wiki로 복리 누적** → "AI한테 시켜놓으면 검증된 나만의 위키 백과가 스스로 자란다."

📖 더 깊이: 볼트의 [`README.md`](../LLMWiki/README.md) · [`LLM-Wiki-Starter-Kit.md`](../LLMWiki/LLM-Wiki-Starter-Kit.md) · [`Setup Guide`](../LLMWiki/90.%20Settings/Sharing/Setup%20Guide.md)
