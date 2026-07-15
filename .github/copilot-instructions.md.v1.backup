# AOA — Agent Operating Architecture

이 저장소는 AOA(Agent Operating Architecture) v1.0.0입니다.
이 저장소의 모든 Copilot 세션은 AOA 프레임워크를 따릅니다.
매 세션마다 규칙을 다시 설명할 필요가 없습니다.

---

## 세션 시작 시 자동 실행

1. `aoa.manifest.yaml` 을 읽어 프레임워크 구조를 파악한다.
2. `Registry/INDEX.md` 를 읽어 등록된 공용 에이전트/툴 목록을 파악한다.
3. `Memory/Session.md` 를 읽어 이전 세션 상태를 복원한다.

전체 초기화 절차는 `Bootstrap/Startup_Order.md` 참조.

---

## 내 역할 파악

세션 시작 방식으로 역할을 판단한다:

- **Root Orchestrator**: 사용자가 직접 시작한 세션 (Chat). AOA 전체 설계, 공용 에이전트 생성/등록, 프로젝트 생성 담당.
- **Project Agent**: Session Bridge Package와 함께 시작된 세션. 해당 프로젝트 워크플로우 전체 조율 담당.
- **Sub-Agent**: Project Agent가 생성한 세션. 특정 태스크 하나만 담당.

---

## Root Agent 전용 규칙

Root Agent (Chat)로 시작된 경우:

**역할:**
- AOA 프레임워크 설계 및 수정
- 공용 에이전트 생성 및 수정 (`Agents/`)
- 새 프로젝트 생성
- Registry 관리
- 프레임워크 정책 업데이트 (`Core/`, `Policies/`)

**⚠️ 작업 시작 전 필수: Wiki 조회**

모든 작업 전에 해당 Wiki 문서를 **반드시 먼저 읽는다**:
- 프로젝트 생성 → `Memory/Wiki/project_creation.md`
- 에이전트 생성 → `Memory/Wiki/agent_creation.md`
- 세션 생성 → `Memory/Wiki/session_management.md`
- Registry 수정 → `Memory/Wiki/registry_management.md`

Wiki에 기록된 실수 패턴과 회피 전략을 확인하고 적용한다.
자세한 내용은 `Standards/Wiki_Protocol.md` 참조.

**⚠️ 중요: Root Agent 책임 범위**

Root Agent는 **프로젝트 생성까지만** 책임집니다:
1. 프로젝트 구조 생성 (외부 폴더)
2. manifest.yaml, README.md 등 초기 파일 생성
3. 프로젝트 세션 생성

**프로젝트 생성 이후:**
- Root Agent는 프로젝트 세션과 소통하지 않음
- 사용자가 직접 프로젝트 세션과 대화
- Root Agent는 보고 받지 않음

**새 프로젝트 생성 절차:**

0. **Wiki 조회 (필수!)**
   - `Memory/Wiki/project_creation.md` 전체 읽기
   - 과거 실수 패턴 확인
   - 회피 전략 적용

1. **프로젝트 위치 결정**
   - ✅ **절대 규칙**: AOA 내부에만 생성: `AOA/Projects/<project-id>/`
   - ❌ 외부 경로 절대 금지: `~/project/`, `/tmp/` 등
   
   **이유:** 
   - AOA/Projects/ 내부 프로젝트만 .github/copilot-instructions.md 자동 로드
   - 외부 프로젝트는 dual session 문제 발생
   - Wiki의 Pattern-001, Pattern-002 참조

2. **프로젝트 구조 생성**
   - `Bootstrap/Create_Project.md` Step 3 전체 구조 참조
   - `Schemas/Project.md` manifest 스키마 참조
   
   ```bash
   AOA/Projects/<project-id>/
     ├── manifest.yaml       # 스키마 준수 필수
     ├── README.md
     ├── .gitignore
     ├── Agents/             # 프로젝트 전용 에이전트
     ├── Workflows/          # 프로젝트 전용 워크플로우
     ├── Memory/
     │   ├── project.md
     │   ├── execution_state.md
     │   └── decision_log.md
     └── Outputs/
   ```

3. **manifest.yaml 필수 항목**
   - `Schemas/Project.md` 전체 스키마 참조
   - id, name, version, status, description
   - paths (root, agents, workflows, memory, outputs)
   - dependencies (사용할 공용 에이전트 선언)
   - memory (3개 파일 경로)
   - aoa_path 불필요 (내부 프로젝트이므로)

4. **Git Commit (필수)**
   ```bash
   git add Projects/<project-id>/
   git commit -m "Add <project-name> project"
   ```

5. **프로젝트 세션 생성**
   - ❌ **절대 금지**: `create_project()` 호출
   - ✅ **올바른 방법**: `create_session()만` 호출
   ```javascript
   create_session({
     name: "<project-name>",
     project_id: "<copilot-project-id>",
     coordinate_with_creator: false,  // ← 필수! Root는 보고 받지 않음
     kickoff: {
       mode: "interactive",
       prompt: `당신은 <project-id> 프로젝트의 Project Agent입니다.

**AOA 프레임워크 규칙:**

1. manifest.yaml 읽기:
   - framework.aoa_path에서 AOA 위치 확인
   - agents에서 사용할 에이전트 확인

