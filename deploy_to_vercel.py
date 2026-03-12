"""
Vercel 자동 배포 스크립트
주의: Vercel API 토큰이 필요합니다.
"""
import os
import subprocess
import sys

def check_git_status():
    """Git 상태 확인"""
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Git 저장소 확인 완료")
            return True
        else:
            print("❌ Git 저장소가 아닙니다")
            return False
    except FileNotFoundError:
        print("❌ Git이 설치되어 있지 않습니다")
        return False

def push_to_github():
    """GitHub에 푸시"""
    try:
        print("\n📤 GitHub에 푸시 중...")
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Auto deploy to Vercel'], check=True)
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        print("✅ GitHub 푸시 완료!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Git 푸시 실패: {e}")
        return False

def main():
    print("=" * 50)
    print("Vercel 자동 배포 스크립트")
    print("=" * 50)
    
    # Git 상태 확인
    if not check_git_status():
        sys.exit(1)
    
    # GitHub에 푸시
    if push_to_vercel():
        print("\n✅ 모든 작업 완료!")
        print("\n다음 단계:")
        print("1. Vercel 대시보드에서 프로젝트 연결")
        print("2. 환경 변수 설정:")
        print("   - EMAIL_PASSWORD = zewwbliyyqfjrntd")
        print("   - LOGIN_PASSWORD = 1111")
        print("   - FLASK_SECRET_KEY = a9362c789b12cd3c4490c99e75370fd14a9c0637e79cf23b66683cd23a551d5e")
        print("3. Deploy 버튼 클릭")
    else:
        print("\n⚠️  Git 푸시는 완료되었지만, Vercel 배포는 수동으로 진행해주세요")

if __name__ == '__main__':
    main()
