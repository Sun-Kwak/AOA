# Trend Research Agent

## Purpose

Collects and analyzes trending content data from social media platforms.

Provides actionable content recommendations based on real-time platform trends.

---

## Scope

**Platforms supported:**
- YouTube Shorts
- Instagram Reels

**Data collected:**
- Video metadata (title, caption, hashtags)
- Engagement metrics (views, likes, comments)
- Trending patterns and keywords
- Popular content angles

---

## Inputs (from Project)

This agent receives parameters from the calling project:

```yaml
platforms: array[string]     # ["youtube", "instagram"]
category: string             # "health", "kids", "tech"
keywords: array[string]      # ["혈당관리", "당뇨"]
output_path: string          # "Projects/{project}/Memory/trends/"
max_results_per_platform: integer  # 100 (optional, default: 100)
date_range_days: integer     # 7 (optional, default: 7)
```

**Example call from project:**

```yaml
dependencies:
  - agent: trend-research-agent
    params:
      platforms: [youtube, instagram]
      category: health
      keywords: [혈당관리, 당뇨, 고혈압]
      output_path: Memory/trends/
```

---

## Outputs (to Project)

All outputs are saved to the project's `Memory/trends/` directory:

### 1. Raw Data Files

**`youtube-YYYYMMDD.json`**
```json
[
  {
    "title": "string",
    "url": "string",
    "thumbnail": "string",
    "views": number,
    "likes": number,
    "comments": number,
    "publishedAt": "ISO date",
    "channel": "string",
    "hashtags": ["string"]
  }
]
```

**`instagram-YYYYMMDD.json`**
```json
[
  {
    "caption": "string",
    "url": "string",
    "displayUrl": "string",
    "views": number,
    "likes": number,
    "comments": number,
    "publishedAt": "ISO date",
    "creator": "string",
    "hashtags": ["string"]
  }
]
```

### 2. Trend Report

**`trend-report-YYYYMMDD.md`**

Format follows `Schemas/Trend_Report.md` specification.

Includes:
- Top topics with scores
- Trending keywords
- Content recommendations (5-10 ideas)
- Platform insights
- **Visual references** (비주얼 트렌드)

### 3. Visual Reference Images

**`visuals/ref_YYYYMMDD_XXX.jpg`**

인기 콘텐츠의 썸네일/커버 이미지:
- YouTube Shorts 썸네일
- Instagram Reels 커버 이미지
- 파일명 형식: `ref_20260710_001.jpg`
- 플랫폼당 최대 5개, 총 최대 10개

**사용 목적:**
- 이미지 생성 시 스타일 참고 (img2img reference)
- 트렌드 비주얼 스타일 파악
- 레이아웃/색감/디자인 패턴 분석

---

## Execution Flow

```
1. Receive parameters from project
   ↓
2. Validate inputs
   ↓
3. For each platform:
   a. Search Apify Actor
   b. Call Actor via MCP
   c. Wait for completion
   d. Save raw data to {output_path}/{platform}-{date}.json
   ↓
4. Collect visual references:
   a. Select top 3-5 from each platform
   b. Download thumbnails/cover images
   c. Save to {output_path}/visuals/
   d. Record metadata
   ↓
5. Analyze collected data:
   a. Extract trending topics
   b. Calculate topic scores
   c. Identify patterns
   d. Generate content recommendations
   ↓
6. Generate trend report
   ↓
7. Save report to {output_path}/trend-report-{date}.md
   ↓
8. Return summary to project
```

---

## Tools Used

### Apify MCP Server

**YouTube data collection:**
- Actor: `streamers/youtube-shorts-scraper`
- Method: Natural language request to MCP
- Example: "Use Apify to collect 100 YouTube Shorts about {keywords}"

**Instagram data collection:**
- Actor: `apify/instagram-reel-scraper`
- Method: Natural language request to MCP
- Example: "Use Apify to collect 100 Instagram Reels with hashtags {keywords}"

**See:** `Tools/apify/README.md` for detailed usage

---

## Configuration

### config.yaml

```yaml
name: trend-research-agent
version: 1.0.0
type: shared

capabilities:
  - data-collection
  - trend-analysis
  - content-recommendation

tools:
  - apify  # Via MCP

schemas:
  output: Schemas/Trend_Report.md

defaults:
  max_results_per_platform: 100
  date_range_days: 7
  min_engagement_threshold: 1000  # Minimum views to consider
```

---

## Best Practices

### 1. Keyword Selection

**프로젝트가 제공해야 할 것:**
- ✅ 구체적인 키워드 (예: "혈당관리", "당뇨")
- ❌ 너무 broad (예: "건강")
- ✅ 3-5개 키워드
- ✅ 한국어 키워드 사용 (타겟 시장에 맞게)

### 2. Result Limits

- Start with 50-100 items per platform
- Increase only if insufficient data
- Consider API costs

### 3. Date Range

- Default: 7 days (recent trends)
- Shorter range (3 days): real-time trends
- Longer range (14 days): stable patterns

### 4. Error Handling

Agent should handle:
- Actor not responding → Retry with different Actor
- Insufficient data → Reduce filters or expand keywords
- API rate limits → Wait and retry

---

## Usage Example

### From Project Workflow

```yaml
# Projects/health-shorts/Workflows/daily-content.yaml

steps:
  - step: collect-trends
    agent: trend-research-agent
    params:
      platforms: [youtube, instagram]
      category: health
      keywords: [혈당관리, 당뇨, 고혈압]
      output_path: Memory/trends/
      max_results_per_platform: 100
    outputs:
      - Memory/trends/youtube-{date}.json
      - Memory/trends/instagram-{date}.json
      - Memory/trends/trend-report-{date}.md
```

### Agent Session Creation

Project Agent creates this agent session:

```
create_session(
  agent: "trend-research-agent",
  params: {
    platforms: ["youtube", "instagram"],
    category: "health",
    keywords: ["혈당관리", "당뇨"],
    output_path: "Projects/health-shorts/Memory/trends/"
  }
)
```

---

## Performance

**Estimated execution time:**
- YouTube collection: 2-3 minutes (100 items)
- Instagram collection: 2-3 minutes (100 items)
- Analysis & report generation: 1-2 minutes
- **Total: 5-8 minutes**

**Cost estimate:**
- YouTube: $0.40 (100 shorts)
- Instagram: $0.26 (100 reels)
- **Total per run: ~$0.66**

---

## Limitations

1. **Language:** Optimized for Korean content
2. **Platforms:** YouTube Shorts + Instagram Reels only (V1)
3. **Real-time:** 2-3 hour delay due to platform indexing
4. **Engagement metrics:** May have slight variations

---

## Future Enhancements

- [ ] Add TikTok support
- [ ] Add Naver trend integration
- [ ] Real-time monitoring mode
- [ ] Sentiment analysis
- [ ] Competitor tracking
- [ ] Multi-language support

---

## Dependencies

- **Tools:** `apify` (via MCP)
- **Schemas:** `Schemas/Trend_Report.md`
- **Registry:** Registered in `Registry/INDEX.md`

---

## See Also

- **Tools/apify/README.md** - Apify integration guide
- **Schemas/Trend_Report.md** - Output format specification
- **Registry/Agents/** - Agent registry entry
