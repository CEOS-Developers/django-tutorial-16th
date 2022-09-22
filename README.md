
# 1주차 미션: Django 튜토리얼

## 새로운 프로젝트 생성

    django-admin startprojeft mysite

현재 디렉토리에 mysite라는 이름을 가진 디렉토리가 하나가 생성이 되는데, 폴더를 자세히 살펴보면, 

    mysite/
	    manage.py
	    mysite/
	        __init__.py
	        settings.py
	        urls.py
	        asgi.py
	        wsgi.py

이렇게 mysite 안에 mysite 폴더가 하나 더 존재한다.

manage.py는 대부분의 명령어를 실행할 때 사용하는 파일이고, 주로

    python manage.py runserver / makemigration / migrate

같은걸 사용한다.


서버를 실행을 하려면 앞서 말한 

` python manage.py runserver`

를 실행하면 되는데, 그럼 자동으로 http://127.0.0.1:8000으로 서버가 실행이 된다.

만약 포트를 바꾸고 싶으면 

    python manage.py runserver "port"

이런식으로 하면 된다.


### 하나의 프로젝트에는 여러개의 앱이 존재할 수 있다

이게 무슨 말이냐면, 페이스북으로 예를 들면

페이스북이라는 프로젝트 안에는 "프로필앱", "그룹앱", "피드앱" 등등 여러가지가 존재하는 것처럼, 장고 프로젝트도 여러개의 앱이 있을 수 있다. 

## 투표앱 생성

    python manage.py startapp polls

명령어를 실행을 하면 이런 폴더가 생긴다

    polls/
	    __init__.py
	    admin.py
	    apps.py
	    migrations/
	        __init__.py
	    models.py
	    tests.py
	    views.py


장고는 MTV 패턴을 주로 사용하는데, MTV란 

> Model Template View 의 약자로, 일반적으로 개발할 때 저 순서대로 개발한다. ~~개인적인 경험입니다~~


아무튼 View를 개발하기 위해서는 생성한 앱 내부에 있는 view.py 파일을 열고 개발을 하면 된다. 

    from django.http import HttpResponse
    
    def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")

시험 삼아 첫 번째 뷰를 작성해보았다. index라는 뷰는 호출이 됐을 때 "Hello, world. You're at the polls index."를 반환하는 함수같은거라고 생각하면 편하다. 

작성한 index 뷰에 접근하려면 urls.py에서 url 설정을 해줘야한다. 

앱 내부에 있는 urls.py에서 우선 index 뷰로 연결을 해주고, 프로젝트 폴더에 있는 urls.py에서 polls 앱의 url과 연결을 해주면 된다.

    # polls/urls.py
    from django.urls import path
    from . import views
    urlpatterns = [
	    path('', views.index, name='index'),
    ]

	# mysite/urls.py
    from django.contrib import admin
    from django.urls import include, path
    
    urlpatterns = [
        path('polls/', include('polls.urls')),
        path('admin/', admin.site.urls),
    ]


## Django에서 Model이 무엇일까요

> 본질적으로, 모델이란 부가적인 메타데이터를 가진 데이터베이스의 구조(layout)를 말합니다.
> 
라고 장고 공식 문서에서 말을 하니까 맞는 것 같은데, ~~부가적인 메타데이터를 가진 데이터베이스의 구조를 말한다라는 말이 도대체 무슨 말인지를 모르겠는 말을 하고싶은것같기도 하고 아닌 것 같기도 하고~~

쉽게 생각하면 모델은 DB에서의 TABLE같은 느낌이다. 

간단하게 예를 들어보자.

Question이라는 모델에는 두가지의 요소가 존재할 수 있다. 
1. Question의 값 (질문이 뭔지)
2. Question이 생성된 시간 (질문이 언제 만들어진건지)

그러면 장고에서 Question 모델을 생성할 때는 두가지 요소를 포함해서 하나의 클래스를 생성하면 된다.

    class Question(models.Model):
	    question_text = models.CharField(max_length=200)
	    pub_date = models.DateTimeField('date published')

이렇게 models.py에서 모델을 하나 생성을 하면, 연동된 DB에 수정사항을 반영을 해줘야하는데, 그러려면 두가지 작업을 해줘야한다.

    1. python manage.py makemigrations
    2. python manage.py migrate

첫번째 명령어는 DB에서 이러한 변경사항들이 있다는걸 인지시켜주는거고, 두번째 명령어는 DB에게 이제 그거에 맞춰서 변하라고 명령하는 느낌이라고 보면 된다.


이제 이렇게 새로운 모델을 생성을 했으면, 테스트를 해보고 싶은 생각이 막 들 것이다. ~~저는 그랬습니다~~

몰랐던 사실인데, shell을 바로 실행을 해서 DB에 쿼리를 마구마구 날릴 수 있다고 한다. 그렇게 하려면

    python manage.py shell

이걸 실행하면 터미널이 있는 위치에 shell이 열리는데, 그러면 이제 막 DB에 이것저것 물어보고 추가할 수가 있다.

ex)

    Question.objects.all() #Question 테이블에 있는 모든 값들을 가져와라
	q = Question(question_text="What's new?", pub_date=timezone.now())
	q.save() #새로운 Question을 생성해서 테이블에 추가를 해줘라


