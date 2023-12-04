from django.db import models

# Create your models here.
from application.models import BaseModel

from config.env import TABLE_PREFIX


# 登录日志模型
class LoginLog(BaseModel):
    # 登录用户
    login_name = models.CharField(max_length=50, verbose_name="登录用户", help_text="登录用户")
    # 登录IP
    login_ip = models.CharField(max_length=30, verbose_name="登录IP", help_text="登录IP")
    # 登录代理
    login_agent = models.CharField(max_length=255, verbose_name="登录代理", help_text="登录代理")
    # 登录浏览器
    login_browser = models.CharField(max_length=255, verbose_name="登录浏览器", help_text="登录浏览器")
    # 操作系统
    login_os = models.CharField(max_length=255, verbose_name="操作系统", help_text="操作系统")
    # 登录属地
    login_area = models.CharField(max_length=255, verbose_name="登录属地", help_text="登录属地")
    # 登录时间
    login_time = models.DateTimeField(null=True, max_length=11, verbose_name="登录时间", help_text="登录时间")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "login_log"
        verbose_name = "登录日志表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "登录日志{}".format(self.login_name)
