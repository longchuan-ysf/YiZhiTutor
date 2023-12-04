from django.db import models

# Create your models here.
from application.models import BaseModel
from config.env import TABLE_PREFIX


# 通知公告模型
class Notice(BaseModel):
    # 通知标题
    title = models.CharField(null=False, max_length=255, verbose_name="通知标题", help_text="通知标题")
    # 通知来源：1官方平台 2开源中国 3CSDN官方 4新浪微博
    SOURCE_CHOICES = (
        (1, "官方平台"),
        (2, "开源中国"),
        (3, "CSDN官方"),
        (2, "新浪微博"),
    )
    source = models.IntegerField(choices=SOURCE_CHOICES, default=0, verbose_name="通知来源：1官方平台 2开源中国 3CSDN官方 4新浪微博",
                                 help_text="通知来源：1官方平台 2开源中国 3CSDN官方 4新浪微博")
    # 外部地址
    url = models.CharField(null=True, max_length=255, verbose_name="外部地址", help_text="外部地址")
    # 点击率
    click = models.IntegerField(default=0, verbose_name="点击率", help_text="点击率")
    # 通知状态：1-正常 2-停用
    STATUS_CHOICES = (
        (1, "正常"),
        (2, "停用"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="通知状态：1-正常 2-停用",
                                 help_text="通知状态：1-正常 2-停用")
    # 是否置顶：1-是 2-否
    is_top = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="是否置顶：1-是 2-否",
                                 help_text="是否置顶：1-是 2-否")
    # 通知公告内容
    content = models.TextField(null=True, verbose_name="通知公告标题", help_text="通知公告标题")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "notice"
        verbose_name = "通知公告表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "通知公告{}".format(self.title)
