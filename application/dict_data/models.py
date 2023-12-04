from django.db import models

# Create your models here.
from application.models import BaseModel

from config.env import TABLE_PREFIX


# 字典项模型
class DictData(BaseModel):
    # 字典项名称
    name = models.CharField(null=False, max_length=150, verbose_name="字典项名称", help_text="字典项名称")
    # 字典项值
    value = models.CharField(null=False, max_length=150, verbose_name="字典项值", help_text="字典项值")
    # 字典ID
    dict_id = models.IntegerField(default=0, verbose_name="字典ID", help_text="字典ID")
    # 字典项备注
    note = models.CharField(null=True, max_length=255, verbose_name="字典项备注", help_text="字典项备注")
    # 字典项排序
    sort = models.IntegerField(default=0, verbose_name="字典项顺序", help_text="字典项顺序")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "dict_data"
        verbose_name = "字典项表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "字典项{}".format(self.id)
