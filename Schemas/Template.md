# Template Schema

## Purpose

모든 AOA 프로젝트 템플릿 정의 파일이 따라야 하는 표준 구조를 정의한다.
템플릿은 새 프로젝트를 빠르게 시작할 수 있는 재사용 가능한 구조다.

---

## Scope

`Templates/<category>/<template-name>/` 디렉터리에 있는 모든 템플릿에 적용된다.

---

## Template Schema

```yaml
# Templates/<category>/<template-name>/template.yaml
# Standards/Naming.md: ID는 kebab-case, -template 접미사 필수

id: <template-id>                 # 예: youtube-shorts-template
name: <Display Name>
version: 1.0.0
status: active

description: >
  이 템플릿이 어떤 종류의 프로젝트를 위한 것인지 한 문장.

category: <automation|assistant|document|video|social|email|meeting|spreadsheet>

# 이 템플릿을 사용하면 생성되는 디렉터리 구조
directory_structure:
  - path: <상대 경로>
    type: <directory|file>
    description: <역할>

# 반드시 포함되어야 하는 파일 목록
required_files:
  - path: manifest.yaml
    template_source: Templates/<category>/<name>/manifest.template.yaml

# 이 템플릿 사용 시 기본으로 포함되는 에이전트
default_agents:
  - id: <agent-id>
    role: <역할>

# 이 템플릿 사용 시 기본으로 포함되는 워크플로우
default_workflows:
  - id: <workflow-id>

# 프로젝트 생성 시 사용자에게 물어볼 변수
variables:
  - name: <변수명>
    prompt: <사용자에게 물어볼 질문>
    default: null

tags: []

changelog:
  - version: 1.0.0
    date: <YYYY-MM-DD>
    note: 최초 등록
```

---

## 필수 필드

- `id`, `name`, `version`, `status`
- `category`
- `required_files`

---

## Template 디렉터리 구조

```
Templates/<category>/<template-name>/
  ├── template.yaml             ← 이 스키마를 따르는 정의 파일
  ├── manifest.template.yaml    ← 프로젝트 manifest 템플릿
  └── README.md                 ← 사용 방법, 생성되는 구조 설명
```

---

## TODO

템플릿 변수 치환 규칙 정의.
템플릿 상속 (다른 템플릿 확장) 규칙 추가.
