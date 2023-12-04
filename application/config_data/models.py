from django.db import models

# Create your models here.
from application.models import BaseModel

from config.env import TABLE_PREFIX


# 配置项模型
class ConfigData(BaseModel):
    # 配置项标题
    title = models.CharField(max_length=150, verbose_name="配置项标题", help_text="配置项标题")
    # 配置项编码
    code = models.CharField(max_length=150, verbose_name="配置项编码", help_text="配置项编码")
    # 配置项值
    value = models.CharField(max_length=1000, verbose_name="配置项值", help_text="配置项值")
    # 配置选项
    options = models.CharField(max_length=255, verbose_name="配置选项", help_text="配置选项")
    # 配置ID
    config_id = models.IntegerField(default=0, verbose_name="配置ID", help_text="配置ID")
    # 配置类型
    type = models.CharField(max_length=150, verbose_name="配置类型", help_text="配置类型")
    # 配置状态
    STATUS_CHOICES = (
        (1, "正常"),
        (2, "停用"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="配置状态：1-正常 2-停用",
                                 help_text="配置状态：1-正常 2-停用")
    # 配置项排序
    sort = models.IntegerField(default=0, verbose_name="配置项顺序", help_text="配置项顺序")
    # 配置项备注
    note = models.CharField(null=True, max_length=255, verbose_name="配置项备注", help_text="配置项备注")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "config_data"
        verbose_name = "配置项表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "配置项{}".format(self.id)
