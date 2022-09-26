# Python 의 표준 모듈인 datetime 모듈
import datetime

from django.db import models
# Django 의 시간대 관련 유틸리티인 django.utils.timezone 을 참조
from django.utils import timezone


class Question(models.Model):
    # 문자 필드 / 길이 제한
    question_text = models.CharField(max_length=200)
    # 날짜와 시간 필드
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # 각각의 choice 가 하나의 question 에 관계됨
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # 숫자 필드
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
