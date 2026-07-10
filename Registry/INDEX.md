# AOA Registry Index

> **Cold Start Instruction**: Read this file first.
> Do NOT read individual registry directories until a specific asset is needed.
> This index provides enough information to determine whether an asset exists.
> Load full asset details on demand only.

---

## Framework Version

| Key | Value |
|-----|-------|
| AOA Version | 1.0.0 |
| Schema Version | 1.0 |
| Index Last Updated | 2026-07-09 |

---

## Asset Summary

| Type | Registered | Path |
|------|-----------|------|
| Agents | 3 | Registry/Agents/ |
| Capabilities | 0 | Registry/Capabilities/ |
| Workflows | 0 | Registry/Workflows/ |
| Tools | 1 | Registry/Tools/ |
| Templates | 0 | Registry/Templates/ |

> When assets are registered, they appear in the sections below.
> Each entry contains: ID, name, version, tags, description, path.

---

## Agents

| ID | Name | Version | Tags | Description | Path |
|----|------|---------|------|-------------|------|
| trend-research-agent | Trend Research Agent | 1.0.0 | trends, social-media, content-research, youtube, instagram, visual-references | YouTube Shorts + Instagram Reels 트렌드 수집 + Visual Reference 다운로드 | Agents/trend-research-agent/ |
| image-generator | Image Generator | 1.1.0 | image-generation, fal-ai, text2img, img2img, image-edit, card-news, nanovana2 | 범용 이미지 생성 Agent (text2img, img2img, image_edit). Reference 기반 트렌드 스타일 복제 + 정밀 편집 지원. | Agents/image-generator/ |
| browser-controller | Browser Controller | 1.0.0 | browser-automation, web-automation, canvas, sns-deployment, instagram, youtube, tiktok | Canvas Browser 통제. 자연어 명령을 Canvas action으로 변환. Instagram/YouTube/TikTok 배포 플로우 실행. | Agents/browser-controller/ |

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

| ID | Name | Version | Tags | Description | Path |
|----|------|---------|------|-------------|------|
| apify | Apify Integration | 1.0.0 | data-collection, web-scraping, mcp, youtube, instagram | Apify MCP Server를 통한 소셜 미디어 데이터 수집 | Tools/apify/ |

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
