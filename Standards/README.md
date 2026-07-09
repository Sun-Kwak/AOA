# Standards

## Purpose

AIOS 전체에서 일관성을 유지하기 위한 작성 규칙을 정의한다.
Standards는 AI가 어떻게 동작하는가가 아니라
어떻게 쓰고, 이름 붙이고, 버전을 관리하는가를 다룬다.

---

## Scope

| 파일 | 역할 |
|------|------|
| `Naming.md` | ID, 파일명, 디렉터리명, 에이전트명 규칙 |
| `Versioning.md` | 공용 자산의 버전 관리 (Semantic Versioning) |
| `Prompt.md` | 에이전트 프롬프트 작성 구조와 길이 규칙 |
| `Markdown.md` | 모든 문서의 마크다운 작성 규칙 |

---

## 우선 적용 순서

새 자산을 만들 때 다음 순서로 Standards를 확인한다:

1. `Naming.md` — ID와 파일명부터 결정
2. `Versioning.md` — 초기 버전 설정 (1.0.0)
3. `Prompt.md` — 에이전트 프롬프트 작성 (에이전트일 경우)
4. `Markdown.md` — 문서 작성

---

## TODO

Standards 위반 감지 규칙 추가.
