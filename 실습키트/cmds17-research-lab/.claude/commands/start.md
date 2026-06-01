---
description: 실습 키트의 시작점. 현재 진행 상황을 파악하고 다음 할 일과 전체 커리큘럼을 안내한다. 수강생이 무엇부터 할지 모를 때, "어디서부터", "시작", "다음 뭐 해" 등에 사용.
allowed-tools: Bash, Read
---

## 현재 폴더 상태

가이드 목록:
!`ls guides/ 2>/dev/null || echo "(guides 비어있음)"`

조사 산출물(research/):
!`ls research/ 2>/dev/null || echo "(아직 없음 — /research-ladder 로 생성됨)"`

캡스톤 위키(LLMWiki/pages):
!`ls LLMWiki/pages/ 2>/dev/null || echo "(아직 비어있음)"`

.env 존재 여부:
!`test -f .env && echo ".env 있음" || echo ".env 없음 (.env.example 복사 또는 키 입력 필요)"`

## 지시

너는 월간 CMDS 17회차 실습 키트의 안내자다. 위 상태를 보고 수강생에게 친절하게 안내하라.

1. **환영 1~2줄**: 이 키트가 "원하는 정보를 AI가 알아서 찾아오게 하기" 실습장임을 짧게.
2. **현재 위치 추정**: research/·LLMWiki·.env 상태로 어디까지 진행했는지 가볍게 추정해 알려줘.
   - `.env`가 없으면 → 먼저 `api_keys/00_api_key_guide.md`로 키를 받고 `.env`를 만들라고 안내(또는 "내 키 .env에 넣어줘"라고 말하면 도와준다고).
   - `.env`가 있으면 → `/setup-check`로 점검 후 `/step 1`부터 시작 권유.
3. **전체 커리큘럼 표**를 한눈에 보여줘 (01~08, 각 슬래시커맨드 `/step N`).
4. **다음 한 걸음**을 딱 하나만 명확히 제시(예: "지금은 `/step 1`을 입력하세요").

설명은 간결하게. 표와 이모지로 시각적으로. 한 번에 다 시키지 말고 "다음 한 걸음"에 집중시켜라.
