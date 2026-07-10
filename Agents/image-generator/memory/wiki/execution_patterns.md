# Execution Patterns

image-generator 실행 시 발견한 실수와 회피 전략.

---

## [Pattern-001] image_edit 모드에서 잘못된 모델 사용

**발생일**: 2026-07-10  
**상황**: image_edit 모드로 텍스트가 많은 인포그래픽 카드 편집 요청  
**실수**: flux-pro/v1.1-ultra (img2img 방식)를 사용함  
**결과**: 
- strength 0.25: 모든 텍스트가 재생성되어 원본 내용 손실
- strength 0.15: 텍스트 여전히 변형됨
- strength 0.08: 거의 모든 콘텐츠가 사라짐
- **텍스트 보존 실패!**

**올바른 방법**:
```python
# ✅ CORRECT
result = fal_client.subscribe(
    "fal-ai/nano-banana-2/edit",  # edit 전용 모델!
    arguments={
        "prompt": "간단하고 명확한 한국어 프롬프트",
        "image_urls": [reference_url],  # ⚠️ 배열 형태
        "logs": True
    }
)
# 응답: result['images'][0]['url']
```

**회피전략**:
1. **image_edit 모드 = nano-banana-2/edit 모델 필수**
2. img2img 방식(flux-pro)은 텍스트 보존 불가
3. 프롬프트는 간단하고 명확한 한국어로 작성
4. Arguments: `image_urls` (배열), 응답: `result['images'][0]`

---

## [Pattern-002] 프롬프트 작성 실수 (image_edit)

**발생일**: 2026-07-10  
**상황**: nano-banana-2/edit 사용 시 영어로 긴 프롬프트 작성  
**실수**: 
```python
prompt = "KEEP exact same illustration style, characters, positions..."  # 너무 길고 복잡
```

**결과**: 대시보드에서는 간단한 한국어로 성공했는데, 길고 복잡한 영어 프롬프트로는 효과 떨어짐

**올바른 방법**:
```python
# ✅ 간단하고 명확한 한국어
prompt = """이미지의 모든 콘텐츠 텍스트는 절대 유지
타이틀만 다르게 표현 가능 (같은 의미)
배경, 폰트, 색상만 변경
캐릭터, 레이아웃은 완전 동일하게"""
```

**회피전략**:
1. **간단하고 명확한 한국어 프롬프트 사용**
2. 무엇을 유지/변경할지 명확히 구분
3. 영어로 길게 작성하지 말 것
4. 불필요한 디테일 제거

---

## 업데이트 이력

- 2026-07-10: 초기 생성
- 2026-07-10: Pattern-001, Pattern-002 추가 (image_edit 모드 학습)
