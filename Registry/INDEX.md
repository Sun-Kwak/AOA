# AIOS Registry Index

> **Cold Start Instruction**: Read this file first.
> Do NOT read individual registry directories until a specific asset is needed.
> This index provides enough information to determine whether an asset exists.
> Load full asset details on demand only.

---

## Framework Version

| Key | Value |
|-----|-------|
| AIOS Version | 1.0.0 |
| Schema Version | 1.0 |
| Index Last Updated | 2026-07-09 |

---

## Asset Summary

| Type | Registered | Path |
|------|-----------|------|
| Agents | 2 | Registry/Agents/ |
| Capabilities | 0 | Registry/Capabilities/ |
| Workflows | 0 | Registry/Workflows/ |
| Tools | 0 | Registry/Tools/ |
| Templates | 0 | Registry/Templates/ |

> When assets are registered, they appear in the sections below.
> Each entry contains: ID, name, version, tags, description, path.

---

## Agents

| ID | Name | Version | Tags | Description | Path |
|----|------|---------|------|-------------|------|
| news-fetcher-agent | News Fetcher Agent | 1.0.0 | news, research, stock-market, korean-market | 영어권 뉴스에서 한국 주식 시장 영향 핫 토픽 10개 수집 | Agents/news-fetcher-agent/ |
| translation-agent | Translation Agent | 1.0.0 | translation, korean, report-style, finance | 영문을 보고서용 한국어로 번역 (구어체·존댓말 없음) | Agents/translation-agent/ |

---

## Capabilities

<!-- Registered capabilities will be listed here.
Format:
| ID | Name | Version | Tags | Description | Path |
-->

*No capabilities registered yet.*

---

## Workflows

<!-- Registered workflows will be listed here.
Format:
| ID | Name | Version | Pattern | Tags | Description | Path |
-->

*No workflows registered yet.*

---

## Tools

<!-- Registered tools will be listed here.
Format:
| ID | Name | Version | Tags | Description | Path |
-->

*No tools registered yet.*

---

## Templates

<!-- Registered templates will be listed here.
Format:
| ID | Name | Version | Tags | Description | Path |
-->

*No templates registered yet.*

---

## Registration Protocol

When creating a new shared asset:

1. Create the implementation file in the appropriate top-level directory.
2. Add an entry to the relevant section above.
3. Create a registration file in the appropriate `Registry/<type>/` sub-directory.
4. Update the Asset Summary count.

**Format for registration entries:**

```
| <id> | <name> | <version> | <tags> | <one-line description> | <path-to-implementation> |
```

---

## How to Search

See `Registry/Search_Guide.md` for search strategies by keyword, tag, and type.
