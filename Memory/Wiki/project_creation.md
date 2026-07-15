# Wiki: Project Creation

프로젝트 생성 시 반복된 실수와 회피 전략.

---

## [Pattern-PROC] Project Creation Procedure

**통합**: Pattern-001 (외부 경로) + Pattern-002 (dual session)  
**발생일**: 2026-07-10

### 문제

- 외부 경로에 프로젝트 생성
- create_project() 호출로 dual session 발생

### 회피 전략

#### 절대 규칙
- ✅ 모든 프로젝트는 `AOA/Projects/<id>/` 내부에만 생성
- ❌ `create_project()` 절대 호출 금지

#### 올바른 절차
```
1. AOA/Projects/<id>/ 에 파일 생성
2. git add + git commit
3. create_session()만 호출
4. coordinate_with_creator: false
```

---

## [Pattern-DOC] Document Quality & Schema Compliance

**통합**: Pattern-003 (디렉터리 누락) + Pattern-004 (manifest 불완전)  
**발생일**: 2026-07-10

### 문제

- 필수 디렉터리 누락
- manifest.yaml 필수 필드 누락

### 회피 전략

#### 필수 구조
```
Projects/<id>/
  ├── manifest.yaml
  ├── README.md
  ├── Agents/
  ├── Workflows/
  ├── Memory/
  │   ├── project.md
  │   ├── execution_state.md
  │   ├── decision_log.md
  │   └── wiki/
  └── Outputs/
```

#### manifest.yaml 필수 필드
- id, name, version, status, description
- paths, dependencies, memory, outputs

---

## [Pattern-005] 불필요한 프로젝트 자동 실행

**발생일**: 2026-07-10

### 문제

모든 프로젝트를 autopilot으로 즉시 실행

### 회피 전략

#### 판단 기준
- ✅ 자동 실행: 테스트, 검증 프로젝트
- ✅ 대기 상태: 실제 업무 프로젝트

---

## [Pattern-007] Registry INDEX 전체 로딩

**발생일**: 2026-07-15

### 문제

- Registry/INDEX.md 전체 읽기
- 사용하지 않을 에이전트 정보까지 로딩

### 회피 전략

#### 올바른 초기화
```
✅ 1. manifest.yaml 읽기
✅ 2. dependencies.agents만 확인
✅ 3. on-demand Registry 조회

❌ Registry/INDEX.md 전체 읽기 금지
```

---

## 범용 Pattern (공통 적용)

### Pattern-WIKI: Wiki Protocol Enforcement
→ `Memory/Wiki/universal_patterns.md` 참조

### Pattern-AUTH: Access Control & Authority Protocol
→ `Memory/Wiki/universal_patterns.md` 참조

---

## 작업 시작 전 체크리스트

- [ ] `Bootstrap/Create_Project.md` 읽음
- [ ] `Schemas/Project.md` 읽음
- [ ] `Memory/Wiki/universal_patterns.md` 읽음
- [ ] 현재 경로가 `/Users/sun/project/AOA`인지 확인
- [ ] 디렉터리 구조 전체 생성
- [ ] manifest.yaml 필수 필드 작성
- [ ] Memory/ 하위 파일 생성
- [ ] Memory/wiki/ 생성
- [ ] pre_execution_check.sh 생성
- [ ] git commit
- [ ] create_session()만 호출
- [ ] kickoff prompt에 Wiki + Access Control 포함

---

## 업데이트 이력

- 2026-07-10: 초기 작성
- 2026-07-15: **v2.0 통합** - 8개 → 4개 + 2개 범용 분리
  - Pattern-001 + 002 → Pattern-PROC
  - Pattern-003 + 004 → Pattern-DOC
  - Pattern-006 → Pattern-WIKI (universal로 이동)
  - Pattern-008 → Pattern-AUTH (universal로 이동)
