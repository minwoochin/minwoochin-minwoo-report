My Personal Website (Django Project)
1. 프로젝트 개요
이 프로젝트는 Django를 사용하여 본인을 소개하는 웹 애플리케이션입니다. 개인 소개, 관심 분야, 개발 실적 등을 포함하며 자유롭게 디자인할 수 있습니다.

2. 프로젝트 다운로드 및 환경 설정
  1)GitHub에서 프로젝트 다운로드
     GitHub 저장소 이동: minwoochin-minwoo-report
     "Code" 버튼 클릭
     "Download ZIP" 선택하여 압축 파일 다운로드
     압축 해제 후 원하는 폴더에 저장
     또는 Git 명령어를 사용하여 직접 클론할 수도 있습니다.

 ->git clone https://github.com/minwoochin/minwoo-report.git
    cd minwoochin-minwoo-report

3. Python 설치 확인(설치 여부 확인)
   -> python --version
설치되어 있지 않다면 Python 공식 웹사이트에서 다운로드 후 설치

3.가상 환경 설정 및 Django 설치
  가상 환경 생성 및 활성화
 -> python -m venv myenv
 -> source myenv/bin/activate

4. Django 및 필수 패키지 설치
->pip install -r requirements.txt


Django 설치 확인
->django-admin --version

3. 프로젝트 실행 방법
   1) 데이터베이스 초기화
-> python manage.py migrate

   2) 서버 실행
-> python manage.py runserver
    브라우저에서 http://127.0.0.1:8000/ 로 접속하여 실행 결과를 확인
