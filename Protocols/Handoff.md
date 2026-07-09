# Handoff

## Purpose

한 에이전트에서 다른 에이전트로 제어권과 컨텍스트를 이전하는 절차를 정의한다.
Handoff는 위임(Delegation)과 다르다.
위임은 태스크를 나눠주는 것, Handoff는 주도권 자체를 넘기는 것이다.

---

## Scope

다음 상황에서 Handoff가 발생한다:
- 워크플로우의 한 단계가 완료되고 다음 에이전트가 이어받을 때
- 에이전트가 자신의 역할 범위를 벗어난 작업이 필요할 때
- Pipeline 패턴에서 이전 에이전트의 출력이 다음 에이전트의 입력이 될 때

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
