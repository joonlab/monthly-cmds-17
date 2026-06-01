# 05. 한 단계 위 — AI에게 리서치를 통째로 위임 (Gemini)

> **준비물**: `GEMINI_API_KEY` (AI Studio 무료 발급, Grounding 무료 5,000 prompts/월)
> **예상시간**: 15분 · **난이도**: ★★★☆☆
> **사전 설치**: `pip install google-genai`

---

## 이 단계의 한 줄

> 1~4단은 "내가 도구를 골라 수집"한다. **Gemini는 검색·읽기·종합을 AI가 알아서 한다.**

난이도 사다리로 보면 효과가 극적이다:
**① 그냥 LLM(컷오프 한계) → ② grounding 한 줄(실시간+출처) → ③ Deep Research(자율 보고서)**

---

## STEP 1 — Google Search Grounding: 툴 한 줄

`generateContent`에 `google_search` 툴 하나만 붙이면 모델이 검색→읽기→인용을 자동 수행한다. 전문: [`code/gemini_grounding.py`](../code/gemini_grounding.py).

**핵심 코드:**
```python
from google import genai
from google.genai import types
client = genai.Client()                       # GEMINI_API_KEY 자동 인식
cfg = types.GenerateContentConfig(tools=[types.Tool(google_search=types.GoogleSearch())])
r = client.models.generate_content(model="gemini-3.5-flash",
        contents="2026년 소형 LLM 동향 요약", config=cfg)
print(r.text)
```

**입력 프롬프트 (Claude Code):**
```
code/gemini_grounding.py 를 실행해서 "2026년 소형 LLM 동향"을 grounding으로 조사하고,
groundingMetadata에서 각 문장의 근거 URL을 뽑아 각주로 붙여줘.
```

> ⭐ `r.candidates[0].grounding_metadata`의 `grounding_chunks`(web.uri/title) + `grounding_supports`(문장↔출처)로 **"이 문장은 이 URL 근거"** 인라인 각주를 만든다 → 캡스톤 위키 각주로 직결.

### ✅ 체크포인트 1
- [ ] 컷오프 이후 최신 내용이 출처와 함께 나왔다
- [ ] 각 문장에 근거 URL을 매핑할 수 있다

---

## STEP 2 — Deep Research Agent: 맡겨두고 받는 자율 보고서

`generate_content`가 **아니라** 별도 **Interactions API**(`client.interactions`)로만 접근한다. 수 분 소요라 `background=True` + 폴링. 전문: [`code/gemini_deep_research.py`](../code/gemini_deep_research.py).

**핵심 코드:**
```python
it = client.interactions.create(input="소형 LLM 상용화 동향 조사",
        agent="deep-research-preview-04-2026", background=True)
while True:
    it = client.interactions.get(it.id)
    if it.status == "completed": print(it.output_text); break
    if it.status == "failed": print("failed:", it.error); break
    time.sleep(10)
```

**입력 프롬프트:**
```
code/gemini_deep_research.py 로 "소형 LLM 상용화 동향"을 Deep Research에 맡기고,
완료되면 보고서를 받아서 핵심 결론만 5줄로 요약해줘.
```

- 계획 협업(`collaborative_planning`) · 시각화(`visualization`) · MCP · 문서 입력 지원
- **멘탈모델**: Grounding = 즉답 / Deep Research = "백그라운드 잡" → 에이전트적 사고 전환 포인트

### ✅ 체크포인트 2
- [ ] 폴링이 `completed`로 끝나고 보고서를 받았다
- [ ] Grounding vs Deep Research 차이를 한 문장으로 말할 수 있다

---

## 이 단계의 산출물
- 출처가 인라인 각주로 붙은 grounding 결과
- Deep Research 자율 보고서 1건

➡️ 이런 능력을 **내 앱에 코드로 임베드**하려면 → [`06_agent_sdk.md`](06_agent_sdk.md)
