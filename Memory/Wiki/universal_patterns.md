# Wiki: Universal Patterns

모든 에이전트와 프로젝트에 공통 적용되는 범용 Pattern.

---

## [Pattern-WIKI] Wiki Protocol Enforcement

**범주**: 강제 메커니즘 (Enforcement)  
**대상**: 모든 공용 에이전트, 모든 프로젝트 에이전트  
**발생일**: 2026-07-10

### 문제

**상황**: 에이전트/프로젝트 재사용 시  
**실수**: 
- Agent `memory/wiki/` 디렉터리 존재함
- 과거 실수 패턴 명시됨
- **그럼에도 Wiki 조회 없이 작업 시작** → 같은 실수 반복

**결과**:
- Wiki Protocol 무용지물
- 매 세션마다 동일한 실수 반복
- 프로젝트가 수동으로 지적해야 했음

**근본 원인**:
- Wiki 파일은 생성되지만 **Wiki 조회를 강제하는 메커니즘 없음**
- 새 세션이 Wiki 존재를 모르거나 무시 가능

### 회피 전략

#### 1. 강제 메커니즘 추가

에이전트/프로젝트 생성 시 다음 파일 함께 생성:
```
Agents/<id>/pre_execution_check.sh         # Wiki 자동 읽기 스크립트
Projects/<id>/pre_execution_check.sh
```

#### 2. prompt.md에 필수 절차 섹션 추가

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

❌ Wiki 조회 없이 작업 시작 금지!
```

#### 3. pre_execution_check.sh 역할

- `memory/wiki/` 전체 문서 자동 읽기
- 필수 패턴 자동 출력
- 체크리스트 강제 표시

#### 4. Kickoff Prompt에 명시

프로젝트 세션 생성 시:
```markdown
## 🚨 작업 시작 전 필수 절차

1. **Wiki 조회 (필수)**
   ./pre_execution_check.sh

2. **체크리스트 검증**
   - [ ] Wiki 전체 읽음
   - [ ] 과거 실수 패턴 확인
   - [ ] 회피 전략 적용

3. **작업 시작**

