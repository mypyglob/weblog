from django.db import models

# Create your models here.

class User(models.Model):
    nickname = models.CharField(max_length=16,verbose_name='用户昵称',blank=True)
    username = models.CharField(max_length=16,verbose_name='用户名',blank=True)
    password = models.CharField(max_length=16,verbose_name='用户密码',blank=True)
    head_img = models.ImageField(verbose_name='头像')
    token = models.UUIDField(verbose_name='单点登录')



class UserInfo(models.Model):
    birthday = models.DateField(verbose_name='用户生日')
    county = models.SmallIntegerField(verbose_name='国家')
    address = models.CharField(max_length=100,verbose_name='地址')
    user = models.OneToOneField('User',on_delete=True)


source=(
    ('1',"转载"),
    ('2','原创')
)
class Comment(models.Model):
    '''
    评论表
    '''
    user=models.ForeignKey('User',on_delete=True,max_length=255,default=None)
    article=models.ForeignKey('Article',on_delete=True,default=None)
    parent_comment=models.CharField(default=None,max_length=20)
    create_time=models.CharField(default=None,max_length=20)
    content=models.TextField(default=None,)

class Article(models.Model):
    '''
    文章表Cagetory
    '''
    title=models.CharField(max_length=255,blank=True,null=True)
    content=models.TextField(blank=True,null=True)
    create_time=models.DateTimeField(blank=True,null=True)
    read_count=models.BigIntegerField(blank=True,null=True,default=0)
    source_type=models.SmallIntegerField(blank=True,null=True,choices=source)
    category=models.ForeignKey('Cagetory',on_delete=True)
    author=models.ForeignKey("User",on_delete=True)
    up_count=models.PositiveIntegerField(default=0)
    down_count=models.PositiveIntegerField(default=0)

class Cagetory(models.Model):
    '''类别表'''
    chinese_name = models.CharField(max_length=10, null=True, help_text='类别中文名称')
    foreign_name = models.CharField(max_length=20, null=True, help_text='类别英文名称')
    widget = models.SmallIntegerField(null=True, help_text='类别权重值，类别推荐值')


class Banner(models.Model):
    '''轮播图表'''
    img_url = models.ImageField(null=True, help_text='轮播图资源地址')
    article = models.OneToOneField('Article',on_delete=True, related_name='article')
    widget = models.SmallIntegerField(default=500, help_text='权重值')


class Advertise(models.Model):
    '''广告表'''
    url = models.CharField(max_length=100,null=True, help_text='广告路径')
    img = models.ImageField(null=True, help_text='图片')
    name = models.CharField(max_length=20, null=True, help_text='广告名字')
    widget = models.SmallIntegerField(null=True, help_text='权重值')