# Generated by Django 5.0.6 on 2024-05-23 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Departments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=16, verbose_name="标题")),
            ],
        ),
        migrations.CreateModel(
            name="Admin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=32, verbose_name="用户名")),
                ("password", models.CharField(max_length=64, verbose_name="密码")),
                ("age", models.IntegerField(blank=True, null=True, verbose_name="年龄")),
                (
                    "gender",
                    models.IntegerField(
                        choices=[(1, "男"), (2, "女")], verbose_name="性别"
                    ),
                ),
                (
                    "depart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.departments",
                        verbose_name="部门",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Phone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("moblie", models.CharField(max_length=11, verbose_name="手机号")),
                ("price", models.PositiveIntegerField(default=0, verbose_name="价格")),
                (
                    "level",
                    models.SmallIntegerField(
                        choices=[(1, "1级"), (2, "2级"), (3, "3级"), (4, "4级")],
                        default=1,
                        verbose_name="级别",
                    ),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "已使用"), (2, "未使用")], default=2, verbose_name="状态"
                    ),
                ),
                (
                    "admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.admin",
                        verbose_name="管理员",
                    ),
                ),
            ],
        ),
    ]
