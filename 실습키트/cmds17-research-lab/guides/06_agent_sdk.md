# 06. 코드로 임베드 — Claude Agent SDK (개념)

> **준비물**: `ANTHROPIC_API_KEY` (실습 시) — 이 단계는 **개념 소개**라 키 없이 읽기만 해도 OK
> **예상시간**: 10분 · **난이도**: ★★☆☆☆
> **사전 설치(실습 시)**: `pip install claude-agent-sdk anyio`

---

## 이 단계의 한 줄

> **손으로 한 번 시킬 일 = Claude Code CLI / 시스템이 반복 호출할 일 = Agent SDK.**

Agent SDK는 **Claude Code를 움직이는 엔진**(에이전트 루프 + 내장 도구 + 컨텍스트 관리)을 내 Python/TS 앱에 라이브러리로 임베드하는 것이다.

| | Claude Code (CLI/대화형) | Claude Agent SDK (앱 내장) |
|--|--------------------------|----------------------------|
| 사용 | 사람이 터미널에서 대화 | 코드(`query()`/`ClaudeSDKClient`)로 호출 |
| 트리거 | 사람이 타이핑 | HTTP·크론·파이프라인·다른 코드 |
| 적합 | 1회성 탐색·디버깅 | 반복·서비스화·앱 기능으로 내장 |
| 예 | "이 레포 버그 찾아줘" | "질문하면 리서치해 답하는 웹 서비스" |

---

## STEP 1 — 5줄로 시작

**핵심 코드:**
```python
import anyio
from claude_agent_sdk import query
async def main():
    async for msg in query(prompt="한 줄 자기소개"):
        print(msg)
anyio.run(main)   # 여기에 allowed_tools만 붙이면 곧장 웹 검색 에이전트
```

**입력 프롬프트 (Claude Code에게 시켜보기):**
```
claude_agent_sdk의 query()로 "한 줄 자기소개"를 출력하는 최소 스크립트를 만들고 실행해줘.
그다음 allowed_tools에 WebSearch를 추가해서 간단한 리서치 에이전트로 확장해줘.
```

> **자료조사 맥락**: WebSearch+WebFetch 리서치 에이전트를 **웹앱/백엔드로** 배포할 수 있다(예: FastAPI + SSE 스트리밍 리서치 웹앱). 커스텀 툴·훅·세션·스킬을 코드에서 통제.

---

## 꼭 짚을 구분

- **Client SDK**(도구 루프를 직접 구현) ≠ **Agent SDK**(도구 실행까지 내장).
- 이번 회차는 **"이런 게 있고 언제 쓴다"** 까지. 깊은 실습은 별도 회차 소재.

### ✅ 체크포인트
- [ ] CLI를 쓸 때 vs Agent SDK를 쓸 때를 구분할 수 있다
- [ ] "리서치 에이전트를 웹 서비스로 만든다"는 그림이 그려진다

---

➡️ 코드 임베드는 별도 회차. 이번 회차의 **심장**은 Claude Code 자체를 자료조사 머신으로 조립하는 것 → [`07_claude_harness.md`](07_claude_harness.md)
