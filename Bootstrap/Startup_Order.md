# Startup Order

## Purpose

Define the exact sequence in which AOA loads its framework components.
This document is the bootloader of AOA.
AI must follow this order every time it initializes a session within an AOA repository.

---

## Scope

This document covers the full initialization sequence from cold start to project execution.
It does not define rules or policies — only the load order.

---

## Startup Sequence

### Step 1 — Read Framework Manifest
- Read `aios.manifest.yaml` from the repository root.
- Confirm `id: AOA` is present.
- Record the framework version and all root paths.

### Step 2 — Verify Repository Structure
- Confirm that the following directories exist:
  - `Bootstrap/`, `Core/`, `Policies/`, `Standards/`
  - `Registry/`, `Schemas/`, `Capabilities/`, `Agents/`
  - `Workflows/`, `Tools/`, `Templates/`, `Memory/`
  - `Knowledge/`, `Projects/`, `Observability/`, `Docs/`
- If any required directory is missing, halt and report to the user.

### Step 3 — Load Bootstrap Documents
- Read `Bootstrap/Initialize.md`
- Read `Bootstrap/Load_Framework.md`

### Step 4 — Load Core
- Read `Core/BOOT.md`
- Read `Core/SYSTEM.md`
- Read `Core/ORCHESTRATOR.md`
- Read `Core/EXECUTION_POLICY.md`
- Read `Core/CONTEXT_POLICY.md`
- Read `Core/FILE_ACCESS_POLICY.md`
- Read `Core/DECISION_POLICY.md`
- Read `Core/OBSERVABILITY_POLICY.md`

### Step 5 — Load Policies
- Read all documents in `Policies/`

### Step 6 — Load Standards
- Read all documents in `Standards/`

### Step 7 — Load Registry Index
- Read `Registry/INDEX.md`
- Read `Registry/Search_Guide.md`
- Do not load individual registry entries yet — load on demand only.

### Step 8 — Restore Memory
- Read `Memory/Framework.md`
- Read `Memory/Session.md`
- If a current project is detected, read `Memory/Project.md`
- Read `Memory/Execution_State.md`
- Read `Memory/Decision_Log.md`

### Step 9 — Detect Current Project
- Inspect `Projects/` for active project context.
- If a project manifest exists, load it.
- If no project context is found, present project selection to the user.

### Step 10 — Load Project Context
- Load the project-specific agents, workflows, and tools as declared in the project manifest.
- Do not load all registry entries — load only what the project requires.

### Step 11 — Execute Request
- Framework is fully loaded.
- Begin processing the user's request.

---

## Rules

- Steps must be followed in order. Do not skip steps.
- If any step fails, halt execution and follow `Bootstrap/Recovery.md`.
- Do not load project-specific context before Core and Policies are loaded.
- Registry entries are loaded on demand, not at startup.

---

## TODO

Extend with environment-specific startup variants (e.g., cloud, local, CI).
