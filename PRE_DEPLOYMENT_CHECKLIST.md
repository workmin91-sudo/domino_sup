# 배포 전 체크리스트

## ✅ 사전 준비 사항

### 1. GitHub 저장소 준비
- [ ] GitHub 계정 생성/로그인
- [ ] 새 저장소 생성
- [ ] 로컬 프로젝트를 GitHub에 푸시

### 2. Vercel 계정 준비
- [ ] [Vercel](https://vercel.com) 계정 생성 (GitHub 연동 권장)
- [ ] Vercel 대시보드 접속 가능 확인

### 3. 환경 변수 값 준비
다음 값들을 준비해두세요:

#### 필수 값
- [ ] **EMAIL_PASSWORD**: `zewwbliyyqfjrntd` (Gmail 앱 비밀번호)
- [ ] **LOGIN_PASSWORD**: `1111` (웹 접속 비밀번호)

#### 선택 값 (기본값 사용 가능)
- [ ] **FLASK_SECRET_KEY**: 랜덤 문자열 생성
  ```python
  # Python에서 생성:
  import secrets
  print(secrets.token_hex(32))
  ```

### 4. 파일 확인
- [ ] `sup/domino_inventory_training.xlsx` 파일이 프로젝트에 포함되어 있는지 확인
- [ ] `.gitignore`에서 엑셀 파일이 제외되지 않았는지 확인

### 5. 코드 확인
- [ ] `requirements.txt`에 모든 패키지가 포함되어 있는지 확인
- [ ] `vercel.json` 파일이 생성되었는지 확인
- [ ] `api/index.py` 파일이 생성되었는지 확인

## 📋 Vercel 배포 시 설정할 항목

### 프로젝트 설정
- Framework Preset: **Other**
- Root Directory: `./` (기본값)
- Build Command: (비워두기)
- Output Directory: (비워두기)

### 환경 변수 설정 (Settings > Environment Variables)

#### Production 환경
```
EMAIL_PASSWORD = zewwbliyyqfjrntd
LOGIN_PASSWORD = 1111
FLASK_SECRET_KEY = [생성한 랜덤 문자열]
```

#### Preview 환경 (선택사항)
```
EMAIL_PASSWORD = zewwbliyyqfjrntd
LOGIN_PASSWORD = 1111
FLASK_SECRET_KEY = [생성한 랜덤 문자열]
```

#### Development 환경 (선택사항)
```
EMAIL_PASSWORD = zewwbliyyqfjrntd
LOGIN_PASSWORD = 1111
FLASK_SECRET_KEY = [생성한 랜덤 문자열]
```

## ⚠️ 주의사항

### 데이터베이스 제한
- Vercel은 serverless 환경이므로 **SQLite 데이터베이스가 배포 시마다 초기화될 수 있습니다**
- 프로덕션 환경에서는 외부 데이터베이스(PostgreSQL 등) 사용을 권장합니다
- 현재는 개발/테스트 목적으로만 사용하세요

### 파일 저장 제한
- `uploads/` 디렉토리의 파일은 배포 시마다 사라질 수 있습니다
- 영구 저장이 필요하면 외부 스토리지(S3 등) 사용을 권장합니다

## 🚀 배포 후 확인사항

배포 완료 후 다음을 확인하세요:

1. [ ] 배포된 URL로 접속 가능한지 확인
2. [ ] 로그인 페이지가 정상적으로 표시되는지 확인
3. [ ] 비밀번호 `1111`로 로그인 가능한지 확인
4. [ ] 재고 목록이 정상적으로 표시되는지 확인
5. [ ] 이메일 발송 기능이 정상 작동하는지 확인

## 📞 문제 발생 시

- Vercel 대시보드의 "Deployments" 탭에서 로그 확인
- 환경 변수가 올바르게 설정되었는지 재확인
- `DEPLOYMENT.md` 파일의 문제 해결 섹션 참고
