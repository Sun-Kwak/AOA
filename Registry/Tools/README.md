# Registry — Tools

## Purpose

Store registration entries for all shared tools in AIOS.
Each file in this directory is a registration record, not an implementation.
Implementations live in `Tools/`.

---

## Scope

One registration file per tool.
File naming: `<id>.md`

---

## Registration Entry Format

```markdown
# <Name>

id: <unique-id>
type: tool
version: 1.0.0
tags: [tag1, tag2]
path: Tools/<name>/
description: One-line description.
status: active

## Summary
Brief description of what this tool does.

## Inputs
List of expected inputs.

## Outputs
List of expected outputs.

## Dependencies
List of other agents, capabilities, or tools this tool requires.
```

---

## TODO

Add registration entries as tools are created.
