# Project Memory

## Purpose

AOA에 등록된 모든 프로젝트의 요약 인덱스.
Root Orchestrator가 어떤 프로젝트가 존재하고 어느 단계인지 파악하기 위해 읽는다.
상세 프로젝트 메모리는 각 프로젝트 디렉터리에 있다.

---

## Scope

프로젝트 목록, 상태 요약, 경로 참조.
프로젝트 상세 내용은 `Projects/<name>/Memory/project.md` 참조.

---

## Schema

```yaml
projects:
  - id: <project-id>
    name: <프로젝트 이름>
    status: <active|paused|archived>
    current_phase: <현재 단계 한 줄>
    last_updated: <ISO 8601 date>
    path: Projects/<name>/Memory/project.md
```

---

## Current Projects

```yaml
projects:
  - id: daily-stock-pick
    name: 해외 뉴스 기반 오늘의 추천 주
    status: active
    current_phase: 첫 워크플로우 실행 완료
    last_updated: 2026-07-09
    path: Projects/daily-stock-pick/Memory/project.md
```

---

## Update Rules

- 프로젝트 생성 시: 항목 추가.
- 프로젝트 상태 변경 시: `status`, `current_phase`, `last_updated` 갱신.
- 프로젝트 아카이브 시: `status: archived` (삭제하지 않음).
- Root Orchestrator만 수정 가능.

---

## TODO

프로젝트 태그 및 카테고리 필터 추가.
