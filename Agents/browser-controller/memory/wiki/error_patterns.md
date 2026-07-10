# Error Patterns

browser-controller 실행 중 발생한 에러와 회피 전략.

---

## Format

```markdown
## [Pattern-001] 셀렉터 찾기 실패

**발생일**: YYYY-MM-DD  
**상황**: Instagram 업로드 버튼 클릭 시  
**실수**: .upload-button 셀렉터가 .create-button으로 변경됨  
**결과**: Canvas action 실패  
**회피전략**:
1. ✅ 대체 셀렉터 시도
2. ✅ 스크린샷 촬영
3. ✅ instagram_workflow.md 업데이트
```

---

## TODO

실제 에러 발생 시 패턴이 기록됩니다.
