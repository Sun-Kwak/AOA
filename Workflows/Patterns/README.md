# Workflow Patterns

## Purpose

Define the canonical execution patterns available in AOA.
These patterns are the building blocks for composing workflows from agents.

---

## Scope

| Pattern | Description |
|---------|-------------|
| `Sequential.md` | Agents execute one after another. Each step depends on the previous. |
| `Parallel.md` | Agents execute simultaneously on independent tasks. |
| `Pipeline.md` | Output of one agent is the direct input of the next. |
| `Fan_Out_Fan_In.md` | One task is split across multiple agents, results are aggregated. |
| `Graph_Routing.md` | Dynamic routing based on task state and agent capability. |
| `Delegation.md` | Root hands off a task fully to a sub-agent. |
| `Escalation.md` | Sub-agent cannot resolve — returns control upward. |

---

## TODO

Define pattern composition rules (combining multiple patterns).
Define pattern selection criteria.
