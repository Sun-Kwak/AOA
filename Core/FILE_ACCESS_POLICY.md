# FILE ACCESS POLICY

## Purpose

Define which agents can read, write, and create files within the AIOS repository.
This policy protects the integrity of the framework and enforces project isolation.
All agents must comply with this policy at all times.

---

## Scope

Covers access rules for every directory in the AIOS repository.
Applies to: Root Orchestrator, Project Agents, Shared Agents, Project Sub-Agents.

---

## Access Matrix

| Directory | Root | Project Agent | Shared Agent | Project Sub-Agent |
|-----------|------|---------------|--------------|-------------------|
| `Core/` | Read | Read | Read | Read |
| `Policies/` | Read | Read | Read | Read |
| `Standards/` | Read | Read | Read | Read |
| `Schemas/` | Read | Read | Read | Read |
| `Protocols/` | Read | Read | Read | Read |
| `Registry/` | Read + Write* | Read | Read | Read |
| `Agents/` | Read + Write* | Read | Read | Read |
| `Capabilities/` | Read + Write* | Read | Read | Read |
| `Workflows/` | Read + Write* | Read | Read | Read |
| `Tools/` | Read + Write* | Read | Read | Read |
| `Templates/` | Read + Write* | Read | Read | Read |
| `Memory/` | Read + Write | Read + Write | Read | Read |
| `Knowledge/` | Read + Write* | Read | Read | Read |
| `Observability/` | Read + Write | Read + Write | Read + Write | Read + Write |
| `Projects/<own>/` | Read + Write | Read + Write | Read | Read + Write |
| `Projects/<other>/` | Read | ❌ No Access | ❌ No Access | ❌ No Access |
| `Bootstrap/` | Read | Read | Read | Read |
| `Docs/` | Read + Write* | Read | Read | Read |
| `aios.manifest.yaml` | Read | Read | Read | Read |

> `*` Write requires explicit user approval. Root does not self-approve writes to framework files.

---

## Immutable Directories

The following directories are **read-only for all agents without exception**.
Only a human (the user) may modify their contents directly:

- `Core/`
- `Policies/`
- `Standards/`
- `Schemas/`
- `Bootstrap/`
- `Protocols/`
- `aios.manifest.yaml`

If an agent determines that a framework file needs updating, it must:
1. Flag the proposed change to Root Orchestrator.
2. Root Orchestrator presents the change to the user for review.
3. The user decides and makes the change manually or approves Root to apply it.

---

## Shared Asset Directories

The following directories contain shared assets reusable across all projects:

- `Agents/`
- `Capabilities/`
- `Workflows/`
- `Tools/`
- `Templates/`
- `Registry/`
- `Knowledge/`

**Rules for shared asset directories:**
- Any agent may read.
- Only Root Orchestrator may create or modify, and only with explicit user approval.
- Project Agents must never write directly to these directories.
- If a shared asset needs customization, it must be wrapped inside the project directory.

---

## Project Directory Rules

Each project lives in `Projects/<project-name>/`.

**Project Agent may:**
- Read and write all files within its own `Projects/<project-name>/` directory.
- Create project sub-agents in `Projects/<project-name>/Agents/`.
- Create project-specific workflows, tools, and memory within its project directory.

**Project Agent must never:**
- Read or write files in another project's directory (`Projects/<other-name>/`).
- Write to any shared asset directory (`Agents/`, `Capabilities/`, etc.).
- Write to any framework directory (`Core/`, `Policies/`, `Standards/`, etc.).
- Modify `Registry/INDEX.md` or any Registry entry directly.

---

## Shared Agent Reuse and Override Pattern

When a Project Agent needs a shared agent with modifications:

```
❌ Do NOT:  Modify Agents/<shared-agent>/
✅ Do:      Create Projects/<name>/Agents/<override-agent>/
            Reference the original shared agent
            Override only the parts that differ
```

This preserves shared agent integrity across all projects.

---

## Project Sub-Agent Creation

Project Agents may create project sub-agents directly within their project scope
when all of the following are true:

1. No suitable shared agent exists in `Registry/Agents/`.
2. The required agent is specific to this project only.
3. The user is aware and in active conversation with the Project Agent.

Project sub-agents are created in: `Projects/<project-name>/Agents/`
They must not be registered in the global `Registry/` unless promoted to shared status
by Root Orchestrator with user approval.

---

## Violation Handling

If an agent attempts to access a file outside its permitted scope:

1. Halt the operation immediately.
2. Report the violation to Root Orchestrator.
3. Root Orchestrator logs the violation to `Observability/`.
4. Root Orchestrator informs the user.
5. Do not retry the operation without explicit user approval.

---

## TODO

Define file access audit logging format.
Define promotion process for project-specific agent to shared agent.
