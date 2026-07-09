# ORCHESTRATOR

## Purpose

Define how AIOS Root Orchestrator delegates tasks to sub-agents and project agents.
The Root Orchestrator is the single entry point for all execution within AIOS.
All sub-agents and project agents operate under the authority of the Root Orchestrator.

---

## Scope

This document covers:
- Orchestrator hierarchy and roles
- Task delegation rules
- Agent selection and lookup
- Missing agent escalation
- Context passing between agents
- Shared vs project-specific agent boundaries
- Token efficiency rules

---

## Orchestrator Hierarchy

```
User
  └── AIOS Root Orchestrator
        ├── Shared Agents (Registry — reusable across all projects)
        └── Project Agent (project-specific root)
              ├── Shared Agents (delegated from Registry)
              └── Project Sub-Agents (project-specific)
```

### Root Orchestrator
- Owns the full AIOS framework context.
- Is the only agent that reads Core, Policies, Standards, and Registry at startup.
- Delegates tasks downward. Never executes project-specific logic directly.
- Is the arbiter for missing agents and escalation.

### Project Agent
- Scoped to one project.
- Reports to the Root Orchestrator.
- Can call Shared Agents from the Registry.
- Can spawn Project Sub-Agents for specialized tasks within the project.
- Does not have direct access to other projects.

### Shared Agent
- Registered in `Registry/Agents/`.
- Stateless and project-independent.
- Can be called by any Project Agent.
- Defined in `Agents/`.

### Project Sub-Agent
- Defined within a specific project.
- Operates under the Project Agent.
- Has access only to the project's own context.

---

## Delegation Rules

1. **Root to Project Agent**
   - The Root Orchestrator delegates the full user request to the relevant Project Agent.
   - The Project Agent receives task scope, relevant context, and memory state.
   - The Root Orchestrator does not re-explain Core or Policies — the Project Agent inherits them.

2. **Project Agent to Shared Agent**
   - Look up `Registry/Agents/` before delegating.
   - Pass only the minimum context required for the task.
   - Shared Agents must not receive full project memory unless explicitly required.

3. **Project Agent to Project Sub-Agent**
   - Spawn a Project Sub-Agent only when the task is specialized enough to warrant isolation.
   - Pass scoped context only.
   - Sub-Agent results are returned to the Project Agent, not to the Root.

---

## Agent Selection

When delegating a task, follow this order:

1. Search `Registry/Agents/` for a matching Shared Agent.
2. If found → delegate to the Shared Agent.
3. If not found → search `Projects/<project>/Agents/` for a Project Sub-Agent.
4. If not found → escalate to Root Orchestrator.
5. Root Orchestrator escalates to user → new agent is created and registered.

---

## Missing Agent Protocol

When a required agent does not exist:

1. The requesting agent reports the missing agent to the Root Orchestrator.
2. The Root Orchestrator informs the user.
3. The user and Root Orchestrator define the new agent together.
4. The new agent is created in `Agents/` (if shared) or `Projects/<project>/Agents/` (if project-specific).
5. The new agent is registered in `Registry/Agents/`.
6. The task is resumed with the new agent.

---

## Context Passing Rules

- The Root Orchestrator holds the full framework context. Sub-agents do not re-load it.
- When delegating, pass only the context slice relevant to the sub-task.
- Sub-agents return results, not full context, back to the caller.
- Memory updates are written by the agent that performed the action, not the caller.

---

## Token Efficiency Rules

- Sub-agents do not re-read Core, Policies, or Standards — they inherit from the Root.
- Do not pass full project memory to Shared Agents.
- Do not pass registry contents to sub-agents unless required.
- Scope every delegation to the minimum necessary context.

---

## Execution Patterns

| Pattern    | When to Use                                           |
|------------|-------------------------------------------------------|
| Sequential | Task B depends on the result of Task A                |
| Parallel   | Task A and Task B are independent                     |
| Pipeline   | Output of Agent A is the input of Agent B             |
| Delegation | Task is fully handed to a sub-agent                   |
| Escalation | Sub-agent cannot resolve — returns to Root            |

---

## TODO

Define inter-project agent collaboration rules.
Define agent versioning and compatibility rules.
Define timeout and retry behavior for delegated tasks.

---

## On-Demand Session Management

Agent sessions in the Copilot session panel are created on demand, not at boot.

### Rules

1. When a task requires delegation, Root checks whether the target agent has an active session.
2. If no session exists → Root creates the session immediately before delegation.
3. The session is injected with the appropriate Task Context slice.
4. The session appears in the panel so the user can observe and interact if needed.
5. Sessions persist until the user closes them.

### Why On-Demand

- Avoids cluttering the session panel with unused agent sessions.
- Ensures every visible session is actively working on something.
- Allows the user to see exactly which agents are currently in use.

### Session Naming Convention

```
[AIOS] <Project Name> — <Agent Role>
Examples:
  [AIOS] kids-video-gen — Video Script Agent
  [AIOS] Shared — YouTube Upload Agent
```
