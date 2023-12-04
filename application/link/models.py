from django.db import models

# Create your models here.
from application.models import BaseModel

from config.env import TABLE_PREFIX


# 友链模型
class Link(BaseModel):
    # 友链名称
    name = models.CharField(null=False, max_length=255, verbose_name="友链名称", help_text="友链名称")
    # 友链类型
    TYPE_CHOICES = (
        (1, "友情链接"),
        (2, "合作伙伴"),
    )
    type = models.IntegerField(choices=TYPE_CHOICES, default=1, verbose_name="友链类型：1友情链接 2合作伙伴",
                               help_text="友链类型：1友情链接 2合作伙伴")
    # 友链URL
    url = models.CharField(null=True, default=None, max_length=255, verbose_name="友链URL", help_text="友链URL")
    # 站点ID
    item_id = models.IntegerField(null=False, default=0, verbose_name="站点ID", help_text="站点ID")
    # 栏目ID
    cate_id = models.IntegerField(null=False, default=0, verbose_name="栏目ID", help_text="栏目ID")
    # 投放平台
    PLATFORM_CHOICES = (
        (1, "PC站"),
        (2, "WAP站"),
        (3, "微信小程序"),
        (4, "APP应用"),
    )
    platform = models.IntegerField(choices=PLATFORM_CHOICES, default=1, verbose_name="投放平台：1PC站 2WAP站 3微信小程序 4APP应用",
                                   help_text="投放平台：1PC站 2WAP站 3微信小程序 4APP应用")
    # 友链形式
    TYPE_CHOICES = (
        (1, "文字链接"),
        (2, "图片链接"),
    )
    form = models.IntegerField(choices=TYPE_CHOICES, default=1, verbose_name="友链形式：1文字链接 2图片链接",
                               help_text="友链形式：1文字链接 2图片链接")
    # 友链图片
    image = models.CharField(null=False, max_length=255, verbose_name="友链图片", help_text="友链图片")

    # 友链状态
    STATUS_CHOICES = (
        (1, "正常"),
        (2, "停用"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="友链状态：1-正常 2-停用",
                                 help_text="友链状态：1-正常 2-停用")
    # 友链顺序
    sort = models.IntegerField(default=0, verbose_name="友链顺序", help_text="友链顺序")
    # 友链备注
    note = models.CharField(null=True, max_length=255, verbose_name="友链备注", help_text="友链备注")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "link"
        verbose_name = "友链表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "友链{}".format(self.name)
