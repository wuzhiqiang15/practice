from django.conf.urls import include, url
from django.contrib import admin

from meetyou import meetyou_urls
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 视图函数中只有函数名，无括号和参数
    url(r'jingqi/', views.do_jingqi),
    url(r'(?:index=(?P<index_num>\d+))', views.do_index),
]
