# Content Transformer

**ID:** content-transformer  
**Version:** 1.0.0  
**Status:** Active  
**Created:** 2026-07-15

---

## 메타데이터

```yaml
id: content-transformer
name: Content Transformer
version: 1.0.0
type: 공용 에이전트
category: Content Analysis & Transformation
tags:
  - content-analysis
  - prompt-generation
  - context-preservation
  - image-editing
```

---

## 설명

트렌드 콘텐츠(이미지 + 메타데이터)를 분석하여 **맥락(주제, 형식, 스타일)은 유지하되 세부 내용만 변형**하는 전문 에이전트.

image-generator의 `image_edit` 모드에 최적화된 프롬프트를 자동 생성합니다.

---

## 핵심 기능

| 기능 | 설명 |
|------|------|
| 맥락 분석 | OCR/Vision API로 이미지 + 메타데이터 분석 |
| 맥락 보존 | 주제, 형식, 스타일 추출 및 유지 |
| 콘텐츠 변형 | 세부 항목만 변경 |
| 프롬프트 생성 | image_edit용 구조화된 프롬프트 자동 생성 |

---

## 사용 시나리오

### 문제 상황
- 프로젝트 에이전트가 수동으로 프롬프트 작성
- 실수: "여름 빨래 팁" → "아침 공복 운동" (주제 완전 변경) ❌

### 해결책
```
Phase 1: 트렌드 수집
↓
Phase 1.5: Content Transformer ✨
  - 이미지 분석
  - 맥락 추출: {"theme": "여름 빨래 팁", "format": "numbered_list"}
  - 세부 항목만 변형
  - 프롬프트 자동 생성
↓
Phase 2: 이미지 생성 (image_edit 모드)
```

---

## 입력 스키마

```yaml
reference_image: string  # 필수, 참조 이미지 경로
reference_metadata:      # 선택
  caption: string
  hashtags: array
  topic: string
transformation_mode: enum  # context_preserving | theme_variation | style_variation
variation_level: enum      # low | medium | high
target_language: string    # 기본값: ko
```

---

## 출력 스키마

```yaml
original_context:
  theme: string
  format: string
  item_count: integer
  style: string
  color_scheme: string
  aspect_ratio: string

transformed_content:
  title: string
  item_count: integer
  summary: string

image_edit_prompt: string  # image-generator에 전달

metadata:
  transformation_applied: boolean
  variation_level: string
  context_preserved: boolean
  analysis_method: string
```

---

## 변형 모드

### 1. context_preserving (기본)
- 주제 100% 유지
- 형식 100% 유지
- 스타일 100% 유지
- 세부 항목만 변경

### 2. theme_variation
- 주제 카테고리 유지, 세부 주제 변경
- 형식 유지

### 3. style_variation
- 주제 유지
- 형식 유지
- 스타일만 변경

---

## 품질 검증

**자동 검증:**
- ✅ 주제 키워드 Jaccard 유사도 ≥ 0.6
- ✅ 항목 개수 변화 ≤ ±3개
- ✅ 스타일 키워드 일치

---

## 의존성

**필수:**
- pytesseract (OCR)
- Pillow (이미지 분석)

**선택:**
- OpenAI Vision API (더 높은 정확도)
- Anthropic Claude Vision

---

## 비용

- **기본 (OCR):** 무료
- **Vision API 사용 시:** $0.01-0.02/image

---

## 사용 프로젝트

- health-fitness-cards (트렌드 카드 자동 생성)

---

## 관련 에이전트

- **trend-research-agent**: 트렌드 수집
- **image-generator**: 이미지 생성 (image_edit 모드)

---

## 파일 위치

- **Agent YAML:** `Agents/content-transformer/agent.yaml`
- **Prompt:** `Agents/content-transformer/prompt.md`
- **README:** `Agents/content-transformer/README.md`

---

## Best Practices

1. **transformation_mode: context_preserving 사용** (가장 안전)
2. **variation_level: low 시작** (점진적 변형)
3. **reference_metadata 제공** (분석 정확도 향상)
4. **검증 결과 확인** (context_preserved: true인지 확인)

---

## 버전 이력

- **1.0.0** (2026-07-15): 초기 생성
  - OCR 기반 맥락 분석
  - context_preserving 모드
  - image_edit 프롬프트 자동 생성
