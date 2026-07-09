# Capability Schema

## Purpose

모든 AOA Capability 정의 파일이 따라야 하는 표준 구조를 정의한다.
Capability는 에이전트를 구성하는 가장 작은 재사용 단위다.
하나의 Capability는 하나의 원자적 행동만 수행한다.

---

## Scope

공용 Capability (`Capabilities/<name>/capability.yaml`) 모두에 적용된다.

---

## Capability Schema

```yaml
# Capabilities/<capability-name>/capability.yaml
# Standards/Naming.md: ID는 kebab-case, -capability 접미사 필수

id: <capability-id>               # 예: text-summarize-capability
name: <Display Name>
version: 1.0.0
status: active

description: >
  이 Capability가 하는 단일 행동 한 문장.

# 단일 행동 유형
action: <generate|transform|extract|validate|classify|search>

# 입력
inputs:
  - name: <입력 이름>
    type: <text|file_path|yaml|json>
    required: true
    description: <설명>

# 출력
outputs:
  - name: <출력 이름>
    type: <text|file_path|yaml|json>
    description: <설명>

# 이 Capability를 사용하는 에이전트 목록 (역참조)
used_by_agents: []

tags: []

changelog:
  - version: 1.0.0
    date: <YYYY-MM-DD>
    note: 최초 등록
```

---

## Capability vs Agent

| 구분 | Capability | Agent |
|------|-----------|-------|
| 크기 | 원자적 (1개 행동) | 복합 (여러 Capability 조합) |
| 상태 | 항상 Stateless | 가급적 Stateless |
| 재사용 | 여러 Agent에서 공유 | 역할 단위로 재사용 |

---

## Capability 디렉터리 구조

```
Capabilities/<capability-name>/
  ├── capability.yaml ← 이 스키마를 따르는 정의 파일
  └── README.md
```

---

## TODO

Capability 조합 규칙 정의.
Capability 테스트 케이스 필드 추가.
