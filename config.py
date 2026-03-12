import os

# 환경 변수 로드 (로컬 개발 환경에서만)
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass  # dotenv가 없거나 Vercel 환경에서는 무시

# 이메일 설정
EMAIL_SENDER = os.getenv('EMAIL_SENDER', 'workmin91@gmail.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', '')  # 환경 변수에서 가져옴
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')

# SMTP_PORT 안전하게 처리
try:
    SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
except (ValueError, TypeError):
    SMTP_PORT = 587

# 웹 접속 비밀번호
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD', '1111')  # 환경 변수에서 가져옴

# 데이터베이스 설정
# Vercel 환경에서는 /tmp 디렉토리 사용 (쓰기 가능한 유일한 디렉토리)
if os.getenv('VERCEL'):
    DATABASE = '/tmp/inventory.db'
else:
    DATABASE = os.getenv('DATABASE', 'inventory.db')

# 재고 최소 기준 (예시)
try:
    DEFAULT_MIN_STOCK = int(os.getenv('DEFAULT_MIN_STOCK', '10'))
except (ValueError, TypeError):
    DEFAULT_MIN_STOCK = 10
