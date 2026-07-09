# BOOT

## Purpose

Define the kernel initialization rules of AOA.
BOOT establishes the fundamental operating conditions that must be satisfied
before any agent, workflow, or project can execute.

---

## Scope

BOOT covers:
- Framework identity verification
- Minimum required context before execution
- Failure conditions that block execution
- Handoff to SYSTEM after successful boot

BOOT does not define agent behavior, policies, or project logic.

---

## Boot Conditions

### Required to proceed

Before executing any user request, the following must be confirmed:

1. `aios.manifest.yaml` has been read and validated.
2. `id: AOA` is confirmed in the manifest.
3. Framework version is recorded.
4. `Bootstrap/Startup_Order.md` has been followed.
5. All Core documents have been loaded.
6. All Policies have been loaded.
7. All Standards have been loaded.
8. `Registry/INDEX.md` has been read.
9. Memory state has been restored.

### Boot is complete when

All nine conditions above are satisfied.
Execution is then handed to `Core/SYSTEM.md`.

---

## Boot Failure

If any condition cannot be satisfied:

1. Do not proceed with execution.
2. Report the failure condition clearly to the user.
3. Follow `Bootstrap/Recovery.md`.

---

## Principles

- Boot must be silent unless a failure occurs.
- Boot must not modify any file.
- Boot must not execute any project-specific logic.
- Boot must complete before any user request is processed.

---

## TODO

Define environment-specific boot checks (local, cloud, CI/CD).
