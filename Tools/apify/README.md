# Apify Tool Integration

## Purpose

Apify Tool provides data collection capabilities through Apify platform via MCP Server integration.

Agents use Apify MCP to scrape data from various platforms (YouTube, Instagram, TikTok, etc.) without requiring custom scripts.

---

## Integration Method

**MCP Server (Model Context Protocol)**

AOA integrates with Apify through GitHub Copilot's MCP Server connection.

**Benefits:**
- No custom scripts required
- Natural language control
- Dynamic parameter adjustment
- Automatic error handling

---

## Setup

### 1. MCP Server Configuration

**GitHub Copilot Desktop App:**
1. Open Settings → **MCP servers**
2. Click **"+ Add server"**
3. Select **"apify"** from list
4. Configure:
   - **Server name:** `apify`
   - **Type:** `HTTP`
   - **URL:** `https://mcp.apify.com`
   - **Headers:**
     - Key: `Authorization`
     - Value: `Bearer YOUR_APIFY_API_TOKEN`
   - **Timeout:** `180` seconds

### 2. API Token

**Get your token:**
1. Visit https://console.apify.com/account/integrations
2. Copy your **API Token**
3. Format: `apify_api_xxxxxxxxxxxxx`

**Usage in MCP:**
```
Authorization: Bearer apify_api_xxxxxxxxxxxxx
```

⚠️ **Important:** Must include `Bearer ` prefix!

---

## Available Actors

### YouTube

**streamers/youtube-shorts-scraper**
- **Purpose:** Extract YouTube Shorts data
- **Input:** Channel URLs, keywords
- **Output:** Video URL, caption, likes, views, comments, timestamp
- **Stats:** 52K users, 98.9% success rate

### Instagram

**apify/instagram-reel-scraper**
- **Purpose:** Scrape Instagram Reels
- **Input:** Username, hashtags
- **Output:** Caption, hashtags, likes, views, comments, timestamp
- **Stats:** 117K users, 99.6% success rate

---

## Usage by Agents

Agents use Apify through natural language requests to MCP:

**Example (in agent prompt):**

```markdown
Use Apify MCP to collect YouTube Shorts:
- Actor: streamers/youtube-shorts-scraper
- Search keywords: {keywords}
- Max results: 100
- Save to: {output_path}/youtube-{date}.json
```

**MCP handles:**
- Actor execution
- Wait for completion
- Data retrieval
- Error handling

---

## Data Output Format

### YouTube Shorts

```json
{
  "title": "string",
  "url": "string",
  "views": number,
  "likes": number,
  "comments": number,
  "publishedAt": "ISO date",
  "channel": "string",
  "hashtags": ["string"]
}
```

### Instagram Reels

```json
{
  "caption": "string",
  "url": "string",
  "views": number,
  "likes": number,
  "comments": number,
  "publishedAt": "ISO date",
  "creator": "string",
  "hashtags": ["string"]
}
```

---

## Cost Estimation

### YouTube (streamers/youtube-shorts-scraper)
- **Per short:** $0.004
- **100 shorts:** $0.40

### Instagram (apify/instagram-reel-scraper)
- **Per reel:** $0.0026
- **100 reels:** $0.26

**Daily run (both platforms):** ~$0.66

---

## Best Practices

### 1. Use Specific Keywords
```
❌ "health"
✅ "혈당관리", "당뇨", "고혈압"
```

### 2. Limit Results
- Start with 50-100 items per platform
- Increase only if needed

### 3. Cache Results
- Save raw data to `Memory/apify-raw/`
- Reuse data for analysis without re-scraping

### 4. Error Handling
- MCP automatically retries on failures
- Check dataset for partial results

---

## Troubleshooting

### MCP Connection Issues

**Symptom:** "Authenticating..." stuck

**Solution:**
1. Check Authorization header format: `Bearer apify_api_xxx`
2. Toggle MCP server OFF → ON
3. Restart GitHub Copilot app

### Invalid Token

**Symptom:** 401 Unauthorized

**Test token validity:**
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  https://api.apify.com/v2/users/me
```

### Actor Not Found

**Solution:** Search actors first:
```
Use apify-search-actors tool with keywords
```

---

## References

- **Apify Store:** https://apify.com/store
- **Apify API Docs:** https://docs.apify.com/api/v2
- **MCP Setup Guide:** [GitHub Copilot MCP Documentation]
- **AOA Registry:** `/Registry/INDEX.md`
