from django.db import models

class Departments(models.Model):
    title=models.CharField(verbose_name="标题",max_length=16)
    def __str__(self):
        return self.title

class Admin(models.Model):
    username=models.CharField(verbose_name="用户名",max_length=32)
    password=models.CharField(verbose_name="密码",max_length=64)
    age=models.IntegerField(verbose_name="年龄",null=True,blank=True) 
    gender=models.IntegerField(verbose_name="性别",choices=[(1,"男"),(2,"女")])
    depart=models.ForeignKey(verbose_name="部门",to="Departments",on_delete=models.CASCADE)

class Phone(models.Model):
    moblie=models.CharField(verbose_name="手机号",max_length=11)
    price=models.PositiveIntegerField(verbose_name="价格",default=0)
    level=models.SmallIntegerField(verbose_name="级别",choices=[(1,"1级"),(2,"2级"),(3,"3级"),(4,"4级")],default=1)
    status=models.SmallIntegerField(verbose_name="状态",choices=[(1,"已使用"),(2,"未使用")],default=2)
    admin=models.ForeignKey(verbose_name="管理员",to="Admin",on_delete=models.CASCADE)