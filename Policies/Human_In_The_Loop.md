# Human In The Loop

## Purpose

Define the conditions under which an agent must pause and wait for human input
before proceeding with execution.
Automation is powerful — this policy defines its limits.

---

## Scope

Applies to all agents. Defines mandatory pause points, not suggestions.

---

## Mandatory Pause Conditions

An agent must stop and wait for user confirmation before proceeding when:

### Creation
- Creating a new shared agent, capability, workflow, tool, or template.
- Registering any new asset in `Registry/INDEX.md`.
- Creating a new project in `Projects/`.

### Modification
- Modifying any file in a shared asset directory.
- Changing a project manifest.
- Updating `Memory/Framework.md` or `Memory/Project.md`.

### Deletion
- Deleting any file or directory anywhere in the repository.

### External Actions
- Sending any content to an external API or service.
- Publishing, posting, or distributing any content.
- Sending any message (email, chat, notification) on behalf of the user.

### Scope-Exceeding Actions
- Any single operation affecting more than 10 files simultaneously.
- Any task that was not explicitly part of the original user request.
- Any action that cannot be undone.

---

## Pause Format

When pausing for human input, present clearly:

```
⏸ Human Input Required

Action: <description of what is about to happen>
Reason: <why this requires confirmation>
Impact: <what will change if approved>

Options:
  [Approve] — Proceed with the action
  [Modify]  — Change parameters before proceeding
  [Cancel]  — Do not proceed
```

---

## Autonomous Operation (No Pause Required)

An agent may proceed without pausing for:
- Reading any permitted file.
- Writing within its own project directory (non-destructive operations).
- Creating new project sub-agents within project scope.
- Updating `Memory/Session.md` or `Memory/Execution_State.md`.
- Logging to `Observability/`.
- Searching the Registry.

---

## TODO

Define async approval flow for long-running workflows.
Define approval delegation (can Project Agent approve on behalf of user for pre-approved task types?).
