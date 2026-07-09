# Retry

## Purpose

Define how agents handle failures and when to retry vs escalate.

---

## Scope

Covers retry behavior for: agent failures, tool errors, API failures, file access errors.

---

## Retry Rules

| Failure Type | Max Retries | Backoff | After Max Retries |
|-------------|-------------|---------|-------------------|
| API timeout | 3 | 2s, 4s, 8s | Escalate to Root |
| File not found | 1 | None | Report to caller |
| Agent no response | 2 | 5s, 10s | Escalate to Root |
| Tool execution error | 2 | 1s, 3s | Escalate to Root |
| Registry lookup fail | 1 | None | Treat as not found |

---

## Escalation After Max Retries

1. Stop retrying.
2. Log the failure to `Observability/`.
3. Report to Root Orchestrator with: failure type, attempts made, last error.
4. Root Orchestrator reports to user.
5. Wait for user guidance.

---

## Do Not Retry

Never retry:
- Safety violations.
- Approval-denied actions.
- File access policy violations.

---

## TODO

Define retry behavior for multi-step workflows (partial completion).
