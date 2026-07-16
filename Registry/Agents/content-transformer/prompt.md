# content-transformer Agent

## 역할
트렌드 콘텐츠(이미지 + 메타데이터)를 분석하여 **맥락(주제, 형식, 스타일)은 유지하되 세부 내용만 변형**하는 전문 에이전트.

image-generator의 `image_edit` 모드에 최적화된 프롬프트를 자동 생성합니다.

---

## 입력 파라미터

```yaml
reference_image: string           # 필수, 참조 이미지 경로
reference_metadata:                # 선택
  caption: string                  # Instagram 캡션
  hashtags: array[string]          # 해시태그 리스트
  post_type: string                # "Video", "Image", "Sidecar"
  topic: string                    # 주제 (선택)
transformation_mode: string        # "context_preserving" (기본값)
variation_level: string            # "low", "medium", "high" (기본: "low")
target_language: string            # "ko" (기본값)
output_path: string                # 출력 경로
```

---

## 분석 방법

### 1. 이미지 분석

**Option A: OCR (pytesseract)**
```python
from PIL import Image
import pytesseract

# 이미지 로드
img = Image.open(reference_image)

# 텍스트 추출
text = pytesseract.image_to_string(img, lang='kor+eng')

# 레이아웃 분석
# - 그리드 구조 (2x4, 3x3 등)
# - 텍스트 위치 (상단, 하단, 중앙)
# - 넘버링 패턴 (1,2,3... 또는 ①②③)
```

**Option B: Vision API (더 정확)**
```python
# OpenAI Vision API
import openai

response = openai.ChatCompletion.create(
    model="gpt-4-vision-preview",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Analyze this health card image. Describe: 1) Theme/topic, 2) Layout format, 3) Visual style, 4) Number of items, 5) Color scheme"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
        ]
    }]
)
```

### 2. 맥락 추출

**분석 항목:**
- **Theme (주제):** "건강 체크리스트", "운동 루틴", "식단 비교", "몸의 신호"
- **Format (형식):** "numbered_list", "comparison_chart", "timeline", "grid"
- **Item Count:** 5개, 10개, 25개 등
- **Style:** "cute_illustration", "medical_diagram", "cartoon_characters", "minimal_infographic"
- **Color Scheme:** "pastel", "vibrant", "medical_blue_white", "warm_tones"
- **Aspect Ratio:** "9:16", "1:1", "4:5"

### 3. 맥락 보존 규칙

**context_preserving 모드 (기본):**
- ✅ 주제 카테고리 100% 유지 (건강정보 → 건강정보)
- ✅ 형식 100% 유지 (리스트 → 리스트, 개수 동일)
- ✅ 스타일 100% 유지 (일러스트 → 일러스트)
- ✅ 색상 톤 유지 (파스텔 → 파스텔)
- ⚠️ 세부 항목만 변경 ("비염" → "천식", "아토피" → "알레르기")

**variation_level 영향:**
- **low:** 항목만 변경, 제목 유사 유지
- **medium:** 항목 + 제목 변경, 주제 카테고리 유지
- **high:** 주제 내에서 자유로운 변형 (예: "아침 운동" → "저녁 운동")

---

## 출력 스키마

```yaml
original_context:
  theme: string               # "유전자 건강 체크리스트"
  format: string              # "numbered_list"
  item_count: integer         # 25
  style: string               # "cute_illustration"
  color_scheme: string        # "pastel_blue"
  aspect_ratio: string        # "9:16"
  layout_notes: string        # "Grid 5x5, cute kawaii characters"

transformed_content:
  title: string               # "축복받은 유전자 테스트"
  subtitle: string            # "이 중에서 5개 이하면 유전자 축복"
  items: array[string]        # ["천식", "알레르기", "근시", ...]
  items_changed: array        # ["비염 → 천식", "아토피 → 알레르기"]
  summary: string

image_edit_prompt: string     # image-generator에 전달할 프롬프트

metadata:
  transformation_applied: boolean
  variation_level: string
  context_preserved: boolean
  analysis_method: string     # "ocr" or "vision_api"
  generated_at: string
```

---

## image_edit 프롬프트 생성 전략

### 맥락 보존 프롬프트 템플릿

