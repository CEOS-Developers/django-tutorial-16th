# 1주차 미션: Django 튜토리얼
## 📚 What I learned
### 📌 path의 인수
* route
  - 필수 인수
  - URL 패턴을 가진 문자열
  - 요청된 url을 urlpatterns에서 찾음
* view
  - 필수 인수
  - 일치하는 패턴을 찾은 경우, 해당 view 함수를 호출함
* kwargs
  - 목표한 view에 사전형으로 전달
* name
  - Django 어디에서나 명확하게 참조할 수 있도록 URL에 이름을 지음

### 📌 Model
* 부가적인 메타데이터를 가진 데이터베이스의 구조(layout)
* 데이터베이스의 각 필드는 Field 클래스의 인스턴스로 표현됨
* Field는 다양한 선택적 인수들을 가질 수 있음 (필수 인수가 있는 경우도 존재)

### 📌 Python Shell
* Django에서 동작하는 모든 명령을 대화식 Python 쉘에서 그대로 시험해 볼 수 있음
```shell
python manage.py shell
```

### 📌 Django 관리자
* Django는 모델에 대한 관리용 인터페이스를 모두 자동으로 생성함
* http://127.0.0.1:8000/admin/으로 접근 가능
```shell
python manage.py createsuperuser
```

### 📌 View
* Django 어플리케이션이 일반적으로 특정 기능과 템플릿을 제공하는 웹페이지의 한 종류
* URLconf이 URL 패턴을 뷰에 연결

### 📌 View 작동
* HttpResponse 객체 반환
  1. HttpResponse
  2. render()
* Http404 예외 발생
  1. 단순 방법
  2. get_object_or_404()
  
### 📌 Generic View
- 일반적인 패턴을 추상화한 View
- URL에서 전달된 매개변수에 따라 DB에서 데이터를 가져오는 것
- 템플릿을 로드하고 렌더링된 템플릿을 리턴하는 것

### 📌 Generic View 사용
1. URLconf 수정</br>
DetailView 제너릭 뷰는 URL의 기본키 값을 pk로 여기므로, question_id를 pk로 변경한다.
2. views 수정
   - ListView
     개체 목록 표시
   - DetailView
     특정 개체 유형에 대한 세부 정보 페이지 표시

<hr/>

## 🔨 Refactor
### 📌 'Django Secret Key exposed on GitHub' 문제
원인 : SECRET_KEY를 깃헙에 푸쉬한다면 위 문제가 발생함</br>
해결 방법 : SECRET_KEY를 json 파일로 분리한 후, 이 값을 json 파일로부터 읽어서 사용한다면 문제 해결 가능



