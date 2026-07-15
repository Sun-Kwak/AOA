#!/usr/bin/env python3
"""
ComfyUI 이미지 편집 자동화 스크립트
모델: InstructPix2Pix (MPS 호환)
"""
import json
import requests
import time
import random
import sys
from pathlib import Path

def edit_image(
    input_path: str,
    output_dir: str,
    prompt: str,
    negative: str = "blurry, low quality, distorted",
    steps: int = 20,
    cfg: float = 7.5,
    output_prefix: str = "edited"
):
    """
    InstructPix2Pix로 이미지 편집
    
    Args:
        input_path: 원본 이미지 경로 (반드시 ComfyUI input 폴더에 있어야 함)
        output_dir: 출력 디렉토리
        prompt: 편집 지시문 (영어)
        negative: 네거티브 프롬프트
        steps: 샘플링 스텝 (20-30 권장)
        cfg: CFG scale (7-8 권장)
        output_prefix: 출력 파일 프리픽스
    """
    
    # ComfyUI 입력 폴더로 이미지 복사
    input_filename = Path(input_path).name
    comfy_input = Path("/Users/sun/ComfyUI-Shared/input") / input_filename
    
    if not comfy_input.exists():
        import shutil
        shutil.copy2(input_path, comfy_input)
        print(f"✅ 이미지 복사: {comfy_input}")
    
    # 워크플로우 생성
    workflow = {
        "1": {
            "inputs": {"ckpt_name": "instruct-pix2pix.safetensors"},
            "class_type": "CheckpointLoaderSimple"
        },
        "2": {
            "inputs": {"text": prompt, "clip": ["1", 1]},
            "class_type": "CLIPTextEncode"
        },
        "3": {
            "inputs": {"text": negative, "clip": ["1", 1]},
            "class_type": "CLIPTextEncode"
        },
        "4": {
            "inputs": {"image": input_filename},
            "class_type": "LoadImage"
        },
        "5": {
            "inputs": {"pixels": ["4", 0], "vae": ["1", 2]},
            "class_type": "VAEEncode"
        },
        "6": {
            "inputs": {
                "seed": random.randint(1, 2**31),
                "steps": steps,
                "cfg": cfg,
                "sampler_name": "euler",
                "scheduler": "normal",
                "denoise": 1.0,
                "model": ["1", 0],
                "positive": ["2", 0],
                "negative": ["3", 0],
                "latent_image": ["5", 0]
            },
            "class_type": "KSampler"
        },
        "7": {
            "inputs": {"samples": ["6", 0], "vae": ["1", 2]},
            "class_type": "VAEDecode"
        },
        "8": {
            "inputs": {"filename_prefix": output_prefix, "images": ["7", 0]},
            "class_type": "SaveImage"
        }
    }
    
    print("🚀 ComfyUI API 호출...")
    response = requests.post("http://127.0.0.1:8188/prompt", json={"prompt": workflow})
    
    if response.status_code != 200:
        print(f"❌ API 에러: {response.status_code}")
        print(response.text[:400])
        return None
    
    result = response.json()
    prompt_id = result['prompt_id']
    print(f"✅ 큐 등록: {prompt_id}")
    print(f"⏳ 처리 중 (약 60초)...\n")
    
    start_time = time.time()
    
    for _ in range(150):
        time.sleep(2)
        try:
            hr = requests.get(f"http://127.0.0.1:8188/history/{prompt_id}", timeout=5)
            if hr.status_code == 200:
                h = hr.json()
                if prompt_id in h:
                    status_info = h[prompt_id].get('status', {})
                    st = status_info.get('status_str')
                    
                    if st == 'success':
                        elapsed = time.time() - start_time
                        print(f"✅ 완료! ({elapsed:.1f}초)")
                        
                        outputs = h[prompt_id].get('outputs', {})
                        for node_id, out in outputs.items():
                            if 'images' in out:
                                for img in out['images']:
                                    comfy_out = Path("/Users/sun/ComfyUI-Shared/output") / img['filename']
                                    final_out = Path(output_dir) / img['filename']
                                    final_out.parent.mkdir(parents=True, exist_ok=True)
                                    
                                    import shutil
                                    shutil.copy2(comfy_out, final_out)
                                    print(f"📁 출력: {final_out}")
                                    return str(final_out)
                        
                    elif st == 'error':
                        print(f"❌ 에러 발생")
                        for msg in status_info.get('messages', []):
                            if 'execution_error' in str(msg):
                                err = msg[1] if len(msg) > 1 else {}
                                print(f"   {err.get('exception_type')}: {err.get('exception_message', '')[:200]}")
                        return None
        except:
            pass
    
    print("⏰ 타임아웃")
    return None

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("""
사용법:
  python3 comfyui_image_edit.py <입력> <출력> "<프롬프트>"

예시:
  python3 comfyui_image_edit.py \\
    ../Memory/trends/visuals/ref_20260710_001.jpg \\
    ../Outputs/ \\
    "change background to soft mint green, modernize washing machine icon"
""")
        sys.exit(1)
    
    result = edit_image(
        input_path=sys.argv[1],
        output_dir=sys.argv[2],
        prompt=sys.argv[3]
    )
    
    sys.exit(0 if result else 1)
