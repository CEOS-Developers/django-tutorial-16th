### !1주차 과제!
#### Date : 22.09.22

- 스프링과 달리 장고는 설정사항을 py파일로 한다는 점
- settings.py 에서 모든 설정을 추가해줘야 한다는 점도 신기했음
- INSTALLED_APPS 에서 생성한 앱을 명시해줘야 인식함 : 알아서 안된다니..
- makemigration 해주고 migration 해야 디비 생성됨 run으로 한방에 안댐
- runserver 로 실행할 수 있음
- shell도 따로 있음 , 테스트 목적으로 쓰기 좋은듯 깔끔하지 않은게 단점
- 어드민도 이런식으로 만들 수 있다니.. 깔끔함
- 제네릭 뷰 란? 장고에서 기본적으로 제공하는 뷰 클래스
  용도에 따라 ListView, DetailView, FormView, TemplateView 등이 있는데, 전부 View 클래스를 상속받고 있음
- 굳이 하나씩 해주지 않아도 된다는 점이 신기함
