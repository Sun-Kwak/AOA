# Policies

## Purpose

Define the execution governance rules for AOA.
Policies control what agents can do, when they must pause, and what is absolutely forbidden.
Policies are enforced at all times across all agents and projects.

---

## Scope

| File | Role |
|------|------|
| `Safety.md` | Absolute prohibitions — rules that can never be violated |
| `File_Access_Policy` | → See `Core/FILE_ACCESS_POLICY.md` |
| `Human_In_The_Loop.md` | When agents must pause for human input |
| `Approval.md` | Approval levels and chains for permitted actions |
| `Retry.md` | Failure handling and retry behavior |
| `Cost_Control.md` | Resource and volume limits |

---

## Policy Priority

When policies conflict, apply in this order:

1. `Safety.md` — highest priority, always wins
2. `Core/FILE_ACCESS_POLICY.md`
3. `Human_In_The_Loop.md`
4. `Approval.md`
5. `Retry.md`
6. `Cost_Control.md`

---

## TODO

Define policy versioning and change approval process.
