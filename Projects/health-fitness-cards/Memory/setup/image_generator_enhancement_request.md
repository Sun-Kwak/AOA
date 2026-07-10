# Image Generator Agent Enhancement Request

**요청자:** health-fitness-cards Project Agent  
**날짜:** 2026-07-10

---

## 문제점

현재 `image-generator` 에이전트는 `text2img`와 `img2img` 모드만 지원합니다.

`img2img` 모드는:
- Reference 이미지를 **참고**해서 완전히 새로운 이미지 재생성
- `strength: 0.6` → 레이아웃 유사하지만 내용은 새로 생성
- **문제:** 텍스트/색상/디자인만 바꾸고 싶은데 전체가 바뀜

---

## 요청 사항

`image_edit` (또는 `inpainting`) 모드 추가:

### 새로운 모드 스펙:

```yaml
mode: image_edit

# 필수 입력
reference_image: "path/to/image.jpg"
edit_prompt: "Change text to '혈당 관리 팁', use warmer colors"
mask: "auto"  # 또는 mask_image 경로

# Optional
preserve_structure: true  # 레이아웃/구조 완전 보존
edit_areas: ["text", "colors"]  # 수정 영역 지정
strength: 0.3  # 낮은 값 = 최소 변경
```

### fal.ai API:

```python
# 제안: fal-ai/flux-general 또는 edit 전용 모델 사용
result = fal_client.subscribe(
    "fal-ai/flux-general",  # 또는 edit 모델
    arguments={
        "prompt": edit_prompt,
        "image_url": reference_image_url,
        "mask": "auto",  # 또는 마스크 이미지
        "strength": 0.3,  # 최소 변경
        "preserve_original": True
    }
)
```

---

## Use Case (health-fitness-cards)

**시나리오:**
1. Instagram 계정에서 일러스트 건강 카드 수집
2. **내용은 그대로, 텍스트만 변경**하고 싶음
3. 예: "몸의 신호 8가지" → "혈당 관리 팁 8가지"

**원하는 결과:**
- 일러스트 캐릭터 동일
- 레이아웃 동일
- 색감 약간 조정 가능
- **텍스트만 한국어로 교체**

**현재 문제:**
- `img2img strength: 0.65` → 완전히 다른 그림
- 캐릭터, 레이아웃 모두 변경됨

---

## 대안 (임시)

`image_edit` 모드 추가가 어렵다면:

### Option 1: strength 파라미터 세분화
```yaml
mode: img2img_preserve  # 새 모드명
strength: 0.2-0.4       # 낮은 값으로 기본값 변경
preserve_elements: ["layout", "characters", "composition"]
```

### Option 2: 프롬프트 전략 개선
```python
# img2img 사용하되 프롬프트에 보존 명령 강화
prompt = f"""
IMPORTANT: Keep the EXACT same illustration style, characters, and layout.
ONLY change: {changes_requested}
Reference image style must be preserved 90%.
"""
```

---

## 우선순위

- **High**: `image_edit` 모드 또는 이에 준하는 기능 추가
- **이유**: 카드뉴스 자동화 프로젝트에 필수
- **대안**: strength 세분화 + 프롬프트 전략 개선

---

## 참고

fal.ai 모델 중 edit/inpainting 지원 모델:
- `fal-ai/flux-general` (확인 필요)
- `fal-ai/stable-diffusion-inpainting` (Stable Diffusion 기반)
- 기타 edit 전용 모델

확인 후 적용 부탁드립니다.
