# Agent Communication

## Purpose

에이전트 간 메시지의 표준 포맷과 상호작용 규칙을 정의한다.
모든 위임 요청과 응답은 이 포맷을 따른다.

---

## Scope

Root ↔ Project Agent, Project Agent ↔ Sub-Agent,
Root ↔ Shared Agent 간의 모든 메시지에 적용된다.

---

## 메시지 유형

| 유형 | 방향 | 설명 |
|------|------|------|
| `delegation` | 상위 → 하위 | 태스크 위임 요청 |
| `response` | 하위 → 상위 | 태스크 결과 반환 |
| `context_request` | 하위 → 상위 | 추가 컨텍스트 요청 |
| `context_response` | 상위 → 하위 | 컨텍스트 제공 |
| `escalation` | 하위 → 상위 | 처리 불가 에스컬레이션 |
| `acknowledgement` | 하위 → 상위 | 수신 확인 |

---

## Delegation 메시지 포맷

```yaml
type: delegation
task_id: <unique-task-id>       # <project-id>-<sequence> 형식
from: <agent-id>                # 위임하는 에이전트
to: <agent-id>                  # 위임받는 에이전트
timestamp: <ISO 8601>

task:
  scope: <태스크 한 줄 설명>
  inputs:
    <key>: <value>
  expected_output:
    format: <markdown|yaml|json|text>
    path: <저장 경로 — 없으면 null>
  constraints:
    - <이 태스크에만 적용되는 제약>
  deadline: null                # 없으면 null
```

---

## Response 메시지 포맷

```yaml
type: response
task_id: <위임 시 받은 task_id>
from: <응답하는 에이전트>
to: <위임한 에이전트>
timestamp: <ISO 8601>

result:
  status: <complete|partial|failed>
  output_path: <결과 파일 경로 — 없으면 null>
  summary: <결과 한 줄 요약>
  errors: []                    # 오류 목록 (없으면 빈 배열)
```

---

## Escalation 메시지 포맷

```yaml
type: escalation
task_id: <task_id>
from: <에스컬레이션하는 에이전트>
to: <상위 에이전트>
timestamp: <ISO 8601>

reason: <왜 처리할 수 없는지>
attempted: <무엇을 시도했는지>
needs: <무엇이 있어야 처리 가능한지>
```

---

## 통신 규칙

1. 모든 메시지는 `task_id`를 포함해야 한다.
2. `task_id`는 위임 시 상위 에이전트가 생성하고 하위 에이전트는 변경하지 않는다.
3. 하위 에이전트는 `delegation` 수신 즉시 `acknowledgement`로 응답한다.
4. 응답 없이 다음 단계로 진행하지 않는다.
5. 에이전트는 자신이 받은 `delegation` 범위 밖의 행동을 하지 않는다.

---

## task_id 생성 규칙

```
형식: <project-id>-<YYYYMMDD>-<sequence>
예시: kids-video-gen-20260709-001
      shared-20260709-042
```

Root가 최초 생성. 서브태스크는 부모 task_id에 suffix 추가:
```
kids-video-gen-20260709-001-a   (서브태스크 a)
kids-video-gen-20260709-001-b   (서브태스크 b)
```

---

## TODO

비동기 메시지 처리 규칙 정의.
메시지 타임아웃 및 재전송 규칙 정의.
