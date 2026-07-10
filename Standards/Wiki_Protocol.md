# Wiki Protocol

## Purpose

AI가 작업 전 Wiki를 조회하고, 작업 후 Wiki를 업데이트하는 규칙을 정의한다.

LLM Wiki는 AI의 누적 학습 시스템이며, 같은 실수를 반복하지 않기 위한 핵심 메커니즘이다.

---

## Scope

이 프로토콜은 **모든 AOA 작업**에 적용된다.

Wiki 조회와 업데이트는 선택이 아닌 **의무**다.

---

## 3-Tier Wiki 구조

AOA는 역할별로 분리된 3계층 Wiki 구조를 사용한다:

### Tier 1: Root Wiki
- **위치**: `Memory/Wiki/`
- **담당**: Root Agent (AOA 프레임워크 관리자)
- **내용**: 프로젝트 생성, 에이전트 생성, Registry 관리, 세션 관리

### Tier 2: 프로젝트 Wiki
- **위치**: `Projects/<id>/Memory/wiki/`
- **담당**: Project Agent (프로젝트 오케스트레이터)
- **내용**: 워크플로우 실행, 에이전트 조율, 출력 처리

### Tier 3: 에이전트 Wiki
- **위치**: `Agents/<id>/memory/wiki/`
- **담당**: 공용 에이전트 (재사용 가능 에이전트)
- **내용**: 실행 패턴, API 에러, 출력 형식, 입력 검증

**원칙**: 각 계층은 자신의 Wiki만 읽고 쓴다. 상위 계층 Wiki는 참조 가능.

---

## 작업 시작 전: Wiki 조회 (필수)

작업 요청이 들어오면 즉시 **자신의 계층** Wiki 문서를 읽는다:

### Root Agent Wiki
| 작업 유형 | 조회할 Wiki 문서 |
|-----------|-----------------|
| 프로젝트 생성 | `Memory/Wiki/project_creation.md` |
| 에이전트 생성 | `Memory/Wiki/agent_creation.md` |
| 세션 생성 | `Memory/Wiki/session_management.md` |
| Registry 수정 | `Memory/Wiki/registry_management.md` |

### Project Agent Wiki
| 작업 유형 | 조회할 Wiki 문서 |
|-----------|-----------------|
| 워크플로우 실행 | `Projects/<id>/Memory/wiki/workflow_execution.md` |
| 에이전트 조율 | `Projects/<id>/Memory/wiki/agent_coordination.md` |
| 출력 처리 | `Projects/<id>/Memory/wiki/output_handling.md` |

### Agent Wiki
| 작업 유형 | 조회할 Wiki 문서 |
|-----------|-----------------|
| 실행 패턴 | `Agents/<id>/memory/wiki/execution_patterns.md` |
| API 에러 | `Agents/<id>/memory/wiki/api_errors.md` |
| 출력 형식 | `Agents/<id>/memory/wiki/output_formats.md` |

### 조회 절차

1. **Wiki 문서 전체 읽기**
2. **기록된 실수 패턴 확인**
3. **회피 전략 적용**
4. **체크리스트 검증**
5. **작업 시작**

Wiki 조회 없이 작업을 시작하면 안 된다.

---

## 작업 완료 후: Wiki 업데이트 (필수)

작업 중 새로운 실수나 해결책을 발견하면 **즉시** 해당 Wiki 문서에 추가한다.

### 업데이트 포맷

```markdown
## [Pattern-XXX] 패턴 이름

**발생일**: YYYY-MM-DD
**상황**: 어떤 상황에서 발생했는가
**실수**: 무엇을 잘못했는가
**결과**: 어떤 문제가 생겼는가
**회피전략**: 다음부턴 어떻게 해야 하는가

---
```

### 업데이트 기준

다음의 경우 Wiki에 기록한다:

- ✅ 같은 실수를 2회 이상 반복
- ✅ 사용자가 명시적으로 지적한 실수
- ✅ 디버깅에 1시간 이상 소요된 문제
- ✅ 명확한 회피 전략이 있는 경우

---

## Wiki 작성 원칙

### 1. 구체성 우선

❌ 나쁜 예: "프로젝트 생성 시 주의한다"  
✅ 좋은 예: "AOA/Projects/<id>/ 내부에만 생성. ~/project/ 금지"

### 2. 실행 가능한 회피 전략

❌ 나쁜 예: "더 주의 깊게 확인한다"  
✅ 좋은 예: "작업 전 `pwd` 명령으로 경로 확인. `/Users/sun/project/AOA`가 아니면 작업 중단"

### 3. 체크리스트 형태

회피 전략은 가능한 체크리스트로 작성한다:

```markdown
- [ ] 항목 1 확인
- [ ] 항목 2 확인
- [ ] 항목 3 확인
```

### 4. 누적식 업데이트

- 기존 패턴 삭제 금지
- 새 패턴만 추가
- 패턴 번호는 연속으로 증가 (Pattern-001, Pattern-002, ...)

---

## Wiki 문서 구조

각 Wiki 문서는 다음 구조를 따른다:

```markdown
# Wiki: <Topic>

<한 줄 설명>

---

## [Pattern-001] 패턴 이름

**발생일**: ...
**상황**: ...
**실수**: ...
**결과**: ...
**회피전략**: ...

---

## [Pattern-002] 다음 패턴

...

---

## 작업 시작 전 체크리스트

- [ ] 항목 1
- [ ] 항목 2

---

## 업데이트 이력

- YYYY-MM-DD: 초기 작성
- YYYY-MM-DD: Pattern-XXX 추가
```

---

## Root Agent 책임

Root Agent(이 세션)는 다음을 보장한다:

### 1. Wiki 조회 의무

프로젝트 생성, 에이전트 생성, 세션 생성 요청 시:

```
1. 해당 Wiki 문서 읽기
2. 과거 실수 패턴 확인
3. 회피 전략 적용
4. 체크리스트 검증
5. 작업 시작
```

### 2. Wiki 업데이트 의무

실수 발견 또는 사용자 지적 시:

```
1. 즉시 해당 Wiki 문서 열기
2. 새 Pattern 번호 부여
3. 발생일/상황/실수/결과/회피전략 기록
4. git commit
```

### 3. 패턴 준수

Wiki에 기록된 회피 전략을 **반드시** 따른다.

Wiki 조회 없이 작업하거나, Wiki 내용을 무시하면 안 된다.

---

## 기대 효과

이 프로토콜을 준수하면:

- ✅ 동일 실수 반복 방지
- ✅ 세션 간 학습 누적
- ✅ 의사결정 일관성 확보
- ✅ 사용자 만족도 향상
- ✅ 토큰 낭비 감소

---

## 예외 상황

Wiki 조회를 생략할 수 있는 유일한 경우:

- **없음**

모든 작업은 Wiki 조회로 시작한다.

---

## 업데이트 이력

- 2026-07-10: 초기 작성
