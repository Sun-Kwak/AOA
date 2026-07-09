# OBSERVABILITY POLICY

## Purpose

AIOS 내에서 발생하는 모든 유의미한 이벤트의 기록 기준을 정의한다.
무엇을, 어디에, 어떤 형식으로 기록할지를 규정한다.
이 정책이 있어야 추적, 디버깅, 재현, 감사가 가능하다.

---

## Scope

모든 에이전트(Root, Project Agent, Shared Agent, Sub-Agent)의
모든 유의미한 행동에 적용된다.

---

## 기록 대상 이벤트

### 반드시 기록해야 하는 이벤트

| 이벤트 | 기록 위치 |
|--------|-----------|
| 에이전트 세션 시작/종료 | `Observability/` 실행 로그 |
| 태스크 시작 | `Observability/` 실행 로그 |
| 태스크 완료 | `Observability/` 실행 로그 |
| 태스크 실패 | `Observability/` 에러 로그 |
| 파일 생성/수정/삭제 | `Observability/` 감사 로그 |
| 외부 API 호출 | `Observability/` 실행 로그 |
| Recovery 이벤트 | `Observability/` 에러 로그 |
| Safety/Policy 위반 시도 | `Observability/` 감사 로그 |
| Level 2 이상 결정 | `Memory/Decision_Log.md` |
| 에이전트 위임 | `Observability/` 실행 로그 |

### 기록하지 않아도 되는 이벤트

- 읽기 전용 파일 접근
- Level 1 자율 결정
- 내부 컨텍스트 슬라이스 생성

---

## 로그 파일 구조

```
Observability/
  ├── execution.log.md    ← 태스크 실행 이력
  ├── error.log.md        ← 실패 및 Recovery 이력
  └── audit.log.md        ← 파일 접근/수정 및 Policy 위반 이력
```

---

## 로그 엔트리 형식

모든 로그 엔트리는 다음 형식을 따른다:

```
---
timestamp : <ISO 8601>
agent     : <에이전트 ID 또는 Root>
event     : <이벤트 유형>
target    : <대상 파일, 태스크, 에이전트>
result    : <success | failure | partial | blocked>
detail    : <한 줄 설명>
---
```

### 예시 — 태스크 완료

```
---
timestamp : 2026-07-09T13:00:00+09:00
agent     : kids-video-gen/script-writer-agent
event     : task.complete
target    : task-001 (유튜브 스크립트 생성)
result    : success
detail    : 3분짜리 어린이 영상 스크립트 생성 완료. 출력: Outputs/script-001.md
---
```

### 예시 — Safety 위반 시도

```
---
timestamp : 2026-07-09T13:05:00+09:00
agent     : kids-video-gen/script-writer-agent
event     : policy.violation.attempt
target    : Core/SYSTEM.md
result    : blocked
detail    : Framework 파일 수정 시도 감지. FILE_ACCESS_POLICY에 의해 차단.
---
```

---

## 기록 원칙

1. **기록은 실행과 동시에** — 완료 후 나중에 쓰지 않는다.
2. **실패도 기록** — 성공한 것만 기록하지 않는다.
3. **에이전트 신원 명시** — 누가 한 일인지 항상 기록한다.
4. **로그 파일 자체는 수정 금지** — 추가(append)만 허용. 기존 로그 삭제/수정 불가.
5. **크리덴셜 기록 금지** — API 키, 토큰, 패스워드는 로그에 포함하지 않는다.

---

## 로그 조회 (Replay)

특정 시점의 실행 상태를 재현하려면:

1. `Observability/execution.log.md`에서 해당 태스크의 시작~완료 엔트리를 찾는다.
2. 각 단계에서 어떤 에이전트가 무엇을 했는지 순서대로 확인한다.
3. 실패 지점은 `Observability/error.log.md`에서 확인한다.
4. 파일 변경 이력은 `Observability/audit.log.md`에서 확인한다.

---

## 프로젝트별 로그

프로젝트 전용 상세 로그는 프로젝트 디렉터리에도 기록한다:

```
Projects/<name>/Memory/execution_state.md  ← 현재 실행 상태
Projects/<name>/Memory/decision_log.md     ← 프로젝트 범위 결정 이력
```

AIOS 레벨 `Observability/`는 전체 이력,
프로젝트 레벨 Memory는 현재 상태에 집중한다.

---

## Observability 로그 초기화

`Observability/` 하위 3개 파일이 없으면 AIOS 부팅 시 자동 생성한다.
로그 파일이 없는 상태에서 이벤트가 발생하면 생성 후 기록한다.

---

## TODO

로그 보존 기간 및 아카이빙 규칙 정의.
로그 기반 자동 알림 규칙 정의.
프로젝트별 로그 집계 방식 정의.
