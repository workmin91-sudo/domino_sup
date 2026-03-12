# GitHub 저장소 설정 가이드

## 오류 원인
"The provided GitHub repository does not contain the requested branch or commit reference" 오류는 다음 중 하나일 수 있습니다:
1. Git 저장소가 초기화되지 않음
2. 파일이 커밋되지 않음
3. GitHub에 푸시되지 않음
4. 기본 브랜치(main/master)가 없음

## 해결 방법

### 1단계: Git 저장소 초기화 및 커밋

터미널에서 프로젝트 폴더로 이동한 후 다음 명령어를 실행하세요:

```bash
# Git 저장소 초기화
git init

# 모든 파일 추가
git add .

# 첫 커밋 생성
git commit -m "Initial commit: 재고 관리 시스템"

# 기본 브랜치를 main으로 설정 (GitHub 기본값)
git branch -M main
```

### 2단계: GitHub 저장소 생성

1. [GitHub](https://github.com)에 로그인
2. 우측 상단 "+" 버튼 클릭 → "New repository"
3. 저장소 이름 입력 (예: `inventory-management-system`)
4. **중요**: "Initialize this repository with a README" 체크 해제
5. "Create repository" 클릭

### 3단계: GitHub에 푸시

GitHub에서 제공하는 저장소 URL을 복사한 후:

```bash
# 원격 저장소 추가 (YOUR_USERNAME과 REPO_NAME을 실제 값으로 변경)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# GitHub에 푸시
git push -u origin main
```

### 4단계: Vercel에서 다시 연결

1. Vercel 대시보드로 돌아가기
2. 프로젝트 삭제 후 다시 생성 (또는 기존 프로젝트에서 재연결)
3. GitHub 저장소 선택
4. 이제 정상적으로 연결될 것입니다

## 문제 해결

### "fatal: not a git repository" 오류
→ `git init` 명령어를 먼저 실행하세요

### "remote origin already exists" 오류
→ 다음 명령어로 기존 원격 저장소 제거 후 다시 추가:
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

### "failed to push" 오류
→ GitHub 인증이 필요할 수 있습니다. GitHub Personal Access Token 사용 필요

## 빠른 체크리스트

- [ ] `git init` 실행 완료
- [ ] `git add .` 실행 완료
- [ ] `git commit` 실행 완료
- [ ] GitHub 저장소 생성 완료
- [ ] `git remote add origin` 실행 완료
- [ ] `git push -u origin main` 실행 완료
- [ ] GitHub에서 파일들이 보이는지 확인
- [ ] Vercel에서 저장소 재연결
