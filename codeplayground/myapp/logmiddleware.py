from django.shortcuts import redirect
from django.urls import reverse
import re

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        #�ж��Ƿ��¼
        #�����̨����¼Ҳ��ֱ�ӷ��ʵ�url�б�
        urllist = ['/','/login','/dologin','/dosign','/vcode','/about','/contact']
        #�жϵ�ǰ����url��ַ�Ƿ�����/myadmin��ͷ,���Ҳ���urllist�У������Ƿ��¼�ж�
        if path not in urllist:
            #�ж��Ƿ��¼(����session��û��adminuser)
            if 'loginuser' not in request.session:
                #�ض��򵽵�¼ҳ
                return redirect(reverse("login"))
                

        response = self.get_response(request)
        return response