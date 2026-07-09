# EXECUTION POLICY

## Purpose

Define how tasks are structured, scoped, and executed within AOA.
This policy ensures that every task has clear boundaries, a defined completion state,
and does not silently expand beyond its original scope.

---

## Scope

Covers:
- What constitutes a task
- Task decomposition rules
- Execution boundaries
- Completion criteria
- Partial completion handling
- Out-of-scope detection

---

## What is a Task

A task is a unit of work that:
- Has a clear start condition (trigger or user request)
- Has a clear completion condition (verifiable output)
- Can be assigned to a single agent or a single delegation chain
- Does not require unplanned Human-in-the-Loop interruptions mid-execution

If a task requires Human input mid-way, it must be split into two tasks:
Task A (up to the pause point) and Task B (after human input).

---

## Task Decomposition Rules

When a user request is too large for a single agent:

1. Root Orchestrator breaks it into sub-tasks.
2. Each sub-task must satisfy the task definition above.
3. Sub-tasks are assigned to appropriate agents via delegation.
4. Sub-task results are aggregated by the Root or Project Agent.
5. The combined result is returned to the user.

**Maximum delegation depth: 3 levels**
```
Root → Project Agent → Sub-Agent → (tool call only beyond this)
```
If a task requires deeper nesting, redesign the task decomposition.

---

## Execution Boundaries

Before starting a task, confirm:

- [ ] Task scope is defined (what will and will not be done)
- [ ] File access is within permitted scope (FILE_ACCESS_POLICY)
- [ ] Human approval conditions are checked (Human_In_The_Loop)
- [ ] Safety rules are satisfied (Safety Policy)
- [ ] Context slice is prepared (CONTEXT_POLICY)

Do not begin execution until all checks pass.

---

## Scope Control

During execution, if a new action is discovered that was not part of the original scope:

1. Do NOT execute the out-of-scope action.
2. Complete the current in-scope task.
3. Report the discovered out-of-scope item to the user as a follow-up suggestion.

**Never silently expand task scope during execution.**

---

## Completion Criteria

A task is complete only when ALL of the following are confirmed:

- [ ] The defined output has been produced
- [ ] All files written are saved and verified
- [ ] `Memory/Execution_State.md` is updated
- [ ] Observability log entry written
- [ ] Result returned to the calling agent or user

A task is NOT complete if any item above is pending.

---

## Partial Completion

If a task fails mid-execution:

1. Record completed steps in `Memory/Execution_State.md`:
   ```
   task_id     : <id>
   status      : partial
   completed   : [list of completed steps]
   failed_at   : <step name>
   reason      : <error description>
   ```
2. Do not leave files in an inconsistent state.
3. Report to Root Orchestrator.
4. Follow `Policies/Retry.md` for retry decisions.
5. Do not auto-resume without user awareness.

---

## Agent Session On-Demand Rule

세션은 부팅 시가 아니라 실제로 필요할 때 생성된다.
**세션 생성 주체는 계층에 따라 다르다.**

### 계층별 세션 생성 책임

| 생성 주체 | 생성 대상 세션 | 규칙 |
|-----------|---------------|------|
| Root | Project Agent 세션 | 프로젝트 워크플로우 실행 요청 시 1개만 생성 |
| Project Agent | 공용 에이전트 세션 | 워크플로우 내 필요한 공용 에이전트 세션 생성 ✅ |
| Project Agent | 프로젝트 서브에이전트 세션 | 프로젝트 전용 서브 작업 시 생성 ✅ |
| Sub-Agent | 추가 서브 세션 | 필요 시 추가 하위 세션 생성 가능 ✅ |

### Root의 역할 범위

Root는 다음만 수행한다:

1. Project Agent 세션이 있는지 확인한다.
2. 없으면 Project Agent 세션을 생성하고 전체 워크플로우를 위임한다.
3. Project Agent가 완료 보고를 보낼 때까지 기다린다.
4. **Root는 공용 에이전트나 프로젝트 서브에이전트를 직접 생성하지 않는다.**

### Project Agent의 역할 범위

Project Agent는 다음을 수행한다:

1. manifest.yaml의 dependencies를 확인한다.
2. 필요한 공용 에이전트 세션을 직접 생성하고 위임한다.
3. 프로젝트 서브에이전트 세션을 직접 생성하고 위임한다.
4. 모든 단계 완료 후 Root에 최종 결과를 보고한다.

### 세션 패널 계층 구조

```
Root Session
  └── [AOA] <Project> — Project Agent       ← Root가 생성
        ├── [AOA] Shared — <Agent>           ← Project Agent가 생성
        ├── [AOA] Shared — <Agent>           ← Project Agent가 생성
        └── [AOA] <Project> — <Sub-Agent>    ← Project Agent가 생성
```

**Sessions are created on demand, not at boot.**

---

## TODO

Define task ID generation format.
Define task history retention policy.
Define parallel task execution coordination rules.
