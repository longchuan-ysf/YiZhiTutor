from django.db import models

# Create your models here.
from application import settings
from application.models import BaseModel


# 职级模型
class Level(BaseModel):
    # 职级名称
    name = models.CharField(db_column='name', unique=False, blank=True, null=False, max_length=150,
                            verbose_name="职级名称",
                            help_text="职级名称")
    # 排序
    sort = models.IntegerField(default=0, verbose_name="职级顺序", help_text="职级顺序")
    # 状态选项
    STATUS_CHOICES = (
        (1, "正常"),
        (2, "停用"),
    )
    # 状态
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="职级状态：1-正常 2-停用",
                                 help_text="职级状态：1-正常 2-停用")

    class Meta:
        # 数据表名
        db_table = settings.TABLE_PREFIX + "level"
        verbose_name = "职级表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)

    def __str__(self):
        return '职级{}'.format(self.name)
