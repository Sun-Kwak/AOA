# EXECUTION POLICY

## Purpose

Define how tasks are structured, scoped, and executed within AIOS.
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

When a task requires delegation to an agent that does not have an active Copilot session:

1. Root Orchestrator checks whether a session for that agent exists in the session panel.
2. If no session exists → Root creates the session at delegation time.
3. The new session is injected with the Task Context slice (CONTEXT_POLICY).
4. The session becomes visible in the panel for the duration of the task.
5. Session remains open for follow-up unless the user closes it.

**Sessions are created on demand, not at boot.**
Only sessions for agents actively being used are created.

---

## TODO

Define task ID generation format.
Define task history retention policy.
Define parallel task execution coordination rules.
