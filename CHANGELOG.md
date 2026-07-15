# CHANGELOG

All notable changes to this project will be documented in this file.

---

## v2.0.1 - Agent Invocation Rules (2026-07-15)

### Added
- **Pattern-AUTH 확장**: Agent Invocation Method by Type
  - 공용 에이전트: `create_session`으로만 호출 (task 금지)
  - 프로젝트 전용 에이전트: `task` 또는 `create_session` 선택 가능
  - 이유: 세션 추적, 재사용성, 지속적 상호작용

### Why
- health-fitness-cards 프로젝트 테스트 중 발견
- 공용 에이전트를 `task`로 호출하는 실수 발생
- 규칙이 명시되지 않아 반복 가능성 있음

### Files
- Modified: `Memory/Wiki/universal_patterns.md` (Pattern-AUTH 섹션 확장)

---

## v2.0.0 - Pattern Consolidation (2026-07-15)

### Breaking Changes
- **Pattern 통합**: 14개 → 8개 (43% 감소)
- **Wiki 구조 개편**: 범용 Pattern 분리

### Pattern Migration Map

| 구 Pattern | 신 Pattern | 비고 |
|-----------|-----------|------|
| agent-002, agent-003 | Pattern-DOC | Document Quality 통합 |
| agent-004, project-006 | Pattern-WIKI | Universal로 분리 |
| agent-008, project-008 | Pattern-AUTH | Universal로 분리 |
| project-001, project-002 | Pattern-PROC | Procedure 통합 |
| project-003, project-004 | Pattern-DOC | Document Quality 통합 |

### New Structure

**agent_creation.md (3개 + 2개 범용 참조):**
1. Pattern-001: Registry 업데이트 누락
2. Pattern-DOC: Document Quality
3. Pattern-005: Reporting Protocol
4. → Pattern-WIKI (universal 참조)
5. → Pattern-AUTH (universal 참조)

**project_creation.md (4개 + 2개 범용 참조):**
1. Pattern-PROC: Procedure
2. Pattern-DOC: Document Quality
3. Pattern-005: 불필요한 자동 실행
4. Pattern-007: Registry INDEX 로딩
5. → Pattern-WIKI (universal 참조)
6. → Pattern-AUTH (universal 참조)

**universal_patterns.md (2개, 새 파일):**
1. Pattern-WIKI: Wiki Protocol Enforcement
2. Pattern-AUTH: Access Control & Authority Protocol

**Total: 8개 독립 Pattern** (기존 14개 → 43% 감소)

### Files
- Added: `Memory/Wiki/universal_patterns.md`
- Modified: `Memory/Wiki/agent_creation.md`
- Modified: `Memory/Wiki/project_creation.md`
- Backup: `*.backup-20260715`

### Purpose
- ✅ Pattern 복잡도 감소 (할루시네이션 방지)
- ✅ 범용 규칙 명확화 (WIKI, AUTH)
- ✅ 중복 제거 (Document Quality, Procedure)
- ✅ 프로젝트 시작 전 정리 완료

---

## Earlier Versions

All changes prior to v2.0.0 are documented in individual Wiki files.
