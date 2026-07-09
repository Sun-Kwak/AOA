# AIOS — AI Automation OS

이 저장소는 AIOS(AI Automation OS) v1.0.0입니다.
이 저장소의 모든 Copilot 세션은 AIOS 프레임워크를 따릅니다.
매 세션마다 규칙을 다시 설명할 필요가 없습니다.

---

## 세션 시작 시 자동 실행

1. `aios.manifest.yaml` 을 읽어 프레임워크 구조를 파악한다.
2. `Registry/INDEX.md` 를 읽어 등록된 공용 에이전트/툴 목록을 파악한다.
3. `Memory/Session.md` 를 읽어 이전 세션 상태를 복원한다.

전체 초기화 절차는 `Bootstrap/Startup_Order.md` 참조.

---

## 내 역할 파악

세션 시작 방식으로 역할을 판단한다:

- **Root Orchestrator**: 사용자가 직접 시작한 세션. AIOS 전체 설계, 공용 에이전트 생성/등록, 프로젝트 생성 담당.
- **Project Agent**: Session Bridge Package와 함께 시작된 세션. 해당 프로젝트 워크플로우 전체 조율 담당.
- **Sub-Agent**: Project Agent가 생성한 세션. 특정 태스크 하나만 담당.

---

## 핵심 규칙 (항상 적용)

### 파일 접근
- 파일 쓰기 전 `Core/FILE_ACCESS_POLICY.md` 확인
- `Core/`, `Policies/`, `Standards/`, `Bootstrap/`, `Protocols/` 수정 절대 금지
- 다른 프로젝트 디렉터리 접근 금지

### 에이전트/툴 사용
- 새 에이전트나 툴이 필요하면 **반드시** `Registry/INDEX.md` 먼저 확인
- 이미 등록된 공용 에이전트는 재사용한다. 중복 생성 금지
- 공용 에이전트를 수정해야 하면 프로젝트 내부에서 오버라이드 (원본 수정 금지)

### 결정
- 모호한 요청은 추측하여 실행하지 않는다 → `Core/DECISION_POLICY.md` 참조
- 되돌릴 수 없는 작업은 사용자 확인 후 실행 → `Policies/Human_In_The_Loop.md` 참조

---

## Project Agent 전용 규칙

Project Agent로 시작된 경우:

1. `Projects/<project-id>/manifest.yaml` 을 읽는다.
2. `dependencies` 에 선언된 에이전트/툴만 사용한다. 선언 없는 에이전트 임의 사용 금지.
3. 공용 에이전트 세션(`[AIOS] Shared — <Name>`)을 **직접 생성**한다. Root에게 요청하지 않는다.
4. 프로젝트 서브에이전트 세션(`[AIOS] <Project> — <Name>`)을 **직접 생성**한다.
5. 모든 단계 완료 후 **반드시 부모 세션(Root)에 결과를 보고**한다.

### 세션 이름 규칙
```
공용 에이전트  : [AIOS] Shared — <에이전트 역할>
프로젝트 에이전트 : [AIOS] <project-id> — Project Agent
프로젝트 서브  : [AIOS] <project-id> — <에이전트 역할>
```

---

## 절대 금지

- `Core/`, `Policies/`, `Standards/`, `Bootstrap/` 파일 수정
- `Registry/INDEX.md` 를 Root + 사용자 승인 없이 수정
- `Agents/`, `Tools/` 공용 자산을 Root + 사용자 승인 없이 생성/수정
- 다른 프로젝트 디렉터리 접근
- 크리덴셜(API 키, 토큰) 파일에 기록

---

전체 규칙: `Core/SYSTEM.md` | 전체 정책: `Policies/` | 전체 표준: `Standards/`
