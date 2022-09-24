# 1주차 미션: Django 튜토리얼

## 스터디 자료
[1주차 : Django와 개발 환경 설정](https://yourzinc.notion.site/1-Django-95b587b18097471c9a07e7cb8b2c598b)

## 미션
- [Writing your first Django app](https://docs.djangoproject.com/ko/3.0/intro/tutorial01/)의 Part 1~4 따라합니다.
- 코딩의 단위를 기능별로 나누어 Commit 메세지를 작성합니다.
- 새롭게 알게 된 것을 정리합니다.

## 목표

- Django 의 MTV 패턴을 이해합니다.

## 배운 점

##### 1. appname/appname 폴더 내 파일들의 용도
`__init__.py`: Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일

`asgi.py`: 현재 프로젝트를 서비스하기 위한 ASGI 호환 웹 서버의 진입점입니다.

`wsgi.py`: 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점입니다.

..?

##### 2. 포트 변경하기
기본적으로, runserver 명령은 내부 IP 의 8000 번 포트로 개발 서버를 띄운다.
예를 들어
`python manage.py runserver 8080`하면 포트를 8080 으로 서버를 시작한다고 한다. 
어떤 상황에서 다른 포트를 쓰는건지 모르겠다. 

##### 3. path() 함수의 인수
route, view, kwargs, name 4가지의 인수를 가진다.
route, view는 필수 인자이고 나머지는 아니다. route, view, name는 튜토리얼에서도 보였지만 임의의 키워드 인수 kwargs를 쓰는 예를 보고 싶다. 

##### 4. INSTALLED_APPS
django.contrib.admin -- 관리용 사이트.

django.contrib.auth -- 인증 시스템.

django.contrib.contenttypes -- 컨텐츠 타입을 위한 프레임워크.

django.contrib.sessions -- 세션 프레임워크.

django.contrib.messages -- 메세징 프레임워크.

django.contrib.staticfiles -- 정적 파일을 관리하는 프레임워크.

프로젝트를 생성하고 마이그레이션하면 자동으로 실행되는 앱 중에서 필요 없는 앱이 있으면 주석처리하거나 지우고 첫 마이그레이션하라고 나와있었다. 이런 앱들이 있는 것도 몰랐는데 새로운 사실을 알게 되었다. 

##### 5. 사람이 읽기 좋은 모델 필드명
pub_date = models.DateTimeField('date published')

첫 번째 인수를 위처럼 전달하면 사람이 읽기 좋은 필드명을 만들어 준다고 하는데 그게 왜 필요한건지 궁금했다. 

##### 6. 내부적으로 실행하는 sql 문장
python manage.py sqlmigrate polls 0001

를 하면 polls 앱 내의 0001번 마이그레이션에서 내부적으로 실행된 sql 문장을 보여준다. 과연 쓸 일이 있을 지 모르겠지만 새롭게 알게 된 사실이다. 


##### 7. runserver 할 때마다 오류 메세지 등장

    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
    }
```
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': str(os.path.join(BASE_DIR, "db.sqlite3")),
  }
}
```

위에서 아래로 바꿨더니 실행할 때마다 나오던 오류 메세지가 사라졌다. 이유를 모르겠다.

##### 8. 어드민 스태틱 파일 not found
`STATIC_URL = 'static/'`

`STATIC_URL = '/static/'`

위에서 아래로 바꿨더니 어드민 페이지에 스타일이 생겼다. 이것도 이유를 모르겠다.

##### 9. render가 shortcut인 이유

    def index(request):
    	latest_question_list = Question.objects.order_by('-pub_date')[:5]
    	template = loader.get_template('polls/index.html')
    	context = {
        	'latest_question_list': latest_question_list,
    	}
    	return HttpResponse(template.render(context, request))
        
```
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

template를 따로 load해서 HttpResponse에 넘겨주기의 지름길이 render임. 


##### 10. request.POST[' ']
`selected_choice = question.choice_set.get(pk=request.POST['choice'])`

템플릿의 input 태그 name으로 설문 답변의 id를 가져오는 방식을 배웠다. 


##### 11. HttpResponseRedirect와 redirect의 차이
HttpResponseRedirect의 인자는 url만 가능하고, redirect의 인자는 url, view, model이 가능해서 redirect가 더 유연함. redirect(to[, permanent=False], *args, **kwargs) 는 전달된 인자에 따라 적절한 HttpResponseRedirect를 리턴함. redirect가 httpresponseredirect를 캡슐화한 형태라고 생각하면 되고 뭘 써도 문제는 없다고 함. httpresponseredirect에 reverse(url이름 또는 viewname)을 하면 url이름으로부터 url을 찾아서 redirect해준다. 

##### 12. 제너릭 뷰
본적으로 DetailView 제너릭 뷰는 `<app name>/<model name>_detail.html` 템플릿을 사용함.url에 사용될 기본 키 값을 pk라고 해줘야함. model을 알려줘야 되고 template_name으로 기본 템플릿 이름에서 변경할 수 있음.

##### 13. django-environ으로 secret key 숨기기
숨기는 파일에서 변수와 값 사이에 공백이 없어어 함.


## 소감
4페이지 안에 모르는 내용이 정말 많이 들어있어서 열심히 해야겠다는 생각이 들었다. 배울 점이 훨씬 더 많았지만 링크를 타고 타고 들어가다가 정보에 잠식될 것 같았다! 
    

## 기한

- 2022년 9월 24일 토요일 
