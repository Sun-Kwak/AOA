# Framework Memory

## Purpose

AIOS 프레임워크 자체의 상태를 기록한다.
거의 변경되지 않으며, 프레임워크 레벨의 결정과 알려진 이슈를 보존한다.
Root Orchestrator가 부팅 시 읽는다.

---

## Scope

프레임워크 버전, 알려진 이슈, 프레임워크 레벨 결정.
프로젝트 관련 내용은 포함하지 않는다.

---

## Current State

```yaml
aios_version: 1.0.0
schema_version: "1.0"
initialized_at: 2026-07-09

status: active              # active | maintenance | degraded

known_issues: []            # 알려진 이슈 목록

framework_decisions:        # 프레임워크 레벨 결정 요약
  - date: 2026-07-09
    decision: "초기 구조 확정"
    note: "Bootstrap, Core, Policies, Standards, Protocols 완성"
```

---

## Update Rules

- Root Orchestrator만 수정 가능.
- 수정 시 `updated_at` 갱신.
- `known_issues` 추가 시 해결 여부도 기록.

---

## TODO

Framework 마이그레이션 이력 추가.
