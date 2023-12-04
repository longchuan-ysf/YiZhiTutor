from django.db import models

# Create your models here.
from application.models import BaseModel

from config.env import TABLE_PREFIX


# 角色模型
class Role(BaseModel):
    # 角色名称
    name = models.CharField(null=False, max_length=150, verbose_name="角色名称", help_text="角色名称")
    # 角色编码
    code = models.CharField(null=False, max_length=30, verbose_name="角色编码", help_text="角色编码")
    # 角色状态
    STATUS_CHOICES = (
        (1, '正常'),
        (2, '停用')
    )
    status = models.IntegerField(null=False, choices=STATUS_CHOICES, default=1, verbose_name="角色状态：1-正常 2-停用",
                                 help_text="角色状态：1-正常 2-停用")
    # 角色排序
    sort = models.IntegerField(null=False, default=0, verbose_name="角色排序", help_text="角色排序")
    # 备注
    note = models.CharField(null=True, max_length=255, verbose_name="备注", help_text="备注")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + 'role'
        verbose_name = '角色表'
        verbose_name_plural = verbose_name
        ordering = ("sort",)

    def __str__(self):
        return '角色{}：'.format(self.name)
