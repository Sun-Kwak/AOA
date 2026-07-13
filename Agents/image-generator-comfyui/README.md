# Image Generator (ComfyUI)

ComfyUI Desktop 기반 로컬 이미지 생성 Agent.

---

## Overview

**역할:** ComfyUI Desktop을 통한 무료 로컬 이미지 생성  
**버전:** 1.0.0  
**상태:** active

---

## Key Features

- ✅ **완전 무료** (로컬 실행)
- ✅ **M1 Max 최적화** (32GB 메모리)
- ✅ **3가지 모드** (text2img, img2img, image_edit)
- ✅ **Workflow 기반** (JSON 조작)
- ✅ **배치 생성** (대량 생산 최적)

---

## Use Cases

1. **카드뉴스 대량 생성** (100장+)
2. **트렌드 이미지 편집** (구조 보존)
3. **커스텀 스타일** (LoRA, ControlNet)
4. **프로토타입** (빠른 반복)

---

## Requirements

- ComfyUI Desktop.app 설치 (`/Applications/Comfy Desktop.app`)
- FLUX Schnell 모델 다운로드 (~12GB)
- 최소 16GB RAM (32GB 권장)

---

## Quick Start

```yaml
# image_edit 예시
mode: image_edit
reference_image: "/path/to/ref.jpg"
prompt: "Change title to '건강한 세탁 팁'"
strength: 0.25
output_path: "/path/to/output.jpg"
```

---

## Performance

| 작업 | 소요 시간 (M1 Max 32GB) | 비용 |
|------|------------------------|------|
| text2img (1024x1024) | 8-15초 | $0 |
| image_edit (9:16) | 10-18초 | $0 |
| Batch 10장 | ~3분 | $0 |

**vs fal.ai:**
- 100장 생성: ComfyUI $0 / fal.ai $3.00

---

## Limitations

- ComfyUI Desktop 실행 필수
- 이미지 생성 시 Mac 다른 작업 느려질 수 있음
- 초기 모델 다운로드 필요 (12GB+)

---

## Related Agents

- `image-generator`: fal.ai 기반 (유료, 안정적)
- `trend-research-agent`: 트렌드 수집
- `browser-controller`: SNS 배포

---

**Created:** 2026-07-13  
**Updated:** 2026-07-13
