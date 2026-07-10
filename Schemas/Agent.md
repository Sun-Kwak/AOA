# Agent Schema

## Purpose

모든 AOA 에이전트 정의 파일이 따라야 하는 표준 구조를 정의한다.
이 스키마를 따라야 Registry에 등록할 수 있다.

---

## Scope

공용 에이전트 (`Agents/<name>/agent.yaml`) 및
프로젝트 에이전트 (`Projects/<name>/Agents/<name>/agent.yaml`) 모두에 적용된다.

---

## Agent Schema

```yaml
# Agents/<agent-name>/agent.yaml
# Standards/Naming.md: ID는 kebab-case, -agent 접미사 필수

id: <agent-id>                    # 예: script-writer-agent
name: <Display Name>              # 예: Script Writer Agent
version: 1.0.0
status: active                    # active | deprecated

role: >
  이 에이전트가 무엇을 하는지 한 문장.

# 이 에이전트가 사용하는 Capability ID 목록
capabilities:
  - <capability-id>

# 입력 정의
inputs:
  - name: <입력 이름>
    type: <text|file_path|yaml|json>
    required: true
    description: <설명>

# 출력 정의
outputs:
  - name: <출력 이름>
    type: <text|file_path|yaml|json>
    path: <저장 경로 패턴 — 없으면 null>
    description: <설명>

# 의존성
dependencies:
  agents: []                      # 협업 에이전트 ID 목록
  tools: []                       # 사용 툴 ID 목록

# 메모리 (선택사항 - 공용 에이전트에 권장)
memory:
  wiki: Agents/<name>/memory/wiki/  # 에이전트별 학습 Wiki
  executions: Agents/<name>/memory/executions/  # 실행 기록 (선택)

# 프롬프트 파일 경로 (Standards/Prompt.md 형식 준수)
prompt_path: Agents/<name>/prompt.md

# 이 에이전트에만 적용되는 제약 (AOA Core 규칙은 포함하지 않음)
constraints: []

# Registry 검색용 태그
tags: []

# 버전 히스토리
changelog:
  - version: 1.0.0
    date: <YYYY-MM-DD>
    note: 최초 등록
```

---

## 필수 필드

등록 시 반드시 있어야 하는 필드:
- `id`, `name`, `version`, `status`
- `role`
- `inputs`, `outputs`
- `prompt_path`

---

## Agent 디렉터리 구조

```
Agents/<agent-name>/
  ├── agent.yaml      ← 이 스키마를 따르는 정의 파일
  ├── prompt.md       ← Standards/Prompt.md 형식의 프롬프트
  └── README.md       ← 사용 방법 및 예시
```

---

## TODO

에이전트 테스트 케이스 필드 추가.
에이전트 성능 메트릭 필드 추가.
