# Health Fitness Cards - Main Workflow

**프로젝트 ID:** health-fitness-cards  
**타겟 플랫폼:** Instagram Reels (9:16 세로형)  
**콘텐츠 타입:** 정보성 카드뉴스 (일러스트, 다이어그램, 텍스트 중심)

---

## Workflow Overview

```
Phase 1: 트렌드 수집 (Instagram only)
   ↓
Phase 2: 이미지 생성 (3개 병렬, img2img)
   ↓
Phase 3: 결과 검증 및 저장
```

---

## Phase 0: 계정 검증 (Setup, 수동)

**수행자:** User (수동)

**목적:** 일러스트 건강 정보 제공 계정 리스트 작성

**방법:**
1. Instagram에서 수동으로 일러스트 스타일 건강 계정 발견
2. 예시 계정:
   - @health__happyvirus
   - @doctor_friends
   - @body_signal

3. `Memory/verified_accounts.json` 파일 생성:
```json
{
  "accounts": [
    {
      "username": "@health__happyvirus",
      "url": "https://www.instagram.com/health__happyvirus/",
      "verified_date": "2026-07-10",
      "content_style": "illustrated health cards"
    }
  ]
}
```

---

## Phase 1: 계정 콘텐츠 수집 (Regular)

**Agent:** account-content-collector (프로젝트 전용)

**목적:** 검증된 계정들의 최신 포스트 직접 수집

**Parameters:**

```yaml
target_accounts: ["@health__happyvirus", "@doctor_friends"]  # 또는 verified_accounts.json 사용
posts_per_account: 10
date_range_days: 7
output_path: "/Users/sun/project/AOA/Projects/health-fitness-cards/Memory/trends/"
```

**실행 방법:**
```javascript
create_session({
  project_id: "52d540bd-4461-4c27-81ed-c460533357ac",
  name: "[AOA] health-fitness-cards — content collection",
  coordinate_with_creator: false,
  kickoff: {
    mode: "autopilot",
    prompt: `당신은 account-content-collector 에이전트입니다.

/Users/sun/project/AOA/Projects/health-fitness-cards/Agents/account-content-collector/prompt.md 규칙을 따라 작업하세요.

입력:
- target_accounts: ["@health__happyvirus"]
- posts_per_account: 10
- output_path: "/Users/sun/project/AOA/Projects/health-fitness-cards/Memory/trends/"

작업 완료 후:
- Memory/trends/visuals/에 이미지 저장
- Memory/trends/references.json 생성
- Memory/trends/account-collection-YYYYMMDD.md 리포트 작성`
  }
})
```

**추가 Instruction (프롬프트에 포함):**

```markdown
**중요: Visual References 필터링 규칙**

1. **의학/건강 정보 일러스트 카드만 수집:**
   - ✅ 일러스트 기반 (만화 스타일, 캐릭터, 장기 다이어그램)
   - ✅ 의학/건강 지식 전달 (신체 신호, 증상, 생활습관, 식단, 운동 효과)
   - ✅ 구조화된 정보 레이아웃 (번호 리스트, 그리드, 타임라인)
   - ✅ 교육적 콘텐츠 (의사 조언, 건강상식, 증상 체크)
   
   **제외 항목 (엄격):**
   - ❌ 실사 운동 영상 썸네일 (사람이 운동하는 사진/영상)
   - ❌ 상품 광고 (운동기구, 건강식품, 앱 광고)
   - ❌ 교육 현장/세미나 사진 (강의실, 단체 사진)
   - ❌ 뉴스 기사 이미지 (골프, 대회, 시설 개장)
   - ❌ 인물 사진 중심 콘텐츠
   - ❌ 동기부여 문구만 있는 이미지

2. **콘텐츠 키워드 우선순위:**
   - 1순위: "몸의 신호", "증상", "냄새", "통증", "장기", "혈관", "호르몬"
   - 2순위: "체크리스트", "OO가지", "의사가 알려주는", "건강상식"
   - 3순위: "아침 루틴", "식습관", "생활습관", "예방법"
   - 제외: "운동 루틴", "홈트", "PT", "다이어트 챌린지"

2. **Style Notes 작성 예시:**
   - ✅ "Illustrated body diagram with 8 labeled symptoms"
   - ✅ "Comic-style health card showing organ characters with warnings"
   - ✅ "Grid layout (3x4) morning routine infographic with illustrations"
   - ✅ "Timeline format pregnancy age chart with illustration"
   - ❌ "Photo of workout session" → 제외
   - ❌ "Product advertisement with model" → 제외

3. **중복 제거:**
   - thumbnail_url이 동일한 이미지는 1개만 수집
   - 동일 계정의 유사한 디자인은 최대 2개까지만

4. **수집 우선순위:**
   - Engagement 높은 순 (likes + comments)
   - 정보 밀도 높은 콘텐츠 우선 (텍스트가 많고 구조화된 레이아웃)
   - 최근 7일 이내 콘텐츠 우선
```

**Expected Output:**
- `Memory/trends/instagram-YYYYMMDD.json`
- `Memory/trends/trend-report-YYYYMMDD.md`
- `Memory/trends/visuals/ref_YYYYMMDD_001.jpg` ~ `005.jpg` (5-7개, 정보성 카드뉴스만)
- `Memory/trends/visuals/references.json`

---

## Phase 2: 이미지 편집 (자유 디자인)

**Agent:** image-generator (공용, 3개 병렬 세션)

**모드:** `image_edit` ✨ (v1.1.0)

### 🎯 image_edit 프롬프트 전략

