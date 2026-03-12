# 🚀 Vercel 자동 배포 단계별 가이드

## ⚡ 빠른 배포 (약 5분 소요)

### 1단계: Vercel 프로젝트 생성
**링크**: https://vercel.com/new

1. "Import Git Repository" 클릭
2. GitHub 저장소 선택: **`workmin91-sudo/domino_sup`**
3. 프로젝트 설정:
   - **Framework Preset**: `Other` 선택
   - 나머지는 기본값 유지

### 2단계: 환경 변수 설정 (중요!)
프로젝트 생성 화면에서 "Environment Variables" 섹션을 찾아 다음 추가:

| Key | Value |
|-----|-------|
| `EMAIL_PASSWORD` | `zewwbliyyqfjrntd` |
| `LOGIN_PASSWORD` | `1111` |
| `FLASK_SECRET_KEY` | `a9362c789b12cd3c4490c99e75370fd14a9c0637e79cf23b66683cd23a551d5e` |

**각 환경 변수 추가 시:**
- Environment: **Production, Preview, Development 모두 체크**

### 3단계: 배포 시작
1. "Deploy" 버튼 클릭
2. 배포 진행 상황 확인 (약 1-2분)
3. 배포 완료 후 **URL이 표시됩니다!**

## 📍 배포 URL 확인 방법

배포 완료 후:
1. Vercel 대시보드에서 프로젝트 클릭
2. "Deployments" 탭에서 최신 배포 확인
3. 배포된 URL 클릭하여 접속

**URL 형식:**
```
https://domino-sup-[랜덤문자].vercel.app
또는
https://domino-sup.vercel.app
```

## ✅ 배포 후 확인사항

1. 배포된 URL로 접속
2. 로그인 페이지 확인
3. 비밀번호 `1111`로 로그인
4. 재고 관리 시스템 정상 작동 확인

## 🔄 자동 배포

GitHub에 푸시하면 Vercel이 자동으로 재배포합니다:
```bash
git add .
git commit -m "Update"
git push origin main
```

## 📞 문제 발생 시

- Vercel 대시보드 → 프로젝트 → "Deployments" → 로그 확인
- 환경 변수가 올바르게 설정되었는지 확인
- `VERCEL_DEPLOY_INSTRUCTIONS.md` 파일 참고
