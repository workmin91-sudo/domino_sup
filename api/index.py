"""
Vercel serverless function entry point
"""
import sys
import os

# 프로젝트 루트를 Python 경로에 추가
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Vercel 환경 변수 설정
os.environ.setdefault('VERCEL', '1')

# 앱 import 전에 환경 변수 로드
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass  # dotenv가 없어도 계속 진행

# 앱 import 및 초기화
try:
    from app import app
    
    # Vercel 환경에서 데이터베이스 초기화 (한 번만 실행)
    if not hasattr(app, '_vercel_initialized'):
        try:
            from app import init_db
            init_db()
            # 엑셀 파일이 있으면 로드 시도 (없어도 계속 진행)
            try:
                from app import load_excel_data
                load_excel_data()
            except Exception as e:
                # 엑셀 파일이 없어도 계속 진행
                pass
            app._vercel_initialized = True
        except Exception as e:
            # 초기화 실패해도 앱은 계속 실행
            app._vercel_initialized = True
    
except Exception as e:
    # 오류 발생 시 간단한 오류 응답 앱 생성
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/<path:path>')
    @app.route('/')
    def error_handler(path=''):
        import traceback
        error_msg = str(e)
        traceback_msg = traceback.format_exc()
        return f"Application initialization error: {error_msg}<br><pre>{traceback_msg}</pre>", 500

# Vercel은 app 변수를 직접 export하면 자동으로 WSGI 앱으로 인식합니다
