# Health Fitness Cards

## 프로젝트 개요

건강 및 여성 운동 트렌드를 수집하여 Instagram Reels/YouTube Shorts용 카드 뉴스 이미지를 자동 생성하는 테스트 프로젝트.

AOA 프레임워크의 **트렌드 → 이미지 생성 → 결과 저장** 워크플로우를 검증합니다.

---

## 목적

1. AOA 공용 에이전트 체인 검증
2. trend-research-agent + image-generator 통합 테스트
3. 프로젝트 세션 → 에이전트 세션 패턴 검증

---

## 워크플로우

### Phase 1: 트렌드 수집
- **Agent**: trend-research-agent
- **키워드**: "건강 운동", "여성 운동", "홈트"
- **출력**: Visual references (이미지 URL + 메타데이터)
- **저장**: Memory/trends/

### Phase 2: 이미지 생성
- **Agent**: image-generator (3회 병렬 실행)
- **모드**: img2img (트렌드 이미지 기반)
- **주제**: 
  1. 아침 공복 운동 vs 식후 운동
  2. 여성 근력운동 3가지 오해
  3. 10분 홈트로 복근 만들기
- **출력**: 9:16 세로형 카드 뉴스 이미지

### Phase 3: 결과 저장
- **저장 위치**: Outputs/
- **파일명**: card_001.jpg, card_002.jpg, card_003.jpg
- **메타데이터**: JSON 파일 포함

---

## 사용 에이전트

| Agent ID | Role | 버전 |
|----------|------|------|
| trend-research-agent | 트렌드 수집 + Visual Reference | 1.0.0 |
| image-generator | img2img 이미지 생성 | 1.0.0 |

---

## 출력물

- `Outputs/card_001.jpg` - 아침 공복 운동 카드
- `Outputs/card_002.jpg` - 여성 근력운동 카드
- `Outputs/card_003.jpg` - 10분 홈트 카드
- `Memory/trends/visual_refs_YYYYMMDD.json` - 수집된 트렌드 데이터

---

## 상태

- **Status**: Active (Test)
- **Created**: 2026-07-10
- **Last Run**: -

---

## 다음 단계

1. ✅ 프로젝트 구조 생성
2. ⏳ 프로젝트 세션 시작
3. ⏳ 워크플로우 실행
4. ⏳ 결과 검증
