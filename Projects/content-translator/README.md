# 영문 콘텐츠 한국어 번역기

## Purpose

사용자가 제공한 영문 콘텐츠(문서, 이메일, 기사 등)를 한국어로 자동 번역합니다.

---

## Project Structure

```
content-translator/
├── manifest.yaml           # 프로젝트 설정
├── README.md              # 이 파일
├── Workflows/
│   └── simple-translation-workflow.yaml
├── Templates/
│   └── translation-output-template.md
├── Outputs/               # 번역 결과
└── Memory/                # 중간 결과
```

---

## Workflow

1. **Step 1:** translation-agent (공용) - 영문 콘텐츠 번역
2. **Step 2:** Project Agent - 최종 결과 파일 생성

---

## Dependencies

### 공용 에이전트 (재사용)
- translation-agent: 영문 → 한국어 번역

### 프로젝트 전용 에이전트
- 없음 (매우 단순한 프로젝트)

---

## Usage

프로젝트 세션에서:
```
워크플로우 실행

입력:
- source_file: /path/to/english-document.txt
- output_filename: translated-2026-07-09.md (선택)
```

출력:
- Outputs/translated-{timestamp}.md

---

## 특징

✅ **가장 단순한 AOA 프로젝트**
- 공용 에이전트 1개만 사용
- 프로젝트 전용 에이전트 없음
- 2단계 워크플로우

✅ **공용 에이전트 재사용 검증**
- translation-agent 단독 사용
- 다른 프로젝트와 독립된 컨텍스트

---

## TODO

프로젝트 초기 설정 완료 후 첫 실행