**맥락만 유지, 내용/디자인은 자유롭게**:
```yaml
edit_prompt: "Keep the [주제] theme but feel free to create new [내용].
              Fresh modern design with [색상/스타일].
              [캐릭터/일러스트] with different style.
              New layout and color scheme.
              Clear Korean text.
              9:16 vertical format."
```

**중요**: 
- ✅ "Keep the [주제] theme" = 맥락만 유지
- ✅ "feel free to create new [내용]" = 내용 자유롭게 변경
- ✅ "Fresh modern design" = 디자인 완전히 새롭게
- ❌ "KEEP exact same", "preserve", "동일하게 유지" 금지

### 🚨 워터마크 처리 규칙 (필수!)

**프롬프트 규칙**:
- ❌ "remove watermark", "워터마크 제거" → 콘텐츠 정책 위반
- ❌ "without watermark" → 새로운 워터마크 생성
- ✅ 프롬프트에 워터마크 언급 없음

**후처리 크롭 (필수 적용)**:
```python
# 이미지 생성 후 자동 크롭
from PIL import Image
img = Image.open(downloaded_path)
width, height = img.size
crop_height = height - 100  # 하단 100px 제거
cropped_img = img.crop((0, 0, width, crop_height))
cropped_img.save(output_path, quality=95)
```

### 공통 Parameters

```yaml
mode: image_edit
aspect_ratio: "9:16"
strength: 0.25
preserve_structure: true  # 기술적 파라미터
model: "nano-banana-2/edit"  # ~₩26-52/장, 15-17초
apply_watermark_crop: true  # 후처리 크롭 적용
crop_pixels: 100  # 하단 크롭 영역
```

### 카드 생성 예시

**Card 1: 주제별 비교/대조**
```yaml
주제: "아침 공복 운동 vs 식후 운동"
reference_image: ref_YYYYMMDD_001.jpg
edit_prompt: "Keep the health tips theme but create new content about '아침 공복 운동 vs 식후 운동'.
              Fresh modern design with bright pastel colors.
              Cute kawaii-style illustrations with different characters.
              New layout and color scheme.
              Clear Korean text.
              9:16 vertical format."
mask: "auto"
edit_areas: ["text", "colors", "layout", "style"]
```

**Card 2: 오해/팁 리스트**
```yaml
주제: "여성 근력운동 3가지 오해"
reference_image: ref_YYYYMMDD_002.jpg
edit_prompt: "Keep the health information theme but create new content about '여성 근력운동 3가지 오해'.
              Fresh empowering design with vibrant feminine colors.
              Modern illustrations with different style.
              New numbered list layout.
              Clear Korean text.
              9:16 vertical format."
mask: "auto"
edit_areas: ["text", "colors", "layout", "style"]
```

**Card 3: 실천 가이드**
```yaml
주제: "10분 홈트로 복근 만들기"
reference_image: ref_YYYYMMDD_003.jpg
edit_prompt: "Keep the workout guide theme but create new content about '10분 홈트로 복근 만들기'.
              Fresh energetic design with bright motivating colors.
              New step-by-step layout with different icons.
              Clear Korean text.
              9:16 vertical format."
mask: "auto"
edit_areas: ["text", "colors", "layout", "style"]
```

### Expected Output

- `Outputs/card_001.jpg` (325-800KB, 1080x1920px) - 자유로운 새 디자인, 워터마크 크롭 적용
- `Outputs/card_002.jpg` - 자유로운 새 디자인, 워터마크 크롭 적용
- `Outputs/card_003.jpg` - 자유로운 새 디자인, 워터마크 크롭 적용
- `Outputs/metadata.json`

### 생성 원칙

- ✅ 이미지 비율 (9:16) 유지
- ✅ 정보성 카드 주제/맥락만 유지
- ✅ 일러스트, 캐릭터, 레이아웃, 색상 모두 자유롭게 변경
- ✅ 워터마크 후처리 크롭 필수 적용
- ⚠️ 프롬프트에 "KEEP exact", "preserve", "동일 유지" 금지
- ⚠️ 프롬프트에 워터마크 관련 단어 금지

---

## Phase 3: 결과 검증

**Validation Checklist:**

- [ ] 3개 이미지 모두 생성 완료
- [ ] 파일 크기 적정 (300KB - 1MB)
- [ ] 해상도 확인 (1080x1920px 이상)
- [ ] JPEG 형식 확인
- [ ] Metadata 저장 완료

**Final Update:**
- `Memory/execution_state.md` 업데이트
- 생성된 이미지 경로 기록

---

## 프로젝트별 규칙 요약

| 항목 | 설정 |
|------|------|
| 플랫폼 | Instagram only (YouTube 제외) |
| 콘텐츠 타입 | 정보성 카드뉴스 (일러스트/다이어그램) |
| 수집 방법 | 계정 기반 (account-content-collector) |
| Visual Reference | 실사 제외, 중복 제거 |
| 이미지 포맷 | 9:16 세로형 |
| 생성 모드 | **image_edit** (자유 디자인) |
| strength | 0.25 |
| preserve_structure | true (기술 파라미터) |
| 병렬 처리 | 3개 동시 생성 |

**생성 원칙:**
- ✅ 이미지 비율 (9:16)만 유지
- ✅ 정보성 카드 컨셉 유지
- ✅ 일러스트, 캐릭터, 레이아웃, 색상 모두 자유롭게 변경
- ⚠️ 프롬프트에 보존 지시 금지

---

## Notes

- 공용 에이전트는 수정하지 않음
- 프로젝트 전용 에이전트: `account-content-collector`
- image-generator v1.1.0 `image_edit` 모드 활용
- 프로젝트별 파라미터로 동작 제어
- 추가 Instruction은 kickoff prompt에 명시적으로 전달
