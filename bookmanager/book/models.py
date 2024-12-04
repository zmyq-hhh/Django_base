from django.db import models

# Create your models here.

class BookInfo(models.Model):
    #系统自动添加一个主键——id
    name=models.CharField(max_length=10)

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()  #布尔类型
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)