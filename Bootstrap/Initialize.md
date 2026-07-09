# Initialize

## Purpose

Define how AOA restores full framework context at the start of every new session.
Every AI session begins cold — no memory, no context.
This document defines the mandatory restoration protocol that bridges sessions.

---

## Scope

This document covers:
- New session detection
- Framework context restoration sequence
- Project context restoration
- Memory restoration
- Verification before execution

---

## The Core Problem

LLM sessions are stateless.
Every new session starts with zero context.
AOA solves this by defining an explicit restoration sequence that the AI must execute
at the beginning of every session before processing any user request.

---

## Restoration Protocol

### Phase 1 — Framework Restoration

Execute `Bootstrap/Startup_Order.md` in full.

This loads:
- `aios.manifest.yaml`
- All Core documents
- All Policies
- All Standards
- Registry index

**This phase must complete before any other phase begins.**

---

### Phase 2 — Session Memory Restoration

Read `Memory/Session.md`.

Extract:
- Last active project
- Last active agent
- Last execution state
- Any pending tasks from the previous session

If `Memory/Session.md` is empty or missing:
- Treat this as a fresh start.
- Proceed to Phase 3.

---

### Phase 3 — Project Context Restoration

If a last active project is found in session memory:

1. Navigate to `Projects/<project-name>/`
2. Read the project manifest (`manifest.yaml`).
3. Load `dependencies` from the manifest — agents and tools declared for this project.
   - Do NOT search Registry at this point — use only what is declared in dependencies.
   - If a declared dependency is missing from Registry, report to user before proceeding.
4. Load project-specific workflows.
5. Read `Memory/Project.md` for project-level state.

If no project context is found:
- Present available projects to the user.
- Wait for user selection before proceeding.

---

### Phase 4 — Execution State Restoration

Read `Memory/Execution_State.md`.

Determine:
- Was there an interrupted task?
- Are there pending decisions?
- Is there a mid-execution workflow to resume?

If interrupted state is found:
- Present the interrupted state to the user.
- Ask whether to resume or start fresh.

---

### Phase 5 — Verification

Before processing any user request, confirm:

- [ ] Framework manifest loaded
- [ ] Core documents loaded
- [ ] Policies loaded
- [ ] Standards loaded
- [ ] Registry index loaded
- [ ] Session memory restored
- [ ] Project context loaded (if applicable)
- [ ] Execution state checked

If all checks pass → proceed to execute the user's request.
If any check fails → follow `Bootstrap/Recovery.md`.

---

## Agent Context Inheritance

When the Root Orchestrator delegates to a sub-agent or project agent within the same session:
- The sub-agent does NOT re-execute the full restoration protocol.
- The Root Orchestrator passes a scoped context slice to the sub-agent.
- The sub-agent operates within the context it receives.

When a sub-agent starts in a NEW session (e.g., a spawned agent in a separate context):
- That agent must execute Phase 1 (Framework Restoration) independently.
- Phase 2–4 are provided by the Root Orchestrator via context injection.

---

## Context Injection Format

When the Root Orchestrator initializes a sub-agent in a new session,
it must provide the following minimum context:

```
AOA Framework Version: <version>
Active Project: <project-name>
Project Manifest: <path>
Assigned Role: <agent-role>
Task Scope: <description of delegated task>
Relevant Memory: <scoped memory slice>
```

The sub-agent must acknowledge receipt before proceeding.

---

## TODO

Define structured context injection schema.
Define session ID tracking across multi-agent sessions.
