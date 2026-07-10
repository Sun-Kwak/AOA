# Image Generator Agent

## 개요

**범용 이미지 생성 Agent**로, 텍스트 프롬프트(text2img), Reference 이미지 기반(img2img), 또는 기존 이미지 편집(image_edit)으로 다양한 용도의 이미지를 생성합니다.

---

## 지원 용도

- ✅ **카드 이미지** (인스타그램, 유튜브 썸네일)
- ✅ **캐릭터 일러스트**
- ✅ **배경 이미지**
- ✅ **상품 이미지**
- ✅ **광고 소재**
- ✅ **블로그 헤더**
- ✅ **이미지 편집** (텍스트/색상만 변경, 구조 보존) ✨ NEW
- ✅ **기타 모든 이미지**

---

## Provider

### **fal.ai** (기본)

| 모델 | ID | 비용 | 용도 | 기능 |
|------|----|----|------|------|
| **nanovana2** ⭐ | flux-pro/v1.1-ultra | $0.05 | 기본 (품질/비용 최적) | text2img, img2img, image_edit ✨ |
| **flux-general** | flux-general | $0.04 | 범용 (inpainting/edit) | text2img, img2img, image_edit ✨ |
| flux-schnell | flux/schnell | $0.003 | 빠른 생성 | text2img |
| flux-dev | flux/dev | $0.025 | 고품질 | text2img, img2img |
| flux-pro | flux-pro | $0.055 | 최고 품질 | text2img, img2img |

**기본 모델:** `nanovana2` (프로젝트에서 변경 가능)

---

## 실행 모드

### **1. text2img (텍스트 → 이미지)**

프롬프트만으로 새 이미지 생성.

```yaml
mode: text2img
prompt: "A vibrant Instagram card about healthy diet"
aspect_ratio: "16:9"
model: nanovana2  # Optional
```

### **2. img2img (Reference 기반)**

기존 이미지 스타일을 유지하며 내용 변경. 트렌드 스타일 복제에 이상적.

```yaml
mode: img2img
prompt: "Keep layout, change text to '혈당 관리'"
reference_image: "Memory/trends/visuals/ref_001.jpg"
strength: 0.6  # 0.0 (원본) ~ 1.0 (완전 재생성)
```

**strength 권장 값:**
- `0.5-0.6`: 레이아웃/구도 유지, 내용만 변경
- `0.7-0.8`: 스타일 유지, 구도는 변경
- `0.9-1.0`: Reference는 힌트만, 거의 새 이미지

### **3. image_edit (이미지 편집)** ✨ NEW

기존 이미지의 **캐릭터/레이아웃은 완전히 보존**하고 **텍스트/색상만 변경**. 카드뉴스 현지화에 이상적.

```yaml
mode: image_edit
edit_prompt: "ONLY change text to '혈당 관리 팁', use warmer colors"
reference_image: "Memory/trends/visuals/ref_001.jpg"
preserve_structure: true  # 구조 보존 (기본값 true)
strength: 0.25  # 0.2-0.3 권장 (최소 변경)
edit_areas: ["text", "colors"]  # Optional
mask: "auto"  # 자동 마스킹 또는 mask 이미지 경로
```

**🚨 중요 규칙:**
- **워터마크/출처는 자동으로 제거됨** (@username, 로고 등)
- 프로젝트에서 명시하지 않아도 에이전트가 자동 처리
- 예: `@health_happyvirus` 같은 출처 표시 제거

**img2img vs image_edit 비교:**

| 기준 | img2img (strength 0.6) | image_edit (strength 0.25) |
|------|------------------------|----------------------------|
| 캐릭터 | 변경됨 | 보존 ✅ |
| 레이아웃 | 유사 | 완전 동일 ✅ |
| 텍스트 | 변경 | 변경 ✅ |
| 색감 | 변경 | 미세 조정 ✅ |
| 워터마크 | 그대로 | 자동 제거 ✅ |
| 용도 | 스타일 복제 | 현지화/편집 |

---

## 입력 형식

### **필수 입력**

```yaml
request:
  mode: text2img | img2img | image_edit  ✨ NEW
  prompt: string  # 생성 또는 변경 요청
  
  # img2img만 필수
  reference_image: string  # 파일 경로
  
  # image_edit 필수 ✨ NEW
  reference_image: string  # 파일 경로
  edit_prompt: string  # 편집 지시
```

### **Optional 입력**

```yaml
  model: nanovana2 | flux-general | flux-schnell | flux-dev | flux-pro
  aspect_ratio: "16:9" | "9:16" | "1:1" | "4:5" | "21:9"
  strength: 0.0~1.0  # img2img, image_edit
  
  # image_edit 전용 ✨ NEW
  preserve_structure: true | false  # 구조 보존 (기본값 true)
  mask: "auto" | string  # 자동 마스킹 또는 mask 이미지 경로
  edit_areas: ["text", "colors", "background"]  # 편집 영역
  guidance_scale: 3.5  # 낮은 값 = 원본 유지
  
  style_modifiers:
    - "vibrant colors"
    - "modern design"
    - "minimalist"
  purpose: string  # 파일명에 포함 (예: "card", "character")
```

---

## 출력 형식

### **성공 응답**

```yaml
status: success
output:
  image_path: "Memory/generated_images/img_20260710_144530_img2img_card.jpg"
  image_url: "https://fal.media/files/abc123/image.jpg"
  metadata:
    mode: img2img
    model: nanovana2
    cost: 0.05
    dimensions: [1920, 1080]
    generation_time: 8.5
```

### **실패 응답**

