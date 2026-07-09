# Context Passing

## Purpose

CONTEXT_POLICY에서 정의한 규칙을 실제 전달 가능한 구조로 구체화한다.
"무엇을 전달하는가"의 규칙은 CONTEXT_POLICY에,
"어떤 형식으로 전달하는가"는 이 문서에 있다.

---

## Scope

모든 에이전트 간 컨텍스트 전달에 적용된다.
세션 내 전달과 세션 간 전달(Session Bridge) 모두 포함한다.

---

## Task Context Slice 구조

위임 시 전달하는 기본 컨텍스트 패키지:

```yaml
# Task Context Slice
context_tier: task                  # framework | project | task

task_id: <task_id>
agent_role: <받는 에이전트의 역할>
task_scope: <태스크 한 줄 설명>

inputs:
  - key: <입력 이름>
    value: <값 또는 파일 경로>
    type: <text|file_path|reference>

constraints:
  - <이 태스크에만 적용되는 제약>

memory_slice:                       # 이 태스크에 필요한 메모리만 발췌
  relevant_decisions: []            # 관련 이전 결정 (없으면 빈 배열)
  relevant_state: null              # 관련 실행 상태 (없으면 null)

framework_note: >
  AOA Core 규칙 및 Policies가 적용됩니다.
  전체 Framework 문서는 Root Orchestrator가 보유합니다.
```

---

## Project Context Slice 구조

Project Agent가 Sub-Agent에게 전달하는 프로젝트 컨텍스트:

```yaml
# Project Context Slice
context_tier: project

project_id: <project-id>
project_manifest_path: Projects/<name>/manifest.yaml
active_workflow: <워크플로우 ID 또는 null>

dependencies_summary:
  - id: <agent-id>
    role: <역할>

memory_slice:
  project_goal: <프로젝트 목표 한 줄>
  current_phase: <현재 단계>
  relevant_decisions: []
```

---

## 컨텍스트 전달 금지 항목

다음은 어떤 컨텍스트 슬라이스에도 포함하지 않는다:

```yaml
# 절대 포함 금지
forbidden:
  - type: credentials
    examples: [api_key, token, password, secret]

  - type: full_framework
    examples: [Core 파일 전체, Policies 파일 전체]

  - type: other_project_memory
    examples: [다른 프로젝트의 project.md, decision_log.md]

  - type: unrelated_task_results
    examples: [이 태스크와 무관한 이전 태스크 결과]

  - type: full_registry
    examples: [Registry 전체 내용 — ID 참조만 허용]
```

---

## 컨텍스트 요청 포맷

Sub-Agent가 추가 컨텍스트가 필요할 때:

```yaml
type: context_request
task_id: <task_id>
from: <요청하는 에이전트>
to: <상위 에이전트>
timestamp: <ISO 8601>

needs:
  - item: <필요한 정보 설명>
    reason: <왜 필요한지>
```

상위 에이전트는 요청 범위를 확인하고 허용된 항목만 제공한다.

---

## 컨텍스트 크기 가이드

| 컨텍스트 유형 | 목표 크기 |
|--------------|-----------|
| Task Context Slice | 200~400자 |
| Project Context Slice | 300~600자 |
| Memory Slice | 100~300자 (핵심만) |
| Framework Note | 50자 이내 (고정 문구) |

목표 크기를 초과하면 내용을 줄이거나 파일 경로 참조로 대체한다.

---

## TODO

컨텍스트 슬라이스 자동 생성 템플릿 추가.
컨텍스트 크기 초과 시 압축 규칙 정의.
