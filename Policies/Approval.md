# Approval

## Purpose

Define which actions require explicit approval, who can approve them,
and what happens when approval is denied.

---

## Scope

Covers the approval chain for actions that are permitted but require authorization
before execution. Complements Safety.md (which covers absolute prohibitions).

---

## Approval Levels

| Level | Approver | Examples |
|-------|----------|---------|
| L1 — User | The user directly | New shared agent, Registry update, external send |
| L2 — Root + User | Root presents, user approves | Framework file update, shared asset deletion |
| L3 — Automatic | No approval needed | Read operations, project-scoped writes, memory updates |

---

## L1 Actions (User Approval Required)

- Creating a new shared agent, capability, workflow, tool, or template.
- Updating `Registry/INDEX.md`.
- Creating a new project.
- Sending content externally (API, email, publish).
- Deleting any file.

## L2 Actions (Root + User Approval Required)

- Modifying any file in `Core/`, `Policies/`, `Standards/`, `Schemas/`.
- Modifying `aios.manifest.yaml`.
- Promoting a project-specific agent to shared status.
- Modifying `Memory/Framework.md`.

## L3 Actions (No Approval Required)

- Any read operation within permitted scope.
- Writing within `Projects/<own>/` (non-destructive).
- Creating project sub-agents within project scope (user in active conversation).
- Updating `Memory/Session.md`, `Memory/Execution_State.md`.
- Logging to `Observability/`.

---

## Approval Denial

If approval is denied:
1. Do not proceed with the action.
2. Record the denial in `Memory/Decision_Log.md`.
3. Propose an alternative if one exists.
4. Close the task cleanly.

---

## TODO

Define approval expiry (does a prior approval cover repeat actions?).
Define bulk approval for pre-approved task types.
