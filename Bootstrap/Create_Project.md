# Create Project

## Purpose

새 프로젝트를 AIOS에 등록하고 초기 구조를 설정하는 절차를 정의한다.
이 문서를 따르면 모든 프로젝트가 동일한 구조로 시작한다.

---

## Scope

신규 프로젝트 생성 전체 흐름:
프로젝트 정의 → 의존성 선언 → 디렉터리 생성 → manifest 작성 → Registry 연결 → 세션 준비

---

## 프로젝트 생성 절차

### Step 1 — 프로젝트 정의
사용자와 다음을 확인한다:

```
- 프로젝트 이름 (ID로 사용할 영문 소문자 + 하이픈)
- 프로젝트 목적 (한 단락)
- 카테고리 (automation / assistant / document / video / social / other)
- 예상 출력물 형식
```

---

### Step 2 — 의존성 선언
필요한 에이전트와 툴을 결정한다.

1. `Registry/INDEX.md`를 확인한다.
2. 필요한 기능별로 적합한 공용 에이전트/툴을 검색한다.
3. 찾은 에이전트/툴을 사용자에게 보여주고 확인한다.
4. 없는 에이전트/툴은 신규 생성 여부를 사용자와 결정한다.
5. 확정된 의존성 목록을 작성한다.

**이 단계에서 의존성을 명확히 선언하지 않으면 프로젝트를 생성하지 않는다.**

---

### Step 3 — 디렉터리 구조 생성
`Projects/<project-id>/` 아래에 다음을 생성한다:

```
Projects/<project-id>/
  ├── manifest.yaml
  ├── README.md
  ├── Agents/          ← 프로젝트 전용 서브에이전트
  ├── Workflows/       ← 프로젝트 전용 워크플로우
  ├── Memory/
  │   ├── project.md
  │   ├── execution_state.md
  │   └── decision_log.md
  └── Outputs/
```

---

### Step 4 — Manifest 작성
`Schemas/Project.md` 스키마를 따라 `manifest.yaml`을 작성한다.

반드시 포함:
- 기본 정보 (id, name, version, description)
- `dependencies` 섹션 (Step 2에서 확정한 목록)
- `paths` 섹션
- `memory` 섹션

---

### Step 5 — Registry 연결 확인
Step 2에서 선택한 공용 에이전트/툴이 Registry에 등록되어 있는지 확인한다.
등록되어 있지 않은 경우 → Root Orchestrator + 사용자 승인 후 등록한다.

---

### Step 6 — 세션 준비
프로젝트가 생성되면:
1. `Memory/Session.md`에 새 활성 프로젝트로 기록한다.
2. 사용자에게 프로젝트 생성 완료를 알린다.
3. 첫 작업 요청을 기다린다.
4. 첫 작업이 들어오면 필요한 에이전트 세션을 온디맨드로 생성한다.

---

## 결과물 체크리스트

프로젝트 생성 완료 기준:

- [ ] `Projects/<id>/manifest.yaml` 작성 완료
- [ ] `Projects/<id>/README.md` 작성 완료
- [ ] 모든 하위 디렉터리 생성 완료
- [ ] `Memory/project.md` 초기화
- [ ] 의존성이 Registry에 등록 확인
- [ ] `Memory/Session.md` 업데이트

---

## TODO

프로젝트 템플릿 선택 단계 추가 (Templates/ 디렉터리 활용).
프로젝트 생성 시 자동 README 생성 규칙 추가.
