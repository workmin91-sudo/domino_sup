"""
Vercel serverless function entry point
"""
import sys
import os

# 프로젝트 루트를 Python 경로에 추가
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Vercel 환경 변수 설정
os.environ['VERCEL'] = '1'

# 환경 변수 로드 (선택적)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# 앱 import
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
            except:
                pass
        except Exception as e:
            # 초기화 실패해도 앱은 계속 실행
            pass
        finally:
            app._vercel_initialized = True
    
except Exception as e:
    # 오류 발생 시 오류 응답 앱 생성
    from flask import Flask
    import traceback
    
    app = Flask(__name__)
    error_msg = str(e)
    error_trace = traceback.format_exc()
    
    @app.route('/<path:path>')
    @app.route('/')
    def error_handler(path=''):
        return f"""
        <html>
        <head>
            <title>Initialization Error</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                pre {{ background: #f5f5f5; padding: 15px; border-radius: 5px; overflow: auto; }}
            </style>
        </head>
        <body>
        <h1>Application Initialization Error</h1>
        <p><strong>Error:</strong> {error_msg}</p>
        <h2>Traceback:</h2>
        <pre>{error_trace}</pre>
        </body>
        </html>
        """, 500

# Vercel은 app 변수를 직접 export하면 자동으로 WSGI 앱으로 인식합니다
