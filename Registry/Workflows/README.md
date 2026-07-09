# Registry — Workflows

## Purpose

Store registration entries for all shared workflows in AIOS.
Each file in this directory is a registration record, not an implementation.
Implementations live in `Workflows/`.

---

## Scope

One registration file per workflow.
File naming: `<id>.md`

---

## Registration Entry Format

```markdown
# <Name>

id: <unique-id>
type: workflow
version: 1.0.0
tags: [tag1, tag2]
path: Workflows/<name>/
description: One-line description.
status: active

## Summary
Brief description of what this workflow does.

## Inputs
List of expected inputs.

## Outputs
List of expected outputs.

## Dependencies
List of other agents, capabilities, or tools this workflow requires.
```

---

## TODO

Add registration entries as workflows are created.
