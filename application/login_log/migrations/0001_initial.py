# Generated by Django 4.1.3 on 2023-03-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_user', models.IntegerField(default=0, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now_add=True, max_length=11, null=True, verbose_name='创建时间')),
                ('update_user', models.IntegerField(default=0, verbose_name='更新人')),
                ('update_time', models.DateTimeField(auto_now=True, max_length=11, null=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=0, verbose_name='逻辑删除')),
                ('login_name', models.CharField(help_text='登录用户', max_length=50, verbose_name='登录用户')),
                ('login_ip', models.CharField(help_text='登录IP', max_length=30, verbose_name='登录IP')),
                ('login_agent', models.CharField(help_text='登录代理', max_length=255, verbose_name='登录代理')),
                ('login_browser', models.CharField(help_text='登录浏览器', max_length=255, verbose_name='登录浏览器')),
                ('login_os', models.CharField(help_text='操作系统', max_length=255, verbose_name='操作系统')),
                ('login_area', models.CharField(help_text='登录属地', max_length=255, verbose_name='登录属地')),
                ('login_time', models.DateTimeField(help_text='登录时间', max_length=11, null=True, verbose_name='登录时间')),
            ],
            options={
                'verbose_name': '登录日志表',
                'verbose_name_plural': '登录日志表',
                'db_table': 'django_login_log',
            },
        ),
    ]
