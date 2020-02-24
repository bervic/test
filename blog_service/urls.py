from django.conf.urls import url

from views import Blog

urlpatterns = [
    url(r'^blog$', Blog.as_view()),
]