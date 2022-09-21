from django.urls import path

from . import views

# 해당 앱의 절대 경로
app_name = 'polls'
# name : url 의 이름 , 어디에서나 명확하게 참조가능하도록
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]