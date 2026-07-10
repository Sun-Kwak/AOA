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

## 업데이트 이력

- 2026-07-10: 초기 작성 (Pattern-001 ~ 003 기록)
