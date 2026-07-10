# Browser Controller Agent - Wiki

## Purpose

browser-controller 에이전트의 실행 패턴, 에러 사례, 플랫폼별 배포 플로우를 누적 학습합니다.

---

## Scope

- Instagram/YouTube/TikTok 배포 워크플로우
- Canvas action 실행 패턴
- 셀렉터 변경 이력
- 에러 대응 전략

---

## Wiki Structure

```
memory/wiki/
  ├── README.md (이 문서)
  ├── instagram_workflow.md (Instagram 배포 플로우)
  ├── youtube_workflow.md (YouTube Shorts 플로우)
  ├── tiktok_workflow.md (TikTok 플로우)
  ├── common_selectors.md (공통 셀렉터 패턴)
  └── error_patterns.md (에러 패턴 누적)
```

---

## Update Protocol

### 플로우 변경 시
1. 새로운 셀렉터 발견 → 해당 플랫폼 workflow.md 업데이트
2. 변경 이력 섹션에 날짜 + 변경 내용 기록

### 에러 발생 시
1. error_patterns.md에 패턴 추가
2. 발생일, 상황, 회피전략 기록

### 성공 플로우
1. 새로운 플랫폼 추가 → 새 workflow.md 생성
2. 단계별 셀렉터 + 대기 시간 문서화

---

## TODO

플랫폼별 배포 플로우는 실제 실행 시 누적됩니다.
