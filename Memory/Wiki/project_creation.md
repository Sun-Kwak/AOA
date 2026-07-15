# Wiki: Project Creation

프로젝트 생성 시 반복된 실수와 회피 전략.

---

## [Pattern-001] 외부 경로에 프로젝트 생성

**발생일**: 2026-07-10 (3회 반복)  
**상황**: 사용자가 "프로젝트 만들어줘" 요청 시  
**실수**: `~/project/<name>/` 외부 경로에 프로젝트 생성  
**결과**: 
- .github/copilot-instructions.md를 읽을 수 없음
- dual session 문제 발생 (UI에 2개 세션 생성됨)
- 프로젝트가 AOA 구조와 분리됨

**회피전략**:
1. ✅ **절대 규칙**: 모든 프로젝트는 `AOA/Projects/<id>/` 내부에만 생성
2. ✅ 프로젝트 생성 전 경로 확인: `pwd`가 `/Users/sun/project/AOA`인지 체크
3. ✅ `Bootstrap/Create_Project.md` Step 3 참조
4. ❌ `~/project/`, `/tmp/`, 기타 외부 경로 절대 금지

---

## [Pattern-002] create_project 호출로 인한 dual session

**발생일**: 2026-07-10 (여러 차례)  
**상황**: 프로젝트 생성 후 세션 시작 시  
**실수**: `create_project()` + `create_session()` 동시 호출  
**결과**: 
- UI에 2개 세션 생성 (하나는 chat 하위, 하나는 별도 project panel)
- 두 세션이 동일 작업을 중복 실행

**회피전략**:
1. ✅ **절대 규칙**: `create_project()` 절대 호출 금지
2. ✅ 올바른 절차:
   ```
   1. AOA/Projects/<id>/ 에 파일 생성
   2. git add + git commit
   3. create_session()만 호출 (project_id는 AOA의 ID 사용)
   4. coordinate_with_creator: false 설정
   5. kickoff.mode: "autopilot" 설정
   ```
3. ✅ `.github/copilot-instructions.md` Root Agent 규칙 참조

---

## [Pattern-003] 불완전한 프로젝트 구조

**발생일**: 2026-07-10  
**상황**: health-fitness-cards 프로젝트 생성 시  
**실수**: manifest.yaml, README.md만 생성하고 필수 디렉터리 누락  
**결과**: 
- Agents/, Workflows/, Memory/ 디렉터리 없음
- 프로젝트 구조가 스키마와 불일치

**회피전략**:
1. ✅ **필수 체크**: `Bootstrap/Create_Project.md` Step 3 디렉터리 구조 확인
2. ✅ **필수 체크**: `Schemas/Project.md` manifest 스키마 확인
3. ✅ 생성해야 할 최소 구조:
   ```
   Projects/<id>/
     ├── manifest.yaml          ← Schemas/Project.md 스키마 준수
     ├── README.md
     ├── .gitignore
     ├── Agents/                ← 프로젝트 전용 에이전트
     ├── Workflows/             ← 프로젝트 전용 워크플로우
     ├── Memory/
     │   ├── project.md
     │   ├── execution_state.md
     │   └── decision_log.md
     └── Outputs/
   ```
4. ✅ 생성 후 체크리스트 검증:
   - [ ] manifest.yaml 스키마 준수?
   - [ ] 모든 디렉터리 존재?
   - [ ] Memory/ 하위 파일 3개 존재?

---

## [Pattern-004] manifest.yaml 불완전 작성

**발생일**: 2026-07-10  
**상황**: 빠르게 manifest만 작성하고 넘어감  
**실수**: 필수 필드 누락 또는 paths 섹션 불완전  
**결과**: 프로젝트 에이전트가 구조를 인식 못함

**회피전략**:
1. ✅ `Schemas/Project.md` 전체 스키마 참조 필수
2. ✅ 필수 필드 체크:
   - id, name, version, status, description
   - paths (root, agents, workflows, memory, outputs)
   - dependencies (비어있어도 선언 필수)
   - memory (3개 파일 경로)
   - outputs (default_path)
3. ✅ dependencies.agents에 사용할 공용 에이전트 명시
4. ✅ aoa_path 불필요 (내부 프로젝트이므로)

---

## [Pattern-005] 불필요한 프로젝트 자동 실행

**발생일**: 2026-07-10  
**상황**: 프로젝트 세션 생성 시 kickoff.prompt에 "준비되면 시작하세요!" 포함  
**실수**: 모든 프로젝트를 autopilot으로 즉시 실행  
**결과**: 
- 사용자가 프로젝트와 기획 조정할 기회 없음
- 불필요한 리소스 소비
- 테스트가 아닌 실제 프로젝트에 부적합

