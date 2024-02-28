from distutils.command.upload import upload
from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.
class Users(models.Model):
    #id = models.AutoField(primary_key=True) #主键可省略不写
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    sex = models.IntegerField(default=0) #未知:0  男性:1  女性:2
    user_image = models.ImageField(default='None', upload_to='static/media/head_img', verbose_name='user_image')
    email = models.CharField(max_length=100)
    qpass = models.IntegerField(default=0)
    qtry = models.IntegerField(default=0)
    status = models.IntegerField(default=1)  #状态:1正常/2禁用/6管理员/9删除
    addtime = models.DateTimeField(auto_now_add=True)

    def toDict(self):
        return {'id':self.id,
                'username':self.username,
                'password':self.password,
                'sex':self.sex,
                'email':self.email,
                'qpass':self.qpass,
                'qtry':self.qtry,
                'status':self.status,
                'addtime':self.addtime.strftime('%Y-%m-%d %H:%M:%S'),
                }

    def emailname(self):
        a = self.email.find('@')
        return self.email[0:a]

    def emailadd(self):
        a = self.email.find('@')
        return self.email[a:]

    def percen(self):
        if self.qtry!=0:
            return int(self.qpass/self.qtry*100)
        else:
            return 0

    def rank(self):
        umod = Users.objects.all()
        qpss = umod.filter(status__lt=2)
        qpss = qpss.order_by('-qpass','qtry','id')
        for i in range(len(qpss)):
            if qpss[i].id == self.id:
                return i+1
        return 100

    class Meta:
        db_table = "users"  # 更改表名


class Category(models.Model):
    #id = models.AutoField(primary_key=True) #主键可省略不写
    topic = models.CharField(max_length=50)
    status = models.IntegerField(default=1)  #状态:1正常/9删除
    addtime = models.DateTimeField(auto_now_add=True)

    def toDict(self):
        return {'id':self.id,
                'topic':self.topic,
                'status':self.status,
                'addtime':self.addtime.strftime('%Y-%m-%d %H:%M:%S'),
                }

    class Meta:
        db_table = "category"  # 更改表名

class Question(models.Model):
    #id = models.AutoField(primary_key=True) #主键可省略不写  
    category = models.ForeignKey(Category,on_delete=models.PROTECT) #难度: 4未知/1/2/3
    user = models.ForeignKey(Users,on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    difficulty = models.IntegerField(default=0)  #难度: 0未知/1简单/2中等/3困难
    details = models.TextField()
    fun_name = models.CharField(max_length=255)
    code = models.TextField()
    qoutput = models.CharField(max_length=255)
    hint = models.TextField()
    nanswer = models.IntegerField(default=0)
    ncorrect = models.IntegerField(default=0)
    status = models.IntegerField(default=1)  #状态:1正常/9删除
    addtime = models.DateTimeField(auto_now_add=True)

    def toDict(self):
        return {'id':self.id,
                'category_id':self.category_id,
                'user_id':self.user_id,
                'title':self.title,
                'difficulty':self.difficulty,
                'details':self.details,
                'fun_name':self.fun_name,
                'code':self.code,
                'qoutput':self.qoutput,
                'hint':self.hint,
                'nanswer':self.nanswer,
                'ncorrect':self.ncorrect,
                'status':self.status,
                'addtime':self.addtime.strftime('%Y-%m-%d %H:%M:%S'),
                }

    def percen(self):
        if self.nanswer!=0:
            return int(self.ncorrect/self.nanswer*100)
        else:
            return 0

    def qtry(self):
        return User_Question.objects.filter(question_id = self.id).count()

    def qpass(self):
        return User_Question.objects.filter(question_id = self.id, pss = 1).count()

    def username(self):
        return Users.objects.get(id = self.user_id).username

    class Meta:
        db_table = "question"  # 更改表名


class User_Question(models.Model):
    #id = models.AutoField(primary_key=True) #主键可省略不写
    user = models.ForeignKey(Users,on_delete=models.PROTECT)
    question = models.ForeignKey(Question,on_delete=models.PROTECT)
    pss = models.IntegerField(default=9)  #通过:1  未通过:9
    subcode = models.TextField()

    def toDict(self):
        return {'id':self.id,
                'user_id':self.user_id,
                'question_id':self.question_id,
                'pss':self.pss,
                'subcode':self.subcode
                }

    class Meta:
        db_table = "user_question"  # 更改表名

class Discussion(models.Model):
    #id = models.AutoField(primary_key=True) #主键可省略不写
    user = models.ForeignKey(Users,on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    details = models.TextField()
    status = models.IntegerField(default=1)  #状态:1正常/9删除
    addtime = models.DateTimeField(auto_now_add=True)

    def toDict(self):
        return {'id':self.id,
                'user_id':self.user_id,
                'title':self.title,
                'details':self.details,
                'status':self.status,
                'addtime':self.addtime.strftime('%Y-%m-%d %H:%M:%S')
                }

    def viewdetails(self):
        if len(self.details)>=210:
            return str(self.details[:210]) + '...'
        else:
            return self.details

    def username(self):
        return Users.objects.get(id = self.user_id).username

    def anwsers(self):
        ud = User_Discussion.objects.filter(discussion_id = self.id)
        ud = ud.filter(status__lt=9)
        return ud.count()

    class Meta:
        db_table = "discussion"  # 更改表名

class User_Discussion(models.Model):
    #id = models.AutoField(primary_key=True) #主键可省略不写
    discussion = models.ForeignKey(Discussion,on_delete=models.PROTECT)
    user = models.ForeignKey(Users,on_delete=models.PROTECT)
    speech = models.TextField()
    status = models.IntegerField(default=1)  #状态:1正常/9删除
    addtime = models.DateTimeField(auto_now_add=True)

    def toDict(self):
        return {'id':self.id,
                'discussion_id':self.discussion_id,
                'user_id':self.user_id,
                'speech':self.speech,
                'status':self.status
                }

    def username(self):
        return Users.objects.get(id = self.user_id).username

    class Meta:
        db_table = "user_discussion"  # 更改表名

