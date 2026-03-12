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

# Vercel serverless function handler
def handler(request):
    """Vercel serverless function handler"""
    return app(request.environ, request.start_response)

# WSGI 호환을 위한 export
__all__ = ['handler', 'app']
