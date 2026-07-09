# Translation Agent

id: translation-agent
type: agent
version: 1.0.0
status: active
tags: [translation, korean, report-style, finance]
path: Agents/translation-agent/
description: 영문 텍스트를 보고서용 한국어로 번역함. 구어체·존댓말 없이 간결한 보고서 문체 사용.

## Summary

영문 입력을 받아 `-다`, `-임`, `-됨` 체의 보고서용 한국어로 번역한다.
금융·경제 표준 용어를 적용하며 주요 용어 glossary를 함께 반환한다.

## Inputs

- `text` (required): 번역할 영문 원문
- `context` (optional): 번역 맥락 힌트

## Outputs

- `translated_text`: 보고서용 한국어 번역
- `glossary`: 주요 용어 원문/번역어 쌍 (선택적)

## Dependencies

없음
