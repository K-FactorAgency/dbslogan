# Nemo-Coded-by-ChatGPT

"Nemo"는 Django에 기반한 PoC(Proof of Concept) 수준의 미니 SNS 애플리케이션입니다.

이 애플리케이션은 "**과연 AI 챗봇과의 대화 만으로 간단한 웹 애플리케이션을 만들어낼 수 있을까**" 라는 의문을 해소하기 위한 실험의 결과로 만들어졌습니다. 
이 애플리케이션에 포함된 **모델(Models), 뷰(Views), 템플릿(Templates) 그리고 URL 패턴** 코드들은 모두 **ChatGPT에서의 프롬프트 입력 만으로 완성**되었습니다.

ChatGPT로 "Nemo"를 개발하는 실험 과정은 아래 블로그 글에서 자세히 확인하실 수 있습니다.
* https://seongjin.me/experiment-of-creating-web-app-with-chatgpt/

## 주요 기능

* Django 프레임워크와 Bootstrap을 사용합니다.
* 사용자명(`username`)과 비밀번호(`password`)로 등록하고 로그인할 수 있습니다.
* 인덱스(`index`) 페이지에는 모든 사용자의 포스트들이 노출됩니다.
* 로그인한 사용자는 1,000자 이내의 포스트를 올릴 수 있습니다.
* 로그인한 사용자는 자신이 올린 포스트를 삭제할 수 있습니다.
* 로그인한 사용자는 다른 사용자의 포스트에 '좋아요'를 추가하거나 취소할 수 있습니다.

## 동작 화면
### 사용자 등록 및 로그인
![사용자 등록 및 로그인 화면](https://seongjin.me/content/images/2023/02/nemo-register-login.gif)

### 포스트 작성 및 게시
![포스트 작성 및 게시 화면](https://seongjin.me/content/images/2023/02/nemo-post-creation.gif)

### 좋아요 추가 및 취소
![좋아요 추가 및 취소 화면](https://seongjin.me/content/images/2023/02/nemo-login-like.gif)


## 설치 방법

1. 원하시는 경로에 `git clone`으로 이 저장소의 코드들을 내려받습니다.
2. `pip3 install virtualenv` 명령으로 가상 환경(virtualenv)을 설치합니다.
3. `pip3 install django` 명령으로 Django 최신 버전을 설치합니다.
4. `chatgpt_coding_test/settings.py` 파일을 편집기로 열어 `SECRET_KEY`에 키값을 입력합니다. [Djecrety](https://djecrety.ir/)에서 필요한 키값을 생성하실 수 있습니다.
5. 프로젝트 디렉터리로 돌아와 `python manage.py makemigrations nemo`, `python manage.py migrate` 명령을 차례로 실행하여 모델 마이그레이션을 완료합니다.
6. `python manage.py runserver` 명령으로 서버를 구동시킵니다.
