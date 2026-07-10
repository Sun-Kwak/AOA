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

에이전트 실행 패턴:
<create_session 규칙만 기술>

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
- [ ] manifest.yaml 필수 필드 모두 작성
- [ ] Memory/ 하위 파일 3개 생성
- [ ] git commit
- [ ] create_session()만 호출 (create_project 금지)

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
# - manifest.yaml (스키마 준수)
# - README.md
# - .gitignore
# - Memory/project.md
# - Memory/execution_state.md
# - Memory/decision_log.md

# 4. Git commit
git add Projects/<id>/
git commit -m "Add <project> project"

# 5. 세션 생성 (create_project 호출 금지!)
create_session({
  project_id: "52d540bd-4461-4c27-81ed-c460533357ac",  # AOA project ID
  coordinate_with_creator: false,
  kickoff: {
    mode: "autopilot",
    prompt: "AOA 규칙 + 작업 지시"
  }
})
```

---

## 업데이트 이력

- 2026-07-10: 초기 작성 (Pattern-001 ~ 004 기록)
- 2026-07-10: Pattern-005 추가 (불필요한 자동 실행)
