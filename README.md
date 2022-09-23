# 1주차 미션: Django 튜토리얼

## 스터디 자료
[1주차 : Django와 개발 환경 설정](https://yourzinc.notion.site/1-Django-95b587b18097471c9a07e7cb8b2c598b)

## 미션
- [Writing your first Django app](https://docs.djangoproject.com/ko/3.0/intro/tutorial01/)의 Part 1~4 따라합니다.
- 코딩의 단위를 기능별로 나누어 Commit 메세지를 작성합니다.
- 새롭게 알게 된 것을 정리합니다.

## 목표

- Django 의 MTV 패턴을 이해합니다.

## 기한

- 2022년 9월 24일 토요일  

## 과제를 하면서 알게 된 점  
#### 데이터베이스
- sqlite는 처음 사용해 보는데 파이썬 쉘을 실행해서 데이터베이스에 insert나 delete 등을 할 수 있구나 알게 되었다.
- 파이썬 쉘: python manage.py shell

#### 관리자
- admin 페이지를 사용해 보는 것은 처음인데 따로 만들 필요 없이 관리용 메뉴가 다 있다는 점이 인상깊었다.

#### 뷰
- HttpResponse, Http404, render 등 다양한 리턴을 해보면서 각각에 대해 알아볼 수 있어서 좋았다.
- 템플릿 사용은 처음 해본다. Django로 만든 기능들을 html을 통해 확인할 수 있다는 점이 신기했고 하드코딩 없이 만드는 방법까지 알게 되어 좋았다.
- 제네릭 뷰를 제공해 코드를 길게 작성할 필요가 없다는 점이 너무 편리한 것 같다!

#### Secret Key
- 보안상 문제로 settings.py에 적혀있는 secret key를 숨겨야 하는데 어떻게 하는지 방법을 알게 되었다.