**회피전략**:

**테스트/검증 프로젝트 (자동 실행 O)**:
```javascript
create_session({
  project_id: "52d540bd...",
  name: "[AOA] Test Project",
  coordinate_with_creator: false,
  kickoff: {
    mode: "autopilot",  // 즉시 실행
    prompt: `...규칙 + 워크플로우...
    
준비되면 시작하세요!`
  }
})
```

**실제 프로젝트 (대기 상태 O)**:

Option 1 - kickoff 없이 idle 생성:
```javascript
create_session({
  project_id: "52d540bd...",
  name: "[AOA] Real Project",
  coordinate_with_creator: false
  // kickoff 생략 → 사용자 지시 대기
})
```

Option 2 - 규칙만 전달 후 대기:
```javascript
create_session({
  project_id: "52d540bd...",
  name: "[AOA] Real Project",
  coordinate_with_creator: false,
  kickoff: {
    mode: "interactive",  // autopilot 아님!
    prompt: `당신은 <project> Project Agent입니다.

manifest.yaml: /Users/sun/project/AOA/Projects/<id>/manifest.yaml

## 하위 에이전트 실행 규칙
- 에이전트 호출 전 list_agents()로 기존 세션 확인
- 존재하면 재사용, 없으면 생성
- Memory/execution_state.md 기반 Phase 진행 판단
- FAILED 세션만 재생성, IDLE/RUNNING은 상호작용

사용자 지시를 기다립니다.`
  }
})
```

**판단 기준**:
- ✅ 자동 실행: 테스트, 검증, 정기 실행 프로젝트
- ✅ 대기 상태: 기획 조정 필요, 사용자 승인 필요, 실제 업무 프로젝트

---

## 작업 시작 전 체크리스트

프로젝트 생성 요청이 들어오면:

- [ ] `Bootstrap/Create_Project.md` 읽음
- [ ] `Schemas/Project.md` 읽음
- [ ] 이 Wiki 문서 읽음
- [ ] 현재 경로가 `/Users/sun/project/AOA`인지 확인
- [ ] Registry에서 필요한 에이전트 검색
- [ ] 디렉터리 구조 전체 생성
- [ ] manifest.yaml 필수 필드 모두 작성 + **🚨 필수 절차 주석**
- [ ] Memory/ 하위 파일 3개 생성
- [ ] **Memory/wiki/ 디렉터리 생성** (Wiki_Protocol.md 포함)
- [ ] **pre_execution_check.sh 생성** (Wiki 자동 읽기)
- [ ] git commit
- [ ] create_session()만 호출 (create_project 금지) + **kickoff prompt에 Wiki 조회 규칙**

모든 항목을 통과해야 프로젝트 생성 시작.

---

## 성공 패턴 (참고용)

**올바른 프로젝트 생성 플로우**:

```bash
# 1. 경로 확인
cd /Users/sun/project/AOA

# 2. 디렉터리 생성
mkdir -p Projects/<id>/{Agents,Workflows,Memory,Outputs}

# 3. 파일 생성
# - manifest.yaml (스키마 준수 + 🚨 필수 절차 주석)
# - README.md
# - .gitignore
# - Memory/project.md
# - Memory/execution_state.md
# - Memory/decision_log.md
# - pre_execution_check.sh (Wiki 자동 읽기)

# 4. Git commit
git add Projects/<id>/
git commit -m "Add <project> project"

# 5. 세션 생성 (create_project 호출 금지!)
create_session({
  project_id: "52d540bd-4461-4c27-81ed-c460533357ac",  # AOA project ID
  coordinate_with_creator: false,
  kickoff: {
    mode: "autopilot",
    prompt: `
당신은 <project> Project Agent입니다.

manifest.yaml: /Users/sun/project/AOA/Projects/<id>/manifest.yaml

## 🚨 작업 시작 전 필수 절차

1. **Wiki 조회 (필수)**
   ./pre_execution_check.sh

2. **체크리스트 검증**
   - [ ] Wiki 전체 읽음
   - [ ] 과거 실수 패턴 확인
   - [ ] 회피 전략 적용

3. **작업 시작**

❌ Wiki 조회 없이 작업 시작 금지!

## Registry 및 공용 에이전트 사용 규칙

**초기화 시:**
- ✅ manifest.yaml의 dependencies.agents만 확인
- ❌ Registry/INDEX.md 전체 읽기 금지
- ❌ 모든 공용 에이전트 정보 사전 로딩 금지

