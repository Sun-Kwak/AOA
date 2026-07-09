# Session Memory

## Purpose

현재 및 마지막 세션의 상태를 기록한다.
모든 새 세션은 이 파일을 읽어 이전 상태를 복원한다.
세션 시작 시 읽고, 세션 종료 시 덮어쓴다.

---

## Scope

세션 식별 정보, 활성 프로젝트, 마지막 에이전트.
상세 실행 상태는 Execution_State.md에 있다.

---

## Schema

```yaml
session_id: null
status: null                # active | ended | interrupted
started_at: null            # ISO 8601
ended_at: null              # ISO 8601 — 진행 중이면 null

active_project: null        # 프로젝트 ID
active_agent: null          # 마지막 활성 에이전트 ID
last_task_id: null          # 마지막 태스크 ID

notes: null                 # 특이사항
```

---

## Current Session

```yaml
session_id: null
status: null
started_at: null
ended_at: null
active_project: null
active_agent: null
last_task_id: null
notes: null
```

---

## Update Rules

- 세션 시작 시: `status: active`, `started_at` 기록.
- 세션 정상 종료 시: `status: ended`, `ended_at` 기록.
- 세션 중단 시: `status: interrupted`, `ended_at` 기록.
- 다음 세션 시작 시: 이전 값을 읽고 새 값으로 덮어씀.

---

## TODO

멀티 세션 동시 실행 시 세션 ID 충돌 처리 정의.