근데 이게 물론 mongoDB마냥 웹사이트 타고 들어가서 막 데이터 확인하고 하는거보다 편할 수 있다고 하더라도, 실제로 데이터가 눈에 대놓고 보이는거보다는 불편하다. 그걸 조금이라도 더 편하게 만드려면 어드민 페이지를 통해서 확인하면 된다.

## 뷰를 더 만들어보자

투표 앱에는 필요한 기능이 여러가지가 있을 수 있는데, 대표적인 세가지를 나열하자면
1. 투표 현황
2. 투표 결과
3. 투표하기

이렇게 세가지가 일단 있다고 보면 된다.

그럼 마찬가지로 그 기능들을 구현하기 위해 뷰를 생성해준다. 

    def detail(request, question_id):
        return HttpResponse("You're looking at question %s." % question_id)
    
    def results(request, question_id):
        response = "You're looking at the results of question %s."
        return HttpResponse(response % question_id)
    
    def vote(request, question_id):
        return HttpResponse("You're voting on question %s." % question_id)

일단 예의상 만들어놓기만 한거고 실제로 저렇게 구현을 하면 아무 의미가 없다.

아까 한 것 처럼 뷰를 생성했으니 이제 뷰로 이어지는 링크를 연결해줘야한다. 

    from django.urls import path
    
    from . import views
    
    urlpatterns = [
        # ex: /polls/
        path('', views.index, name='index'),
        # ex: /polls/5/
        path('<int:question_id>/', views.detail, name='detail'),
        # ex: /polls/5/results/
        path('<int:question_id>/results/', views.results, name='results'),
        # ex: /polls/5/vote/
        path('<int:question_id>/vote/', views.vote, name='vote'),
    me='vote'),
    ]

요로코롬 만들어주면 각 투표앱의 자세한 현황 및 투표 결과 보기, 그리고 투표하기를 연결해줄 수 있다. 

그럼 이제 제대로 된 뷰를 만들어보자

    from django.http import HttpResponse
    
    from .models import Question
    
    
    def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        output = ', '.join([q.question_text for q in latest_question_list])
        return HttpResponse(output)

앞서 생성했던 뷰 중에서 index 뷰를 수정을 해봤다. 시간 순으로 가장 최근에 만들어진 질문 다섯가지를 DB에서 불러오고, ','.join()을 통해서 하나의 string으로 묶어주고, HttpResponse를 통해 데이터를 클라로 보내준다. 

원래 강의에서는 Template을 수정하고 장고를 풀스택으로 이용하는 그런걸 하는데, 나는 장고를 굳이 풀스택으로 이용할 필요가 없다고 생각하기 때문에 따로 필기는 안할 생각이다. . .  굳이 장고를 풀스택으로..? ? ? 리액트가 더 좋아! !

물론 과제니까 구현해보기는 했다. . . 하지만 하면서도 계속 굳이라는 생각이 머리속에 맴돌긴 했는데, 장고의 기초가 되는 부분이니까 배워서 나쁠건 없다고 생각했다.

데이터를 반환하는 부분을 조금 더 간편하게 하는 방법이 있는데, 그건 바로 render 함수를 이용하는 것이다. 

    from django.shortcuts import render
    
    from .models import Question
    
    
    def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
    _list}
	    return render(request, 'polls/index.html', context)


이렇게 하면 거추장스러운 HttpResponse를 매번 칠 필요 없다. 근데 정확한 차이는 잘 모르겠다... 그냥 편하려고 쓰는건지, 아니면 성능상의 이점이 존재해서 사용하는건지,,

그리고 만약 DB에서 데이터를 요청했는데 존재하지가 않는다면 당연히 404를 반환해야한다. 근데 그거를 주먹구구식으로 try catch를 사용하는 것보다는 

    get_object_or_404()

라는 함수를 이용하면 한번에 그걸 처리할 수가 있다. 저건 진짜 편리한듯

## Generics ? Mixins ? APIView ? 그게 뭐지? ?

Generics랑 Mixins, 그리고 APIView 모두 자주 사용되는 코드와 반복되는 코드를 축약시켜놓은 아주 좋은 기능이라고 생각하면 편하다!

쉽게 생각하면 자주 사용되는 기능들을 모아놓은 라이브러리같은 느낌인데, 예를 들어서
generic.ListView는 List를 보여줄 때 사용하는 generic이고,
generic.DetailView는 Detail페이지를 보여줄 때 사용하는 generic이다..

근데 사실 아직 제대로 이해를 못하고 저게 왜 되는건지도 제대로 이해를 못한 상태이긴 하다... 근데 개인적으로 초보일 때는 하나하나 다 따져가면서 외우고 하는거보단 "쓰다보니 익숙해졌다"가 훨씬 더 효율적이라고 생각해서 일단은 어떤 느낌인지만 가져가려 한다. 



# 끝

첫 백엔드 스터디 과제를 해봤는데, 재밌었다! 나도 드디어 풀스택이 될 수 있나? 라는 기대감때문에 더욱 열심히 하게 될 것 같다. 