**에이전트 호출 시:**
- ✅ 필요한 시점에 Registry/Agents/<id>.md 개별 조회
- ✅ 파라미터 스키마 확인 필요 시에만 조회
- ✅ on-demand 방식 사용

**명확한 원칙:**
- manifest.yaml이 단일 진실 공급원
- dependencies.agents에 명시된 것만 사용
- Registry는 on-demand 조회

## 하위 에이전트 실행 규칙
- 에이전트 호출 전 list_agents()로 기존 세션 확인
- 존재하면 재사용, 없으면 생성
- Memory/execution_state.md 기반 Phase 진행 판단
- FAILED 세션만 재생성, IDLE/RUNNING은 상호작용

## 작업 지시
<사용자 요구사항 + 워크플로우 설명>

준비되면 시작하세요!
    `
  }
})
```

---

## [Pattern-006] Wiki Protocol 무시 (에이전트와 동일)

**발생일**: 2026-07-10 (health-fitness-cards 프로젝트 보고)  
**상황**: 프로젝트 세션에서 하위 에이전트(image-generator) 호출 시  
**실수**: 
- 프로젝트 `Memory/wiki/` 존재함
- 하위 에이전트 `memory/wiki/` 존재함
- **양쪽 모두 Wiki 조회 없이 작업 시작**

**결과**: Pattern-004와 동일 (에이전트 참조)

**회피전략**:
1. ✅ 프로젝트 생성 시 다음 파일 함께 생성:
   ```
   Projects/<id>/pre_execution_check.sh     # Wiki 자동 읽기 스크립트
   Projects/<id>/.session_init               # 세션 시작 훅
   ```
2. ✅ `manifest.yaml`에 "🚨 작업 시작 전 필수 절차" 필드 추가
3. ✅ Kickoff prompt에 "pre_execution_check.sh 실행 필수" 명시
4. ✅ 기존 모든 프로젝트에 소급 적용

---

## [Pattern-007] Registry INDEX 전체 로딩 (불필요한 컨텍스트 소비)

**발생일**: 2026-07-15 (health-fitness-cards 프로젝트 보고)  
**상황**: 프로젝트 세션 초기화 시  
**실수**:
- Registry/INDEX.md 전체 읽기
- 모든 공용 에이전트 정보 로딩 (4개)
- `manifest.yaml`의 `dependencies.agents`에 없는 에이전트까지 메모리에 로딩

**예시**:
```yaml
# manifest.yaml
dependencies:
  agents:
    - trend-research-agent  # ✅ 사용
    - image-generator       # ✅ 사용
# image-generator-comfyui  ❌ 미사용
# browser-controller       ❌ 미사용
```

**실제 발생**:
1. Registry/INDEX.md 전체 읽음
2. 4개 에이전트 모두 정보 로딩
3. 사용하지 않을 에이전트 정보도 컨텍스트 소비

**문제점**:
- 불필요한 Registry 데이터 로딩
- 컨텍스트 낭비
- 프로젝트는 `dependencies.agents`만 보면 충분함

**회피 전략**:

### 올바른 프로젝트 세션 초기화 절차

```markdown
✅ 1. manifest.yaml 읽기
✅ 2. dependencies.agents 리스트만 확인
      예: ["trend-research-agent", "image-generator"]
✅ 3. on-demand Registry 조회 (필요 시점에만)
      - 에이전트 호출 직전
      - 파라미터 스키마 확인 필요 시
      - Registry/Agents/<id>.md 개별 조회

❌ Registry/INDEX.md 전체 읽기 금지
❌ 모든 공용 에이전트 정보 사전 로딩 금지
```

### Kickoff Prompt 템플릿 개선

**기존 (잘못됨):**
```
3. **공용 에이전트 확인**
   - Registry에서 사용 가능한 공용 에이전트 확인
```

**개선 (올바름):**
```
3. **공용 에이전트 확인**
   - manifest.yaml의 dependencies.agents 리스트만 확인
   - Registry INDEX 전체 읽기 금지
   - 필요한 에이전트는 호출 시점에 개별 조회
```

### 프로젝트 세션 초기화 규칙

**명확한 원칙:**
```
1. ✅ manifest.yaml이 단일 진실 공급원
2. ✅ dependencies.agents에 명시된 것만 사용
3. ✅ Registry는 on-demand 조회
4. ❌ Registry INDEX 전체 읽기 금지
5. ❌ 사용하지 않을 에이전트 정보 로딩 금지
```

