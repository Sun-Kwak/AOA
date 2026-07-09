# Execution State

## Purpose

현재 실행 중이거나 중단된 태스크의 상태를 기록한다.
세션이 끊겼을 때 Recovery의 핵심 입력값이다.
태스크 시작 시 기록하고, 완료 시 초기화한다.

---

## Scope

프레임워크 레벨 현재 실행 상태.
프로젝트 상세 실행 상태는 `Projects/<name>/Memory/execution_state.md` 참조.

---

## Schema

```yaml
current_task:
  task_id: null
  project_id: null
  agent_id: null
  status: null              # running | paused | interrupted | null
  started_at: null
  scope: null

completed_steps: []         # 완료된 단계 목록
pending_steps: []           # 남은 단계 목록

interrupted_at: null        # 중단 지점 (없으면 null)
interrupt_reason: null      # 중단 이유 (없으면 null)
resumable: null             # true | false | null
```

---

## Current State

```yaml
current_task:
  task_id: null
  project_id: null
  agent_id: null
  status: null
  started_at: null
  scope: null

completed_steps: []
pending_steps: []
interrupted_at: null
interrupt_reason: null
resumable: null
```

---

## Update Rules

- 태스크 시작 시: `current_task` 채움.
- 단계 완료 시: `completed_steps`에 추가.
- 태스크 정상 완료 시: 전체 초기화 (null로 리셋).
- 중단 시: `interrupted_at`, `interrupt_reason`, `resumable` 기록.

---

## TODO

병렬 태스크 동시 실행 상태 관리 정의.
