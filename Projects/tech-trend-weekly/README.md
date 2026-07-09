# 주간 기술 트렌드 리포트 프로젝트

## Purpose

글로벌 기술 트렌드 뉴스를 수집, 번역, 분석하여 주간 트렌드 리포트를 자동 생성합니다.

---

## Project Structure

```
tech-trend-weekly/
├── manifest.yaml           # 프로젝트 설정
├── README.md              # 이 파일
├── Workflows/
│   └── weekly-tech-report-workflow.yaml
├── Agents/
│   └── trend-analyzer-agent/
│       ├── prompt.md
│       └── config.yaml
├── Templates/
│   └── weekly-report-template.md
├── Outputs/               # 생성된 리포트
└── Memory/                # 단계별 중간 결과
```

---

## Workflow

1. **Step 1:** news-fetcher-agent (공용) - 기술 뉴스 10개 수집
2. **Step 2:** translation-agent (공용) - 한국어 번역
3. **Step 3:** trend-analyzer-agent (프로젝트 전용) - 트렌드 분석
4. **Step 4:** Project Agent - 최종 리포트 생성

---

## Dependencies

### 공용 에이전트 (재사용)
- news-fetcher-agent: 뉴스 수집
- translation-agent: 번역

### 프로젝트 전용 에이전트
- trend-analyzer-agent: 트렌드 분석 및 인사이트 도출

---

## Usage

프로젝트 세션에서:
```
워크플로우 실행
```

입력:
- week_start_date: 2026-07-01
- week_end_date: 2026-07-07
- tech_categories: ["AI", "Cloud", "DevOps", "Web3"]

출력:
- Outputs/tech-trend-report-2026-07-01.md

---

## TODO

프로젝트 초기 설정 완료 후 첫 실행
