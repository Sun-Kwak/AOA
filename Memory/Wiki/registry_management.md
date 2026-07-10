# Wiki: Registry Management

Registry 업데이트 시 반복된 실수와 회피 전략.

---

## [Pattern-001] 에이전트 생성 후 Registry 누락

**상세**: agent_creation.md의 [Pattern-001] 참조

**회피전략**:
1. ✅ 에이전트/툴/워크플로우 생성은 Registry 업데이트와 원자적 작업
2. ✅ 같은 response에서 모두 처리

---

## [Pattern-002] Registry 검색 안함

**발생일**: 다수  
**상황**: 새 에이전트/툴 생성 요청 시  
**실수**: Registry 확인 안하고 바로 생성  
**결과**: 
- 중복 에이전트 생성 (이미 있는데 모름)
- Registry 의미 상실

**회피전략**:
1. ✅ **절대 규칙**: 에이전트/툴 생성 전 **반드시 Registry 검색**
2. ✅ 검색 순서:
   ```
   1. Registry/INDEX.md 전체 확인
   2. 관련 카테고리 Registry/<Type>/ 확인
   3. 유사 에이전트 있으면 재사용 여부 사용자 확인
   4. 없으면 생성 진행
   ```
3. ✅ `Bootstrap/Create_Project.md` Step 2 참조

---

## [Pattern-003] INDEX.md 카운트 불일치

**발생일**: 다수  
**상황**: Registry/INDEX.md 업데이트 시  
**실수**: 총 개수 업데이트 안함  
**결과**: INDEX.md 신뢰도 하락

**회피전략**:
1. ✅ 에이전트 추가/삭제 시 총 개수 동시 업데이트
2. ✅ 예시:
   ```markdown
   ## Agents (3)  ← 개수 확인!
   | ID | Name | Category |
   |-----|------|----------|
   | ... | ...  | ...      |
   ```

---

## 작업 시작 전 체크리스트

Registry 관련 작업 시:

- [ ] `Standards/Registry_Protocol.md` 읽음
- [ ] 이 Wiki 문서 읽음
- [ ] Registry/INDEX.md 검색
- [ ] 중복 여부 확인
- [ ] 생성/삭제 시 INDEX.md + <Type>/<id>.md 동시 처리
- [ ] 총 개수 업데이트

---

## 업데이트 이력

- 2026-07-10: 초기 작성 (Pattern-001 ~ 003 기록)
