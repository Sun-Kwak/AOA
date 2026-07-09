# Search Guide

## Purpose

Define how to efficiently find assets in the AIOS Registry.
Following this guide avoids unnecessary file reads and reduces token cost.

---

## Scope

Covers search strategies for:
- Finding an asset by type
- Finding an asset by keyword
- Finding an asset by tag
- Determining if an asset exists before creating a new one

---

## Search Strategy

### Step 1 — Check INDEX.md first

Always start at `Registry/INDEX.md`.

- Scan the Asset Summary table to confirm the asset type has registered entries.
- If count is 0 for the needed type → asset does not exist → skip to Step 4.
- If count > 0 → proceed to Step 2.

**Do not open individual registry files before completing Step 1.**

---

### Step 2 — Scan the relevant section in INDEX.md

Each asset type has its own section in INDEX.md with a summary table.

- Scan the `Name` and `Tags` columns for a match.
- If a match is found → note the `Path` → proceed to Step 3.
- If no match → proceed to Step 4.

---

### Step 3 — Load the asset

Navigate to the `Path` from the INDEX entry.
Read the implementation file.
Do not read other assets in the same directory.

---

### Step 4 — Asset not found

If no matching asset exists:

1. Report to Root Orchestrator: "No matching asset found for [description]."
2. Root Orchestrator escalates to user.
3. New asset is defined, created, and registered.
4. INDEX.md is updated.

---

## Tag Conventions

Tags are comma-separated keywords in the INDEX entry.
Use tags to narrow search before reading asset details.

| Tag | Meaning |
|-----|---------|
| `content` | Content creation related |
| `video` | Video production related |
| `social` | Social media related |
| `email` | Email automation related |
| `data` | Data processing related |
| `research` | Research and information gathering |
| `writing` | Text generation and editing |
| `scheduling` | Time and calendar related |
| `notification` | Alerts and messaging |
| `file` | File management related |

> New tags can be added as needed. Document new tags in this table.

---

## Search Decision Tree

```
Need an asset?
  ↓
Read Registry/INDEX.md
  ↓
Asset type has entries?
  → NO  → Create new asset
  → YES ↓
Scan name/tags in INDEX section
  ↓
Match found?
  → NO  → Create new asset
  → YES ↓
Load implementation at Path
  ↓
Asset fits the need?
  → NO  → Create new asset (or adapt existing)
  → YES → Use the asset
```

---

## TODO

Define fuzzy matching guidelines for similar-but-not-identical assets.
Define deprecation search behavior (skip deprecated assets by default).
