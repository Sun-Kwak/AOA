# Registry Protocol

## Purpose

Registry는 AOA의 검색 가능한 자산 카탈로그입니다.

**모든 공유 자산 생성/수정/삭제 시 Registry를 자동으로 업데이트해야 합니다.**

---

## 핵심 원칙

⚠️ **절대 규칙**: Agent, Tool, Workflow, Capability, Template을 생성/수정/삭제할 때 **반드시** Registry를 동시에 업데이트합니다.

사용자가 지적하기 전에 자동으로 처리해야 합니다.

---

## 자산 생성 시 체크리스트

### ✅ Agent 생성

```
1. [ ] Agents/<agent-id>/ 디렉토리 생성
2. [ ] config.yaml, prompt.md, README.md 작성
3. [ ] Registry/INDEX.md의 Agents 섹션에 추가
4. [ ] Registry/INDEX.md의 Asset Summary 카운트 증가
5. [ ] Registry/Agents/<agent-id>.md 등록 파일 생성
```

### ✅ Tool 생성

```
1. [ ] Tools/<tool-id>/ 디렉토리 생성
2. [ ] README.md, 설정 파일 작성
3. [ ] Registry/INDEX.md의 Tools 섹션에 추가
4. [ ] Registry/INDEX.md의 Asset Summary 카운트 증가
5. [ ] Registry/Tools/<tool-id>.md 등록 파일 생성
```

### ✅ Workflow 생성

```
1. [ ] Workflows/<workflow-id>/ 디렉토리 생성
2. [ ] README.md, workflow.yaml 작성
3. [ ] Registry/INDEX.md의 Workflows 섹션에 추가
4. [ ] Registry/INDEX.md의 Asset Summary 카운트 증가
5. [ ] Registry/Workflows/<workflow-id>.md 등록 파일 생성
```

### ✅ Capability 생성

```
1. [ ] Capabilities/<capability-id>/ 디렉토리 생성
2. [ ] README.md 작성
3. [ ] Registry/INDEX.md의 Capabilities 섹션에 추가
4. [ ] Registry/INDEX.md의 Asset Summary 카운트 증가
5. [ ] Registry/Capabilities/<capability-id>.md 등록 파일 생성
```

### ✅ Template 생성

```
1. [ ] Templates/<category>/<template-id>/ 디렉토리 생성
2. [ ] README.md 작성
3. [ ] Registry/INDEX.md의 Templates 섹션에 추가
4. [ ] Registry/INDEX.md의 Asset Summary 카운트 증가
5. [ ] Registry/Templates/<template-id>.md 등록 파일 생성
```

---

## 자산 삭제 시 체크리스트

### ✅ 모든 자산 타입

```
1. [ ] 구현 디렉토리 삭제 (Agents/, Tools/, etc.)
2. [ ] Registry/INDEX.md에서 해당 행 제거
3. [ ] Registry/INDEX.md의 Asset Summary 카운트 감소
4. [ ] Registry/<type>/<id>.md 등록 파일 삭제
5. [ ] 의존하는 다른 자산이 있는지 확인 및 업데이트
```

---

## Registry/INDEX.md 업데이트 규칙

### **Asset Summary 섹션**

자산 생성/삭제 시 카운트를 즉시 업데이트합니다.

```markdown
| Type | Registered | Path |
|------|-----------|------|
| Agents | 2 | Registry/Agents/ |  ← 생성 시 +1, 삭제 시 -1
```

### **개별 자산 섹션**

테이블 형식을 유지하며 추가/제거합니다.

```markdown
| ID | Name | Version | Tags | Description | Path |
|----|------|---------|------|-------------|------|
| image-generator | Image Generator | 1.0.0 | image, fal-ai | 범용 이미지 생성 | Agents/image-generator/ |
```

**필수 항목:**
- ID (kebab-case)
- Name (Human-readable)
- Version (Semantic versioning)
- Tags (comma-separated, 검색용)
- Description (한 줄 설명)
- Path (구현 경로)

---

## Registry/<Type>/ 등록 파일 형식

### **파일명**

`Registry/<Type>/<id>.md`

예:
- `Registry/Agents/image-generator.md`
- `Registry/Tools/apify.md`

### **필수 섹션**

```markdown
# <Asset Name>

## Metadata

| Field | Value |
|-------|-------|
| ID | <id> |
| Name | <name> |
| Version | <version> |
| Status | Active | Deprecated |
| Created | YYYY-MM-DD |
| Last Updated | YYYY-MM-DD |

---

## Tags

`tag1`, `tag2`, `tag3`

---

## Description

상세 설명...

핵심 기능:
- 기능 1
- 기능 2

---

## Dependencies

### Tools
- tool1
- tool2

### Environment
- ENV_VAR (required/optional)

---

## Usage

```yaml
# 사용 예시
```

---

## Path

`<Type>/<id>/`

---

## Related Assets

- **Tools:** ...
- **Agents:** ...
- **Used by:** ...

---

## Notes

추가 정보...
```

---

## 의존성 체크

자산 삭제 시 다음을 확인합니다:

```
1. [ ] 다른 Agent가 이 자산을 사용하는가?
2. [ ] 현재 실행 중인 프로젝트가 의존하는가?
3. [ ] Related Assets에 링크된 곳이 있는가?
```

**의존성이 있으면:**
- 사용자에게 경고
- 대체 방안 제시
- 또는 삭제 중단

---

## 자동화 원칙

### ❌ 하지 말 것

```
"Agent를 만들었습니다. Registry는 나중에 업데이트하세요."
```

### ✅ 해야 할 것

```
"Agent를 만들고 Registry에 자동 등록했습니다."
```

**사용자가 지적하기 전에 모든 연관 작업을 완료합니다.**

---

## 검증 명령어

Registry가 올바른지 확인:

```bash
# Agent 카운트 확인
ls Agents/ | grep -v README | wc -l
grep "| Agents |" Registry/INDEX.md

# 등록 파일 존재 확인
for agent in Agents/*/; do
  id=$(basename "$agent")
  [ -f "Registry/Agents/$id.md" ] || echo "Missing: $id"
done
```

---

## 예시: Agent 생성 전체 프로세스

```bash
# 1. Agent 구현
mkdir -p Agents/new-agent
touch Agents/new-agent/{config.yaml,prompt.md,README.md}

# 2. Registry/INDEX.md 업데이트
# - Asset Summary: Agents 카운트 +1
# - Agents 섹션: 새 행 추가

# 3. 등록 파일 생성
touch Registry/Agents/new-agent.md
# (Metadata, Tags, Description, Dependencies 작성)

# 4. 검증
ls Agents/ | grep -v README | wc -l  # 카운트 확인
cat Registry/INDEX.md | grep "| Agents |"  # Registry 확인
ls Registry/Agents/new-agent.md  # 등록 파일 확인
```

**모든 단계를 한 번에 처리합니다.**

---

## 성공 조건

✅ 자산 구현 완료  
✅ Registry/INDEX.md 업데이트 완료  
✅ Registry/<Type>/<id>.md 등록 파일 생성 완료  
✅ 카운트 정확  
✅ 의존성 확인 완료  
✅ 사용자가 별도로 지적할 필요 없음  

---

## 실패 사례

❌ Agent를 만들고 Registry를 업데이트하지 않음  
❌ Registry/INDEX.md만 업데이트하고 등록 파일 미생성  
❌ 카운트를 업데이트하지 않음  
❌ 삭제 시 Registry에 남겨둠  
❌ 사용자가 지적한 후에야 수정  

**이런 일은 절대 발생해서는 안 됩니다.**
