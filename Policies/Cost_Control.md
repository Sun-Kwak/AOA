# Cost Control

## Purpose

Define thresholds and controls that prevent unintended resource consumption.

---

## Scope

Covers: API call volume, batch operation size, and external service usage limits.

---

## Default Thresholds

| Resource | Soft Limit | Hard Limit | Action at Hard Limit |
|----------|-----------|------------|----------------------|
| Files per operation | 10 | 50 | Halt + user approval |
| External API calls per task | 20 | 100 | Halt + user approval |
| Agent delegations per workflow | 5 | 15 | Halt + report |

Soft limit: warn the user and continue.
Hard limit: halt and require explicit user approval to continue.

---

## Rules

- Never run unbounded loops that call external APIs.
- Always estimate cost/volume before starting a batch operation.
- If estimated volume exceeds soft limit, inform user before starting.

---

## TODO

Define per-project cost budgets.
Define cost tracking integration with Observability.