**적용:**
1. ✅ Kickoff prompt 템플릿 업데이트 (Line 212-234)
2. ✅ 모든 신규 프로젝트 세션에 자동 적용
3. ✅ 기존 프로젝트 재시작 시 적용

---

## [Pattern-008] Access Control & Authority Protocol 위반

**발생일**: 2026-07-15  
**상황**: health-fitness-cards 프로젝트 실행 중  
**실수**: 
1. 프로젝트 에이전트가 공용 에이전트 생성을 직접 시도
2. 공용 에이전트가 프로젝트 파일(manifest.yaml) 직접 수정 시도

**결과**:
- 권한 경계 위반
- 잘못된 디렉터리 접근
- 협업 프로토콜 미준수

**근본 원인**:
프로젝트 에이전트의 **접근 권한과 책임 범위**가 kickoff prompt에 명시되지 않음.

---

### 회피 전략: Kickoff Prompt에 Access Control 추가

**프로젝트 세션 생성 시 kickoff prompt에 필수 포함:**

```markdown
## 🚨 Access Control (필수 준수)

당신은 **프로젝트 에이전트**입니다.

**접근 가능:**
- ✅ 자신의 프로젝트 디렉터리 (Projects/<project-name>/*)
- ✅ Registry/ (읽기 전용)
- ✅ 공용 Agents/ (읽기 전용, 호출만)

**접근 불가:**
- ❌ Registry/Agents/ 생성/수정
- ❌ Agents/ 디렉터리 수정
- ❌ Core/, Policies/, Standards/ 수정
- ❌ 다른 프로젝트 디렉터리

**공용 에이전트 생성 필요 시:**
→ send_session_message로 Root(General Chat)에 요청
→ **절대 직접 생성하지 말 것**

예시:
send_session_message(
  session_id="<root_chat_id>",
  message="## 🚨 공용 에이전트 생성 요청\n\n..."
)

**프로젝트 전용 에이전트 생성 시:**
→ Projects/<project-name>/Agents/ 내부에만 생성
→ manifest.yaml의 project_agents에 등록
```

---

### 올바른 Cross-Agent 협업 패턴

#### Pattern: 프로젝트 에이전트 → 공용 에이전트 생성 요청
```yaml
발견: "맥락 보존 변형 전문 에이전트 필요"
action: send_session_message
to: <root_chat_id>
message: |
  ## 🚨 공용 에이전트 생성 요청
  
  **From**: <project-name> 프로젝트 에이전트
  **To**: Root (General Chat)
  
  **요청 배경:** ...
  **제안 에이전트 ID:** content-transformer
  **역할:** ...
  **입력 스키마:** ...
  **출력 스키마:** ...
  
  공용 에이전트 생성 부탁드립니다!
do_not: Registry/Agents/ 직접 생성
```

---

### Kickoff Prompt 템플릿 업데이트

**기존 템플릿 (Line 212-234)에 Access Control 섹션 추가:**

```markdown
You are the <project-name> project agent.

## 🚨 Access Control (필수 준수)

**접근 가능:**
- ✅ Projects/<project-name>/*
- ✅ Registry/ (읽기 전용)
- ✅ Agents/ (읽기 전용, 호출만)

**접근 불가:**
- ❌ Registry/Agents/ 생성/수정
- ❌ Core/, Policies/, Standards/ 수정
- ❌ 다른 프로젝트

**공용 에이전트 필요 시:**
→ Root에 요청 (session_id 제공 예정)
→ 직접 생성 금지

...
```

---

### 적용 범위

**즉시 적용:**
1. ✅ 신규 프로젝트 세션 생성 시 kickoff prompt에 포함
2. ✅ 기존 프로젝트 재시작 시 적용
3. ✅ Memory/Wiki/project_creation.md 업데이트

---

## 업데이트 이력

- 2026-07-10: 초기 작성 (Pattern-001 ~ 004 기록)
- 2026-07-10: Pattern-005 추가 (불필요한 자동 실행)
- 2026-07-10: Pattern-006 추가 (Wiki Protocol 적용)
- 2026-07-15: Pattern-007 추가 (Registry INDEX 전체 로딩 방지)
- 2026-07-15: Pattern-008 추가 (Access Control & Authority Protocol)
- 2026-07-10: Kickoff prompt 템플릿에 "하위 에이전트 중복 생성 방지" 규칙 추가
- 2026-07-10: Pattern-006 추가 (Wiki Protocol 강제 메커니즘)
- 2026-07-15: Pattern-007 추가 (Registry INDEX 전체 로딩 방지)
