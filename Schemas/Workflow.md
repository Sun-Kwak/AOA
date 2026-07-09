# Workflow Schema

## Purpose

모든 AIOS 워크플로우 정의 파일이 따라야 하는 표준 구조를 정의한다.
워크플로우는 에이전트들을 순서에 따라 조율하는 단위다.

---

## Scope

공용 워크플로우 (`Workflows/<name>/workflow.yaml`) 및
프로젝트 워크플로우 (`Projects/<name>/Workflows/<name>.yaml`) 모두에 적용된다.

---

## Workflow Schema

```yaml
# Workflows/<workflow-name>/workflow.yaml
# Standards/Naming.md: ID는 kebab-case, -workflow 접미사 필수

id: <workflow-id>                 # 예: video-production-workflow
name: <Display Name>
version: 1.0.0
status: active

description: >
  이 워크플로우가 무엇을 하는지 한 문장.

# 실행 패턴 (Workflows/Patterns/ 참조)
pattern: <sequential|parallel|pipeline|fan_out_fan_in|graph>

# 필요한 에이전트 목록
agents_required:
  - id: <agent-id>
    role: <이 워크플로우에서의 역할>

# 워크플로우 전체 입력
inputs:
  - name: <입력 이름>
    type: <text|file_path|yaml|json>
    required: true
    description: <설명>

# 워크플로우 최종 출력
outputs:
  - name: <출력 이름>
    type: <text|file_path|yaml|json>
    description: <설명>

# 실행 단계 정의
steps:
  - step_id: <step-001>
    name: <단계 이름>
    agent: <agent-id>
    inputs_from:
      - source: workflow_input    # workflow_input | <step-id>
        field: <필드 이름>
    outputs_to:
      - target: <step-id>|workflow_output
        field: <필드 이름>
    on_failure: <retry|escalate|halt>

# Human-in-the-Loop 포인트
hitl_points:
  - after_step: <step-id>
    reason: <왜 사람 확인이 필요한지>

tags: []

changelog:
  - version: 1.0.0
    date: <YYYY-MM-DD>
    note: 최초 등록
```

---

## 필수 필드

- `id`, `name`, `version`, `status`
- `pattern`
- `agents_required`
- `steps` (최소 1개)
- `inputs`, `outputs`

---

## Workflow 디렉터리 구조

```
Workflows/<workflow-name>/
  ├── workflow.yaml   ← 이 스키마를 따르는 정의 파일
  └── README.md       ← 실행 방법, 단계별 설명, 예시
```

---

## TODO

Graph 패턴의 조건부 라우팅 스키마 추가.
워크플로우 실행 이력 연결 방식 정의.
