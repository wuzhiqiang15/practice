from django.conf.urls import include, url
from django.contrib import admin

from meetyou import meetyou_urls
from meetyou import views as mv

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^meetyou/', include(meetyou_urls)),
    # URL中 嵌套参数
    url(r'^book/(?:page-(?P<pagenum>\d+))', mv.do_page),
    # URL中 传递额外参数
    url(r'extrem/$', mv.extremParam, {"name":"wuzhiqiang"}),

    # 使用 name 来给视图中的方法，增加名称，这样即使修改了路由地址，也不会影响到视图中的函数
    #url(r'^old/(?:url_0(?P<num>\d+))', mv.do_reversal_url, name="revers"),
    # url(r'^new/(?:url_0(?P<num>\d+))', mv.do_new_url, name="new"),

    # 先访问v9_get,然后通过渲染后的for_post.html页面，访问v9_post/页面
    url(r'^v9_get/', mv.v9_get),
    url(r'^v9_post/', mv.v9_post),

]
