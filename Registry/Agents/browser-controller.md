# Registry Entry: Browser Controller

## Metadata

| Field | Value |
|-------|-------|
| ID | browser-controller |
| Name | Browser Controller |
| Version | 1.0.0 |
| Status | active |
| Category | automation |
| Registered | 2026-07-10 |

---

## Description

Canvas Browser를 통제하여 웹 자동화를 수행하는 범용 에이전트.

자연어 명령을 Canvas action으로 변환하고, Instagram/YouTube/TikTok 등 SNS 플랫폼 배포 플로우를 실행합니다.

---

## Tags

- browser-automation
- web-automation
- canvas
- sns-deployment
- instagram
- youtube
- tiktok

---

## Capabilities

- Canvas Browser 제어 (open_canvas, invoke_canvas_action)
- 자연어 명령 → Canvas action 변환
- 웹 요소 탐색/클릭/입력
- SNS 플랫폼 배포 플로우 실행 (Instagram/YouTube/TikTok)
- 브라우저 세션 상태 추적
- 플로우 학습 (memory/wiki)

---

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| canvas_instance_id | text | ✅ | 제어할 Canvas Browser 인스턴스 ID |
| command | text | ✅ | 자연어 명령 |
| context | yaml | ❌ | 추가 컨텍스트 (파일 경로, 캡션 등) |

---

## Outputs

| Name | Type | Path | Description |
|------|------|------|-------------|
| execution_result | yaml | null | 실행 결과 (성공/실패, 스크린샷, 에러) |

---

## Dependencies

**None** - 순수 Canvas Browser 기반

---

## Use Cases

### 1. Instagram 이미지 배포
```yaml
command: "Instagram에 이미지 업로드하고 캡션 달아줘"
context:
  image_path: "/path/to/card.jpg"
  caption: "10분 홈트"
  tags: ["홈트", "복근"]
```

### 2. YouTube Shorts 업로드
```yaml
command: "YouTube Shorts에 동영상 업로드"
context:
  video_path: "/path/to/short.mp4"
  title: "복근 만드는 루틴"
  visibility: "public"
```

### 3. TikTok 영상 배포
```yaml
command: "TikTok에 영상 올려줘"
context:
  video_path: "/path/to/video.mp4"
  caption: "따라하기 쉬운 홈트"
```

---

## Implementation Path

`Agents/browser-controller/`

---

## Related Assets

- None (독립적 에이전트)

---

## Best Practices

1. **Canvas 인스턴스 계정별 분리**: 로그인 충돌 방지
2. **Canvas 세션 유지**: 닫지 않고 계속 열어둠
3. **사용자 로그인**: 에이전트는 로그인 후 세션만 사용
4. **Wiki 학습**: 플랫폼 UI 변경 시 `memory/wiki/` 자동 업데이트

---

## Version History

- **1.0.0** (2026-07-10): 최초 등록

---

## Notes

- 로그인은 사용자가 Canvas에서 수동으로 수행
- 플랫폼별 배포 플로우는 memory/wiki에서 학습
- Canvas는 계정별로 독립 인스턴스 유지
