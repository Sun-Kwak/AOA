# CONTEXT POLICY

## Purpose

Define what context is passed between agents, how it is scoped, and what is excluded.
This policy is the primary mechanism for token efficiency in AOA.
Without this policy, agents re-read the entire framework on every operation.

---

## Scope

Covers:
- Context layers and ownership
- Context slice construction rules
- What is never included in a context slice
- On-demand context loading

---

## Context Layers

AOA context is organized into three layers.
Each layer is owned by a specific agent tier.

### Layer 1 — Framework Context
**Owner: Root Orchestrator only**

Contents:
- Core documents (BOOT, SYSTEM, ORCHESTRATOR, all policies)
- Standards
- Registry INDEX

Rules:
- Root loads this once at boot.
- Never passed to sub-agents.
- Sub-agents operate under the assumption that Framework rules apply — they do not need the files.
- If a sub-agent needs to reference a specific rule, Root looks it up and passes only the relevant excerpt.

---

### Layer 2 — Project Context
**Owner: Project Agent**

Contents:
- Project manifest
- Project memory (`Memory/Project.md`)
- Active workflow definition
- Registered project agents list

Rules:
- Project Agent loads this when the project is activated.
- Passed to Project Sub-Agents as a scoped slice (not the full project context).
- Never passed to another project's agents.

---

### Layer 3 — Task Context
**Owner: Created per task delegation**

Contents:
- Task description and scope
- Required inputs
- Expected outputs
- Relevant memory slice (only what the task needs)
- Reference to applicable agents or tools

Rules:
- Created by the delegating agent before each delegation.
- Contains only what is needed to complete the specific task.
- Discarded after task completion.
- Never accumulates across tasks.

---

## Slice Construction Rules

When delegating a task, the delegating agent constructs a Task Context slice:

```
Task Context Slice Format:

task_id     : <unique id>
task_scope  : <one sentence describing what this task does>
inputs      : <list of inputs available>
outputs     : <list of expected outputs>
constraints : <any rules specific to this task>
memory      : <only the memory fields relevant to this task>
agent_role  : <role the receiving agent should play>
```

**Include only what the receiving agent needs to complete the task.**
Do not include project history, unrelated memory, or framework content.

---

## What is Never Included in a Context Slice

- Full Core or Policy documents
- Another project's memory or context
- Credentials, API keys, secrets
- Completed task results from unrelated tasks
- Full Registry contents (reference by ID only)
- Full agent definitions (reference by ID and role only)

---

## On-Demand Context Loading

Sub-agents may request additional context from their parent agent when needed.

Protocol:
1. Sub-agent sends a context request: `"Need: <specific information>"`
2. Parent agent evaluates whether the request is within scope.
3. If within scope → parent passes the specific excerpt only.
4. If out of scope → parent denies and explains why.

Sub-agents must not independently load files outside their permitted scope.

---

## Session Context Injection (Cross-Session)

When a sub-agent starts in a new Copilot session:

Root Orchestrator provides the minimum viable context package:

```
aios_version    : <version>
active_project  : <project name>
project_path    : Projects/<name>/
agent_role      : <assigned role>
task_scope      : <description of delegated work>
memory_slice    : <relevant memory excerpt>
framework_rules : "Apply AOA Core rules. Full framework loaded by Root."
```

The sub-agent acknowledges this package before proceeding.

---

## TODO

Define context slice size guidelines (token budget per tier).
Define context request throttling to prevent excessive back-and-forth.
