# Registry — Capabilities

## Purpose

Store registration entries for all shared capabilities in AIOS.
Each file in this directory is a registration record, not an implementation.
Implementations live in `Capabilities/`.

---

## Scope

One registration file per capability.
File naming: `<id>.md`

---

## Registration Entry Format

```markdown
# <Name>

id: <unique-id>
type: capability
version: 1.0.0
tags: [tag1, tag2]
path: Capabilities/<name>/
description: One-line description.
status: active

## Summary
Brief description of what this capability does.

## Inputs
List of expected inputs.

## Outputs
List of expected outputs.

## Dependencies
List of other agents, capabilities, or tools this capability requires.
```

---

## TODO

Add registration entries as capabilities are created.
