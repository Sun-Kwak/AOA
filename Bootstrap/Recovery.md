# Recovery

## Purpose

Define how AIOS recovers from boot failures and unexpected execution states.
Recovery is triggered when any step in Startup_Order or Initialize fails.

---

## Scope

Covers recovery procedures for:
- Boot failure (Startup_Order step failure)
- Session restore failure (Initialize phase failure)
- Agent execution failure mid-task
- Memory corruption or missing state

---

## Step 1 — Immediate Halt

Stop all execution immediately.
If a file write was in progress, do not finalize it.
Do not attempt to continue the failed step.

---

## Step 2 — Diagnose and Report

Identify and report to the user:

```
⚠️ AIOS Recovery Mode

Failed Step : <step name or phase>
Error       : <what went wrong>
Last Known State : <last successful step>
Impact      : <what cannot proceed without recovery>
```

---

## Step 3 — Safe State Check

Enter read-only mode.
Verify the following are intact (read only, no writes):

- [ ] `aios.manifest.yaml` is readable
- [ ] `Core/BOOT.md` is readable
- [ ] `Core/SYSTEM.md` is readable
- [ ] `Memory/Session.md` is readable (missing is acceptable — treat as fresh start)
- [ ] `Registry/INDEX.md` is readable

If any framework file is missing or unreadable → escalate to user immediately.
Do not attempt auto-repair of framework files.

---

## Step 4 — Present Recovery Options

```
Recovery Options:

  [A] Retry from failed step
      Resume Startup_Order from the point of failure.

  [B] Full reboot
      Restart Startup_Order from Step 1.
      Memory state is preserved but not applied until reboot succeeds.

  [C] Fresh start
      Restart with no memory restoration.
      Current session memory is cleared.
      Use if memory corruption is suspected.

  [D] Manual intervention
      Halt AIOS completely.
      User inspects files directly.
```

Wait for user selection. Do not auto-select.

---

## Step 5 — Post-Recovery

After successful recovery:
- Log the recovery event to `Observability/` with: timestamp, failure type, recovery path taken.
- Update `Memory/Session.md` to reflect the recovery.
- Notify user that AIOS is fully operational.

---

## What Recovery Must Never Do

- Never auto-repair or overwrite framework files (`Core/`, `Policies/`, etc.).
- Never delete Memory files during recovery.
- Never resume an interrupted task without user confirmation.
- Never silently skip a failed boot step.

---

## TODO

Define recovery behavior for multi-agent mid-workflow failures.
Define partial memory recovery when only some Memory files are corrupted.
