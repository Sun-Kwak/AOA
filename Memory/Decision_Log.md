# Decision Log

## Purpose

프레임워크 레벨의 Level 2 이상 결정을 기록한다.
추가(append)만 허용. 수정 및 삭제 금지.
일관성 유지와 감사 추적을 위해 사용된다.

---

## Scope

Root Orchestrator의 Level 2 이상 결정.
프로젝트 범위 결정은 `Projects/<name>/Memory/decision_log.md`에 기록.

---

## Entry Format

```
---
timestamp : <ISO 8601>
agent     : <결정한 에이전트 ID>
level     : <2 | 3 | 4>
context   : <어떤 상황이었는지>
decision  : <무엇을 결정했는지>
reasoning : <왜 이 결정을 했는지>
outcome   : <결과 — 완료 후 업데이트>
---
```

---

## Log

<!-- 결정 엔트리는 아래에 추가 (append-only) -->

---
timestamp : 2026-07-09
agent     : root
level     : 2
context   : AOA 초기 구조 설계
decision  : 프레임워크 메모리와 프로젝트 메모리를 분리하는 하이브리드 구조 채택
reasoning : FILE_ACCESS_POLICY에 따라 Project Agent는 자신의 프로젝트 메모리만
            접근 가능해야 하며, Root는 전체 인덱스만 필요하기 때문.
outcome   : Memory/ (전역 요약) + Projects/<name>/Memory/ (프로젝트 상세) 구조 확정
---

