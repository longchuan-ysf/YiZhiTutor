from django.db import models

# Create your models here.
from application.models import BaseModel

from config.env import TABLE_PREFIX


# 站点模型
class Item(BaseModel):
    # 站点名称
    name = models.CharField(null=False, max_length=150, verbose_name="站点名称", help_text="站点名称")
    # 站点类型
    TYPE_CHOICES = (
        (1, "普通站点"),
        (2, "其他站点"),
    )
    type = models.IntegerField(choices=TYPE_CHOICES, default=1, verbose_name="站点类型：1普通站点 2其他站点",
                               help_text="站点类型：1普通站点 2其他站点")
    # 站点地址
    url = models.CharField(null=True, max_length=255, verbose_name="站点地址", help_text="站点地址")
    # 站点图片
    image = models.CharField(null=True, max_length=255, verbose_name="站点图片", help_text="站点图片")
    # 站点状态
    STATUS_CHOICES = (
        (1, "正常"),
        (2, "停用"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="站点状态：1-正常 2-停用",
                                 help_text="站点状态：1-正常 2-停用")
    # 站点备注
    note = models.CharField(null=True, max_length=255, verbose_name="站点备注", help_text="站点备注")
    # 站点排序
    sort = models.IntegerField(default=0, verbose_name="站点顺序", help_text="站点顺序")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "item"
        verbose_name = "站点表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "站点{}".format(self.name)
