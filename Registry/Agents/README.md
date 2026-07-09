# Registry — Agents

## Purpose

Store registration entries for all shared agents in AOA.
Each file in this directory is a registration record, not an implementation.
Implementations live in `Agents/`.

---

## Scope

One registration file per agent.
File naming: `<id>.md`

---

## Registration Entry Format

```markdown
# <Name>

id: <unique-id>
type: agent
version: 1.0.0
tags: [tag1, tag2]
path: Agents/<name>/
description: One-line description.
status: active

## Summary
Brief description of what this agent does.

## Inputs
List of expected inputs.

## Outputs
List of expected outputs.

## Dependencies
List of other agents, capabilities, or tools this agent requires.
```

---

## TODO

Add registration entries as agents are created.
