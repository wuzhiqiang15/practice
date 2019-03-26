from django.db import models
import time

# Create your models here.


class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=20)
    roomName = models.CharField(max_length=20)

    def curTime(self):
        return time.time()

    # 设置该函数在页面的显示
    curTime.short_description = "当前时间"

    def __str__(self):
        return self.roomName

class Teacher(models.Model):
    name = models.CharField(max_length=5)
    course = models.CharField(max_length=20)
    # 设置Teacher和ClassRoom 一对一
    room = models.OneToOneField(ClassRoom)

    def curTime(self):
        return time.ctime()
    # 设置curTime方法在后台显示的名称
    curTime.short_description = "当前时间"
    # 设置curTime方法显示结果的排序（这里是以"name”来排序）
    curTime.admin_order_field = "name"

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    # 设置Student跟ClassRoom 一对多（一个ClassRoom下，可以有多个Student）
    room = models.ForeignKey(ClassRoom)
