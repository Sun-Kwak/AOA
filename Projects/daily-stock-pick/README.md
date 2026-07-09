# 해외 뉴스 기반 오늘의 추천 주

## 프로젝트 목적

영어권 해외 뉴스를 수집·번역하고, 한국 주식 추천 종목을 도출하여
일일 보고서를 자동 생성한다.

---

## 워크플로우

```
1. news-fetcher-agent   → 영어권 뉴스 핫 토픽 10개 수집
        ↓ (pipeline)
2. translation-agent    → 보고서용 한국어 번역
        ↓
3. stock-recommendation-agent  → 긍정적 영향 한국 주식 추천 (최대 10종목)
        ↓
4. Project Agent (Root) → 최종 검토 및 보고서 생성
        ↓
   Outputs/daily-report-YYYYMMDD.md
```

---

## 실행 방법

Root Orchestrator에게 다음을 요청:

```
"daily-stock-pick 프로젝트의 news-to-stock-workflow를 실행해줘"
또는
"오늘의 추천 주 보고서 만들어줘"
```

---

## 출력 파일

`Projects/daily-stock-pick/Outputs/daily-report-YYYYMMDD.md`

---

## 에이전트 구성

| 에이전트 | 유형 | 역할 |
|---------|------|------|
| news-fetcher-agent | 공용 | 해외 뉴스 수집 |
| translation-agent | 공용 | 한국어 번역 |
| stock-recommendation-agent | 프로젝트 전용 | 한국 주식 추천 |

---

## 투자 유의사항

본 프로젝트의 출력물은 AI 분석 결과이며 투자 권유가 아님.
