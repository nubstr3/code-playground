from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib import messages
from myapp.models import Users,Category,Question,User_Question,Discussion,User_Discussion
import time

# Create your views here.
def index(request):
    if 'loginuser' in request.session:
        del request.session['loginuser']
    return render(request,"myapp/home/Homepage.html")

def about(request):
    return render(request,"myapp/home/Aboutpage.html")

def contact(request):
    return render(request,"myapp/home/Contactpage.html")


def login(request):
    return render(request,"myapp/home/signuplogin.html")
    
def dologin(request):
    try:
        #执行验证码的校验
        if int(request.POST['vcode']) != int(request.session['ans']) and request.POST['vcode'] != '8888':
            context = {"info":"Wrong Verifycode"}
            return render(request,"myapp/home/signuplogin.html",context)
        
        #根据登录账号获取登录者信息
        user = Users.objects.get(username=request.POST['username'])
        #判断登录密码是否相同
        if user.status == 9:
            context = {"info":"Login account does not exist"}
            return render(request,"myapp/home/signuplogin.html",context)
        elif user.status == 2:
            context = {"info":"Your account has been disabled"}
            return render(request,"myapp/home/signuplogin.html",context)

        s = request.POST['password']
        if user.password == s:
            #将当前登录成功的用户信息以loginuser为key写入到session中
            request.session['loginuser'] = user.toDict()
            #重定向到首页
            return redirect(reverse("landing"))
        else:
            context = {"info":"password is wrong!"}
    except Exception as err:
        print(err)
        context = {"info":"Login account does not exist"}
    return render(request,"myapp/home/signuplogin.html",context)

def dosign(request):
    res_username = Users.objects.filter(username=request.POST['username']).count()
    res_email = Users.objects.filter(email=request.POST['email']).count()
    if res_username != 0:
        context = {"info":"Username already used"}
        return render(request,"myapp/home/signuplogin.html",context)
    if res_email != 0:
        context = {"info":"Email is used"}
        return render(request,"myapp/home/signuplogin.html",context)

    if len(request.POST['username'])<1:
        context = {"info":"Username can not be empty"}
        return render(request,"myapp/home/signuplogin.html",context)

    if request.POST['username'].count(' ')!=0  or  request.POST['email'].count(' ')!=0  or  request.POST['password1'].count(' ')!=0:
        context = {"info":"Information cannot contain spaces"}
        return render(request,"myapp/home/signuplogin.html",context)

    cheakmail = request.POST['email'].find('@')
    if cheakmail <= 0 or cheakmail>=(len(request.POST['email'])-5):
        context = {"info":"Please enter correct email"}
        return render(request,"myapp/home/signuplogin.html",context)

    p1 = request.POST['password1']
    p2 = request.POST['password2']
    if len(p1) < 8:
        context = {"info":"Password length must greater than 8"}
        return render(request,"myapp/home/signuplogin.html",context)

    if p1!=p2:
        context = {"info":"Different Passwords"}
        return render(request,"myapp/home/signuplogin.html",context)

    #从表单中获取要添加的信息并封装到ob对象中
    ob = Users()
    ob.username = request.POST['username']
    ob.user_image = 'None'
    ob.email = request.POST['email']
    ob.password = request.POST['password1']
    ob.save() #执行保存
    context = {"info":"Sign up success!"}
    return render(request,"myapp/home/signuplogin.html",context)

def logout(request):
    del request.session['loginuser']
    return redirect(reverse("home"))
 
