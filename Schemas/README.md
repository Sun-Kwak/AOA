# Schemas

## Purpose

AOA의 모든 재사용 가능한 자산이 따라야 하는 표준 구조를 정의한다.
이 스키마를 따라야 Registry에 등록하고 다른 프로젝트에서 재사용할 수 있다.

---

## Scope

| 파일 | 대상 자산 | 저장 위치 |
|------|-----------|-----------|
| `Agent.md` | 에이전트 정의 | `Agents/<name>/agent.yaml` |
| `Tool.md` | 툴 정의 | `Tools/<name>/tool.yaml` |
| `Workflow.md` | 워크플로우 정의 | `Workflows/<name>/workflow.yaml` |
| `Capability.md` | Capability 정의 | `Capabilities/<name>/capability.yaml` |
| `Template.md` | 프로젝트 템플릿 정의 | `Templates/<cat>/<name>/template.yaml` |
| `Project.md` | 프로젝트 manifest | `Projects/<name>/manifest.yaml` |

---

## 사용 방법

새 자산을 만들 때:

1. 해당 스키마 파일을 연다.
2. Schema 섹션의 YAML을 복사한다.
3. 필수 필드를 채운다.
4. `Registry/INDEX.md`에 등록한다.

---

## TODO

스키마 자동 검증 규칙 추가.
