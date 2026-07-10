# Trend Report Schema

## Purpose

Defines the output format for trend research results.

Trend reports provide actionable content recommendations based on platform data analysis.

---

## Scope

This schema applies to all trend research outputs across AOA.

Used by: `trend-research-agent` and other trend analysis agents.

---

## Schema Definition

```yaml
trend_report:
  generated_at: string (ISO 8601 timestamp)
  category: string
  platforms: array[string]
  date_range:
    start: string (ISO date)
    end: string (ISO date)
  
  top_topics: array
    - topic: string
      score: integer (0-100)
      signals: array[string]
      content_angles: array[string]
      example_content:
        platform: string
        url: string
        title: string
        engagement:
          views: integer
          likes: integer
          comments: integer
      
  trending_keywords: array
    - keyword: string
      frequency: integer
      platforms: array[string]
      
  content_recommendations: array
    - title: string
      angle: string
      hook: string
      target_platforms: array[string]
      estimated_engagement: string (high/medium/low)
      
  platform_insights:
    youtube:
      total_analyzed: integer
      avg_views: integer
      top_hook_patterns: array[string]
      optimal_duration: string
    instagram:
      total_analyzed: integer
      avg_views: integer
      top_hashtags: array[string]
      optimal_format: string
  
  visual_references: array  # ⭐ 비주얼 트렌드 추가
    - platform: string (youtube | instagram)
      source_url: string
      image_path: string (프로젝트 Memory 경로)
      thumbnail_url: string (원본 URL)
      engagement:
        views: integer
        likes: integer
      style_notes: string
      collected_at: string (ISO 8601 timestamp)
```

---

## Example

```yaml
trend_report:
  generated_at: "2026-07-10T14:00:00+09:00"
  category: "health"
  platforms: ["youtube", "instagram"]
  date_range:
    start: "2026-07-03"
    end: "2026-07-10"
  
  top_topics:
    - topic: "혈당 관리"
      score: 92
      signals:
        - "최근 7일 YouTube Shorts 조회수 150% 증가"
        - "Instagram Reels #혈당관리 태그 10K+ 게시물"
        - "아침 습관 관련 콘텐츠 높은 참여도"
      content_angles:
        - "의사가 피하는 아침 습관 3가지"
        - "혈당 낮추는 5분 루틴"
        - "당뇨 예방 아침 식단"
      example_content:
        platform: "youtube"
        url: "https://youtube.com/shorts/xxxxx"
        title: "의사가 알려주는 혈당관리 3가지"
        engagement:
          views: 250000
          likes: 15000
          comments: 892
    
    - topic: "당뇨 예방"
      score: 85
      signals:
        - "Instagram Reels #당뇨예방 주간 300% 증가"
        - "식단 관련 콘텐츠 높은 저장률"
      content_angles:
        - "당뇨 위험 신호 5가지"
        - "혈당 스파이크 막는 음식 조합"
      example_content:
        platform: "instagram"
        url: "https://instagram.com/reel/xxxxx"
        title: "당뇨 전 단계 증상 알아보기"
        engagement:
          views: 180000
          likes: 12000
          comments: 650
  
  trending_keywords:
    - keyword: "혈당관리"
      frequency: 1250
      platforms: ["youtube", "instagram"]
    - keyword: "당뇨예방"
      frequency: 980
      platforms: ["youtube", "instagram"]
    - keyword: "아침습관"
      frequency: 750
      platforms: ["youtube"]
  
  content_recommendations:
    - title: "의사가 피하는 혈당 올리는 아침 습관 3가지"
      angle: "전문가 관점 + 부정형 (피해야 할 것)"
      hook: "이 습관 때문에 혈당이..."
      target_platforms: ["youtube", "instagram"]
      estimated_engagement: "high"
    
    - title: "혈당 낮추는 5분 아침 루틴"
      angle: "실용적 솔루션 + 짧은 시간"
      hook: "하루 5분으로 혈당 관리"
      target_platforms: ["youtube", "instagram"]
      estimated_engagement: "high"
    
    - title: "당뇨 전 단계 자가 체크 5가지"
      angle: "자가 진단 + 리스트 형식"
      hook: "이 증상 있다면 당뇨 전 단계"
      target_platforms: ["instagram"]
      estimated_engagement: "medium"
  
  platform_insights:
    youtube:
      total_analyzed: 150
      avg_views: 85000
      top_hook_patterns:
        - "의사가 알려주는..."
        - "이것만 알면..."
        - "○○ 때문에..."
      optimal_duration: "30-45초"
    instagram:
      total_analyzed: 120
      avg_views: 65000
      top_hashtags:
        - "#혈당관리"
        - "#당뇨예방"
        - "#건강습관"
      optimal_format: "텍스트 오버레이 + 배경음악"
  
  visual_references:
    - platform: "instagram"
      source_url: "https://instagram.com/reel/CxYz123"
      image_path: "Memory/trends/visuals/ref_20260710_001.jpg"
      thumbnail_url: "https://scontent.cdninstagram.com/..."
      engagement:
        views: 458000
        likes: 4722
      style_notes: "3x4 grid layout, 바다 배경, 일러스트, 번호 매기기"
      collected_at: "2026-07-10T14:05:00+09:00"
    
    - platform: "youtube"
      source_url: "https://youtube.com/shorts/abc123"
      image_path: "Memory/trends/visuals/ref_20260710_002.jpg"
      thumbnail_url: "https://i.ytimg.com/vi/abc123/maxresdefault.jpg"
      engagement:
        views: 125000
        likes: 921
      style_notes: "단색 배경, 큰 텍스트, 이모지 강조"
      collected_at: "2026-07-10T14:06:00+09:00"
    
    - platform: "instagram"
      source_url: "https://instagram.com/reel/Def456"
      image_path: "Memory/trends/visuals/ref_20260710_003.jpg"
      thumbnail_url: "https://scontent.cdninstagram.com/..."
      engagement:
        views: 320000
        likes: 1847
      style_notes: "만화 패널 형식, 캐릭터 중심, 말풍선"
      collected_at: "2026-07-10T14:07:00+09:00"
```

---

## Output Format

**File format:** Markdown (`.md`)

**File naming:** `trend-report-YYYYMMDD.md`

**Location:** `Projects/{project}/Memory/trends/`

---

## Usage by Agents

**trend-research-agent generates:**

```markdown
# Trend Report: {category}
Generated: {timestamp}

## Executive Summary
{Top 3 topics with scores}

## Top Topics
### 1. {topic}
**Score:** {score}/100
**Signals:**
- {signal 1}
- {signal 2}

**Content Angles:**
- {angle 1}
- {angle 2}

...

## Content Recommendations
1. **{title}**
   - Angle: {angle}
   - Hook: {hook}
   - Platforms: {platforms}
   - Est. Engagement: {level}

...

## Platform Insights
### YouTube
- Analyzed: {count} shorts
- Avg. Views: {views}
- Top Hooks: {list}

### Instagram
- Analyzed: {count} reels
- Avg. Views: {views}
- Top Hashtags: {list}
```

---

## Validation Rules

1. **Score Range:** 0-100 (higher = more trending)
2. **Signals:** Minimum 2 per topic
3. **Content Angles:** Minimum 2 per topic
4. **Recommendations:** Minimum 5, maximum 10
5. **Date Range:** Maximum 7 days

---

## TODO

- Add sentiment analysis fields
- Add competitor analysis section
- Add seasonal trend indicators