❌ Wiki 조회 없이 작업 시작 금지!
```

### 적용 범위

- ✅ 모든 공용 에이전트 (prompt.md에 필수 절차 섹션)
- ✅ 모든 프로젝트 세션 (kickoff prompt에 필수 절차)
- ✅ 기존 에이전트/프로젝트에 소급 적용

---

## [Pattern-AUTH] Access Control & Authority Protocol

**범주**: 권한 관리 (Authorization)  
**대상**: Root, 공용 에이전트, 프로젝트 에이전트, 프로젝트 전용 에이전트  
**발생일**: 2026-07-15

### 문제

**상황**: health-fitness-cards 프로젝트 실행 중  
**실수**: 
1. 프로젝트 에이전트가 공용 에이전트 생성을 직접 시도
2. 공용 에이전트가 프로젝트 파일(manifest.yaml) 직접 수정 시도

**결과**:
- 권한 경계 위반
- 잘못된 디렉터리 접근
- 협업 프로토콜 미준수

**근본 원인**:
각 에이전트 타입의 **접근 권한과 책임 범위**가 명확하지 않음.

### 회피 전략: 에이전트 타입별 권한 정의

#### 1️⃣ Root Agent (General Chat)

**접근 권한:**
- ✅ 전체 AOA 디렉터리 (읽기/쓰기)
- ✅ 모든 프로젝트 디렉터리 (읽기/쓰기)
- ✅ Registry 수정
- ✅ 공용 에이전트 생성/수정/삭제
- ✅ 프로젝트 생성

**책임:**
- 공용 에이전트 생성 요청 처리
- 프로젝트 생성
- 프레임워크 레벨 규칙 수정
- Cross-agent 협업 중재

**절대 규칙:**
- 공용 에이전트는 오직 Root만 생성
- Registry 수정은 오직 Root만 수행

---

#### 2️⃣ 공용 에이전트 (Agents/*)

**접근 권한:**
- ✅ 자신의 디렉터리 (Agents/agent-name/*)
- ✅ 자신의 memory/wiki/ (읽기/쓰기)
- ✅ Registry/ (읽기 전용)
- ✅ 입력으로 받은 파일 (읽기)
- ✅ 출력 파일 생성 (지정된 경로만)
- ❌ 다른 에이전트 디렉터리
- ❌ Projects/ 내부 파일

**금지 행동:**
- ❌ Projects/*/manifest.yaml 수정
- ❌ Projects/*/Workflows/ 수정
- ❌ Projects/*/Agents/ 생성
- ❌ Registry/ 수정 (자신의 Registry 엔트리 제외)
- ❌ 다른 공용 에이전트 파일 수정

**권한 밖 작업 발견 시:**
```python
# 프로젝트 파일 수정 필요 → 프로젝트 에이전트에 메시지
send_session_message(
  session_id=os.environ.get('PROJECT_SESSION_ID'),
  message="manifest.yaml 수정 필요: dependencies.agents에 'my-agent' 추가"
)
```

**절대 규칙:**
- 프로젝트 디렉터리는 절대 직접 수정하지 말 것
- 변경 필요 시 프로젝트 에이전트에 메시지 전달

---

#### 3️⃣ 프로젝트 에이전트 (Projects/*/session)

**접근 권한:**
- ✅ 자신의 프로젝트 디렉터리 (Projects/project-name/*)
- ✅ 자신의 프로젝트 Wiki (Projects/project-name/Memory/wiki/*)
- ✅ Registry/ (읽기 전용)
- ✅ Agents/ (읽기 전용, 호출 목적)
- ❌ 다른 프로젝트 디렉터리
- ❌ Registry/ 수정
- ❌ Agents/ 수정/생성

**금지 행동:**
- ❌ Registry/Agents/ 직접 생성
- ❌ Agents/*/prompt.md 수정
- ❌ Core/ 수정
- ❌ Policies/ 수정
- ❌ Standards/ 수정

**권한 밖 작업 발견 시:**
```python
# 공용 에이전트 필요 → Root에 요청
send_session_message(
  session_id=<root_chat_id>,
  message="## 🚨 공용 에이전트 생성 요청\n\n..."
)
```

**절대 규칙:**
- 공용 에이전트는 절대 직접 생성하지 말 것
- 필요 시 Root에 요청 메시지 전달

---

#### 4️⃣ 프로젝트 전용 에이전트 (Projects/*/Agents/*)

**접근 권한:**
- ✅ 자신의 디렉터리 (Projects/project-name/Agents/agent-name/)
- ✅ 프로젝트 디렉터리 (Projects/project-name/*, 읽기만)
- ✅ Registry/ (읽기 전용)
- ✅ 공용 Agents/ (읽기 전용, 호출 목적)
- ❌ 프로젝트 설정 파일 (manifest.yaml, Workflows/*.md) 수정

**금지 행동:**
- ❌ Projects/project-name/manifest.yaml 수정
- ❌ Projects/project-name/Workflows/ 수정
- ❌ 다른 프로젝트 접근

**권한 밖 작업 발견 시:**
→ 프로젝트 에이전트(세션)에 메시지 전송

---

### 권한 위반 감지 자가 점검

**모든 에이전트는 파일 수정 전 반드시 확인:**

**공용 에이전트 체크리스트:**
- [ ] Projects/ 디렉터리 수정하려고 하는가?
  → ❌ 중단, 프로젝트 에이전트에 메시지
- [ ] Registry/INDEX.md 수정하려고 하는가?
  → ❌ Root 작업, 요청 메시지 전달
- [ ] 다른 에이전트 디렉터리 접근하려고 하는가?
  → ❌ 중단

**프로젝트 에이전트 체크리스트:**
- [ ] Registry/Agents/ 생성하려고 하는가?
  → ❌ 중단, Root에 요청 메시지
- [ ] Agents/*/prompt.md 수정하려고 하는가?
  → ❌ 중단, Root에 요청 메시지
- [ ] Core/, Policies/, Standards/ 수정하려고 하는가?
  → ❌ 중단, Root에 요청 메시지

---

### 올바른 Cross-Agent 협업 패턴

#### Pattern A: 공용 에이전트 → 프로젝트 설정 변경
```yaml
발견: "manifest.yaml에 dependencies 추가 필요"
action: send_session_message
to: <project_session_id>
message: |
  ## 📝 프로젝트 설정 변경 필요
  
  **파일:** manifest.yaml
  **변경 내용:**
  dependencies.agents에 'content-transformer' 추가
  
  **이유:** Phase 1.5에서 사용
