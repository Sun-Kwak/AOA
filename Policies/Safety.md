# Safety

## Purpose

Define the actions that are absolutely prohibited within AIOS.
Safety rules are non-negotiable and cannot be overridden by any agent, workflow, or project.
When a safety rule conflicts with a task requirement, the safety rule always wins.

---

## Scope

Applies to all agents at all times:
- Root Orchestrator
- Project Agents
- Shared Agents
- Project Sub-Agents

---

## Absolute Prohibitions

### 1. Framework Integrity
- Never modify any file in `Core/`, `Policies/`, `Standards/`, `Bootstrap/`, `Protocols/`, `Schemas/`.
- Never modify `aios.manifest.yaml` without explicit user approval.
- Never delete any framework file.
- Never rename or move framework directories.

### 2. Registry and Shared Asset Protection
- Never write to `Registry/INDEX.md` without Root Orchestrator + user approval.
- Never create or modify files in `Agents/`, `Capabilities/`, `Workflows/`, `Tools/`, `Templates/` without Root Orchestrator + user approval.
- Never delete a registered shared asset.

### 3. Project Isolation
- Never read files from another project's directory (`Projects/<other>/`).
- Never write files to another project's directory.
- Never pass one project's memory or context to another project's agent.

### 4. Credential and Secret Handling
- Never log, store, or transmit API keys, tokens, passwords, or secrets.
- Never include credentials in any Markdown, YAML, or memory file.
- Never pass credentials between agents as part of a context slice.

### 5. Irreversible Actions
- Never delete files or directories without explicit user confirmation.
- Never overwrite an existing file without confirming the operation is intentional.
- Never execute batch operations affecting more than 10 files without user approval.

### 6. External Communication
- Never send data to external APIs without explicit user approval per operation.
- Never transmit project content, memory, or user data to third-party services without approval.

### 7. Self-Modification
- No agent may modify its own definition file.
- No agent may modify the agent definition of another agent.
- Agent definitions may only be modified by Root Orchestrator with user approval.

---

## Safety Check Protocol

Before executing any significant action, an agent must verify:

- [ ] Does this action modify a framework file? → If yes, HALT.
- [ ] Does this action write to a shared asset directory? → If yes, require Root + user approval.
- [ ] Does this action affect another project's directory? → If yes, HALT.
- [ ] Does this action involve credentials or secrets? → If yes, HALT.
- [ ] Does this action delete or overwrite existing files? → If yes, require user confirmation.
- [ ] Does this action send data externally? → If yes, require user approval.

If any check fails, halt immediately and report to Root Orchestrator.

---

## When Safety Conflicts with Task Requirements

If completing a user's requested task would require violating a safety rule:

1. Do not proceed with the task.
2. Explain clearly which safety rule would be violated.
3. Propose an alternative approach that does not violate safety.
4. Wait for user guidance before continuing.

Do not attempt to find workarounds that technically comply but violate the spirit of the rule.

---

## Safety Violation Response

When a safety violation is detected or attempted:

1. Halt execution immediately.
2. Log the violation to `Observability/` with: timestamp, agent, attempted action, violated rule.
3. Report to Root Orchestrator.
4. Root Orchestrator notifies the user.
5. Do not resume until the user explicitly clears the violation.

---

## TODO

Define safety rule versioning and change approval process.
Define escalation path for ambiguous safety decisions.
