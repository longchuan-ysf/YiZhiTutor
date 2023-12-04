from django.db import models

# Create your models here.
from application.models import BaseModel
from config.env import TABLE_PREFIX


# 广告位模型
class AdSort(BaseModel):
    # 广告位名称
    name = models.CharField(null=False, max_length=255, verbose_name="广告位名称",
                            help_text="广告位名称")
    # 站点ID
    item_id = models.IntegerField(default=0, verbose_name="站点ID", help_text="站点ID")
    # 栏目ID
    cate_id = models.IntegerField(default=0, verbose_name="栏目ID", help_text="栏目ID")
    # 广告位位置
    loc_id = models.IntegerField(default=0, verbose_name="广告位位置", help_text="广告位位置")
    # 投放平台
    PLATFORM_CHOICES = (
        (1, "PC站"),
        (2, "WAP站"),
        (3, "微信小程序"),
        (4, "APP应用"),
    )
    platform = models.IntegerField(choices=PLATFORM_CHOICES, default=0, verbose_name="投放平台：1PC站 2WAP站 3微信小程序 4APP应用",
                                   help_text="投放平台：1PC站 2WAP站 3微信小程序 4APP应用")
    # 广告位描述
    description = models.CharField(null=True, max_length=255, verbose_name="广告位描述", help_text="广告位描述")
    # 广告位排序
    sort = models.IntegerField(default=0, verbose_name="广告位排序", help_text="广告位排序")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "ad_sort"
        verbose_name = "广告位表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "广告位{}".format(self.name)
