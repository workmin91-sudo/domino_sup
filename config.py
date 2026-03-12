import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# 이메일 설정
EMAIL_SENDER = os.getenv('EMAIL_SENDER', 'workmin91@gmail.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', '')  # 환경 변수에서 가져옴
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))

# 웹 접속 비밀번호
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD', '1111')  # 환경 변수에서 가져옴

# 데이터베이스 설정
# Vercel 환경에서는 /tmp 디렉토리 사용 (쓰기 가능한 유일한 디렉토리)
if os.getenv('VERCEL'):
    DATABASE = '/tmp/inventory.db'
else:
    DATABASE = os.getenv('DATABASE', 'inventory.db')

# 재고 최소 기준 (예시)
DEFAULT_MIN_STOCK = int(os.getenv('DEFAULT_MIN_STOCK', '10'))
