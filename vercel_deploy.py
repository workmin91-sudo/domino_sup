"""
Vercel 자동 배포 스크립트
Vercel API를 사용하여 프로젝트를 자동으로 배포합니다.
"""
import requests
import json
import os
import sys

# Vercel API 엔드포인트
VERCEL_API_BASE = "https://api.vercel.com"

def deploy_to_vercel(api_token=None):
    """Vercel에 프로젝트 배포"""
    
    # Vercel API 토큰 확인
    if not api_token:
        api_token = os.getenv('VERCEL_TOKEN')
    
    if not api_token:
        print("=" * 60)
        print("⚠️  Vercel API 토큰이 필요합니다!")
        print("=" * 60)
        print("\n다음 단계를 따라주세요:")
        print("1. https://vercel.com/account/tokens 접속")
        print("2. 'Create Token' 클릭")
        print("3. 토큰 이름 입력 (예: deploy-token)")
        print("4. 생성된 토큰 복사")
        print("\n토큰을 제공해주시면 자동 배포를 진행하겠습니다.")
        print("\n또는 환경 변수로 설정:")
        print("  set VERCEL_TOKEN=your_token_here  (Windows)")
        print("  export VERCEL_TOKEN=your_token_here  (Linux/Mac)")
        return False, None
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    # 프로젝트 정보
    project_name = "domino-sup"
    repo_url = "https://github.com/workmin91-sudo/domino_sup.git"
    
    print("=" * 60)
    print("Vercel 자동 배포 시작")
    print("=" * 60)
    
    try:
        # 1. 프로젝트 생성 또는 확인
        print("\n📦 프로젝트 확인 중...")
        projects_url = f"{VERCEL_API_BASE}/v9/projects"
        response = requests.get(projects_url, headers=headers)
        
        if response.status_code == 200:
            projects = response.json().get('projects', [])
            existing_project = next((p for p in projects if p['name'] == project_name), None)
            
            if existing_project:
                print(f"✅ 기존 프로젝트 발견: {project_name}")
                project_id = existing_project['id']
            else:
                print(f"📝 새 프로젝트 생성 중: {project_name}")
                create_data = {
                    "name": project_name,
                    "gitRepository": {
                        "type": "github",
                        "repo": "workmin91-sudo/domino_sup"
                    },
                    "framework": None
                }
                create_response = requests.post(projects_url, headers=headers, json=create_data)
                if create_response.status_code in [200, 201]:
                    project_id = create_response.json().get('id')
                    print(f"✅ 프로젝트 생성 완료: {project_id}")
                else:
                    print(f"❌ 프로젝트 생성 실패: {create_response.text}")
                    return False
        
        # 2. 환경 변수 설정
        print("\n🔐 환경 변수 설정 중...")
        env_vars = {
            "EMAIL_PASSWORD": "zewwbliyyqfjrntd",
            "LOGIN_PASSWORD": "1111",
            "FLASK_SECRET_KEY": "a9362c789b12cd3c4490c99e75370fd14a9c0637e79cf23b66683cd23a551d5e"
        }
        
        env_url = f"{VERCEL_API_BASE}/v9/projects/{project_name}/env"
        
        for key, value in env_vars.items():
            # 기존 환경 변수 확인
            get_env = requests.get(env_url, headers=headers, params={"key": key})
            if get_env.status_code == 200 and get_env.json().get('envs'):
                print(f"  ⚠️  {key} 이미 존재 (업데이트 필요시 수동으로)")
            else:
                env_data = {
                    "key": key,
                    "value": value,
                    "type": "encrypted",
                    "target": ["production", "preview", "development"]
                }
                env_response = requests.post(env_url, headers=headers, json=env_data)
                if env_response.status_code in [200, 201]:
                    print(f"  ✅ {key} 설정 완료")
                else:
                    print(f"  ⚠️  {key} 설정 실패: {env_response.text}")
        
        # 3. 배포 트리거
        print("\n🚀 배포 시작...")
        deploy_url = f"{VERCEL_API_BASE}/v13/deployments"
        deploy_data = {
            "name": project_name,
            "project": project_name,
            "target": "production"
        }
        
        deploy_response = requests.post(deploy_url, headers=headers, json=deploy_data)
        
        if deploy_response.status_code in [200, 201]:
            deployment = deploy_response.json()
            deployment_url = deployment.get('url', '')
            deployment_id = deployment.get('id', '')
            
            # 배포 상태 확인
            print(f"\n✅ 배포 시작 성공!")
            print(f"📦 배포 ID: {deployment_id}")
            print(f"🌐 배포 URL: https://{deployment_url}")
            print(f"\n⏳ 배포 진행 중... (약 1-2분 소요)")
            
            # 배포 완료 대기
            import time
            check_url = f"{VERCEL_API_BASE}/v13/deployments/{deployment_id}"
            max_wait = 120  # 최대 2분 대기
            waited = 0
            
            while waited < max_wait:
                time.sleep(5)
                waited += 5
                status_response = requests.get(check_url, headers=headers)
                if status_response.status_code == 200:
                    status_data = status_response.json()
                    state = status_data.get('readyState', '')
                    if state == 'READY':
                        print(f"\n🎉 배포 완료!")
                        final_url = status_data.get('url', deployment_url)
                        print(f"🌐 최종 URL: https://{final_url}")
                        return True, final_url
                    elif state == 'ERROR':
                        print(f"\n❌ 배포 실패")
                        return False, None
                    else:
                        print(f"  ⏳ 배포 진행 중... ({state})")
            
            print(f"\n⚠️  배포가 완료되지 않았습니다. Vercel 대시보드에서 확인하세요.")
            print(f"🌐 예상 URL: https://{deployment_url}")
            return True, deployment_url
        else:
            print(f"❌ 배포 실패: {deploy_response.text}")
            print("\n💡 대안: Vercel이 GitHub 저장소 변경을 감지하여 자동 배포합니다.")
            print("   GitHub에 푸시하면 자동으로 배포가 시작됩니다.")
            return False, None
    
    except Exception as e:
        print(f"❌ 오류 발생: {str(e)}")
        return False

