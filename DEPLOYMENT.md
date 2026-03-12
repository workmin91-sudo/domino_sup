# Vercel 배포 가이드

## 사전 준비 사항

### 1. Vercel 계정 생성
- [Vercel](https://vercel.com)에 가입 (GitHub 계정으로 가입 권장)

### 2. GitHub 저장소 준비
- 프로젝트를 GitHub에 푸시
- Vercel은 GitHub 저장소와 연동하여 배포합니다

### 3. 환경 변수 준비
Vercel 대시보드에서 다음 환경 변수들을 설정해야 합니다:

#### 필수 환경 변수
```
EMAIL_PASSWORD=zewwbliyyqfjrntd
LOGIN_PASSWORD=1111
```

#### 선택 환경 변수 (기본값 사용 가능)
```
EMAIL_SENDER=workmin91@gmail.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
FLASK_SECRET_KEY=your-random-secret-key-here
DATABASE=inventory.db
DEFAULT_MIN_STOCK=10
```

## 배포 단계

### 1단계: GitHub에 코드 푸시
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin [your-github-repo-url]
git push -u origin main
```

### 2단계: Vercel 프로젝트 생성
1. [Vercel 대시보드](https://vercel.com/dashboard) 접속
2. "Add New..." → "Project" 클릭
3. GitHub 저장소 선택
4. 프로젝트 설정:
   - **Framework Preset**: Other
   - **Root Directory**: `./` (기본값)
   - **Build Command**: (비워두기)
   - **Output Directory**: (비워두기)

### 3단계: 환경 변수 설정
1. 프로젝트 설정 페이지에서 "Environment Variables" 탭 클릭
2. 다음 환경 변수들을 추가:

| Key | Value | Environment |
|-----|-------|-------------|
| `EMAIL_PASSWORD` | `zewwbliyyqfjrntd` | Production, Preview, Development |
| `LOGIN_PASSWORD` | `1111` | Production, Preview, Development |
| `FLASK_SECRET_KEY` | (랜덤 문자열 생성) | Production, Preview, Development |

**FLASK_SECRET_KEY 생성 방법:**
```python
import secrets
print(secrets.token_hex(32))
```

### 4단계: 배포
1. "Deploy" 버튼 클릭
2. 배포 완료 대기 (약 1-2분)
3. 배포 완료 후 제공되는 URL로 접속

## 주의사항

### 1. 데이터베이스 제한사항
- Vercel은 serverless 환경이므로 파일 시스템이 임시적입니다
- **SQLite 데이터베이스는 배포 시마다 초기화될 수 있습니다**
- 프로덕션 환경에서는 외부 데이터베이스(PostgreSQL, MySQL 등) 사용 권장

### 2. 파일 업로드
- `uploads/` 디렉토리의 파일은 배포 시마다 사라질 수 있습니다
- 영구 저장이 필요하면 S3, Cloudinary 등 외부 스토리지 사용 권장

### 3. 엑셀 파일 경로
- `sup/domino_inventory_training.xlsx` 파일이 GitHub에 포함되어 있는지 확인
- `.gitignore`에서 제외되어 있지 않은지 확인

## 배포 후 확인사항

1. ✅ 환경 변수가 올바르게 설정되었는지 확인
2. ✅ 로그인 페이지가 정상적으로 표시되는지 확인
3. ✅ 비밀번호 `1111`로 로그인 가능한지 확인
4. ✅ 이메일 발송 기능이 정상 작동하는지 확인

## 문제 해결

### 배포 실패 시
- Vercel 대시보드의 "Deployments" 탭에서 로그 확인
- 환경 변수가 올바르게 설정되었는지 확인
- `requirements.txt`의 패키지 버전 호환성 확인

### 데이터베이스 오류 시
- Vercel은 읽기 전용 파일 시스템을 사용하므로 SQLite 쓰기 오류 발생 가능
- 프로덕션 환경에서는 외부 데이터베이스 사용 권장

## 대안: 다른 배포 플랫폼

Vercel이 적합하지 않은 경우:
- **Heroku**: PostgreSQL 지원, 파일 시스템 영구 저장
- **Railway**: 간단한 배포, PostgreSQL 지원
- **Render**: 무료 티어 제공, PostgreSQL 지원
- **AWS/GCP/Azure**: 더 많은 제어권, 복잡한 설정
