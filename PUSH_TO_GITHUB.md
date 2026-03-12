# GitHub에 푸시하는 방법

## 현재 상태
- ✅ 로컬 Git 저장소 초기화 완료
- ✅ 파일 커밋 완료
- ❌ GitHub에 푸시 안 됨

## 해결 방법

### 방법 1: 명령어로 푸시 (권장)

1. **GitHub에서 저장소 생성**
   - https://github.com 접속
   - 우측 상단 "+" → "New repository"
   - 저장소 이름 입력 (예: `inventory-system`)
   - **중요**: "Initialize this repository with a README" 체크 해제
   - "Create repository" 클릭

2. **터미널에서 다음 명령어 실행**

```bash
# 원격 저장소 추가 (YOUR_USERNAME과 REPO_NAME을 실제 값으로 변경)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# GitHub에 푸시
git push -u origin main
```

**예시:**
```bash
git remote add origin https://github.com/johndoe/inventory-system.git
git push -u origin main
```

### 방법 2: GitHub Desktop 사용

1. GitHub Desktop 설치: https://desktop.github.com
2. GitHub Desktop에서:
   - File → Add Local Repository
   - 프로젝트 폴더 선택
   - Publish repository 클릭
   - 저장소 이름 입력 후 Publish

## 인증 오류 발생 시

### Personal Access Token 사용 (권장)

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. "Generate new token (classic)" 클릭
3. 권한 선택: `repo` 체크
4. 토큰 생성 후 복사
5. 푸시 시 비밀번호 대신 토큰 사용

### 또는 SSH 사용

```bash
# SSH 키 생성 (이미 있으면 스킵)
ssh-keygen -t ed25519 -C "your_email@example.com"

# SSH 키를 GitHub에 추가
# GitHub → Settings → SSH and GPG keys → New SSH key
# 생성된 키 복사하여 추가

# SSH URL로 원격 저장소 추가
git remote add origin git@github.com:YOUR_USERNAME/REPO_NAME.git
git push -u origin main
```

## 확인 방법

푸시가 성공했는지 확인:
1. GitHub 저장소 페이지 새로고침
2. 파일들이 보이는지 확인
3. Vercel에서 다시 저장소 연결 시도
