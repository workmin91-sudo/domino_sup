# Vercel 배포 완료 가이드

## ✅ 완료된 작업

1. ✅ Git 저장소 초기화 및 커밋 완료
2. ✅ GitHub에 푸시 완료 (https://github.com/workmin91-sudo/domino_sup)
3. ✅ Vercel 배포 설정 파일 준비 완료

## 🚀 Vercel 배포 단계 (웹 대시보드)

### 1단계: Vercel 프로젝트 생성

1. [Vercel 대시보드](https://vercel.com/dashboard) 접속
2. "Add New..." → "Project" 클릭
3. GitHub 저장소 선택: **`workmin91-sudo/domino_sup`**
4. 프로젝트 설정:
   - **Framework Preset**: `Other`
   - **Root Directory**: `./` (기본값)
   - **Build Command**: (비워두기)
   - **Output Directory**: (비워두기)
   - **Install Command**: (비워두기)

### 2단계: 환경 변수 설정 (중요!)

프로젝트 생성 후 "Environment Variables" 탭에서 다음을 추가:

| Key | Value | Environment |
|-----|-------|-------------|
| `EMAIL_PASSWORD` | `zewwbliyyqfjrntd` | Production, Preview, Development |
| `LOGIN_PASSWORD` | `1111` | Production, Preview, Development |
| `FLASK_SECRET_KEY` | `a9362c789b12cd3c4490c99e75370fd14a9c0637e79cf23b66683cd23a551d5e` | Production, Preview, Development |

**설정 방법:**
1. 프로젝트 설정 → "Environment Variables" 탭
2. 각 환경 변수 추가:
   - Name: 환경 변수 Key
   - Value: 환경 변수 Value
   - Environment: Production, Preview, Development 모두 체크
3. "Save" 클릭

### 3단계: 배포

1. "Deploy" 버튼 클릭
2. 배포 완료 대기 (약 1-2분)
3. 배포 완료 후 제공되는 URL로 접속
4. 로그인 비밀번호: `1111`

## 📝 배포 후 확인사항

- [ ] 배포된 URL로 접속 가능
- [ ] 로그인 페이지 정상 표시
- [ ] 비밀번호 `1111`로 로그인 가능
- [ ] 재고 목록 정상 표시
- [ ] 이메일 발송 기능 정상 작동

## ⚠️ 주의사항

1. **데이터베이스**: Vercel은 serverless 환경이므로 SQLite 데이터베이스가 배포 시마다 초기화될 수 있습니다.
2. **파일 저장**: `uploads/` 디렉토리의 파일은 배포 시마다 사라질 수 있습니다.

## 🔗 유용한 링크

- GitHub 저장소: https://github.com/workmin91-sudo/domino_sup
- Vercel 대시보드: https://vercel.com/dashboard
