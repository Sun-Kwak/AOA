# API Errors

image-generator fal.ai API 호출 시 발견한 에러와 해결책.

---

## [Error-001] flux-general 모델 타임아웃/작동 불가

**발생일**: 2026-07-10  
**API**: fal.ai (flux-general)  
**에러**: 
- 120초 이상 응답 없음 (타임아웃)
- 또는 작동하지 않음

**원인**: 
- prompt.md에 `flux-general` 추천했으나 실제로는 작동 안 함
- image_edit 모드에서 사용 불가

**해결책**:
```python
# ❌ WRONG
"fal-ai/flux-general"  # 작동 안 함

# ✅ CORRECT
"fal-ai/nano-banana-2/edit"  # edit 전용 모델
```

---

## [Error-002] nano-banana-2/edit 응답 구조 오해

**발생일**: 2026-07-10  
**API**: fal.ai (nano-banana-2/edit)  
**에러**: `result['image']` KeyError

**원인**: 
- flux-pro는 `result['images'][0]['url']` 구조
- nano-banana-2/edit도 동일한 구조인데 `result['image']`로 접근 시도

**해결책**:
```python
# ✅ CORRECT
if result and 'images' in result and len(result['images']) > 0:
    image_url = result['images'][0]['url']  # images 배열!
```

---

## [Error-003] flux-pro img2img로 텍스트 보존 시도 실패

**발생일**: 2026-07-10  
**API**: fal.ai (flux-pro/v1.1-ultra)  
**에러**: 텍스트가 완전히 재생성됨 (의도와 다름)

**원인**: 
- img2img는 이미지를 "재생성"하는 방식
- strength를 낮춰도 텍스트 보존 불가
- 텍스트를 별도 레이어로 인식하지 못함

**해결책**:
- **텍스트 보존이 필요한 경우 = nano-banana-2/edit 필수**
- img2img는 스타일 복제 용도로만 사용
- image_edit 모드로 명확히 구분

---

## 업데이트 이력

- 2026-07-10: 초기 생성
- 2026-07-10: Error-001, Error-002, Error-003 추가 (image_edit 모델 학습)
