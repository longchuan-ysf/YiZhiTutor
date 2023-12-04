from django.db import models

from application import settings
from application.models import BaseModel


# 岗位模型
class Position(BaseModel):
    # 岗位名称
    name = models.CharField(null=False, max_length=150, blank=True, default=None, verbose_name="岗位名称", help_text="岗位名称")
    # 排序
    sort = models.IntegerField(default=0, verbose_name="岗位顺序", help_text="岗位顺序")
    # 状态选项
    STATUS_CHOICES = (
        (1, "正常"),
        (2, "停用"),
    )
    # 状态
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="岗位状态：1-正常 2-停用",
                                 help_text="岗位状态：1-正常 2-停用")

    class Meta:
        # 数据表名
        db_table = settings.TABLE_PREFIX + "position"
        verbose_name = "岗位表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)

    def __str__(self):
        return '岗位{}'.format(self.name)
