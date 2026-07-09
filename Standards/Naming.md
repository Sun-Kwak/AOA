# Naming

## Purpose

AOA 전체에서 일관된 이름 규칙을 정의한다.
일관된 이름이 있어야 Registry 검색이 정확하고
파일 참조가 깨지지 않는다.

---

## Scope

에이전트, 툴, 워크플로우, 캐퍼빌리티, 템플릿, 프로젝트,
파일명, 디렉터리명, ID 전체에 적용된다.

---

## ID 규칙

모든 등록 가능한 자산(Agent, Tool, Workflow, Capability, Template, Project)의
ID는 다음 규칙을 따른다:

| 규칙 | 내용 |
|------|------|
| 형식 | `kebab-case` |
| 문자 | 영문 소문자, 숫자, 하이픈(`-`) |
| 시작 | 영문자로 시작 |
| 금지 | 공백, 언더스코어, 대문자, 특수문자 |
| 최대 길이 | 50자 |

```
✅ image-generation-agent
✅ youtube-upload-tool
✅ kids-video-gen
❌ ImageGenAgent
❌ image_generation_agent
❌ image generation agent
```

---

## 파일명 규칙

| 대상 | 규칙 | 예시 |
|------|------|------|
| Markdown 문서 | `PascalCase` + `.md` | `Startup_Order.md`, `SYSTEM.md` |
| Core 문서 | `ALL_CAPS` + `.md` | `BOOT.md`, `SYSTEM.md` |
| YAML 파일 | `kebab-case` + `.yaml` | `manifest.yaml`, `aios.manifest.yaml` |
| 로그 파일 | `kebab-case.log.md` | `execution.log.md` |
| 디렉터리 | `PascalCase` | `Bootstrap/`, `Registry/` |
| 프로젝트 디렉터리 | `kebab-case` | `kids-video-gen/` |

---

## 에이전트 이름 규칙

에이전트 ID와 표시명(Display Name)을 구분한다.

```
ID (Registry, manifest에서 참조):
  image-generation-agent

Display Name (README, 문서에서):
  Image Generation Agent

세션 패널 표기:
  [AOA] <Project Name> — <Display Name>
  예) [AOA] kids-video-gen — Image Generation Agent
```

에이전트 ID는 역할을 명확히 나타내야 한다.
`agent-1`, `helper`, `util` 같은 모호한 이름 금지.

---

## 워크플로우, 툴, 캐퍼빌리티 이름 규칙

| 자산 유형 | 접미사 규칙 | 예시 |
|-----------|------------|------|
| Agent | `-agent` | `script-writer-agent` |
| Tool | `-tool` | `youtube-upload-tool` |
| Workflow | `-workflow` | `video-production-workflow` |
| Capability | `-capability` | `text-summarize-capability` |
| Template | `-template` | `youtube-shorts-template` |

접미사가 있으면 Registry에서 유형을 즉시 파악할 수 있다.

---

## 프로젝트 이름 규칙

```
형식   : kebab-case
예시   : kids-video-gen, card-news-automation, sns-factory
금지   : 날짜 포함 (my-project-20260709)
       : 버전 포함 (project-v2)
       : 모호한 이름 (new-project, test)
```

---

## TODO

다국어 이름 처리 규칙 추가.
이름 충돌 감지 및 해소 규칙 추가.
