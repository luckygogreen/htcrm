from django.db import models

# Create your models here.
# 创建数据库  create database htcrm;
class userinfo(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=100,null=False,unique=True)
    upassword = models.CharField(max_length=50,null=False)
    def __str__(self):
        #return "<userinfo object: {}>".format(self.uname)
        return self.uname
class usertags(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=64,null=False)
    userinfo = models.ForeignKey("userinfo",on_delete=models.CASCADE)

class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    pet_name = models.CharField(max_length=32,unique=True,null=False)
    uname = models.ManyToManyField(to='userinfo')
    def __str__(self):
        #return "<Pet object: {}>".format(self.pet_name)
        return self.pet_name