# 환경 변수 설정 가이드

## Vercel (또는 다른 플랫폼)에 설정할 환경 변수

다음 환경 변수들을 플랫폼에 설정해주세요:

### 필수 환경 변수

| Key | 설명 | 예시 값 |
|-----|------|---------|
| `EMAIL_PASSWORD` | Gmail 앱 비밀번호 | `zewwbliyyqfjrntd` |
| `LOGIN_PASSWORD` | 웹 접속 비밀번호 | `1111` |

### 선택 환경 변수

| Key | 설명 | 기본값 |
|-----|------|--------|
| `EMAIL_SENDER` | 발신 이메일 주소 | `workmin91@gmail.com` |
| `SMTP_SERVER` | SMTP 서버 주소 | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP 포트 | `587` |
| `DATABASE` | 데이터베이스 파일명 | `inventory.db` |
| `DEFAULT_MIN_STOCK` | 기본 최소 재고 기준 | `10` |
| `FLASK_SECRET_KEY` | Flask 세션 암호화 키 | (랜덤 문자열 권장) |

## Vercel 설정 방법

1. Vercel 대시보드에서 프로젝트 선택
2. Settings > Environment Variables 메뉴로 이동
3. 각 환경 변수를 추가:
   - **Name**: 환경 변수 Key (예: `EMAIL_PASSWORD`)
   - **Value**: 환경 변수 Value (예: `zewwbliyyqfjrntd`)
   - **Environment**: Production, Preview, Development (필요에 따라 선택)

## 로컬 개발 환경 설정

로컬에서 개발할 때는 `.env` 파일을 생성하여 환경 변수를 설정할 수 있습니다:

1. `.env.example` 파일을 `.env`로 복사
2. `.env` 파일에 실제 값 입력

```bash
# .env 파일 예시
EMAIL_PASSWORD=zewwbliyyqfjrntd
LOGIN_PASSWORD=1111
FLASK_SECRET_KEY=your-secret-key-here
```

**주의**: `.env` 파일은 Git에 커밋하지 마세요! (이미 .gitignore에 포함되어 있습니다)