if __name__ == '__main__':
    import sys
    
    print("\n" + "=" * 60)
    print("Vercel 자동 배포 스크립트")
    print("=" * 60)
    
    # 명령줄 인자로 토큰 전달 가능
    api_token = None
    if len(sys.argv) > 1:
        api_token = sys.argv[1]
        print(f"\n✅ API 토큰을 명령줄 인자로 받았습니다.")
    else:
        print("\n⚠️  API 토큰이 필요합니다.")
        print("   사용법: python vercel_deploy.py YOUR_TOKEN")
        print("   또는 환경 변수: set VERCEL_TOKEN=YOUR_TOKEN")
        print("\n토큰 발급: https://vercel.com/account/tokens")
    
    if api_token or os.getenv('VERCEL_TOKEN'):
        print("\n🚀 자동 배포 시작...\n")
        success, url = deploy_to_vercel(api_token)
        
        if success and url:
            print("\n" + "=" * 60)
            print("✅ 배포 완료!")
            print("=" * 60)
            print(f"\n🌐 배포 URL: https://{url}")
            print(f"\n📝 다음 단계:")
            print(f"1. https://{url} 접속")
            print(f"2. 비밀번호 '1111'로 로그인")
            print(f"3. 재고 관리 시스템 사용 시작!")
        else:
            print("\n" + "=" * 60)
            print("❌ 배포 실패")
            print("=" * 60)
            print("\n수동 배포 가이드: QUICK_DEPLOY.md 파일 참고")
    else:
        print("\n" + "=" * 60)
        print("📋 수동 배포 가이드")
        print("=" * 60)
        print("\n1. https://vercel.com/new 접속")
        print("2. GitHub 저장소 선택: workmin91-sudo/domino_sup")
        print("3. 프로젝트 설정:")
        print("   - Framework Preset: Other")
        print("   - Root Directory: ./")
        print("4. Environment Variables 추가:")
        print("   - EMAIL_PASSWORD = zewwbliyyqfjrntd")
        print("   - LOGIN_PASSWORD = 1111")
        print("   - FLASK_SECRET_KEY = a9362c789b12cd3c4490c99e75370fd14a9c0637e79cf23b66683cd23a551d5e")
        print("5. Deploy 클릭")
        print("\n배포 완료 후 URL이 표시됩니다!")
