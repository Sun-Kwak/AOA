# Wiki: Agent Creation

에이전트 생성 시 반복된 실수와 회피 전략.

---

## [Pattern-001] Registry 업데이트 누락

**발생일**: 2026-07-09 (사용자 명시적 지적: "알잘딱깔센 안돼?")  
**상황**: 새 에이전트(image-generator) 생성 완료 후  
**실수**: Registry/INDEX.md 업데이트 안함, Registry/Agents/<id>.md 생성 안함  
**결과**: 
- 에이전트가 Registry에 보이지 않음
- 다른 프로젝트가 해당 에이전트 발견 못함
- 사용자가 수동으로 지적해야 했음

**회피전략**:
1. ✅ **절대 규칙**: 에이전트 생성과 Registry 업데이트는 **원자적 작업**
2. ✅ 에이전트 생성 시 필수 3단계:
   ```
   1. Agents/<id>/ 디렉터리 + 파일 생성
   2. Registry/INDEX.md 업데이트 (동일 response)
   3. Registry/Agents/<id>.md 생성 (동일 response)
   ```
3. ✅ `Standards/Registry_Protocol.md` 참조 필수
4. ✅ 같은 response에서 모든 파일 생성 (나중에 업데이트 X)

---

## [Pattern-DOC] Document Quality & Schema Compliance

**통합**: Pattern-002 (prompt.md 불완전) + Pattern-003 (config.yaml 누락)  
**범주**: 문서 품질 (Documentation Quality)  
**발생일**: 다수

### 문제

#### 실수 A: 에이전트 prompt.md 불완전
**상황**: 에이전트 프롬프트 작성 시 구조 누락  
**실수**: 실행 예시, 에러 처리, 출력 형식 누락  
**결과**: 에이전트가 실행 시 혼란스러워함

#### 실수 B: config.yaml 필수 필드 누락
**상황**: config.yaml 작성 시  
**실수**: version, tags, dependencies 누락  
**결과**: 에이전트 메타데이터 불완전

### 회피 전략

#### 1. Schemas/Agent.md 스키마 참조 필수

#### 2. prompt.md 필수 섹션
- Role & Responsibility
- Input Schema (YAML 예시)
- Execution Steps (구체적 단계)
- Output Format (예시 포함)
- Error Handling
- Best Practices
- Examples (성공 케이스)
- 🚨 필수 절차 섹션 (Wiki Protocol)
- 🚨 Access Control 섹션
- Reporting Protocol 섹션

#### 3. config.yaml 필수 필드
```yaml
id: <kebab-case>
name: <Human Readable>
version: 1.0.0
role: <한 줄 역할>
category: <적절한 카테고리>
tags: [tag1, tag2]
dependencies:
  tools: [...]
  external_apis: [...]
```

#### 4. API 키가 필요한 경우 명시적 환경변수 설명

#### 5. 출력 파일 경로를 상대 경로로 명시

---

## [Pattern-005] Reporting Protocol 누락

**발생일**: 2026-07-15  
**상황**: account-content-collector 에이전트 실행 중 발견

### 문제

- 작업 완료 후 보고 지시를 무시
- prompt.md에 **HOW to report** 명시 없음
- 파일 생성 = 보고로 착각

**근본 원인:**
"작업 완료 후 보고"는 **모든 에이전트 범용 규칙**인데, 개별 prompt.md에만 의존.

### 회피 전략

**모든 에이전트 prompt.md에 Reporting Protocol 섹션 필수:**

```markdown
## Reporting Protocol

**Task completion is NOT complete without reporting back.**

Use send_session_message to report completion with:
- ✅ Status (완료/실패)
- 📊 Key metrics/results
- 📁 Generated files/paths
- 🔍 Critical findings
- ⚠️ Errors/warnings
```

---

## 범용 Pattern (공통 적용)

### Pattern-WIKI: Wiki Protocol Enforcement
→ `Memory/Wiki/universal_patterns.md` 참조

**요약:**
- 작업 시작 전 pre_execution_check.sh 실행 필수
- memory/wiki/ 전체 읽기
- 과거 실수 패턴 확인

### Pattern-AUTH: Access Control & Authority Protocol
→ `Memory/Wiki/universal_patterns.md` 참조

**요약:**
- 공용 에이전트는 Projects/ 수정 금지
- 프로젝트 파일 변경 필요 시 프로젝트 에이전트에 메시지
- 권한 밖 작업 = send_session_message

---

## 작업 시작 전 체크리스트

에이전트 생성 요청이 들어오면:

- [ ] `Schemas/Agent.md` 읽음
- [ ] `Standards/Registry_Protocol.md` 읽음
- [ ] `Memory/Wiki/universal_patterns.md` 읽음
- [ ] 이 Wiki 문서 읽음
- [ ] Registry에서 중복 에이전트 검색
- [ ] 에이전트 디렉터리 생성
- [ ] config.yaml 필수 필드 작성
- [ ] prompt.md 전체 섹션 작성 (필수 절차 + Access Control + Reporting)
- [ ] README.md 작성
- [ ] memory/wiki/ 디렉터리 생성
- [ ] pre_execution_check.sh 생성
- [ ] **동일 response에서** Registry/INDEX.md 업데이트
- [ ] **동일 response에서** Registry/Agents/<id>.md 생성
- [ ] git commit

---

## 업데이트 이력

- 2026-07-10: 초기 작성
- 2026-07-15: **v2.0 통합** - 6개 → 3개 + 2개 범용 분리
  - Pattern-002 + 003 → Pattern-DOC
  - Pattern-004 → Pattern-WIKI (universal로 이동)
  - Pattern-008 → Pattern-AUTH (universal로 이동)
