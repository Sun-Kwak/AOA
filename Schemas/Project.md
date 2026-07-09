# Project Schema

## Purpose

모든 AIOS 프로젝트가 따라야 하는 manifest 구조를 정의한다.
프로젝트 manifest는 프로젝트의 선언서이다.
무엇을 하는 프로젝트인지, 어떤 에이전트/툴을 사용하는지,
어디에 무엇이 있는지를 한 파일에서 알 수 있어야 한다.

---

## Scope

이 스키마는 모든 프로젝트의 `Projects/<name>/manifest.yaml`에 적용된다.

---

## Manifest Schema

```yaml
# Projects/<project-name>/manifest.yaml

# ── 기본 정보 ──────────────────────────────────────────
id: <unique-project-id>            # 영문 소문자, 하이픈 허용
name: <Human readable name>
version: 1.0.0
status: active                     # active | paused | archived

description: >
  이 프로젝트가 무엇을 하는지 한 단락으로.

created_at: <ISO 8601>
updated_at: <ISO 8601>

# ── 디렉터리 구조 ──────────────────────────────────────
paths:
  root: Projects/<project-name>/
  agents: Projects/<project-name>/Agents/
  workflows: Projects/<project-name>/Workflows/
  memory: Projects/<project-name>/Memory/
  outputs: Projects/<project-name>/Outputs/

# ── 의존성 선언 (핵심) ────────────────────────────────
# 런타임에 사용할 에이전트와 툴을 여기에 선언한다.
# 선언되지 않은 에이전트/툴은 이 프로젝트에서 사용할 수 없다.
dependencies:
  agents:
    - id: <agent-id>               # Registry/Agents/ 에 등록된 ID
      path: Agents/<agent-name>/   # 공용 에이전트 경로
      role: <이 프로젝트에서의 역할>
      override: null               # 오버라이드 파일 경로 (없으면 null)

    # 오버라이드 예시
    - id: image-generation-agent
      path: Agents/image-generation/
      role: 썸네일 이미지 생성
      override: Projects/<name>/Agents/image-generation-override/

  tools:
    - id: <tool-id>                # Registry/Tools/ 에 등록된 ID
      path: Tools/<tool-name>/
      role: <이 프로젝트에서의 역할>

  project_agents:                  # 이 프로젝트 전용 서브에이전트
    - id: <project-agent-id>
      path: Projects/<name>/Agents/<agent-name>/
      role: <역할>

# ── 워크플로우 ────────────────────────────────────────
workflows:
  default: Projects/<name>/Workflows/main.md
  available:
    - id: <workflow-id>
      path: Projects/<name>/Workflows/<name>.md
      description: <한 줄 설명>

# ── 메모리 설정 ───────────────────────────────────────
memory:
  project_memory: Projects/<name>/Memory/project.md
  execution_state: Projects/<name>/Memory/execution_state.md
  decision_log: Projects/<name>/Memory/decision_log.md

# ── 출력 설정 ─────────────────────────────────────────
outputs:
  default_path: Projects/<name>/Outputs/
  format: markdown                 # markdown | yaml | json | mixed

# ── 태그 및 분류 ──────────────────────────────────────
tags: [tag1, tag2]
category: <automation | assistant | document | video | social | other>
```

---

## 필수 필드

manifest.yaml에서 반드시 있어야 하는 필드:

- `id`
- `name`
- `version`
- `status`
- `description`
- `paths.root`
- `dependencies` (비어있어도 선언은 해야 함)

---

## 의존성 선언 규칙

1. 런타임에 사용할 모든 공용 에이전트와 툴은 반드시 `dependencies`에 선언한다.
2. 선언되지 않은 에이전트/툴은 사용 금지.
3. 새 에이전트/툴이 필요하면 먼저 Registry를 검색하고,
   결정 후 manifest의 `dependencies`에 추가한 뒤 사용한다.
4. 공용 에이전트를 커스터마이즈할 때는 `override` 경로를 지정한다.
   원본 에이전트(`path`)는 수정하지 않는다.

---

## TODO

manifest.yaml 자동 검증 규칙 정의.
dependencies 버전 고정 규칙 추가.