```yaml
status: failed
error:
  code: SAFETY_FILTER_TRIGGERED | RATE_LIMIT | INVALID_INPUT | TIMEOUT
  message: "Error description"
  retry_count: 3
  suggestions: [...]
```

---

## 저장 구조

```
프로젝트/Memory/generated_images/
├── img_20260710_144530_img2img_card.jpg
├── img_20260710_144612_text2img_character.jpg
└── metadata.json
```

**metadata.json:**

```json
{
  "img_20260710_144530_img2img_card.jpg": {
    "mode": "img2img",
    "model": "nanovana2",
    "prompt": "Keep layout, change text to '혈당 관리'",
    "reference_image": "trends/visual_001.jpg",
    "strength": 0.6,
    "cost": 0.05,
    "generated_at": "2026-07-10T14:45:30+09:00"
  }
}
```

---

## Aspect Ratio 지원

| Ratio | 해상도 | 용도 |
|-------|--------|------|
| 16:9 | 1920×1080 | YouTube 가로형, 기본 |
| 9:16 | 1080×1920 | Shorts, Reels (세로형) |
| 1:1 | 1080×1080 | Instagram 정사각형 |
| 4:5 | 1080×1350 | Instagram 피드 |
| 21:9 | 2560×1080 | 시네마틱 |

---

## 프롬프트 최적화

Agent는 입력 프롬프트를 자동 최적화합니다:

```yaml
# 입력
prompt: "건강한 식단 카드"

# 최적화 후
prompt: "A vibrant Instagram card showing healthy diet,
         clean layout, modern typography,
         pastel background, 16:9 aspect ratio,
         professional design, high quality"
```

**자동 추가 요소:**
- 색감 키워드 (vibrant, pastel)
- 스타일 키워드 (modern, minimalist)
- 품질 키워드 (high quality, professional)
- 기술 요구사항 (aspect ratio, resolution)

---

## 에러 핸들링

| 에러 | 처리 |
|------|------|
| Safety filter | 프롬프트 sanitize 후 재시도 (최대 3회) |
| Rate limit | 10초 대기 후 재시도 |
| Invalid reference | 파일 검증 실패 메시지 반환 |
| API timeout | 재시도 (최대 3회) |
| Invalid model | 기본 모델로 fallback |

---

## 프로젝트별 커스터마이징

프로젝트는 호출 시 파라미터를 오버라이드 가능:

```python
# 프로젝트 워크플로우에서
result = image_generator.generate(
    mode="img2img",
    prompt="Keep layout, change to '운동 후 식단'",
    reference_image="trends/ref_001.jpg",
    
    # 커스터마이징
    model="flux-pro",       # 고품질 모델
    aspect_ratio="9:16",    # 세로형
    strength=0.7            # 더 많은 변형
)
```

---

## 사용 예시

### **예시 1: 트렌드 스타일 복제 (카드 이미지)**

```yaml
# trend-research-agent로부터 visual reference 수집
# → image-generator 호출

mode: img2img
prompt: "Keep the layout and design style,
         change main text to '혈당 관리 3가지 팁',
         use warm color palette,
         Korean text clearly readable"
reference_image: "Memory/trends/visuals/ref_20260710_001.jpg"
strength: 0.6
aspect_ratio: "9:16"

# 결과: 트렌드 스타일은 유지하되 내용만 변경된 카드 이미지
```

### **예시 2: 캐릭터 생성 (text2img)**

```yaml
mode: text2img
prompt: "Cute health coach character,
         cartoon style, smiling,
         white background,
         vibrant colors,
         full body illustration"
aspect_ratio: "1:1"
purpose: "character"

# 결과: 건강 코치 캐릭터 일러스트
```

### **예시 3: 배경 이미지**

```yaml
mode: text2img
prompt: "Clean minimalist background,
         pastel gradient,
         no text, no people,
         suitable for text overlay,
         professional quality"
aspect_ratio: "16:9"
purpose: "background"

# 결과: 텍스트 오버레이용 배경
```

---

## 제약사항 및 주의사항

### **제약사항:**

- ⚠️ **Rate Limit:** fal.ai 플랜에 따라 다름
- ⚠️ **비용:** 매 생성마다 API 비용 발생 ($0.003~$0.055)
- ⚠️ **안전 필터:** 민감한 콘텐츠 거부
- ⚠️ **생성 시간:** 5-15초 (모델별 상이)
- ⚠️ **한국어 텍스트:** 이미지 내 한국어는 10-15% 오류 가능

### **주의사항:**

1. **Reference 이미지는 프로젝트가 제공한 경로만 사용**
2. **안전 필터 3회 실패 시 프롬프트 검토 필요**
3. **비용 누적 확인 (프로젝트 예산 고려)**
4. **한국어 텍스트 포함 시 OCR 검증 권장 (프로젝트 레벨)**

---

## 의존성

- **Tools:** fal.ai
- **Environment:** `FAL_KEY` (API Key)

---

## 버전

- **v1.0.0** (2026-07-10)
  - 초기 버전
  - text2img, img2img 모드 지원
  - fal.ai provider (nanovana2 기본)
  - 4가지 모델 선택 가능
  - Aspect ratio 5종 지원
  - 프롬프트 자동 최적화
  - 에러 핸들링 및 재시도

---

## 다음 단계

1. **fal.ai API Key 설정:** `FAL_KEY` 환경변수
2. **테스트 프로젝트 생성:** image-generator 호출 테스트
3. **trend-research-agent와 통합:** visual references → img2img
4. **(Optional) 추가 Provider 지원:** Ideogram, Midjourney, etc.
