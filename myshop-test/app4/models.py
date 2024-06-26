from django.db import models
class UserBaseInfo(models.Model):
    id=models.AutoField(verbose_name='编号',primary_key=True)
    username=models.CharField(verbose_name='用户名称',max_length=30)
    password=models.CharField(verbose_name='密码',max_length=20)
    status=models.CharField(verbose_name='状态',max_length=1)
    createdate=models.DateTimeField(verbose_name='创建日期',db_column='createDate')
    def __str__(self):
        return str(self.id)
    class Meta:
        managed=False
        verbose_name='人员基本信息'
        db_table='UserBaseInfo4'

class UserExtraInfo(models.Model):
    id=models.AutoField(verbose_name='扩展编号',primary_key=True)
    username=models.CharField(verbose_name='用户名称',max_length=30)
    truename=models.CharField(verbose_name='真实姓名',max_length=30)
    password=models.CharField(verbose_name='密码',max_length=20)
    user=models.OneToOneField(UserBaseInfo,on_delete=models.CASCADE)