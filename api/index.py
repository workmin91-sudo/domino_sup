"""
Vercel serverless function entry point
"""
import sys
import os

# 프로젝트 루트를 Python 경로에 추가
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# 작업 디렉토리를 프로젝트 루트로 변경
os.chdir(project_root)

from app import app

# Vercel은 WSGI 앱을 직접 export하면 자동으로 처리합니다
# handler 함수는 선택사항이지만, 명시적으로 제공할 수도 있습니다
def handler(request):
    """Vercel serverless function handler"""
    return app(request.environ, request.start_response)

# Vercel이 인식하는 변수명
# app 변수를 직접 export하면 Vercel이 자동으로 WSGI 앱으로 인식합니다
