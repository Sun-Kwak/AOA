# Registry — Templates

## Purpose

Store registration entries for all shared templates in AOA.
Each file in this directory is a registration record, not an implementation.
Implementations live in `Templates/`.

---

## Scope

One registration file per template.
File naming: `<id>.md`

---

## Registration Entry Format

```markdown
# <Name>

id: <unique-id>
type: template
version: 1.0.0
tags: [tag1, tag2]
path: Templates/<name>/
description: One-line description.
status: active

## Summary
Brief description of what this template does.

## Inputs
List of expected inputs.

## Outputs
List of expected outputs.

## Dependencies
List of other agents, capabilities, or tools this template requires.
```

---

## TODO

Add registration entries as templates are created.
