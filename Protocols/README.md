# Protocols

## Purpose

Define standard communication and interaction protocols between AIOS agents.
Protocols ensure that agents can interoperate without custom integration code.

---

## Scope

This directory contains:
- Agent-to-agent communication standards
- Context passing contracts
- Handoff procedures between agents
- Session bridge protocol for cross-session agent initialization

---

## Contents

| File | Responsibility |
|------|---------------|
| `Agent_Communication.md` | Message format and interaction rules between agents |
| `Handoff.md` | How an agent transfers control and context to another agent |
| `Context_Passing.md` | What context is passed, how it is scoped, and what is excluded |
| `Session_Bridge.md` | How context is preserved and injected across session boundaries |

---

## TODO

Define versioning for protocol changes.
Define backward compatibility rules.
