from django.db import models

# Create your models here.
from application.models import BaseModel

from config.env import TABLE_PREFIX


# 配置模型
class Config(BaseModel):
    # 配置名称
    name = models.CharField(null=False, max_length=150, verbose_name="配置名称", help_text="配置名称")
    # 配置排序
    sort = models.IntegerField(default=0, verbose_name="配置排序", help_text="配置排序")
    # 配置备注
    note = models.CharField(null=True, max_length=255, verbose_name="配置备注", help_text="配置备注")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "config"
        verbose_name = "配置表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "配置{}".format(self.id)