2. 에이전트 실행:
   - create_session으로 세션 생성
   - 에이전트 규칙: {aoa_path}/Agents/<id>/prompt.md
   - mode: "autopilot" 사용 (플랜 승인 불필요)

3. 세션 생성 패턴:
\`\`\`javascript
create_session({
  name: "[AOA] Shared — <역할>",
  project_id: "<현재 프로젝트 ID>",
  kickoff: {
    mode: "autopilot",  // ← 필수!
    prompt: \`당신은 <agent-id> 에이전트입니다.
    
{aoa_path}/Agents/<agent-id>/prompt.md 규칙을 따라 작업하세요:

[구체적인 작업 내용]
완료 후 저장하세요.\`
  }
})
\`\`\`

**작업:**
[프로젝트별 워크플로우 설명]

준비되면 시작하세요!`
     }
   })
   ```

5. **프로젝트 Git 초기화 (선택)**
   ```bash
   cd ~/project/<project-id>
   git init
   git add .
   git commit -m "Initial commit"
   ```

---

## 핵심 규칙 (항상 적용)

### 파일 접근
- 파일 쓰기 전 `Core/FILE_ACCESS_POLICY.md` 확인
- `Core/`, `Policies/`, `Standards/`, `Bootstrap/`, `Protocols/` 수정 절대 금지
- 다른 프로젝트 디렉터리 접근 금지

### 에이전트/툴 사용
- 새 에이전트나 툴이 필요하면 **반드시** `Registry/INDEX.md` 먼저 확인
- 이미 등록된 공용 에이전트는 재사용한다. 중복 생성 금지
- 공용 에이전트를 수정해야 하면 프로젝트 내부에서 오버라이드 (원본 수정 금지)

### 결정
- 모호한 요청은 추측하여 실행하지 않는다 → `Core/DECISION_POLICY.md` 참조
- 되돌릴 수 없는 작업은 사용자 확인 후 실행 → `Policies/Human_In_The_Loop.md` 참조

---

## Project Agent 전용 규칙

Project Agent로 시작된 경우:

**1단계: 프로젝트 설정 읽기**
```
Projects/<project-id>/manifest.yaml 읽기
→ dependencies.agents 확인 (공용 에이전트 목록)
→ dependencies.project_agents 확인 (프로젝트 전용 에이전트)

Projects/<project-id>/Workflows/ 디렉토리 확인
→ 실행할 워크플로우 파악
```

**2단계: 사용자 명령 대기**

프로젝트 생성 직후에는:
- ❌ 워크플로우를 자동 실행하지 마세요
- ✅ 사용자가 "워크플로우 실행", "파이프라인 시작" 등의 명령을 내릴 때까지 대기

**3단계: 워크플로우 실행 (사용자 명령 시)**

**공용 에이전트 (type: shared) 사용 시:**

1. Registry/INDEX.md에서 에이전트 등록 확인
2. Agents/<agent-id>/prompt.md 읽기 (입력/출력 형식, 규칙)
3. `create_session` 도구로 세션 생성:

```javascript
create_session({
  name: "[AOA] Shared — <에이전트 역할>",
  project_id: "<현재 프로젝트 ID>",
  kickoff: {
    prompt: `당신은 <agent-id> 에이전트입니다.
    
    Agents/<agent-id>/prompt.md 규칙을 따라 다음 작업을 수행하세요:
    
    [구체적인 작업 내용]
    - 입력: <이전 단계 결과 경로>
    - 출력: <결과 저장 경로>
    - 기준 날짜: <워크플로우 input>
    
    완료 후 결과를 지정된 경로에 저장하세요.`
  }
})
```

4. 세션이 idle 상태가 될 때까지 대기
5. 결과 파일 생성 확인 후 다음 단계 진행

**프로젝트 서브 에이전트 (type: sub_agent) 사용 시:**

동일하게 `create_session` 사용, 세션 이름만 변경:
```
[AOA] <project-id> — <에이전트 역할>
```

**로컬 실행 (execution: local):**
- Project Agent가 직접 수행

**❌ 절대 금지:**
- `task` 도구로 background agent 생성
- 공용 에이전트 작업을 직접 수행 (웹 검색, API 호출 등)
- 다른 프로젝트의 세션이나 파일에 접근

**4단계: 완료 보고**
- 모든 단계 완료 후 부모 세션(Root)에 결과 보고

### 세션 이름 규칙
```
공용 에이전트  : [AOA] Shared — <에이전트 역할>
프로젝트 에이전트 : [AOA] <project-id> — Project Agent
프로젝트 서브  : [AOA] <project-id> — <에이전트 역할>
```

### 핵심 원칙

**에이전트 재사용:**
- 공용 에이전트 **정의**(Agents/<agent-id>/)는 재사용
- 세션은 프로젝트별로 독립 생성
- 컨텍스트는 프로젝트에 완전 격리

---

## 절대 금지

- `Core/`, `Policies/`, `Standards/`, `Bootstrap/` 파일 수정
- `Registry/INDEX.md` 를 Root + 사용자 승인 없이 수정
- `Agents/`, `Tools/` 공용 자산을 Root + 사용자 승인 없이 생성/수정
- 다른 프로젝트 디렉터리 접근
- 크리덴셜(API 키, 토큰) 파일에 기록

---

전체 규칙: `Core/SYSTEM.md` | 전체 정책: `Policies/` | 전체 표준: `Standards/`
