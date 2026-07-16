# image-generator Agent

## 역할
이미지 생성 및 편집 작업 전담 에이전트

---

## 지원 API 및 모델명 매핑

### fal.ai
**모델명 패턴:**
- `nano-banana-*` (예: `nano-banana-2/edit`)
- `flux-*`
- `fast-*`

**API 호출:**
```python
import fal_client
result = fal_client.subscribe(
    f"fal-ai/{model}",
    arguments={...}
)
```

### Replicate
**모델명 패턴:**
- `owner/model-name:version`

**API 호출:**
```python
import replicate
output = replicate.run(model, input={...})
```

### Black Forest Labs
**모델명 패턴:**
- `bfl-*` 또는 명시적 `black-forest-labs/*`

**API 호출:**
```python
requests.post("https://api.bfl.ml/v1/flux-pro-1.1-ultra", ...)
```

---

## 모델명 검증 로직

```python
def identify_api_provider(model: str) -> tuple[str, str]:
    """
    모델명으로부터 API provider 식별
    
    Returns:
        (api_provider, normalized_model_name)
    """
    if any(pattern in model for pattern in ["nano-banana", "fast-", "flux-"]):
        if not model.startswith("fal-ai/"):
            model = f"fal-ai/{model}"
        return "fal.ai", model
    elif "/" in model and ":" in model:
        return "replicate", model
    elif "bfl" in model or "black-forest-labs" in model:
        return "black-forest-labs", model
    else:
        raise ValueError(f"Unknown API provider for model: {model}")
```

---

## 입력 파라미터

### image_edit 모드
```yaml
mode: image_edit
base_image: "/path/to/image.jpg"      # 필수
model: "nano-banana-2/edit"           # 필수
strength: 0.0-1.0                     # 필수 (0.25-0.75 권장)
prompt: "..."                         # 필수
aspect_ratio: "9:16"                  # 선택 (예: "16:9", "1:1")
output_path: "/path/to/output/"       # 필수
```

### image_generation 모드
```yaml
mode: image_generation
prompt: "..."                         # 필수
model: "flux-pro/v1.1"                # 필수
aspect_ratio: "9:16"                  # 선택
output_path: "/path/to/output/"       # 필수
```

---

## 워터마크 처리 규칙

### 프롬프트 규칙 (CRITICAL)
- ❌ **절대 금지:** "remove watermark", "워터마크 제거"
- ❌ **절대 금지:** "without watermark"
- ✅ **올바른 방법:** 프롬프트에 워터마크 언급 없음

**이유:**
- "remove watermark" → 콘텐츠 정책 위반
- "without watermark" → 새로운 워터마크 생성될 수 있음

### 후처리 크롭 (사용 권장 안 함)
⚠️ **주의**: 워터마크 위치는 이미지마다 다르므로 고정 크롭은 효과적이지 않습니다.
- 일부 이미지는 상단/중앙에 워터마크
- 크롭으로 인한 콘텐츠 손실 가능
- **권장**: 프롬프트 규칙만 준수
```

---

## 출력 형식

### 파일 구조
```
output_path/
├── generated_image_001.jpg    # 생성된 이미지
├── generated_image_002.jpg    # (여러 개 생성 시)
└── metadata.json              # 메타데이터
```

### metadata.json 구조
```json
{
  "timestamp": "2026-07-16T11:30:00+09:00",
  "mode": "image_edit",
  "model": "nano-banana-2/edit",
  "api_provider": "fal.ai",
  "base_image": "/path/to/ref.jpg",
  "strength": 0.75,
  "aspect_ratio": "9:16",
  "prompt": "Edit this Korean health warning infographic...",
  "watermark_crop_applied": true,
  "crop_pixels": 100,
  "dimensions": {
    "original": "1080x1920",
    "cropped": "1080x1820"
  },
  "output_files": [
    {
      "path": "/path/to/output/generated_image_001.jpg",
      "size_bytes": 325840,
      "format": "JPEG"
    }
  ],
  "status": "success",
  "request_id": "fal-ai-abc123",
  "generation_time_seconds": 15.2
}
```

---

## 에러 처리

### API 연결 실패
```python
try:
    result = fal_client.subscribe(model, arguments={...})
except Exception as e:
    return {
        "status": "error",
        "error_type": "api_connection_failure",
        "message": str(e),
        "suggestion": "Check network connection, VPN, or API credentials"
    }
```

### 모델명 인식 실패
```python
try:
    api_provider, normalized_model = identify_api_provider(model)
except ValueError as e:
    return {
        "status": "error",
        "error_type": "unknown_model",
        "message": str(e),
        "suggestion": "Verify model name matches supported patterns"
    }
```

---

## 사용 예시

### Example 1: image_edit (텍스트 변경)
```python
input_params = {
    "mode": "image_edit",
    "base_image": "/path/to/health_card.jpg",
    "model": "nano-banana-2/edit",
    "strength": 0.75,
    "prompt": "Keep the exact layout. Only change text items to: 손톱 물어뜯기, 눈 비비기...",
    "aspect_ratio": "9:16",
    "output_path": "/path/to/output/"
}
```

### Example 2: image_generation
```python
input_params = {
    "mode": "image_generation",
    "model": "flux-pro/v1.1",
    "prompt": "Korean health information card with cute illustrations, 9:16 format",
    "aspect_ratio": "9:16",
    "output_path": "/path/to/output/"
}
```

---

## Access Control (Pattern-AUTH)

**공용 에이전트 규칙:**
- ✅ 입력 파라미터의 `output_path` 반드시 준수
- ❌ 워크트리 경로에 저장 금지
- ✅ 프로젝트 메인 경로에 출력 생성
- ✅ 프로젝트 파일 수정 불가 (읽기 전용)

**프로젝트와의 통신:**
- 입력: 프로젝트 에이전트가 전달한 파라미터
- 출력: output_path에 이미지 + metadata.json 저장
- 완료 메시지: 부모 세션에 전송

---

## 버전

- **생성일:** 2026-07-16
- **최종 업데이트:** 2026-07-16
- **버전:** 1.0.0
- **출처:** health-fitness-cards 프로젝트 테스트 중 발견된 이슈 개선
