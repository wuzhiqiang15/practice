from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.


def do_jingqi(request):
    return HttpResponse("这是经期测试子路由")

def do_page(request, pagenum):
    return HttpResponse("page number is {0}".format(pagenum))

def do_index(request,index_num):
    return HttpResponse("index number is {0}".format(index_num))

def extremParam(request, name):
    return HttpResponse("my name is {0}".format(name))

# 重定向到do_new_url 这个网址中（这里使用了reverse来防止硬编码，new即指向路由中的）
def do_reversal_url(r,num):
    return HttpResponseRedirect(reverse("new"))

def do_new_url(r,num):
    return HttpResponse("这是new_url的第{0}访个问地址".format(num))

def v9_get(request):
    # 渲染模板并返回
    return render_to_response("for_post.html")

def v9_post(request):
    rst = ""
    for k, v in request.POST.items():
        rst += k + "-->" + v
        rst += ","
    return HttpResponse("Get Value of POST is {0}".format(rst))
