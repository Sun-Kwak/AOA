# Versioning

## Purpose

AIOS의 모든 버전 관리 규칙을 정의한다.
에이전트, 툴, 워크플로우 등 공용 자산이 업데이트될 때
기존 프로젝트에 미치는 영향을 예측 가능하게 만든다.

---

## Scope

공용 자산 (Agents, Tools, Workflows, Capabilities, Templates) 및
프로젝트 manifest, AIOS Framework 자체의 버전 관리에 적용된다.

---

## Semantic Versioning

모든 자산은 `MAJOR.MINOR.PATCH` 형식을 따른다.

| 버전 구분 | 변경 내용 | 예시 |
|-----------|-----------|------|
| `MAJOR` | 기존 사용 방식과 호환되지 않는 변경 | `1.0.0 → 2.0.0` |
| `MINOR` | 하위 호환을 유지하면서 기능 추가 | `1.0.0 → 1.1.0` |
| `PATCH` | 버그 수정, 문서 수정 | `1.0.0 → 1.0.1` |

---

## MAJOR 버전 변경 조건

다음 중 하나라도 해당하면 MAJOR를 올린다:

- 에이전트의 입력/출력 인터페이스 변경
- 에이전트 ID 변경
- 툴의 파라미터 구조 변경
- 워크플로우의 필수 단계 제거 또는 순서 변경
- 기존 프로젝트의 manifest를 수정해야 동작하는 변경

**MAJOR 버전 변경은 Root Orchestrator + 사용자 승인이 필요하다.**

---

## 프로젝트 manifest의 버전 고정

프로젝트 manifest의 `dependencies`에서 버전을 고정할 수 있다:

```yaml
dependencies:
  agents:
    - id: image-generation-agent
      version: "1.2.0"        # 정확한 버전 고정
      path: Agents/image-generation/

    - id: script-writer-agent
      version: "~1.1.0"       # 1.1.x 범위 허용 (PATCH만)
      path: Agents/script-writer/

    - id: youtube-upload-tool
      version: "^1.0.0"       # 1.x.x 범위 허용 (MINOR까지)
      path: Tools/youtube-upload/
```

버전을 명시하지 않으면 Registry에 등록된 최신 버전을 사용한다.

---

## 공용 자산 업데이트 절차

1. 변경 유형 파악 (MAJOR / MINOR / PATCH)
2. 변경 내용을 CHANGELOG에 기록
3. MAJOR 변경이면 사용 중인 프로젝트 목록 확인
4. Root Orchestrator가 사용자에게 영향 범위 보고
5. 사용자 승인 후 버전 업데이트
6. Registry/INDEX.md의 버전 정보 업데이트
7. 영향받는 프로젝트의 manifest 업데이트 여부 사용자와 결정

---

## AIOS Framework 버전

`aios.manifest.yaml`의 `version` 필드가 Framework 버전이다.

| 변경 유형 | 조건 |
|-----------|------|
| MAJOR | Core 문서 구조 변경, Bootstrap 절차 변경 |
| MINOR | 새 Policy 추가, 새 디렉터리 추가 |
| PATCH | 문서 수정, 오타 수정 |

---

## 버전 히스토리 기록

각 공용 자산 파일 상단에 버전 히스토리를 포함한다:

```markdown
---
version: 1.2.0
changed: 2026-07-09
changes:
  - 1.2.0: 출력 형식에 JSON 추가
  - 1.1.0: 이미지 크기 파라미터 추가
  - 1.0.0: 최초 등록
---
```

---

## TODO

자동 버전 호환성 검사 규칙 정의.
Deprecated 버전 보존 기간 정의.
