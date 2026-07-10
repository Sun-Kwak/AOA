# Output Formats

image-generator 출력 형식 관련 실수와 해결책.

---

## [Format-001] nano-banana-2/edit PNG 출력

**발생일**: 2026-07-10  
**상황**: nano-banana-2/edit로 이미지 생성 완료  
**발견**: 
- flux-pro는 JPEG로 출력
- nano-banana-2/edit는 **PNG로 출력**
- 파일 크기가 JPEG보다 큼 (1,560 KB vs 500-600 KB)

**올바른 처리**:
```python
# 다운로드 후 저장 시 확장자 맞추기
if result['images'][0]['content_type'] == 'image/png':
    # PNG 그대로 저장 또는
    # 필요시 JPEG로 변환
    output_path = "card_test_001.jpg"  # .jpg로 저장해도 OK
```

**결과**: 
- .jpg 확장자로 저장해도 작동함
- 투명도 필요 없으면 JPEG 변환 고려

---

## [Format-002] image_edit 모드 파일명 패턴

**발생일**: 2026-07-10  
**상황**: image_edit 모드 결과 파일 저장  
**실수**: 기존 img2img와 동일한 파일명 패턴 사용

**올바른 형식**:
```python
# 파일명 패턴
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# text2img
filename = f"img_{timestamp}_text2img_{purpose}.jpg"

# img2img
filename = f"img_{timestamp}_img2img_{purpose}.jpg"

# image_edit ✨ NEW
filename = f"img_{timestamp}_image_edit_{purpose}.jpg"
# 또는
filename = f"img_{timestamp}_edit_{purpose}.jpg"
```

**권장사항**: 모드를 파일명에 포함하여 나중에 추적 가능하게

---

## 업데이트 이력

- 2026-07-10: 초기 생성
- 2026-07-10: Format-001, Format-002 추가 (nano-banana-2/edit 출력 학습)
