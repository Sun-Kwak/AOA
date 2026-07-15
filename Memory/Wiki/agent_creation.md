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

## [Pattern-002] 에이전트 prompt.md 불완전

**발생일**: 다수  
**상황**: 에이전트 프롬프트 작성 시 구조 누락  
**실수**: 실행 예시, 에러 처리, 출력 형식 누락  
**결과**: 에이전트가 실행 시 혼란스러워함

**회피전략**:
1. ✅ `Schemas/Agent.md` 스키마 참조 필수
2. ✅ prompt.md 필수 섹션:
   - Role & Responsibility
   - Input Schema (YAML 예시)
   - Execution Steps (구체적 단계)
   - Output Format (예시 포함)
   - Error Handling
   - Best Practices
   - Examples (성공 케이스)
3. ✅ API 키가 필요한 경우 명시적 환경변수 설명
4. ✅ 출력 파일 경로를 상대 경로로 명시

---

## [Pattern-003] config.yaml 필수 필드 누락

**발생일**: 다수  
**상황**: config.yaml 작성 시  
**실수**: version, tags, dependencies 누락  
**결과**: 에이전트 메타데이터 불완전

**회피전략**:
1. ✅ `Schemas/Agent.md` config 스키마 참조
2. ✅ 필수 필드:
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

---

## 작업 시작 전 체크리스트

에이전트 생성 요청이 들어오면:

- [ ] `Schemas/Agent.md` 읽음
- [ ] `Standards/Registry_Protocol.md` 읽음
- [ ] 이 Wiki 문서 읽음
- [ ] Registry에서 중복 에이전트 검색
- [ ] 에이전트 디렉터리 생성
- [ ] config.yaml 필수 필드 작성
- [ ] prompt.md 전체 섹션 작성
- [ ] README.md 작성
- [ ] **동일 response에서** Registry/INDEX.md 업데이트
- [ ] **동일 response에서** Registry/Agents/<id>.md 생성
- [ ] git commit

모든 항목을 통과해야 에이전트 생성 시작.

---

## [Pattern-004] Wiki Protocol 무시 (Wiki 조회 누락)

**발생일**: 2026-07-10 (health-fitness-cards 프로젝트 보고)  
**상황**: image-generator 에이전트 재사용 시  
**실수**: 
- Agent `memory/wiki/` 디렉터리 존재함
- Pattern-003: "워터마크 제거 필수" 규칙 명시됨
- Wiki_Protocol.md에 "작업 전 Wiki 조회 필수" 명시됨
- **그럼에도 Wiki 조회 없이 작업 시작** → 워터마크 제거 누락

**결과**:
- 같은 실수 반복
- Wiki Protocol 무용지물
- 프로젝트가 수동으로 지적해야 했음

**근본 원인**:
- Wiki 파일은 생성되지만 **Wiki 조회를 강제하는 메커니즘 없음**
- 새 세션이 Wiki 존재를 모르거나 무시 가능
- prompt.md에 "체크리스트"만 있고 강제 수단 없음

**회피전략**:
1. ✅ **강제 메커니즘 추가**: Wiki 조회를 자동화
2. ✅ 에이전트 생성 시 다음 파일 함께 생성:
   ```
   Agents/<id>/pre_execution_check.sh     # Wiki 자동 읽기 스크립트
   Agents/<id>/.session_init               # 세션 시작 훅
   ```
3. ✅ `prompt.md`에 "🚨 작업 시작 전 필수 절차" 섹션 추가:
   ```markdown
   ## 🚨 작업 시작 전 필수 절차
   
   1. **Wiki 조회 (필수)**
      ```bash
      ./pre_execution_check.sh
      ```
   
   2. **체크리스트 검증**
      - [ ] Wiki 전체 읽음
      - [ ] 과거 실수 패턴 확인
      - [ ] 회피 전략 적용
   
   3. **작업 시작**
   ```
4. ✅ `pre_execution_check.sh` 역할:
   - `memory/wiki/` 전체 문서 자동 읽기
   - 필수 패턴 자동 출력
   - 체크리스트 강제 표시
5. ✅ 기존 모든 에이전트에 소급 적용

---

## 작업 시작 전 체크리스트

에이전트 생성 요청이 들어오면:

- [ ] `Schemas/Agent.md` 읽음
- [ ] `Standards/Registry_Protocol.md` 읽음
- [ ] 이 Wiki 문서 읽음
- [ ] Registry에서 중복 에이전트 검색
- [ ] 에이전트 디렉터리 생성
- [ ] config.yaml 필수 필드 작성
- [ ] prompt.md 전체 섹션 작성 + **🚨 필수 절차 섹션** + **Reporting Protocol 섹션**
- [ ] README.md 작성
- [ ] **memory/wiki/ 디렉터리 생성** (Wiki_Protocol.md 포함)
- [ ] **pre_execution_check.sh 생성** (Wiki 자동 읽기)
- [ ] **동일 response에서** Registry/INDEX.md 업데이트
- [ ] **동일 response에서** Registry/Agents/<id>.md 생성
- [ ] git commit

모든 항목을 통과해야 에이전트 생성 시작.

---

## Pattern-005: Reporting Protocol 누락 (2026-07-15)

### 문제

account-content-collector 에이전트 실행 중 발견:
- 작업 완료 후 보고 지시를 무시
- prompt.md에 **HOW to report** 명시 없음
- 파일 생성 = 보고로 착각

**근본 원인:**
"작업 완료 후 보고"는 **모든 에이전트 범용 규칙**인데, 개별 prompt.md에만 의존.

### 영향

- 상위 에이전트가 완료 여부 모름
- 다음 작업 진행 불가
- 수동 확인 필요

### 회피 전략

**모든 에이전트 prompt.md에 Reporting Protocol 섹션 자동 주입:**

```markdown
## Reporting Protocol (All Agents Must Follow)

**Task completion is NOT complete without reporting back.**

### How to Report

Use `send_session_message` to report completion:

```python
from tools import send_session_message
import os

# Report to creator session
send_session_message(
    session_id=os.environ.get('CREATOR_SESSION_ID'),
    message=f"""
✅ Task Complete: {task_name}

**Status:** Success/Failed
**Generated Files:**
- {file_path_1}
- {file_path_2}

**Key Metrics:**
- Items processed: {count}
- Errors: {error_count}

**Critical Findings:**
- {finding_1}
- {finding_2}

**Next Steps:**
Ready for downstream processing.
"""
)
```

**Required Report Content:**
- ✅ Status (완료/실패)
- 📊 Key metrics/results
- 📁 Generated files/paths
- 🔍 Critical findings
- ⚠️ Errors/warnings

**Without this report, upstream agents cannot proceed.**
```

**적용 위치:**
- 모든 공용 에이전트
- 모든 프로젝트 에이전트
- 모든 서브 에이전트

**기존 에이전트 소급 적용:**
1. ✅ Reporting Protocol 섹션 추가
2. ✅ send_session_message 사용 예시 추가
3. ✅ 필수 보고 내용 명시

---

## 업데이트 이력

- 2026-07-10: 초기 작성 (Pattern-001 ~ 003 기록)
- 2026-07-10: Pattern-004 추가 (Wiki Protocol 강제 메커니즘)
- 2026-07-15: Pattern-005 추가 (Reporting Protocol 누락)
