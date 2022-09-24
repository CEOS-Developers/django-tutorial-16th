# 1주차 미션: Django 튜토리얼

## 스터디 자료
[1주차 : Django와 개발 환경 설정](https://yourzinc.notion.site/1-Django-95b587b18097471c9a07e7cb8b2c598b)

## 📚 프로젝트 생성
<pre><code>$ django-admin startproject 디렉토리 이름</code></pre>
  
## 📚 서버 작동
<pre><code>$ python manage.py runserver</code></pre>
- 서버 작동시 커맨드라인 출력 내용
<pre><code>
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

8월 03, 2020 - 15:50:53
Django version 3.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
</code></pre>
- 포트 변경하기
서버의 포트를 변경하고 싶다면, 커맨드라인에서 인수를 전달해줍니다.
<pre><code>$ python manage.py runserver 8080</code></pre>

## 📚 앱 만들기
<pre><code>$ python manage.py startapp 앱 이름</code></pre>


## 📚 path() 함수
### path() 인수
- route
  - URL 패턴을 가진 문자열
  - urlpatterns와 요청된 URL을 각 패턴과 리스트의 순서대로 비교
- view
  - 일치하는 패턴을 찾을 시, 키워드 인수로 특정 view 함수 호출
- kwargs
  - 키워드 인수를 목표 view에 사전형으로 전달
- name
  - URL에 이름을 부여하여 명확하게 참조 
 

## Part2

## Part3

## Part4
