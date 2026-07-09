# Observability

## Purpose

AIOS에서 발생하는 모든 이벤트의 기록을 저장한다.
이 디렉터리가 있어야 추적, 디버깅, 재현, 감사가 가능하다.

---

## Scope

| 파일 | 내용 |
|------|------|
| `execution.log.md` | 태스크 실행 이력 (시작/완료/위임) |
| `error.log.md` | 실패, Recovery, 에러 이력 |
| `audit.log.md` | 파일 접근/수정, Policy 위반 시도 이력 |

로그 형식은 `Core/OBSERVABILITY_POLICY.md`를 따른다.

---

## 규칙

- 로그는 추가(append)만 허용. 수정/삭제 금지.
- 크리덴셜은 절대 기록하지 않는다.
- 에이전트 신원을 항상 명시한다.

---

## TODO

로그 보존 기간 및 아카이빙 규칙 추가.
