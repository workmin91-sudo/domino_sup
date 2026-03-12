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

# 앱 import 및 초기화
app = None
init_error = None
error_trace = None

try:
    # 환경 변수 로드 (선택적)
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        pass
    
    # config import 테스트
    try:
        import config
        print("Config imported successfully")
    except Exception as e:
        print(f"Config import error: {e}")
        raise
    
    # app import
    try:
        from app import app
        print("App imported successfully")
    except Exception as e:
        print(f"App import error: {e}")
        raise
    
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
            print("Initializing database...")
            init_db()
            print("Database initialized")
            
            # 엑셀 파일이 있으면 로드 시도 (없어도 계속 진행)
            try:
                from app import load_excel_data
                load_excel_data()
                print("Excel data loaded")
            except Exception as e:
                # 엑셀 파일이 없어도 계속 진행
                print(f"Excel load warning: {e}")
            
            app._vercel_initialized = True
        except Exception as e:
            # 초기화 실패해도 앱은 계속 실행
            print(f"Init warning: {e}")
            import traceback
            print(traceback.format_exc())
            app._vercel_initialized = True
    
except Exception as e:
    # 오류 발생 시 상세 오류 정보와 함께 오류 응답 앱 생성
    init_error = e
    error_trace = traceback.format_exc()
    
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/<path:path>')
    @app.route('/')
    def error_handler(path=''):
        return f"""
        <html>
        <head><title>Application Initialization Error</title></head>
        <body>
        <h1>Application Initialization Error</h1>
        <p><strong>Error:</strong> {str(init_error)}</p>
        <h2>Traceback:</h2>
        <pre style="background: #f0f0f0; padding: 10px; overflow: auto;">{error_trace}</pre>
        </body>
        </html>
        """, 500

# Vercel은 app 변수를 직접 export하면 자동으로 WSGI 앱으로 인식합니다
