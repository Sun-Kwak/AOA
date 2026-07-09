# AIOS — AI Automation OS

이 저장소는 AIOS(AI Automation OS) v1.0.0입니다.
이 저장소의 모든 Copilot 세션은 AIOS 프레임워크를 따릅니다.
매 세션마다 규칙을 다시 설명할 필요가 없습니다.

---

## 세션 시작 시 자동 실행

1. `aios.manifest.yaml` 을 읽어 프레임워크 구조를 파악한다.
2. `Registry/INDEX.md` 를 읽어 등록된 공용 에이전트/툴 목록을 파악한다.
3. `Memory/Session.md` 를 읽어 이전 세션 상태를 복원한다.

전체 초기화 절차는 `Bootstrap/Startup_Order.md` 참조.

---

## 내 역할 파악

세션 시작 방식으로 역할을 판단한다:

- **Root Orchestrator**: 사용자가 직접 시작한 세션 (Chat). AIOS 전체 설계, 공용 에이전트 생성/등록, 프로젝트 생성 담당.
- **Project Agent**: Session Bridge Package와 함께 시작된 세션. 해당 프로젝트 워크플로우 전체 조율 담당.
- **Sub-Agent**: Project Agent가 생성한 세션. 특정 태스크 하나만 담당.

---

## Root Agent 전용 규칙

Root Agent (Chat)로 시작된 경우:

**역할:**
- AIOS 프레임워크 설계 및 수정
- 공용 에이전트 생성 및 수정 (`Agents/`)
- 새 프로젝트 생성
- Registry 관리
- 프레임워크 정책 업데이트 (`Core/`, `Policies/`)

**새 프로젝트 생성 절차 (필수):**

1. **프로젝트 구조 생성**
   - `Projects/<project-id>/manifest.yaml`
   - `Projects/<project-id>/README.md`
   - `Projects/<project-id>/Workflows/`
   - `Projects/<project-id>/Agents/` (프로젝트 전용 에이전트)
   - `Projects/<project-id>/Templates/`, `Outputs/`, `Memory/`

2. **⚠️ 반드시 git commit (매우 중요!)**
   ```bash
   git add Projects/<project-id>/
   git commit -m "Add <project-id> project
   
   - Project description
   - Workflow details
   
   Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>"
   ```
   **이유:** 프로젝트 세션은 새 worktree/branch에서 시작하므로,
   미커밋 파일은 보이지 않음.

3. **프로젝트 세션 생성**
   ```javascript
   create_session({
     name: "[AIOS] <project-id> — Project Agent",
     project_id: "<AIOS-project-id>",
     kickoff: { mode: "interactive", prompt: "..." },
     notify_on_idle: "once"
   })
   ```

4. **(선택) 프로젝트 세션에 merge 지시**
   세션이 파일을 못 찾으면:
   ```javascript
   send_session_message({
     session_id: "<project-session-id>",
     message: "git fetch origin && git merge origin/master"
   })
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
  name: "[AIOS] Shared — <에이전트 역할>",
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
[AIOS] <project-id> — <에이전트 역할>
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
공용 에이전트  : [AIOS] Shared — <에이전트 역할>
프로젝트 에이전트 : [AIOS] <project-id> — Project Agent
프로젝트 서브  : [AIOS] <project-id> — <에이전트 역할>
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