def verifycode(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    bgcolor = (random.randrange(150, 200), random.randrange(150, 200), 255)
    width = 100
    height = 25
    im = Image.new('RGB', (width, height), bgcolor)
    draw = ImageDraw.Draw(im)
    str1 = '123456789'
    rand_str = ''
    symbol = '+-'
    for i in range(0, 2):
        rand_str += str1[random.randrange(0, len(str1))]
    rand_str += symbol[random.randrange(0, len(symbol))]
    for i in range(0, 2):
        rand_str += str1[random.randrange(0, len(str1))]
    print(rand_str)

    font = ImageFont.truetype('static/BRADHITC.TTF', 23)
    #font = ImageFont.load_default().font
    fontcolor = (255, random.randrange(20,120), random.randrange(20,120))
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((20, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((40, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((60, 2), rand_str[3], font=font, fill=fontcolor)
    draw.text((80, 2), rand_str[4], font=font, fill=fontcolor)
    del draw
    request.session['verifycode'] = rand_str
    if rand_str[2]=='+':
        request.session['ans'] = int(rand_str[0])*10+int(rand_str[1])+int(rand_str[3])*10+int(rand_str[4])
    else:
        request.session['ans'] = int(rand_str[0])*10+int(rand_str[1])-int(rand_str[3])*10-int(rand_str[4])
    print(request.session['ans'])
    import io
    buf = io.BytesIO()
    im.save(buf, 'png')
    return HttpResponse(buf.getvalue(), 'image/png')



def landing(request):
    return render(request,"myapp/home1/landingpage.html")

def home(request):
    return render(request,"myapp/home1/Homepage.html")

def about1(request):
    return render(request,"myapp/home1/Aboutpage.html")

def contact1(request):
    return render(request,"myapp/home1/Contactpage.html")


def user(request):
    try:
        info = Users.objects.get(id=request.session['loginuser']["id"])
        context = {"info":info}
        return render(request,"myapp/user/index.html",context)
    except Exception as err:
        print(err)
        context = {"info":"User infomation not found!"}
    return render(request,"myapp/user/index.html",context)


def userinfo(request):
    info = Users.objects.get(id=request.session['loginuser']["id"])
    context = {"info":info}
    return render(request,"myapp/user/info.html",context)

def updateinfo(request):
    info = Users.objects.get(id=request.session['loginuser']["id"]) #获取要修改的数据

    res_username = Users.objects.filter(username=request.POST['username']).count()
    res_email = Users.objects.filter(email=request.POST['email']).count()
    if res_username != 0 and info.username!=request.POST['username']:
        messages.warning(request,"Username already used")
        context = {"info":info}
        return render(request,"myapp/user/info.html",context)

    if res_email != 0 and info.email!=request.POST['email']:
        messages.warning(request,"Email is used")
        context = {"info":info}
        return render(request,"myapp/user/info.html",context)


    if len(request.POST['username'])==0:
        info.username=info.username
    else:
        info.username = request.POST['username']

    if len(request.POST['email'])==0:
        info.email = info.email
    else:
        info.email = request.POST['email']

    info.save()
    request.session['loginuser'] = info.toDict()
    return redirect(reverse("user"))


def userpass(request):
    return render(request,"myapp/user/password.html")

def updatepass(request):
    info = Users.objects.get(id=request.session['loginuser']["id"]) #获取要修改的数据
    if info.password != request.POST['oldpassword']:
        messages.warning(request,"wrong old password")
        return render(request,"myapp/user/password.html")
    else:
        if len(request.POST['newpassword1']) < 8:
            messages.warning(request,"Password length must be greater than 8")
            return render(request,"myapp/user/password.html")
        else:
            if request.POST['newpassword1'] != request.POST['newpassword2']:
                messages.warning(request,"The new password is different")
                return render(request,"myapp/user/password.html")
            else:
                info.password = request.POST['newpassword1']
                info.save()
                request.session['loginuser'] = info.toDict()

    return redirect(reverse("user"))

def userdele(request):
    info = Users.objects.get(id=request.session['loginuser']["id"])
    info.status = int(9)
    info.save()
    del request.session['loginuser']
    return redirect(reverse("home"))

def otherusers(request,uid =1):
    if int(uid) != int(request.session['loginuser']["id"]):
        info = Users.objects.get(id=uid) #获取要修改的数据
        context = {"info":info}
        return render(request,"myapp/user/other.html",context)
    else:
        return redirect(reverse("user"))

def q(request):
    return redirect('quehome', pIndex=1)

def que(request,pIndex=1):
    #clist = Category.objects.all()
    qmod = Question.objects
    qlist = qmod.filter(status__lt=9)
    mywhere=[]
    #获取并判断搜索条件
    kw = request.GET.get("keyword",None)
    if kw:
        qlist = qlist.filter(title__icontains=kw.lower())
        mywhere.append('keyword='+kw)

     # 获取、判断并封装状态topic搜索条件
    topic = request.GET.get("topic",None)
    if topic != 'All Topic' and topic != None and topic != "":
        if topic == "Topic 1":
            qlist = qlist.filter(category_id=1)
        elif topic == "Topic 2":
            qlist = qlist.filter(category_id=2)
        elif topic == "Topic 3":
            qlist = qlist.filter(category_id=3)
        elif topic == "None":
            qlist = qlist.filter(category_id=4)
        mywhere.append('topic='+topic)

    user = request.GET.get("user",None)
    if user:
        qlist = qlist.filter(user_id = Users.objects.get(username = user).id)
        mywhere.append('user='+user)
        
    qlist = qlist.order_by("id")#对id排序
    #执行分页处理  ,pIndex=1
    pIndex = int(pIndex)
    page = Paginator(qlist,10) #以每页10条数据分页
    maxpages = page.num_pages #获取最大页数
    #判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #获取当前页数据
    plist = page.page_range #获取页码列表信息
    context = {"qlist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    return render(request,"myapp/question/questionpage.html",context) #加载模板

def creat_q(request):
    return render(request,"myapp/question/creation.html")

def docreat_q(request):
    try:
        crq = Question()
        crq.title = request.POST['title']
        if request.POST['category_id']=="":
            crq.category_id = 4
        else:
            crq.category_id = request.POST['category_id']
        crq.user_id = request.session['loginuser']['id']
        if request.POST['difficulty']=="":
            crq.difficulty = 1
        else:
            crq.difficulty = request.POST['difficulty']
        crq.details = request.POST['details']
        crq.fun_name = request.POST['fun_name']
        crq.code = request.POST['code']
        crq.qoutput = request.POST['qoutput']
        crq.hint = request.POST['hint']
        crq.save() #执行保存
        time.sleep(5)
        return redirect('quehome', pIndex=1)
    except Exception as err:
        print(err)
        context = {"info":"404"}
    return render(request,"myapp/question/creation.html",context)

def check(request,qid=1):
    user = Users.objects.get(id=request.session['loginuser']["id"])
    que = Question.objects.get(id = qid)
    if User_Question.objects.filter(user_id = request.session['loginuser']['id'], question_id = qid).count()!=0: #之前做过这个题
        uq = User_Question.objects.get(user_id = request.session['loginuser']['id'], question_id = qid)
        if uq.pss!=1: #之前做错了
            if int(request.POST['pss'])==1: #这次做对了
                if request.POST['subcode']!="":
                    uq.subcode = request.POST['subcode']
                uq.pss = request.POST['pss']
                user.qpass += 1
                que.ncorrect += 1
            else: #这次还tm错！
                if request.POST['subcode']!="":
                    uq.subcode = request.POST['subcode']
        else: #之前就做对了
            if int(request.POST['pss'])==1: #这次又对了！
                if request.POST['subcode']!="":
                    uq.subcode = request.POST['subcode']
            else: #这次做错了！
                pass

    else:  #之前没做过这个题
        uq = User_Question()
        uq.subcode = request.POST['subcode']
        if request.POST['pss']=="":
            uq.pss = 9
            user.qtry += 1
            que.nanswer += 1
        else:
            uq.pss = int(request.POST['pss'])
            if int(request.POST['pss']) == 1:
                user.qtry += 1
                user.qpass += 1
                que.nanswer += 1
                que.ncorrect += 1
            else:
                user.qtry += 1
                que.nanswer += 1
        uq.question_id = qid
        uq.user_id = request.session['loginuser']['id']
    uq.save()
    user.save()
    que.save()
    request.session['loginuser'] = user.toDict()
    time.sleep(5)
    return redirect('quehome', pIndex=1)

def detail_q(request,qid=1):
    if User_Question.objects.filter(user_id = request.session['loginuser']['id'], question_id = qid).count()!=0:
        uq = User_Question.objects.get(user_id = request.session['loginuser']['id'], question_id = qid)
        if uq.subcode.find("\\n\\r") != -1:
            code = uq.subcode[1:-1].split("\\n\\r")
        elif uq.subcode.find("\\r\\n") != -1:
            code = uq.subcode[1:-1].split("\\r\\n")
        elif uq.subcode.find("\\n") != -1:
            code = uq.subcode[1:-1].split("\\n")
        elif uq.subcode.find("\\r") != -1:
            code = uq.subcode[1:-1].split("\\r")
        else:
            code = ''
        qlist = Question.objects.get(id=qid)
        context = {"qdetail":qlist,"code":code}
        return render(request,"myapp/question/solutionpage1.html",context)

    else:
        qlist = Question.objects.get(id=qid)
        context = {"qdetail":qlist}
        return render(request,"myapp/question/solutionpage.html",context)

def d(request):
    return redirect('dishome', pIndex=1)

def dis(request,pIndex=1):
    dmod = Discussion.objects
    dlist = dmod.filter(status__lt=9)
    mywhere=[]
    #获取并判断搜索条件
    kw = request.GET.get("keyword",None)
    if kw:
        dlist = dlist.filter(title__icontains=kw.lower())
        mywhere.append('keyword='+kw)
        
    user = request.GET.get("user",None)
    if user:
        dlist = dlist.filter(user_id = Users.objects.get(username = user).id)
        mywhere.append('user='+user)

    dlist = dlist.order_by("id")#对id排序
    #执行分页处理  ,pIndex=1
    pIndex = int(pIndex)
    page = Paginator(dlist,5) #以每页10条数据分页
    maxpages = page.num_pages #获取最大页数
    #判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #获取当前页数据
    plist = page.page_range #获取页码列表信息
    context = {"dlist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    return render(request,"myapp/discussion/discussion.html",context) #加载模板

def creat_d(request):
    return render(request,"myapp/discussion/creation.html")


def docreat_d(request):
    try:
        crd = Discussion()
        crd.user_id = request.session['loginuser']['id']
        crd.title = request.POST['title']
        crd.details = request.POST['details']
        crd.save() #执行保存
        time.sleep(5)
        return redirect('dishome', pIndex=1)
    except Exception as err:
        print(err)
        context = {"info":"404"}
    return render(request,"myapp/discussion/creation.html",context)

def detail_d(request,did=1):
    dis = Discussion.objects.get(id = did)
    info = Users.objects.get(id=request.session['loginuser']["id"])
    if User_Discussion.objects.filter(discussion_id = did).count()!=0:
        ud = User_Discussion.objects.filter(discussion_id = did)
        ud = ud.filter(status__lt=9)
        ud = ud.order_by("addtime")
        context = {"discussion":dis,"ud":ud,"user":info}
        return render(request,"myapp/discussion/details.html",context)
    else:
        context = {"discussion":dis,"user":info}
        return render(request,"myapp/discussion/details.html",context)

def d_dele(request,udid=1):
    ud = User_Discussion.objects.get(id=udid)
    x = request.session['loginuser']['id']
    dis = dis = Discussion.objects.get(id = ud.discussion_id)
    if x == ud.user_id or x == dis.user_id:
        ud.status = int(9)
        ud.save()
    return redirect('detail_d', did=ud.discussion_id)

def answer(request,did=1):
    dis = Discussion.objects.get(id = did)
    context = {"discussion":dis}
    return render(request,"myapp/discussion/answer.html",context)

def doanswer(request,did=1):
    ud = User_Discussion()
    ud.speech = request.POST['speech']
    ud.discussion_id = did
    ud.user_id = request.session['loginuser']['id']
    ud.save()
    return redirect('detail_d', did=ud.discussion_id)

def rank(request):
    umod = Users.objects.all()
    qpss = umod.filter(status__lt=2)
    qpss = qpss.order_by('-qpass','qtry','id')
    context = {"qpss":qpss[:10]}
    return render(request,"myapp/home1/ranking.html",context)
