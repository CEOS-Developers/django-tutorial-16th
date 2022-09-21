from django.urls import path

from . import views

# 해당 앱의 절대 경로
app_name = 'polls'
# name : url 의 이름 , 어디에서나 명확하게 참조가능하도록
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]