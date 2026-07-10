# Trend Research Agent

## Metadata

| Field | Value |
|-------|-------|
| ID | trend-research-agent |
| Name | Trend Research Agent |
| Version | 1.0.0 |
| Status | Active |
| Created | 2026-07-10 |
| Last Updated | 2026-07-10 |

---

## Tags

`trends`, `social-media`, `content-research`, `youtube`, `instagram`, `visual-references`, `apify`, `mcp`

---

## Description

YouTube Shorts + Instagram Reels에서 트렌드 콘텐츠를 수집하고 분석하는 Agent.

**핵심 기능:**
- 플랫폼별 인기 콘텐츠 수집 (조회수, 좋아요, 댓글 기준)
- 트렌드 패턴 분석 및 키워드 추출
- **Visual Reference 다운로드** (썸네일/커버 이미지)
- 콘텐츠 추천 생성 (주제, 각도, 형식)

**출력:**
- `trend_report_YYYYMMDD.md` (트렌드 리포트)
- `Memory/trends/raw_YYYYMMDD.json` (원본 데이터)
- `Memory/trends/visuals/ref_*.jpg` (Visual References)

---

## Dependencies

### Tools
- **apify** (Apify MCP Server)
  - `streamers/youtube-shorts-scraper`
  - `apify/instagram-reel-scraper`

### Environment
- `APIFY_API_TOKEN` (required)

---

## Usage

```yaml
# 프로젝트에서 호출
trend_research_agent.run(
  platform: "youtube"  # or "instagram"
  search_keyword: "건강 관리"
  max_results: 20
  output_dir: "Memory/trends/"
)
```

---

## Path

`Agents/trend-research-agent/`

---

## Related Assets

- **Tools:** `apify`
- **Schemas:** `Schemas/Trend_Report.md`
- **Used by:** image-generator (visual references 소비)

---

## Notes

- Visual references는 img2img 이미지 생성에 필수
- Apify MCP 연결 필수 (HTTP transport)
- Rate limit 고려 필요 (Apify 플랜별 상이)
