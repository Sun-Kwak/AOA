# AOA — Agent Operating Architecture v2.0.1

이 저장소는 **Agent Operating Architecture (AOA)** 프레임워크입니다.  
모든 Copilot 세션은 AOA 규칙을 따릅니다.

---

## 🚨 필수 시작 절차 (MANDATORY)

**모든 작업 전에 다음을 읽으세요:**

1. **경로 검증 (최우선)**
   - ✅ 현재 작업 경로가 AOA 저장소 내부인지 확인
   - ✅ `git rev-parse --show-toplevel` 실행
   - ✅ 결과가 `/Users/sun/project/AOA` 또는 워크트리 경로인지 확인
   - ❌ 잘못된 경로(중복 클론)에서 작업 금지

2. **범용 패턴 (모든 역할 필수)**
   - `Memory/Wiki/universal_patterns.md`
     - Pattern-WIKI: Wiki Protocol
     - Pattern-AUTH: Access Control & Agent Invocation

3. **역할별 Wiki**
   - **Root Agent** (프로젝트/에이전트 생성):
     - `Memory/Wiki/project_creation.md`
     - `Memory/Wiki/agent_creation.md`
   
   - **Project Agent** (프로젝트 실행):
     - `manifest.yaml` (dependencies.agents 확인)
     - `Workflows/main.md` (Phase와 Agent 확인)
     - `Memory/Wiki/project_creation.md` (Pattern-WORKFLOW)

3. **과거 실수 확인**
   - `Memory/Wiki/` 전체 스캔
   - 실수 패턴과 회피 전략 학습

---

## 🎯 핵심 규칙 (절대 준수)

### Pattern-007: Registry 사용 규칙
- ❌ **Registry/INDEX.md 전체 읽기 금지**
- ✅ manifest.yaml의 dependencies.agents만 확인
- ✅ 필요 시 Registry/Agents/<id>.md 개별 조회 (on-demand)

### Pattern-AUTH: Agent Invocation Method
- ❌ **공용 에이전트(Registry/Agents/)를 task로 호출 금지**
- ✅ 공용 에이전트는 create_session으로만 호출
- ✅ 프로젝트 전용 에이전트: task 또는 create_session

### Pattern-WORKFLOW: Workflow Enforcement
- ❌ **Workflows/*.md 무시하고 직접 실행 금지**
- ✅ Phase 순서와 Agent 필수 준수
- ✅ 사용자가 "직접 실행" 요청해도 워크플로우 우선

### Pattern-PROC: Project Creation
- ❌ **외부 경로에 프로젝트 생성 금지**
- ❌ **create_project() 호출 금지**
- ✅ AOA/Projects/<id>/ 내부에만 생성
- ✅ create_session()만 사용

---

## 🔒 절대 금지 (CRITICAL)

**파일 수정:**
- ❌ Core/, Policies/, Standards/, Bootstrap/ 수정 금지
- ❌ 다른 프로젝트 디렉터리 접근 금지
- ❌ Registry/INDEX.md 직접 수정 금지

**실행:**
- ❌ 워크플로우 건너뛰기 금지
- ❌ 에이전트 대신 직접 API 호출 금지
- ❌ 사용자 요청이어도 AOA 규칙 우선

---

## 📋 역할별 시작 가이드

### Root Agent (General Chat)
```
1. Memory/Wiki/universal_patterns.md 읽기
2. 작업 종류 확인:
   - 프로젝트 생성 → Memory/Wiki/project_creation.md
   - 에이전트 생성 → Memory/Wiki/agent_creation.md
3. 체크리스트 준수
4. 작업 실행
```

### Project Agent (프로젝트 세션)
```
1. Memory/Wiki/universal_patterns.md 읽기
2. manifest.yaml 읽기 (dependencies.agents)
3. Workflows/main.md 읽기 (Phase, Agent)
4. Pattern-WORKFLOW 준수
5. 사용자 명령 대기
6. 워크플로우 실행 (Agent 호출)
```

---

## 📚 상세 규칙

모든 상세 규칙은 `Memory/Wiki/`에 있습니다:
- `universal_patterns.md`: Pattern-WIKI, Pattern-AUTH
- `project_creation.md`: Pattern-PROC, Pattern-DOC, Pattern-005, Pattern-007, Pattern-WORKFLOW
- `agent_creation.md`: 에이전트 생성 패턴
- `registry_management.md`: Registry 관리 규칙
- `session_management.md`: 세션 생성 규칙

---

**AOA v2.0.1** — 2026-07-15 업데이트
