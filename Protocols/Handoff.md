# Handoff

## Purpose

한 에이전트에서 다른 에이전트로 제어권과 컨텍스트를 이전하는 절차를 정의한다.
Handoff는 위임(Delegation)과 다르다.
위임은 태스크를 나눠주는 것, Handoff는 주도권 자체를 넘기는 것이다.

---

## Scope

다음 상황에서 Handoff가 발생한다:
- **Root → Project Agent**: 워크플로우 전체 실행 권한을 Project Agent에 이전
- 워크플로우의 한 단계가 완료되고 다음 에이전트가 이어받을 때
- 에이전트가 자신의 역할 범위를 벗어난 작업이 필요할 때
- Pipeline 패턴에서 이전 에이전트의 출력이 다음 에이전트의 입력이 될 때

---

## Root → Project Agent Handoff (가장 중요)

Root는 프로젝트 워크플로우를 직접 실행하지 않는다.
Project Agent 세션을 생성하고 전체 실행 권한을 이전한다.

### Root가 하는 것

1. `Projects/<name>/manifest.yaml` 을 읽어 dependencies를 확인한다.
2. Project Agent 세션을 생성한다 (`[AOA] <Project> — Project Agent`).
3. 아래 Handoff 패키지를 Project Agent에 전달한다.
4. Project Agent가 완료 보고를 보낼 때까지 기다린다.
5. **Root는 공용 에이전트나 서브에이전트 세션을 직접 생성하지 않는다.**

### Root → Project Agent Handoff 패키지

```yaml
type: root_to_project_handoff
task_id: <project-id>-<YYYYMMDD>-<seq>
from: root
to: project-agent
timestamp: <ISO 8601>

project:
  id: <project-id>
  manifest_path: Projects/<name>/manifest.yaml
  workflow: <workflow-id>              # 실행할 워크플로우

context:
  framework_rules: >
    AOA Core 규칙 및 Policies 적용.
    Framework 파일(Core/, Policies/ 등) 수정 금지.
    Root는 Framework 컨텍스트를 보유함. 재로드 불필요.
  memory_slice:
    project_goal: <프로젝트 목표>
    current_phase: <현재 단계>

responsibilities:
  - 워크플로우의 모든 단계를 직접 조율할 것
  - 필요한 공용 에이전트 세션을 직접 생성할 것
  - 프로젝트 서브에이전트 세션을 직접 생성할 것
  - 모든 단계 완료 후 Root에 최종 결과 보고할 것

reporting:
  report_to: root
  on_completion: "모든 단계 완료 시 Root에 결과 요약 전송"
  on_failure: "실패 시 즉시 Root에 에스컬레이션"
```

### Project Agent가 받은 후 하는 것

1. Handoff 패키지를 수신하고 `acknowledgement`를 전송한다.
2. manifest.yaml을 읽어 dependencies를 로드한다.
3. 워크플로우 단계별로 공용 에이전트/서브에이전트 세션을 직접 생성한다.
4. 단계 간 파일 전달을 직접 관리한다.
5. 완료 시 Root에 결과를 보고한다.

---

## Handoff vs Delegation

| 구분 | Delegation | Handoff |
|------|-----------|---------|
| 제어권 | 상위가 유지 | 이전됨 |
| 완료 후 | 결과를 상위에 반환 | 다음 에이전트가 계속 진행 |
| 사용 패턴 | 병렬, 팬아웃 | 파이프라인, 순차 |
| Root→Project | 해당 없음 | Root가 Project에 전체 위임 시 |

---

## Handoff 패키지 (일반)

Pipeline 패턴에서 에이전트 간 Handoff:

```yaml
type: handoff
task_id: <task_id>
from: <넘기는 에이전트>
to: <받는 에이전트>
timestamp: <ISO 8601>

handoff_package:
  completed:
    - step: <완료된 단계 이름>
      output_path: <결과 파일 경로>
      summary: <한 줄 요약>

  next_task:
    scope: <이어서 해야 할 작업>
    inputs:
      - source: <이전 단계 출력 경로>
        role: <이 입력의 역할>
    expected_output:
      format: <형식>
      path: <저장 경로>

  context_slice:
    project: <프로젝트 ID>
    relevant_memory: <필요한 메모리 발췌>
```

---

## Handoff 절차

### 넘기는 에이전트 (Sender)

1. 현재 태스크가 완전히 완료됐는지 확인한다.
2. 결과물이 저장됐는지 확인한다.
3. Handoff 패키지를 구성한다.
4. 받는 에이전트에게 Handoff 메시지를 전송한다.
5. `acknowledgement`를 받을 때까지 대기한다.
6. 확인 수신 후 제어권을 이전한다.

### 받는 에이전트 (Receiver)

1. Handoff 패키지를 수신한다.
2. 패키지 완전성을 확인한다 (필수 필드 존재 여부).
3. `acknowledgement`를 전송한다.
4. `next_task`를 기반으로 작업을 시작한다.

---

## Handoff 실패 처리

받는 에이전트가 패키지를 수락할 수 없는 경우:
1. 수락 거부 메시지를 보낸다 (이유 포함).
2. 넘기는 에이전트는 상위(Root 또는 Project Agent)에 에스컬레이션한다.
3. 상위가 중재하거나 대안 에이전트를 찾는다.

---

## TODO

부분 완료 상태에서의 Handoff 처리 정의.
Handoff 실패 시 자동 롤백 규칙 정의.

---

## Handoff vs Delegation

| 구분 | Delegation | Handoff |
|------|-----------|---------|
| 제어권 | 상위가 유지 | 이전됨 |
| 완료 후 | 결과를 상위에 반환 | 다음 에이전트가 계속 진행 |
| 사용 패턴 | 병렬, 팬아웃 | 파이프라인, 순차 |

---

## Handoff 패키지

제어권을 넘길 때 전달하는 패키지:

```yaml
type: handoff
task_id: <task_id>
from: <넘기는 에이전트>
to: <받는 에이전트>
timestamp: <ISO 8601>

handoff_package:
  completed:
    - step: <완료된 단계 이름>
      output_path: <결과 파일 경로>
      summary: <한 줄 요약>

  next_task:
    scope: <이어서 해야 할 작업>
    inputs:
      - source: <이전 단계 출력 경로>
        role: <이 입력의 역할>
    expected_output:
      format: <형식>
      path: <저장 경로>

  context_slice:
    project: <프로젝트 ID>
    relevant_memory: <필요한 메모리 발췌>
```

---

## Handoff 절차

### 넘기는 에이전트 (Sender)

1. 현재 태스크가 완전히 완료됐는지 확인한다.
2. 결과물이 저장됐는지 확인한다.
3. Handoff 패키지를 구성한다.
4. 받는 에이전트에게 Handoff 메시지를 전송한다.
5. `acknowledgement`를 받을 때까지 대기한다.
6. 확인 수신 후 제어권을 이전한다.

### 받는 에이전트 (Receiver)

1. Handoff 패키지를 수신한다.
2. 패키지 완전성을 확인한다 (필수 필드 존재 여부).
3. `acknowledgement`를 전송한다.
4. `next_task`를 기반으로 작업을 시작한다.

---

## Handoff 실패 처리

받는 에이전트가 패키지를 수락할 수 없는 경우:
1. 수락 거부 메시지를 보낸다 (이유 포함).
2. 넘기는 에이전트는 상위(Root 또는 Project Agent)에 에스컬레이션한다.
3. 상위가 중재하거나 대안 에이전트를 찾는다.

---

## TODO

부분 완료 상태에서의 Handoff 처리 정의.
Handoff 실패 시 자동 롤백 규칙 정의.
