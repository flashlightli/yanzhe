from app2.views import Test
from django.conf.urls import url


urlpatterns = [
    url('test/', Test.as_view())
]