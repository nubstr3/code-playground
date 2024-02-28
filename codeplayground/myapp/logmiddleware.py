from django.shortcuts import redirect
from django.urls import reverse
import re

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        #判断是否登录
        #定义后台不登录也可直接访问的url列表
        urllist = ['/','/login','/dologin','/dosign','/vcode','/about','/contact']
        #判断当前请求url地址是否是以/myadmin开头,并且不在urllist中，才做是否登录判断
        if path not in urllist:
            #判断是否登录(在于session中没有adminuser)
            if 'loginuser' not in request.session:
                #重定向到登录页
                return redirect(reverse("login"))
                

        response = self.get_response(request)
        return response