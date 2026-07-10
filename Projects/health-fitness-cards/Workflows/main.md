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

## Phase 1: 트렌드 수집

**Agent:** trend-research-agent (공용)

**Parameters:**

```yaml
platforms: ["instagram"]  # YouTube 제외, Instagram만
category: "health"
keywords: ["건강 운동", "여성 운동", "홈트"]
output_path: "/Users/sun/project/AOA/Projects/health-fitness-cards/Memory/trends/"
max_results_per_platform: 50
date_range_days: 7
```

**추가 Instruction (프롬프트에 포함):**

```markdown
**중요: Visual References 필터링 규칙**

1. **정보성 카드뉴스만 수집:**
   - ✅ 일러스트 스타일 (캐릭터, 다이어그램, 인포그래픽)
   - ✅ 텍스트 중심 레이아웃 (리스트, 번호, 체크리스트)
   - ✅ 교육/정보 전달 목적의 디자인
   - ❌ 실사 운동 영상 썸네일 제외
   - ❌ 인물 사진 위주 콘텐츠 제외
   - ❌ 단순 동기부여 문구만 있는 이미지 제외

2. **Style Notes 작성 시 구체적으로:**
   - "Illustration style card with numbered list (1-8)"
   - "Diagram with labeled body parts and text explanations"
   - "Grid layout (3x4) with icons and Korean text"
   - "Infographic with timeline/steps format"

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

## Phase 2: 이미지 생성

**Agent:** image-generator (공용, 3개 병렬 세션)

**공통 Parameters:**

```yaml
mode: img2img
aspect_ratio: "9:16"
strength: 0.65
model: "flux-pro/v1.1-ultra"
```

**Card 1: 주제별 비교/대조**
```yaml
주제 예시: "아침 공복 운동 vs 식후 운동"
reference_image: ref_YYYYMMDD_001.jpg (비교 레이아웃 스타일)
style_modifiers:
  - "comparison layout with two sections"
  - "warm morning colors"
  - "clear Korean typography"
```

**Card 2: 오해/팁 리스트**
```yaml
주제 예시: "여성 근력운동 3가지 오해"
reference_image: ref_YYYYMMDD_002.jpg (번호 리스트 스타일)
style_modifiers:
  - "numbered list format (1, 2, 3)"
  - "empowering feminine colors"
  - "bold Korean typography"
```

**Card 3: 실천 가이드**
```yaml
주제 예시: "10분 홈트로 복근 만들기"
reference_image: ref_YYYYMMDD_003.jpg (타임라인/스텝 스타일)
style_modifiers:
  - "step-by-step layout with timer"
  - "energetic bright colors"
  - "bold impactful typography"
```

**Expected Output:**
- `Outputs/card_001.jpg` (325-800KB, 1080x1920px)
- `Outputs/card_002.jpg`
- `Outputs/card_003.jpg`
- `Outputs/metadata.json`

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
| Visual Reference | 실사 제외, 중복 제거 |
| 이미지 포맷 | 9:16 세로형 |
| 생성 모드 | img2img (트렌드 스타일 참조) |
| 병렬 처리 | 3개 동시 생성 |

---

## Notes

- 공용 에이전트(trend-research-agent, image-generator)는 수정하지 않음
- 프로젝트별 파라미터로 동작 제어
- 추가 Instruction은 kickoff prompt에 명시적으로 전달
