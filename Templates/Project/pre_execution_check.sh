#!/bin/bash
# Project Wiki 자동 조회 스크립트
# 프로젝트 작업 시작 전 필수 실행

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WIKI_DIR="${PROJECT_DIR}/Memory/wiki"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚨 Pre-Execution Check: Wiki Protocol"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Wiki 디렉터리 존재 확인
if [ ! -d "${WIKI_DIR}" ]; then
    echo "⚠️  Warning: Memory/wiki/ 디렉터리가 없습니다."
    echo "   첫 실행이거나 Wiki 미생성 상태입니다."
    echo ""
    exit 0
fi

# Wiki 파일 수 확인
WIKI_FILES=$(find "${WIKI_DIR}" -type f -name "*.md" | wc -l | xargs)

if [ "${WIKI_FILES}" -eq 0 ]; then
    echo "✅ Wiki 파일이 없습니다. (첫 실행)"
    echo ""
    exit 0
fi

echo "📚 Wiki 디렉터리: ${WIKI_DIR}"
echo "📄 Wiki 파일 수: ${WIKI_FILES}개"
echo ""

# Wiki 파일 목록 및 내용 출력
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📖 Wiki 문서 내용"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

find "${WIKI_DIR}" -type f -name "*.md" | sort | while read -r file; do
    filename=$(basename "${file}")
    echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "┃ 📄 ${filename}"
    echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    cat "${file}"
    echo ""
    echo ""
done

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ 체크리스트"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "작업 시작 전 다음을 확인하세요:"
echo ""
echo "  [ ] 모든 Wiki 문서를 읽었습니까?"
echo "  [ ] 과거 실수 패턴을 확인했습니까?"
echo "  [ ] 회피 전략을 적용할 수 있습니까?"
echo "  [ ] 필수 규칙을 준수할 준비가 되었습니까?"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
