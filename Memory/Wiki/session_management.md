# Wiki: Session Management

세션 생성/관리 시 반복된 실수와 회피 전략.

---

## [Pattern-001] 플랜 승인 루프 (Plan Approval Loop)

**발생일**: 2026-07-10 (여러 차례)  
**상황**: 하위 세션 생성 시 mode 미지정  
**실수**: kickoff.mode를 지정 안함 → 기본값 "plan" → 승인 대기  
**결과**: 
- 세션이 플랜 단계에서 멈춤
- Root가 계속 승인해줘야 함
- 자동화 불가능

**회피전략**:
1. ✅ **절대 규칙**: kickoff.mode는 **항상 "autopilot"** 지정
2. ✅ 이유: Root는 프로젝트 생성 후 관여 안함 (사용자 명시)
3. ✅ create_session 예시:
   ```javascript
   kickoff: {
     mode: "autopilot",  // 필수!
     prompt: "..."
   }
   ```

---

## [Pattern-002] 환경변수 전달 실패

**발생일**: 2026-07-10  
**상황**: 하위 세션에서 API 키 필요 시  
**실수**: ~/.zshrc의 FAL_KEY를 하위 세션이 읽을 수 없음  
**결과**: 
- 하위 세션이 "API 키 없음" 에러
- 중복 세션 생성

**회피전략**:
1. ✅ **임시 해결책**: kickoff.prompt에 API 키 직접 포함
   ```
   kickoff.prompt: "
   환경변수:
   - FAL_KEY=<value>
   
   작업: ...
   "
   ```
2. ⏳ **향후 개선**: manifest.yaml에 env_vars 섹션 추가 검토

---

## [Pattern-003] coordinate_with_creator 오용

**발생일**: 2026-07-10  
**상황**: 프로젝트 세션 생성 시  
**실수**: coordinate_with_creator: true (또는 미지정)  
**결과**: 
- 프로젝트 에이전트가 Root에게 계속 보고
- Root가 오케스트라 역할 하게 됨 (사용자 의도와 반대)

**회피전략**:
1. ✅ **절대 규칙**: 프로젝트 세션은 **coordinate_with_creator: false**
2. ✅ 이유: "프로젝트 생성까지가 Root의 의무" (사용자 명시)
3. ✅ Root는 프로젝트 생성 후 관여 안함

---

## [Pattern-004] 세션 중복 생성

**발생일**: 2026-07-10  
**상황**: 에러 발생 후 재시도  
**실수**: 같은 작업에 대해 여러 세션 생성  
**결과**: 
- UI에 Card #1, #1 v2, #1 v3 등 중복
- 리소스 낭비

**회피전략**:
1. ✅ 세션 생성 전 list_agents로 중복 확인
2. ✅ 에러 발생 시 새 세션 만들지 말고 기존 세션 디버깅
3. ✅ 실패한 세션은 명시적으로 삭제 후 재생성

---

## [Pattern-005] 하위 에이전트 세션 중복 생성

**발생일**: 2026-07-10  
**상황**: Project Session이 공용 에이전트(trend-research, image-generator) 호출 시  
**실수**: 이미 실행 중인 에이전트 세션이 있는데 또 새로 생성  
**결과**: 
- 리소스 낭비 (동일 작업 중복 실행)
- 실행 상태 혼란 (어느 세션이 최신인지 불명확)
- UI에 중복 세션 표시

**회피전략**:
1. ✅ **Project Agent 생성 시 kickoff prompt에 명시**:
   ```markdown
   ### 하위 에이전트 실행 규칙
   
   1. **기존 세션 확인 필수**
      - 공용 에이전트 호출 전 `list_agents()` 실행
      - 동일 에이전트 이름의 활성/idle 세션 존재 시 재사용
      - 새 세션 생성은 기존 세션이 없을 때만
   
   2. **실행 상태 기반 판단**
      - Memory/execution_state.md 확인
      - 완료된 Phase는 재실행하지 않음
      - 진행 중인 Phase는 결과 대기
   
   3. **에이전트 세션 네이밍**
      - 명확한 이름 사용 (예: "trend-research-health-fitness")
      - 프로젝트명 포함으로 추적 용이
   
   4. **실패 시에만 재생성**
      - 기존 세션이 FAILED 상태일 때만 새로 생성
      - IDLE/RUNNING 상태면 read_agent() 또는 write_agent()로 상호작용
   ```

2. ✅ 예시 프롬프트:
   ```
   kickoff.prompt: `
   ...
   
   ## 하위 에이전트 실행 규칙
   - 에이전트 호출 전 list_agents()로 기존 세션 확인
   - 존재하면 재사용, 없으면 생성
   - Memory/execution_state.md 기반 Phase 진행 판단
   `
   ```

---

## 작업 시작 전 체크리스트

세션 생성 요청이 들어오면:

- [ ] 이 Wiki 문서 읽음
- [ ] list_agents로 중복 세션 확인
- [ ] kickoff.mode: "autopilot" 설정
- [ ] coordinate_with_creator 의도 확인
- [ ] 환경변수 필요 시 prompt에 포함
- [ ] 세션 naming convention 준수

---

## 올바른 세션 생성 패턴

### 프로젝트 세션 (Root → Project)
```javascript
create_session({
  project_id: "52d540bd...",  // AOA project ID
  name: "[AOA] Health Fitness Cards",
  coordinate_with_creator: false,  // 보고 안받음!
  kickoff: {
    mode: "autopilot",  // 필수!
    prompt: `
      AOA Framework Rules + 작업 지시
      환경변수: FAL_KEY=<value>
    `
  }
})
```

### 하위 에이전트 세션 (Project → Agent)
```javascript
create_session({
  project_id: "52d540bd...",
  name: "[AOA] health-fitness-cards — Image Gen",
  coordinate_with_creator: false,  // 또는 true (필요시)
  kickoff: {
    mode: "autopilot",
    prompt: `
      Agent: /Users/sun/project/AOA/Agents/image-generator/prompt.md
      Input: { ... }
      환경변수: FAL_KEY=<value>
    `
  }
})
```

---

## 업데이트 이력

- 2026-07-10: 초기 작성 (Pattern-001 ~ 004 기록)
- 2026-07-10: Pattern-005 추가 (하위 에이전트 세션 중복 생성 방지)
