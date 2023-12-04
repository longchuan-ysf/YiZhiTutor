from django.db import models

# Create your models here.
from application.models import BaseModel

from config.env import TABLE_PREFIX


# 字典模型
class Dict(BaseModel):
    # 字典名称
    name = models.CharField(null=False, max_length=150, verbose_name="字典名称", help_text="字典名称")
    # 字典编码
    code = models.CharField(null=False, max_length=150, verbose_name="字典编码", help_text="字典编码")
    # 字典排序
    sort = models.IntegerField(default=0, verbose_name="字典排序", help_text="字典排序")
    # 字典备注
    note = models.CharField(null=True, max_length=255, verbose_name="字典备注", help_text="字典备注")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "dict"
        verbose_name = "字典表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "字典{}".format(self.id)
