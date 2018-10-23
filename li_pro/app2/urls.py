from app2.views import Test
from django.conf.urls import url
from app2.view.weibo import SearchInfo, Login

urlpatterns = [
    url('test/', Test.as_view()),
    url('search/weibo', SearchInfo.as_view()),
    url('login', Login.as_view()),
]