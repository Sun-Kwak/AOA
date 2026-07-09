# Tool Schema

## Purpose

모든 AOA 툴 정의 파일이 따라야 하는 표준 구조를 정의한다.
툴은 외부 API 호출이나 시스템 작업을 실행하는 최소 단위다.
비즈니스 로직을 포함하지 않는다.

---

## Scope

공용 툴 (`Tools/<name>/tool.yaml`) 모두에 적용된다.

---

## Tool Schema

```yaml
# Tools/<tool-name>/tool.yaml
# Standards/Naming.md: ID는 kebab-case, -tool 접미사 필수

id: <tool-id>                     # 예: youtube-upload-tool
name: <Display Name>              # 예: YouTube Upload Tool
version: 1.0.0
status: active                    # active | deprecated

description: >
  이 툴이 무엇을 하는지 한 문장.

# 툴 유형
action_type: <api_call|file_operation|system_command|data_transform>

# 외부 API를 사용하는 경우
api:
  provider: <제공자 — 예: fal.ai, youtube, openai>
  endpoint: <엔드포인트 URL 또는 null>
  auth_required: true             # true | false
  auth_type: <api_key|oauth|bearer|null>
  docs_url: <API 문서 URL 또는 null>

# 입력 정의
inputs:
  - name: <입력 이름>
    type: <text|file_path|yaml|json|binary>
    required: true
    description: <설명>

# 출력 정의
outputs:
  - name: <출력 이름>
    type: <text|file_path|yaml|json|binary>
    description: <설명>

# 비용 관련 (Cost_Control Policy에서 참조)
cost:
  has_cost: false                 # true | false
  unit: null                      # per_call | per_token | per_mb | null
  estimated_cost_per_unit: null   # 숫자 또는 null

# Human-in-the-Loop 필요 여부
requires_hitl: false              # 외부 전송 툴은 true

# 이 툴에만 적용되는 제약
constraints: []

tags: []

changelog:
  - version: 1.0.0
    date: <YYYY-MM-DD>
    note: 최초 등록
```

---

## 필수 필드

- `id`, `name`, `version`, `status`
- `description`
- `action_type`
- `inputs`, `outputs`
- `requires_hitl`

---

## Tool 디렉터리 구조

```
Tools/<tool-name>/
  ├── tool.yaml       ← 이 스키마를 따르는 정의 파일
  └── README.md       ← 사용 방법, 인증 설정 방법, 예시
```

---

## TODO

툴 버전별 API 변경 이력 추가.
인증 정보 관리 지침 추가 (크리덴셜은 절대 tool.yaml에 포함하지 않음).
