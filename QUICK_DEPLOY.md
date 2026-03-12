# 🚀 Vercel 빠른 배포 가이드

## 현재 상태
- ✅ GitHub에 코드 푸시 완료
- ✅ Vercel 배포 설정 파일 준비 완료
- ⏳ Vercel 프로젝트 연결 및 배포 필요

## ⚡ 빠른 배포 (3단계)

### 1단계: Vercel 프로젝트 생성
1. **https://vercel.com/new** 접속
2. "Import Git Repository" 클릭
3. GitHub 저장소 선택: **`workmin91-sudo/domino_sup`**
4. 프로젝트 설정:
   - **Framework Preset**: `Other` 선택
   - **Root Directory**: `./` (기본값)
   - **Build Command**: (비워두기)
   - **Output Directory**: (비워두기)

### 2단계: 환경 변수 설정 (중요!)
프로젝트 생성 후 "Environment Variables" 섹션에서 다음 추가:

```
EMAIL_PASSWORD = zewwbliyyqfjrntd
LOGIN_PASSWORD = 1111
FLASK_SECRET_KEY = a9362c789b12cd3c4490c99e75370fd14a9c0637e79cf23b66683cd23a551d5e
```

**각 환경 변수에 대해:**
- Environment: Production, Preview, Development 모두 체크

### 3단계: 배포
1. "Deploy" 버튼 클릭
2. 배포 완료 대기 (약 1-2분)
3. 배포 완료 후 **URL이 표시됩니다!**

## 📍 배포 URL 형식

배포 완료 후 URL은 다음과 같은 형식입니다:
```
https://domino-sup-[랜덤문자].vercel.app
또는
https://domino-sup.vercel.app (커스텀 도메인 설정 시)
```

## ✅ 배포 후 확인

1. 배포된 URL로 접속
2. 로그인 페이지 확인
3. 비밀번호 `1111`로 로그인
4. 재고 관리 시스템 정상 작동 확인

## 🔗 유용한 링크

- **Vercel 대시보드**: https://vercel.com/dashboard
- **프로젝트 생성**: https://vercel.com/new
- **GitHub 저장소**: https://github.com/workmin91-sudo/domino_sup
