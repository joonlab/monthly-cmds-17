# 📚 LLM Wiki 캡스톤 — 실습 안내 (먼저 읽기)

> 이 폴더는 월간 CMDS 17회차 **캡스톤**입니다. 앞 단계(01~07)에서 배운 *수집·검증*을, **Karpathy의 LLM Wiki 패턴**(cmds-llm-wiki v1.3.0)으로 "스스로 자라는 검증된 나만의 백과사전"으로 굳힙니다.

---

## 🧠 한 문장

> **RAG는 질문할 때마다 매번 다시 검색**한다. **LLM Wiki는 LLM이 자료를 한 번 읽어 위키 페이지로 "컴파일"**하고, 새 자료가 들어올 때마다 기존 페이지를 갱신한다 → 점점 풍부해지는 **복리(compounding) 지식 베이스**.
> *"Obsidian은 IDE, LLM은 프로그래머, Wiki는 코드베이스." — Andrej Karpathy*

---

## 🏛 3계층 아키텍처 (이 볼트의 핵심)

```
00. Inbox/        ← 수집한 원본을 잠깐 모아두는 곳 (앞 단계 01~06의 결과를 여기로)
      │  /ingest
      ▼
10. Raw Sources/  ← 원본을 "그대로(verbatim)" 보존하는 불변 계층 (출처의 진실)
      │  LLM이 컴파일
      ▼
20. Wiki/         ← LLM이 만드는 합성 지식 (Concepts·Entities·Guides·MOC)
                    + 30. Queries/ ← 질문 답변을 위키로 역피드백 (복리)
```
규칙서(Schema) = 루트 `CLAUDE.md`. 사용자 맥락 = `Core Context.md`.

---

## 🚀 시작하기 (이 폴더에서 Claude Code 열기)

> ⚠️ 앞 실습은 상위 폴더(`cmds17-research-lab`)에서 했지만, **캡스톤은 이 `LLMWiki/` 폴더 안에서** Claude Code를 엽니다. 그래야 이 볼트 전용 7개 슬래시커맨드(`/ingest` 등)가 활성화됩니다.

```bash
cd LLMWiki        # 이 폴더로 이동
claude            # 여기서 Claude Code 실행
```

그다음 순서:
1. **`Core Context.md` 채우기** — 본인 정체성·"재활용 축"(왜 수집하나)·철학. (placeholder를 본인 맥락으로. Claude에게 "내 블로그 글 읽고 Core Context 채워줘"라고 시켜도 됨)
2. **`/status`** — 볼트 현재 상태 한눈에.
3. **`/ingest <URL 또는 파일>`** — 자료를 Raw Source로 보존 + Wiki 페이지 10~15개 컴파일. (수집 목적을 1회 묻습니다 = "미래의 나에게 보내는 편지")
4. **`/query <질문>`** — 쌓인 Wiki로 출처 인용 답변. 좋은 답은 `30. Queries/`로 역피드백.
5. **`/lint`** — 고아 페이지·끊긴 링크·모순·검증 누락 health check.

> 7개 커맨드: `/ingest` `/inbox` `/query` `/lint` `/status` `/reindex` `/refresh-context` (`.claude/commands/`).

---

## 🔗 앞 단계(수집)와 어떻게 연결되나

이 캡스톤의 **입력**이 곧 17회차 앞부분입니다:

| 앞 단계 | 산출 | LLM Wiki 연결 |
|--------|------|--------------|
| 01 공식 API (arXiv·법제처) | 논문·법령 | `/ingest <arXiv URL>` |
| 02 검색 API (Tavily 등) | 웹 동향 | 검색결과 URL을 `/ingest` |
| 03 Firecrawl | 사이트 본문 마크다운 | `00. Inbox/`에 저장 후 `/ingest` |
| 04 브라우저(Playwright) | 로그인/동적 페이지 | 추출본을 Inbox로 |
| 05 Gemini grounding | 출처 달린 답변 | groundingMetadata를 Wiki 각주로 |
| 06~07 하네스·검증 | 교차검증된 사실 | `confidence`/`explored` 프론트매터로 |

> 즉 "AI가 4단 사다리로 모아온 검증된 자료"가 → Inbox → `/ingest` → **복리로 자라는 나만의 위키**가 됩니다.

---

## ⚙️ 준비물 — 가볍게 시작, 선택적으로 고도화

| 항목 | 필수? | 비고 |
|------|------|------|
| Claude Code | ✅ | 이 폴더에서 `claude` |
| Obsidian | 권장 | 이 폴더를 "볼트로 열기" 하면 그래프뷰·위키링크 시각화. 없어도 마크다운으로 동작 |
| Web Clipper 설정 | 선택 | `90. Settings/Sharing/clipper-*.json` 17종 — 브라우저에서 기사·논문·X를 Inbox로 바로 클리핑 |
| **qmd (시맨틱 검색)** | **선택** | 아래 참고 |

### qmd는 "선택"입니다 (없어도 전부 동작)
- 커맨드들은 `qmd`(로컬 시맨틱 검색 MCP)가 있으면 의미 기반 검색을, **없으면 자동으로 `Grep`/`Glob`(키워드)로 폴백**합니다.
- `.claude/hooks/qmd-reindex.sh`는 qmd가 설치돼 있을 때만 백그라운드로 재인덱싱하고, 없으면 조용히 넘어갑니다 → 실습에 지장 없음.
- qmd를 나중에 붙이려면: `90. Settings/qmd-config-template.yml`을 `~/.config/qmd/index.yml`로 복사 후 `qmd update && qmd embed`.

### 운영 모드
- **Standalone(권장·기본)**: 이 볼트 하나로 완결. `Core Context.md` §5(Mothership)는 비우거나 삭제.
- **Satellite**: 이미 쓰는 PKM 볼트가 있으면 §5에 연결 → 교차링크. (자세히는 `90. Settings/Sharing/Setup Guide.md`)

---

## 🔒 안전장치 (하네스가 강제하는 것)
- `PostToolUse` 훅 `validate-raw-source.sh`: Raw Source에 `## Original Content`(원문 verbatim)가 없으면 **차단** → "요약으로 원본을 대체"하는 환각/유실 방지.
- 외부 콘텐츠 = 데이터 취급(프롬프트 인젝션 방지)은 `CLAUDE.md`에 명문화.

---

## 📂 더 읽기
- `README.md` / `LLM-Wiki-Starter-Kit.md` — 패턴 개요·5분 퀵스타트
- `Setup Guide` → `90. Settings/Sharing/Setup Guide.md` — 정식 셋업(모드 A/B)
- `CLAUDE.md` — 볼트 규칙서(스키마) · `Core Context.md` — 사용자 맥락 템플릿
- `index.md` / `log.md` — 마스터 인덱스 · 변경 이력

➡️ 준비됐으면: `cd LLMWiki` → `claude` → `Core Context.md` 채우고 → `/ingest`!