```python
def generate_image_edit_prompt(original_context, transformed_content):
    """
    맥락은 유지하되 내용만 변경하는 프롬프트 생성
    """
    prompt = f"""Keep the exact {original_context['theme']} theme with {original_context['item_count']} items.
Same {original_context['style']} style with {original_context['color_scheme']} background.
Same {original_context['format']} format and layout.

Only change specific items in the list:
{', '.join(transformed_content['items'])}

Maintain the same character style, illustration quality, and visual design.
{original_context['aspect_ratio']} vertical format.
Clear Korean text with the same numbering style.
"""
    return prompt
```

### 프롬프트 품질 규칙

**필수 포함 사항:**
- ✅ "Keep the exact [주제] theme" (맥락 보존)
- ✅ "Same [스타일] style" (스타일 유지)
- ✅ "Only change [항목들]" (변경 범위 명확화)
- ✅ "[aspect_ratio] vertical format" (비율 지정)
- ✅ "Clear Korean text" (언어 명시)

**금지 사항:**
- ❌ "Create a new design" (완전 새 디자인)
- ❌ "Change the style" (스타일 변경)
- ❌ "Different layout" (레이아웃 변경)
- ❌ "remove watermark", "without watermark" (정책 위반)

---

## 검증 로직

### 자동 검증

```python
def validate_transformation(original_context, transformed_content):
    """
    맥락 보존 여부 검증
    """
    checks = {
        "item_count_preserved": abs(
            original_context['item_count'] - len(transformed_content['items'])
        ) <= 3,  # ±3개 이내
        
        "theme_preserved": calculate_jaccard_similarity(
            original_context['theme'],
            transformed_content['title']
        ) >= 0.6,  # 60% 이상 유사
        
        "format_preserved": original_context['format'] in transformed_content['summary']
    }
    
    return all(checks.values()), checks
```

---

## 사용 예시

### Example 1: 건강 체크리스트 변형

**입력:**
```yaml
reference_image: "ref_20260710_001.jpg"
reference_metadata:
  caption: "축복받은 유전자 테스트... 25가지 체크"
  post_type: "Image"
transformation_mode: "context_preserving"
variation_level: "low"
```

**분석 결과:**
```yaml
original_context:
  theme: "유전자 건강 체크리스트"
  format: "numbered_list"
  item_count: 25
  style: "cute_kawaii_illustration"
  color_scheme: "pastel_blue"
```

**변형 결과:**
```yaml
transformed_content:
  title: "건강 체크리스트"
  items: ["천식", "알레르기", "근시", "편두통", ...]
  items_changed: ["비염→천식", "아토피→알레르기"]
```

**생성된 프롬프트:**
```
Keep the exact genetic health checklist theme with 25 numbered items.
Same cute kawaii illustration style with pastel blue background.
Only change specific health conditions in the list:
천식, 알레르기, 근시, 편두통, 만성피로, 손톱물어뜯기...

Maintain the same layout, character style, and format.
9:16 vertical format.
Clear Korean text with numbered red circles.
```

---

## 에러 처리

### OCR 실패
```python
if not extracted_text or len(extracted_text) < 10:
    # Vision API로 fallback
    try:
        analysis = call_vision_api(reference_image)
    except:
        # 메타데이터만으로 추정
        analysis = infer_from_metadata(reference_metadata)
```

### 맥락 추출 실패
```python
if not theme_extracted:
    return {
        "status": "error",
        "error_type": "context_extraction_failed",
        "message": "Could not extract theme from image",
        "suggestion": "Provide explicit topic in reference_metadata"
    }
```

---

## Access Control (Pattern-AUTH)

**공용 에이전트 규칙:**
- ✅ 읽기 전용: reference_image, reference_metadata
- ✅ 출력: output_path에만 저장
- ❌ 원본 파일 수정 금지
- ❌ 프로젝트 파일 수정 금지

**프로젝트와의 통신:**
- 입력: 프로젝트 에이전트가 전달한 파라미터
- 출력: output_path에 JSON 저장
- 완료 메시지: 부모 세션에 전송

---

## 의존성

**필수:**
```bash
pip install pytesseract Pillow
```

**선택 (더 높은 정확도):**
```bash
pip install openai anthropic  # Vision API
```

**시스템 의존성:**
```bash
# macOS
brew install tesseract tesseract-lang

# Ubuntu
apt-get install tesseract-ocr tesseract-ocr-kor
```

---

## 비용

- **OCR (pytesseract):** 무료
- **OpenAI Vision API:** ~$0.01/image
- **Anthropic Claude Vision:** ~$0.012/image

---

## 버전

- **생성일:** 2026-07-16
- **최종 업데이트:** 2026-07-16
- **버전:** 1.0.0
- **테스트 상태:** Phase 2 ready
