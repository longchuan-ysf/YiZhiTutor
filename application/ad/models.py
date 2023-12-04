from django.db import models

# Create your models here.
from application.models import BaseModel

from config.env import TABLE_PREFIX


# 广告模型
class Ad(BaseModel):
    # 广告标题
    title = models.CharField(null=False, max_length=255, verbose_name="广告标题", help_text="广告标题")
    # 广告ID
    sort_id = models.IntegerField(default=0, verbose_name="广告ID", help_text="广告ID")
    # 广告类型：1图片 2文字 3视频 4推荐
    TYPE_CHOICES = (
        (1, "图片"),
        (2, "文字"),
        (3, "视频"),
        (4, "推荐"),
    )
    type = models.IntegerField(choices=TYPE_CHOICES, default=0, verbose_name="广告类型：1图片 2文字 3视频 4推荐",
                               help_text="广告类型：1图片 2文字 3视频 4推荐")
    # 广告封面
    cover = models.CharField(null=True, max_length=255, verbose_name="广告封面", help_text="广告封面")
    # 广告地址
    url = models.CharField(null=True, max_length=255, verbose_name="广告地址", help_text="广告地址")
    # 广告宽度
    width = models.IntegerField(default=0, verbose_name="广告宽度", help_text="广告宽度")
    # 广告高度
    height = models.IntegerField(default=0, verbose_name="广告高度", help_text="广告高度")
    # 开始时间
    start_time = models.DateTimeField(null=True, max_length=11, verbose_name="开始时间", help_text="开始时间")
    # 结束时间
    end_time = models.DateTimeField(null=True, max_length=11, verbose_name="结束时间", help_text="结束时间")
    # 点击率
    click = models.IntegerField(default=0, verbose_name="点击率", help_text="点击率")
    # 广告状态
    STATUS_CHOICES = (
        (1, "正常"),
        (2, "停用"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="广告状态：1-正常 2-停用",
                                 help_text="广告状态：1-正常 2-停用")
    # 广告备注
    note = models.CharField(null=True, max_length=255, verbose_name="广告备注", help_text="广告备注")
    # 广告排序
    sort = models.IntegerField(default=0, verbose_name="广告排序", help_text="广告排序")
    # 广告内容
    content = models.TextField(null=True, verbose_name="广告内容", help_text="广告内容")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "ad"
        verbose_name = "广告表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "广告{}".format(self.title)
