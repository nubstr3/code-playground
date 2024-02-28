#myapp应用的路由文件
from django.urls import path,re_path
from . import views

urlpatterns = [
    path("",views.index, name="home"),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),

    path("login",views.login, name="login"),
    path('dosign', views.dosign, name = 'dosign'),#执行注册
    path('dologin', views.dologin, name="dologin"), #执行登录
    path('logout', views.logout, name="logout"), #退出
    path('vcode', views.verifycode, name="vcode"),
    
    path('landing', views.landing, name="landing"),

    path('home', views.home, name="home1"),
    path("home/about",views.about1, name="about1"),
    path("home/contact",views.contact1, name="contact1"),
    path("home/rank",views.rank, name="rank"),

    path("user",views.user, name="user"),
    path("user/info",views.userinfo, name="userinfo"),
    path("user/info/edit",views.updateinfo, name="updateinfo"),
    path("user/pass",views.userpass, name="userpass"),
    path("user/pass/edit",views.updatepass, name="updatepass"),
    path("user/dele",views.userdele, name="userdele"),
    path("user/<int:uid>",views.otherusers, name="otherusers"),

    path("question",views.q),
    path("question/<int:pIndex>",views.que, name="quehome"),
    path('question/creat', views.creat_q, name="creatq"),
    path('question/docreat', views.docreat_q, name="docreatq"),
    path("question/detail/<int:qid>",views.detail_q, name="detail_q"),
    path("question/check/<int:qid>",views.check, name="check"),

    path("discussion",views.d),
    path("discussion/<int:pIndex>",views.dis, name="dishome"),
    path('discussion/creat', views.creat_d, name="creatd"),
    path('discussion/docreat', views.docreat_d, name="docreatd"),
    path("discussion/detail/<int:did>",views.detail_d, name="detail_d"),
    path("discussion/detail/dele/<int:udid>",views.d_dele, name="d_dele"),

    path('discussion/answer/<int:did>', views.answer, name="answer"),
    path('discussion/doanswer/<int:did>', views.doanswer, name="doanswer"),


]