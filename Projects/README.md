# Projects Directory

## Purpose

이 디렉터리는 AOA 프로젝트 관리 정책과 템플릿을 정의한다.
실제 프로젝트 데이터는 이 디렉터리에 저장되지 않는다.

---

## Scope

- 프로젝트 생성 템플릿
- 프로젝트 구조 표준
- Multi-Repo 정책 설명
- 프로젝트 등록 가이드

**실제 프로젝트는 AOA 저장소 외부에 생성된다.**

---

## Multi-Repo 정책

AOA는 Framework와 프로젝트를 분리하여 관리한다.

### 저장소 구조

```
1. AOA Framework Repository (이 저장소)
   - 위치: ~/project/AOA/
   - 포함: Core, Agents, Tools, Workflows 등 재사용 가능한 컴포넌트
   - Git: Framework만 추적 (Projects/ 디렉터리는 .gitignore)

2. 실제 프로젝트 (별도 폴더)
   - 위치: ~/project/<project-name>/ 또는 임의 경로
   - 포함: manifest.yaml + 프로젝트 데이터 + 산출물
   - Git: 각 프로젝트가 독립적으로 결정 (선택사항)
```

### 분리 이유

1. **저장소 크기 폭발 방지**
   - 프로젝트가 생성하는 영상, 이미지, 데이터는 수 GB에 달함
   - Framework 저장소는 작고 빠르게 유지

2. **프로젝트 간 격리**
   - 한 프로젝트의 변경이 다른 프로젝트에 영향 없음
   - 프로젝트별 독립적 버전 관리

3. **공유 및 협업**
   - Framework는 공개 저장소
   - 프로젝트는 필요 시 비공개 또는 선택적 공유

4. **Git 히스토리 분리**
   - Framework commit: "feat: Add trend-research-agent"
   - 프로젝트 commit: "chore: Update trend data"
   - 서로 섞이지 않음

---

## 프로젝트 생성 위치

### ❌ 잘못된 경로

```bash
~/project/AOA/Projects/health-shorts/
```

이 경로에 생성하면:
- AOA 저장소 크기 증가
- Framework commit에 프로젝트 데이터 포함
- .gitignore로 막혀 있어 오히려 복잡해짐

### ✅ 올바른 경로

```bash
~/project/health-shorts/
~/automation/health-shorts/
~/Documents/projects/health-shorts/
```

AOA 저장소와 **형제 디렉터리** 또는 **완전히 다른 경로**에 생성.

---

## 프로젝트 인식 방법

AOA는 `manifest.yaml` 파일로 프로젝트를 인식한다.

```yaml
# ~/project/health-shorts/manifest.yaml
id: health-shorts
name: "건강 정보 Shorts 자동화"
framework: AOA
version: 1.0.0
# ...
```

이 파일이 있으면 AOA 프로젝트로 간주되며,
어디에 있든 `Bootstrap/Initialize.md` 절차로 로드 가능.

---

## 프로젝트별 Git 관리 (선택사항)

각 프로젝트는 필요에 따라 독립적으로 Git 저장소를 초기화할 수 있다.

### Git 관리를 권장하는 경우

- 프로젝트를 백업하고 싶을 때
- 프로젝트를 다른 사람과 공유할 때
- 프로젝트 변경 이력을 추적하고 싶을 때
- CI/CD 파이프라인을 연결하고 싶을 때

### Git 관리가 불필요한 경우

- 일회성 실험 프로젝트
- 로컬에서만 사용하는 개인 자동화
- 대용량 파일이 너무 많아 Git에 부적합한 경우

### 프로젝트 .gitignore 예시

```gitignore
# 프로젝트 산출물 (대용량)
Outputs/*.mp4
Outputs/*.png
Outputs/*.jpg

# 수집 데이터 (변동성 높음)
Memory/trends/*.json
Memory/raw_data/

# 비밀 정보
.env
credentials.yaml
secrets/

# 로그
*.log
debug/
```

---

## Registry 연결

프로젝트는 AOA Registry와 연결되지 않는다.

- **Registry 대상**: Agents, Tools, Workflows, Templates (재사용 가능한 자산)
- **프로젝트**: Registry에 등록하지 않음 (소비자일 뿐)

프로젝트가 특정 공용 에이전트를 사용하려면:
```yaml
# 프로젝트 manifest.yaml
dependencies:
  agents:
    - id: trend-research-agent
      version: "1.0.0"
      path: ../AOA/Agents/trend-research-agent/  # 상대 경로
```

---

## 프로젝트 템플릿

`Projects/Project_Template.md` 참조.

새 프로젝트 생성 시 이 템플릿을 복사하여 시작한다.

---

## TODO

프로젝트 디스커버리 규칙 추가 (manifest.yaml 기반).
프로젝트 마이그레이션 가이드 추가 (다른 폴더로 이동 시).

