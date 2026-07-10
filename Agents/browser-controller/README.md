# Browser Controller Agent

## Overview

Canvas Browser를 통제하여 웹 자동화를 수행하는 범용 에이전트.

자연어 명령을 Canvas action으로 변환하고, Instagram/YouTube/TikTok 등 SNS 플랫폼 배포 플로우를 실행합니다.

---

## Features

✅ **Canvas Browser 제어**: open_canvas, invoke_canvas_action 사용  
✅ **자연어 명령 지원**: "Instagram에 이미지 업로드" → 자동 실행  
✅ **다중 계정 지원**: Canvas 인스턴스별 독립 세션  
✅ **플로우 학습**: memory/wiki에서 플랫폼별 배포 패턴 누적  
✅ **에러 자동 대응**: 셀렉터 변경 감지 및 Wiki 업데이트

---

## Usage

### 1. Canvas 초기화 (최초 1회)

프로젝트에서 계정별 Canvas 인스턴스 생성:

```yaml
# Projects/<project>/Agents/deployer-insta-main/config.yaml
platform: instagram
account_id: main
canvas_instance: "browser-insta-main"
parent_agent: browser-controller
```

### 2. 사용자 로그인 (최초 1회)

```markdown
Project Agent:
  "browser-controller에게 Canvas 'browser-insta-main'을 열어달라고 요청"

→ Canvas 패널 오픈
→ 사용자: 수동 로그인 ✅
→ Canvas 계속 열어둠 (세션 유지)
```

### 3. 배포 실행 (자동화)

```yaml
# Project Agent → browser-controller
canvas_instance_id: "browser-insta-main"
command: "Instagram에 이미지 업로드하고 캡션 달아줘"
context:
  image_path: "/path/to/card_001.jpg"
  caption: "10분 홈트로 복근 만들기"
  tags: ["홈트", "복근"]
```

---

## Directory Structure

```
Agents/browser-controller/
  ├── agent.yaml           # 에이전트 정의
  ├── prompt.md            # 프롬프트 (실행 로직)
  ├── README.md            # 이 문서
  └── memory/
       ├── wiki/
       │    ├── README.md
       │    ├── instagram_workflow.md
       │    ├── youtube_workflow.md
       │    ├── tiktok_workflow.md
       │    ├── common_selectors.md
       │    └── error_patterns.md
       └── executions/      # 실행 기록 (스크린샷 등)
```

---

## Dependencies

- **None** (순수 Canvas Browser 기반)

---

## Supported Platforms

| Platform | Status | Features |
|----------|--------|----------|
| Instagram | ✅ Ready | 이미지/영상 업로드, 캡션, 태그 |
| YouTube | ✅ Ready | Shorts 업로드, 제목, 설명 |
| TikTok | 🚧 Planned | 영상 업로드, 캡션, 태그 |

---

## Best Practices

### Canvas 관리
- 계정별로 Canvas 인스턴스 분리 (예: browser-insta-main, browser-youtube-fitness)
- Canvas는 닫지 않고 계속 열어둠 (로그인 세션 유지)
- 장시간 미사용 시 세션 만료 가능 (재로그인 필요)

### 플로우 학습
- 플랫폼 UI 변경 시 `memory/wiki/` 자동 업데이트
- 에러 발생 시 Wiki에 패턴 기록
- 성공 플로우도 Wiki에 누적

---

## Troubleshooting

### 문제: Canvas 오픈 실패
→ `list_canvas_capabilities("browser")` 확인  
→ Canvas 도구 사용 가능 여부 체크

### 문제: 로그인 세션 만료
→ 사용자에게 "재로그인 필요" 알림  
→ Canvas 패널에서 수동 로그인 후 재시도

### 문제: 셀렉터 찾기 실패
→ `memory/wiki/<platform>_workflow.md` 확인  
→ 플랫폼 UI 변경 시 새 셀렉터 탐색 후 Wiki 업데이트

---

## Version History

- **1.0.0** (2026-07-10): 최초 등록. Canvas Browser 기반 웹 자동화 + SNS 배포 지원.

---

## Related Documents

- `Schemas/Agent.md` - 에이전트 스키마
- `Standards/Prompt.md` - 프롬프트 표준
- `Registry/Agents/browser-controller.md` - Registry 등록 정보
