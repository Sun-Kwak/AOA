# Image Generator

## Metadata

| Field | Value |
|-------|-------|
| ID | image-generator |
| Name | Image Generator |
| Version | 1.1.0 ✨ |
| Status | Active |
| Created | 2026-07-10 |
| Last Updated | 2026-07-10 |

---

## Tags

`image-generation`, `fal-ai`, `text2img`, `img2img`, `image-edit` ✨, `card-news`, `nanovana2`, `flux`, `visual-content`

---

## Description

범용 이미지 생성 Agent. 텍스트 프롬프트, Reference 이미지 기반 생성, 또는 기존 이미지 편집 지원.

**핵심 기능:**
- **text2img**: 프롬프트만으로 새 이미지 생성
- **img2img**: Reference 이미지 기반 스타일 복제 (트렌드 적용)
- **image_edit**: 기존 이미지 편집 (텍스트/색상만 변경, 구조 보존) ✨ NEW
- 프롬프트 자동 최적화
- 5가지 Aspect Ratio 지원 (16:9, 9:16, 1:1, 4:5, 21:9)
- 에러 핸들링 및 자동 재시도

**지원 용도:**
- 카드 이미지 (SNS 썸네일)
- 캐릭터 일러스트
- 배경 이미지
- 광고 소재
- 블로그 헤더
- **카드뉴스 현지화** (image_edit 모드) ✨

**Provider:**
- fal.ai (기본 모델: nanovana2 / flux-pro/v1.1-ultra)
- flux-general (inpainting/edit 전용) ✨ NEW
- 5가지 모델 선택 가능

---

## Dependencies

### Tools
- **fal.ai** (fal.ai API)

### Environment
- `FAL_KEY` (required)

---

## Usage

```yaml
# text2img (새 이미지 생성)
image_generator.generate(
  mode: "text2img"
  prompt: "A vibrant Instagram card about healthy diet"
  aspect_ratio: "16:9"
  model: "nanovana2"
)

# img2img (Reference 기반 스타일 복제)
image_generator.generate(
  mode: "img2img"
  prompt: "Keep layout, change to '혈당 관리 팁'"
  reference_image: "Memory/trends/visuals/ref_001.jpg"
  strength: 0.6
  aspect_ratio: "9:16"
)

# image_edit (기존 이미지 편집) ✨ NEW
image_generator.generate(
  mode: "image_edit"
  edit_prompt: "ONLY change text to '혈당 관리 팁', use warmer colors"
  reference_image: "Memory/trends/visuals/ref_001.jpg"
  preserve_structure: true
  strength: 0.25
  mask: "auto"
  edit_areas: ["text", "colors"]
)
```

---

## Path

`Agents/image-generator/`

---

## Related Assets

- **Tools:** `fal.ai` (external)
- **Used with:** trend-research-agent (visual references 활용)

---

## Notes

- **기본 모델**: nanovana2 ($0.05/image)
- **strength 권장**: 0.5-0.6 (레이아웃 유지), 0.7-0.8 (스타일만 유지)
- 한국어 텍스트는 10-15% 오류 가능 (이미지 내 텍스트)
- Rate limit: fal.ai 플랜별 상이
- Visual reference는 trend-research-agent 출력 활용 권장
