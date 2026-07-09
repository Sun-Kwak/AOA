# Session Bridge

## Purpose

새 Copilot 세션이 시작될 때 이전 세션의 컨텍스트를 전달하는 구조를 정의한다.
LLM 세션은 상태가 없다(stateless). Session Bridge가 상태를 만든다.

---

## Scope

다음 상황에서 Session Bridge가 필요하다:
- Root가 새 서브에이전트 세션을 온디맨드로 생성할 때
- 이전 세션이 끊기고 새 세션으로 재시작할 때
- 프로젝트 에이전트를 별도 Copilot 세션으로 분리할 때

---

## Session Bridge 패키지

Root가 새 세션에 주입하는 최소 컨텍스트 패키지:

```yaml
# Session Bridge Package
type: session_bridge
bridge_id: <bridge-id>             # <project-id>-<timestamp>
created_by: root
target_session: <세션 패널 표기명>
timestamp: <ISO 8601>

# ── AOA 프레임워크 식별 ──
framework:
  aios_version: 1.0.0
  manifest_path: aios.manifest.yaml
  note: >
    AOA Framework가 적용됩니다.
    Core, Policies, Standards는 Root Orchestrator가 보유합니다.
    이 에이전트는 Framework 파일을 재로드하지 않습니다.

# ── 에이전트 신원 ──
agent:
  id: <이 세션의 에이전트 ID>
  role: <에이전트 역할>
  project_id: <소속 프로젝트 ID>
  project_path: Projects/<name>/

# ── 현재 태스크 ──
task:
  task_id: <task_id>
  scope: <태스크 설명>
  inputs: {}
  expected_output:
    format: <형식>
    path: <저장 경로>

# ── 관련 메모리 ──
memory:
  project_goal: <프로젝트 목표>
  current_phase: <현재 단계>
  last_completed: <마지막 완료 태스크>
  pending: <남은 작업 — 없으면 null>

# ── 의존성 요약 ──
available_agents:
  - id: <agent-id>
    role: <역할>
    session: <세션 패널 표기명 — 없으면 null>
```

---

## 세션 초기화 절차

새 세션이 Session Bridge 패키지를 받으면:

1. 패키지 수신 확인 (`acknowledgement` 전송).
2. `framework.note`를 확인 — Framework 파일은 재로드하지 않는다.
3. `agent.role`을 자신의 역할로 설정한다.
4. `task`를 읽고 작업을 시작한다.
5. 작업 완료 후 결과를 Root에 `response` 메시지로 반환한다.

---

## 세션 재연결 (Reconnect)

진행 중이던 세션이 끊기고 재시작할 때:

1. Root가 `Memory/Session.md`와 `Memory/Execution_State.md`를 확인한다.
2. 중단된 태스크가 있으면 사용자에게 알린다.
3. 사용자가 재개를 선택하면 새 Session Bridge 패키지를 생성한다.
   - `task`에 중단 지점부터의 작업을 기술한다.
   - `memory.last_completed`에 마지막 완료 단계를 포함한다.
4. 새 세션을 생성하고 패키지를 주입한다.

---

## 세션 패널 표기

Session Bridge로 생성된 세션의 이름:

```
[AOA] <project-id> — <agent-role>
예시:
  [AOA] kids-video-gen — Script Writer Agent
  [AOA] Shared — Image Generation Agent
```

Root 세션:
```
[AOA] Root Orchestrator
```

---

## TODO

Session Bridge 패키지 압축 전략 정의 (토큰 절약).
세션 타임아웃 및 자동 재연결 규칙 정의.
멀티 프로젝트 동시 세션 관리 규칙 추가.
