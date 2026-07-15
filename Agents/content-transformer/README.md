# Content Transformer Agent

**Version:** 1.0.0  
**Created:** 2026-07-15  
**Type:** 공용 에이전트

## 목적

트렌드 콘텐츠(이미지 + 메타데이터)를 분석하여 **맥락(주제, 형식, 스타일)은 유지하되 세부 내용만 변형**하는 전문 에이전트.

image-generator의 `image_edit` 모드에 최적화된 프롬프트를 자동 생성합니다.

---

## 핵심 기능

1. **맥락 분석**: OCR/Vision API로 이미지 + 메타데이터 분석
2. **맥락 보존**: 주제, 형식, 스타일 추출 및 유지
3. **콘텐츠 변형**: 세부 항목만 변경
4. **프롬프트 생성**: image_edit용 구조화된 프롬프트 자동 생성

---

## 사용 시나리오

### Before (수동 변형)
```
프로젝트 에이전트가 수동으로 프롬프트 작성
↓
실수: "여름 빨래 팁" → "아침 공복 운동" (주제 완전 변경) ❌
```

### After (자동 변형)
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

## 입력 예시

```yaml
reference_image: "/path/to/ref_image.jpg"
reference_metadata:
  caption: "여름철 빨래 관리 꿀팁 💕"
  hashtags: ["#빨래팁", "#쉽니제거"]
  topic: "생활팁"
transformation_mode: "context_preserving"  # 맥락 완전 보존
variation_level: "low"  # 최소 변경
target_language: "ko"
```

---

## 출력 예시

```json
{
  "original_context": {
    "theme": "여름 빨래 팁",
    "format": "numbered_list",
    "item_count": 10,
    "style": "cute_illustration",
    "color_scheme": "pastel_beige",
    "aspect_ratio": "9:16"
  },
  
  "transformed_content": {
    "title": "빨래 쉽니 제로! 여름 세탁 비법 10가지",
    "item_count": 10,
    "summary": "Similar laundry tips with refreshed content"
  },
  
  "image_edit_prompt": "KEEP the exact same layout and structure of a Korean laundry tips card...",
  
  "metadata": {
    "transformation_applied": true,
    "variation_level": "low",
    "context_preserved": true,
    "analysis_method": "ocr+manual"
  }
}
```

---

## 변형 모드

### 1. context_preserving (기본, 가장 안전)
- 주제 100% 유지
- 형식 100% 유지
- 스타일 100% 유지
- 세부 항목만 변경

### 2. theme_variation
- 주제 카테고리 유지, 세부 주제 변경
- 형식 유지
- 예: "여름 빨래 팁" → "빨래 건조 시간 단축 팁"

### 3. style_variation
- 주제 유지
- 형식 유지
- 스타일만 변경 (cute → minimalist)

---

## 품질 검증

**자동 검증 항목:**
- ✅ 주제 키워드 Jaccard 유사도 ≥ 0.6
- ✅ 항목 개수 변화 ≤ ±3개
- ✅ 스타일 키워드 일치
- ✅ 한국어 자연스러움

---

## 의존성

**필수:**
- pytesseract (OCR)
- Pillow (이미지 분석)

**선택 (더 높은 정확도):**
- OpenAI Vision API
- Anthropic Claude Vision

---

## 비용

- **기본 (OCR):** 무료
- **Vision API 사용 시:** $0.01-0.02/image

---

## 사용 프로젝트

- health-fitness-cards (트렌드 카드 자동 생성)
- [추가 예정]

---

## 관련 에이전트

- **trend-research-agent**: 트렌드 수집
- **image-generator**: 이미지 생성 (image_edit 모드)

---

## 버전 이력

- **1.0.0** (2026-07-15): 초기 생성
