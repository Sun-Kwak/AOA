# image-generator-comfyui

**ComfyUI Desktop 기반 로컬 이미지 생성 Agent**

---

## Metadata

| Field | Value |
|-------|-------|
| **ID** | image-generator-comfyui |
| **Name** | Image Generator (ComfyUI) |
| **Version** | 1.0.0 |
| **Status** | active |
| **Category** | image-generation |
| **Path** | `Agents/image-generator-comfyui/` |
| **Created** | 2026-07-13 |
| **Updated** | 2026-07-13 |

---

## Description

ComfyUI Desktop을 통해 로컬 Mac (M1 Max 32GB)에서 이미지를 생성하는 에이전트.

**핵심 특징:**
- 완전 무료 (로컬 실행)
- M1 Max 최적화
- Workflow 기반 (JSON 조작)
- 3가지 모드: text2img, img2img, image_edit
- 대량 배치 생성 지원

---

## Tags

```
image-generation, comfyui, local, free, text2img, img2img, image-edit, flux, sdxl, batch-processing
```

---

## Use Cases

1. **카드뉴스 대량 생성** (100장+)
   - 비용: $0
   - 속도: ~3분/10장 (M1 Max)

2. **트렌드 이미지 편집** (구조 보존)
   - `mode: image_edit`
   - `strength: 0.25` (최소 변경)

3. **커스텀 스타일** (LoRA, ControlNet)
   - Workflow 커스터마이징
   - 모델 자유 선택

4. **프로토타입 및 실험**
   - 무제한 반복 가능
   - 비용 제약 없음

---

## vs image-generator (fal.ai)

| 항목 | image-generator-comfyui | image-generator (fal.ai) |
|------|-------------------------|-------------------------|
| **비용** | $0 (무료) | $0.003~$0.055/image |
| **속도** | 8-15초 | 5-10초 |
| **안정성** | ComfyUI 실행 필수 | 99.9% uptime |
| **제어** | 완전 제어 | API 제한 |
| **용도** | 대량 생성, 실험 | 프로덕션, 소량 |

---

## Requirements

### System
- **Mac:** Apple Silicon (M1/M2/M3)
- **메모리:** 최소 16GB (32GB 권장)
- **디스크:** 20GB+ (모델 저장 공간)

### Software
- ComfyUI Desktop.app (`/Applications/Comfy Desktop.app`)
- Python 3.8+
- FLUX Schnell 모델 (~12GB)

---

## Inputs

```yaml
mode: text2img | img2img | image_edit  # 필수
prompt: "..."                           # 필수
reference_image: "/path/to/ref.jpg"    # img2img, image_edit
edit_prompt: "..."                      # image_edit
strength: 0.3                           # 기본값: 0.25 (edit), 0.65 (img2img)
model: "flux-schnell"                   # 기본값: flux-schnell
aspect_ratio: "9:16"                    # 기본값: 1:1
batch_size: 1                           # 기본값: 1
output_path: "/path/to/output.jpg"     # 필수
```

---

## Outputs

1. **generated_image** (file_path)
   - 생성된 이미지 파일
   - 경로: `output_path`

2. **metadata** (JSON)
   - 생성 메타데이터
   - 경로: `output_path.replace('.jpg', '.json')`
   - 내용: 프롬프트, 설정, 소요 시간

---

## Dependencies

**Tools:**
- `comfyui-desktop` (ComfyUI Desktop.app)
- `curl` (API 호출)
- `python3` (Workflow 조작)

**External APIs:**
- ComfyUI API: `http://127.0.0.1:8188`

---

## Performance (M1 Max 32GB)

| 작업 | 해상도 | 소요 시간 | 비용 |
|------|--------|-----------|------|
| text2img | 1024x1024 | 8-15초 | $0 |
| image_edit | 1080x1920 (9:16) | 10-18초 | $0 |
| Batch 10장 | 1024x1024 | ~3분 | $0 |
| Batch 100장 | 1024x1024 | ~30분 | $0 |

---

## Best Practices

1. **image_edit 모드:**
   - `strength: 0.2-0.3` (낮을수록 구조 보존)
   - Prompt에 "KEEP EXACT SAME LAYOUT" 명시
   - `steps: 8-12` (품질 향상)

2. **배치 생성:**
   - `batch_size: 10` 이하 권장 (메모리 효율)
   - 32GB 메모리 기준 최대 20장 동시 생성

3. **모델 선택:**
   - 속도 우선: `flux-schnell` (4-step)
   - 품질 우선: `flux-dev` (20-step)

4. **프롬프트:**
   - 영어 권장 (한국어 가능하나 성능 차이)
   - 구체적이고 명확하게

---

## Related Agents

- **image-generator** (fal.ai): 유료, 안정적, 프로덕션용
- **trend-research-agent**: 트렌드 수집
- **browser-controller**: SNS 배포

---

## Known Limitations

1. ComfyUI Desktop 실행 필수 (메모리 항상 점유)
2. 이미지 생성 시 다른 작업 느려짐
3. 초기 모델 다운로드 시간 (12GB+)
4. Mac sleep 시 재시작 필요

---

## Troubleshooting

### ComfyUI 연결 실패
```bash
# ComfyUI Desktop 실행
open -a "Comfy Desktop"
sleep 10
curl http://127.0.0.1:8188/system_stats
```

### 모델 없음
→ ComfyUI Manager에서 FLUX Schnell 다운로드

### 메모리 부족
→ `batch_size` 줄이기, 해상도 낮추기

---

**Created:** 2026-07-13  
**Registry Path:** `Registry/Agents/image-generator-comfyui.md`
