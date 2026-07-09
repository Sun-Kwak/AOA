# News Fetcher Agent

id: news-fetcher-agent
type: agent
version: 1.0.0
status: active
tags: [news, research, stock-market, korean-market]
path: Agents/news-fetcher-agent/
description: 영어권 뉴스에서 한국 주식 시장에 영향을 줄 수 있는 핫 토픽 10개를 수집함.

## Summary

영어권 주요 매체(Reuters, Bloomberg, WSJ, FT, CNBC)를 검색하여
한국 주식 시장과 관련된 글로벌 이슈를 YAML 형식으로 반환한다.

## Inputs

- `date` (optional): 기준 날짜 YYYY-MM-DD

## Outputs

- `news_topics`: 10개 뉴스 항목 (rank, title, source, url, summary, affected_sectors, relevance_reason)

## Dependencies

현재: AI 내장 웹 검색으로 동작 (별도 툴 불필요)
자동화 전환 시: NewsAPI 또는 Tavily 등록 예정
