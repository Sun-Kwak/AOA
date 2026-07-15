# CHANGELOG

All notable changes to this project will be documented in this file.

---

## v2.0.2 - GitHub Copilot Instructions & Workflow Enforcement (2026-07-15)

### Added
- **Pattern-WORKFLOW**: Workflow Enforcement (프로젝트 실행 규칙)
  - Workflows/*.md Phase 순서 필수 준수
  - 각 Phase의 Agent 건너뛰기 금지
  - 사용자 "직접 실행" 요청에도 워크플로우 우선
  - 위치: `Memory/Wiki/project_creation.md`

### Changed
- **.github/copilot-instructions.md 대폭 간소화**
  - 281줄 → 107줄 (-62%)
  - v1.0.0 낡은 규칙 제거 (Registry/INDEX.md 전체 읽기 등)
  - v2.0.1 규칙 반영 (Pattern-AUTH Agent Invocation)
  - 상세 규칙은 Memory/Wiki/로 위임
  - 역할: GitHub Copilot "입구"로 간소화

### Why
- health-fitness-cards 테스트 중 워크플로우 무시 실수 발견
- Markdown 파일만으로 통제 한계 → GitHub 공식 설정 활용
- .github/copilot-instructions.md = 자동 로드, 강제 적용
- Memory/Wiki/ = 상세 패턴, 실수 사례

### Files
- Modified: `Memory/Wiki/project_creation.md` (+90줄, Pattern-WORKFLOW 추가)
- Modified: `.github/copilot-instructions.md` (-174줄, v2.0.1 간소화)
- Backup: `.github/copilot-instructions.md.v1.backup` (v1.0.0 보존)

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
