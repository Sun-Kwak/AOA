# Load Framework

## Purpose

AOA 프레임워크의 모든 핵심 문서를 로드하는 절차를 정의한다.
Startup_Order의 Step 3~6을 실행하는 구체적인 지침이다.

---

## Scope

Core, Policies, Standards, Protocols 문서 로드 순서와
각 문서에서 확인해야 할 핵심 항목을 정의한다.

---

## 로드 절차

### Phase A — Core 로드

다음 순서로 읽는다. 순서를 바꾸지 않는다.

```
1. Core/BOOT.md
   확인: 부팅 조건 9가지
   완료 기준: 모든 조건 체크 가능한 상태

2. Core/SYSTEM.md
   확인: 10가지 운영 원칙
   완료 기준: 원칙 인식 완료

3. Core/ORCHESTRATOR.md
   확인: 계층 구조, 위임 규칙, 온디맨드 세션 규칙
   완료 기준: 에이전트 계층 인식 완료

4. Core/FILE_ACCESS_POLICY.md
   확인: 접근 매트릭스, 불변 디렉터리 목록
   완료 기준: 쓰기 금지 경로 인식 완료

5. Core/CONTEXT_POLICY.md
   확인: 컨텍스트 3계층, 슬라이스 규칙
   완료 기준: 컨텍스트 전달 방식 인식 완료

6. Core/EXECUTION_POLICY.md
   확인: 태스크 정의, 범위 제어, 온디맨드 세션 규칙
   완료 기준: 태스크 실행 기준 인식 완료

7. Core/DECISION_POLICY.md
   확인: 결정 레벨 4단계, 에이전트 선택 규칙
   완료 기준: 결정 기준 인식 완료

8. Core/OBSERVABILITY_POLICY.md
   확인: 기록 대상 이벤트, 로그 형식
   완료 기준: 로그 기록 기준 인식 완료
```

---

### Phase B — Policies 로드

```
1. Policies/Safety.md
   확인: 7가지 절대 금지 항목
   중요: 이 파일은 모든 다른 정책보다 우선한다

2. Policies/Human_In_The_Loop.md
   확인: 필수 pause 조건 목록

3. Policies/Approval.md
   확인: L1/L2/L3 승인 레벨

4. Policies/Retry.md
   확인: 재시도 횟수 및 에스컬레이션 기준

5. Policies/Cost_Control.md
   확인: Soft/Hard 임계값
```

---

### Phase C — Standards 로드

```
1. Standards/Naming.md
   확인: ID 규칙, 파일명 규칙, 에이전트 접미사

2. Standards/Versioning.md
   확인: MAJOR/MINOR/PATCH 기준, 버전 고정 방식

3. Standards/Prompt.md
   확인: 6단계 프롬프트 구조, 길이 가이드

4. Standards/Markdown.md
   확인: 섹션 구분, 테이블, 코드 블록 규칙
```

---

### Phase D — Protocols 로드

```
1. Protocols/Agent_Communication.md
   확인: 메시지 유형 6가지, task_id 생성 규칙

2. Protocols/Handoff.md
   확인: Delegation vs Handoff 구분, Handoff 패키지 구조

3. Protocols/Context_Passing.md
   확인: Task/Project 슬라이스 구조, 금지 항목

4. Protocols/Session_Bridge.md
   확인: Bridge 패키지 구조, 세션 초기화 절차
```

---

## 로드 완료 확인

모든 Phase가 완료되면:

- [ ] Core 8개 문서 로드 완료
- [ ] Policies 5개 문서 로드 완료
- [ ] Standards 4개 문서 로드 완료
- [ ] Protocols 4개 문서 로드 완료

완료 후 Startup_Order Step 7(Registry 인덱스 로드)로 진행한다.

---

## 로드 실패 시

어느 파일이라도 읽을 수 없으면:
1. 즉시 중단.
2. 실패한 파일 경로와 이유를 보고.
3. `Bootstrap/Recovery.md`를 따른다.

---

## TODO

로드 시간 최적화: 자주 변경되지 않는 파일은 캐싱 전략 검토.
