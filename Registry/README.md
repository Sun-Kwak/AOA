# Registry

## Purpose

The Registry is the searchable catalog of all reusable AOA assets.
It is the first place to look before creating any agent, capability, workflow, tool, or template.
The Registry stores only indexes and metadata — never implementations.

---

## Scope

The Registry catalogs:
- Shared Agents
- Capabilities
- Workflows
- Tools
- Templates

Implementations live in their respective top-level directories:
`Agents/`, `Capabilities/`, `Workflows/`, `Tools/`, `Templates/`

---

## How to Use

1. Start at `Registry/INDEX.md` — single entry point for all assets.
2. Use `Registry/Search_Guide.md` to find assets by keyword, tag, or type.
3. Once located, follow the path to the implementation file.
4. If no suitable asset exists, escalate to Root Orchestrator to create and register a new one.

---

## Sub-directories

| Directory | Contains |
|-----------|----------|
| `Agents/` | Agent registration entries |
| `Capabilities/` | Capability registration entries |
| `Workflows/` | Workflow registration entries |
| `Tools/` | Tool registration entries |
| `Templates/` | Template registration entries |

---

## TODO

Define automated index generation from registration files.
