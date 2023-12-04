from django.db import models

# Create your models here.
from application.models import BaseModel
from config.env import TABLE_PREFIX


# 会员等级模型
class MemberLevel(BaseModel):
    # 会员等级名称
    name = models.CharField(db_column='name', unique=False, blank=True, null=False, max_length=150,
                            verbose_name="会员等级名称",
                            help_text="会员等级名称")
    # 排序
    sort = models.IntegerField(default=0, verbose_name="排序", help_text="排序")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "member_level"
        verbose_name = "会员等级表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)

    def __str__(self):
        return '会员等级{}'.format(self.name)
