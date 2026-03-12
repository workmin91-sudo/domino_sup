"""
Vercel serverless function entry point
"""
import sys
import os
import traceback

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
app = None
init_error = None

try:
    from app import app
    
    # Flask 앱에 오류 핸들러 추가
    @app.errorhandler(500)
    def handle_500(e):
        import traceback
        error_trace = traceback.format_exc()
        return f"""
        <h1>Internal Server Error</h1>
        <p>Error: {str(e)}</p>
        <pre>{error_trace}</pre>
        """, 500
    
    @app.errorhandler(Exception)
    def handle_exception(e):
        import traceback
        error_trace = traceback.format_exc()
        return f"""
        <h1>Application Error</h1>
        <p>Error: {str(e)}</p>
        <pre>{error_trace}</pre>
        """, 500
    
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
                print(f"Excel load warning: {e}")
            app._vercel_initialized = True
        except Exception as e:
            # 초기화 실패해도 앱은 계속 실행
            print(f"Init warning: {e}")
            app._vercel_initialized = True
    
except Exception as e:
    # 오류 발생 시 간단한 오류 응답 앱 생성
    init_error = e
    error_trace = traceback.format_exc()
    
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/<path:path>')
    @app.route('/')
    def error_handler(path=''):
        return f"""
        <h1>Application Initialization Error</h1>
        <p>Error: {str(init_error)}</p>
        <pre>{error_trace}</pre>
        """, 500

# Vercel은 app 변수를 직접 export하면 자동으로 WSGI 앱으로 인식합니다