do_not: Projects/*/manifest.yaml 직접 수정
```

#### Pattern B: 프로젝트 에이전트 → 공용 에이전트 생성 요청
```yaml
발견: "맥락 보존 변형 전문 에이전트 필요"
action: send_session_message
to: <root_chat_id>
message: |
  ## 🚨 공용 에이전트 생성 요청
  
  **요청 배경:** ...
  **제안 에이전트:** content-transformer
  **역할:** ...
  **입력/출력:** ...
do_not: Registry/Agents/ 직접 생성
```

#### Pattern C: 프로젝트 전용 에이전트 → 프로젝트 워크플로우 수정 요청
```yaml
발견: "Workflows/main.md에 Phase 1.5 추가 필요"
action: send_session_message
to: <project_session_id>
message: |
  ## 📝 워크플로우 업데이트 필요
  
  **파일:** Workflows/main.md
  **변경:** Phase 1.5 섹션 추가
  **이유:** content-transformer 사용
do_not: Workflows/main.md 직접 수정
```

---

### Prompt 템플릿 적용

**모든 공용 에이전트 prompt.md에 추가:**
```markdown
## 🚨 Access Control (필수 준수)

당신은 **공용 에이전트**입니다.

**접근 가능:**
- ✅ 자신의 디렉터리 (Agents/<agent-name>/*)
- ✅ 입력 파일 (읽기)
- ✅ 출력 파일 (지정 경로만)
- ✅ Registry/ (읽기 전용)

**접근 불가:**
- ❌ Projects/ 내부 파일 수정
- ❌ 다른 에이전트 디렉터리
- ❌ Registry 수정 (자신 제외)

**프로젝트 파일 변경 필요 시:**
→ send_session_message로 프로젝트 에이전트에 전달
→ **절대 직접 수정하지 말 것**

예시:
send_session_message(
  session_id=os.environ.get('PROJECT_SESSION_ID'),
  message="manifest.yaml 수정 필요: ..."
)
```

**모든 프로젝트 세션 kickoff prompt에 추가:**
```markdown
## 🚨 Access Control (필수 준수)

당신은 **프로젝트 에이전트**입니다.

**접근 가능:**
- ✅ 자신의 프로젝트 디렉터리 (Projects/<project-name>/*)
- ✅ Registry/ (읽기 전용)
- ✅ 공용 Agents/ (읽기 전용, 호출만)

**접근 불가:**
- ❌ Registry/Agents/ 생성/수정
- ❌ Core/, Policies/, Standards/ 수정
- ❌ 다른 프로젝트 디렉터리

**공용 에이전트 생성 필요 시:**
→ send_session_message로 Root에 요청
→ **절대 직접 생성하지 말 것**

예시:
send_session_message(
  session_id=<root_chat_id>,
  message="## 공용 에이전트 생성 요청\n\n..."
)
```

---

### 적용 범위

**즉시 적용:**
1. ✅ 모든 공용 에이전트 prompt.md에 Access Control 섹션 추가
2. ✅ 프로젝트 생성 시 kickoff prompt에 Access Control 규칙 포함
3. ✅ Templates/Agent/prompt.md 템플릿 업데이트
4. ✅ 기존 에이전트 소급 적용

**영향 범위:**
- 모든 공용 에이전트 (5개)
- 모든 프로젝트 세션
- 모든 프로젝트 전용 에이전트

---

## 업데이트 이력

- 2026-07-15: 초기 작성 (Pattern-WIKI, Pattern-AUTH)
- 2026-07-15: Pattern 통합 (agent_creation + project_creation에서 분리)
