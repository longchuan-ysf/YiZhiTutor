from django.db import models

# Create your models here.
from application.models import BaseModel
from config.env import TABLE_PREFIX


# 部门模型
class Dept(BaseModel):
    # 部门名称
    name = models.CharField(null=False, max_length=150, verbose_name="部门名称", help_text="部门名称")
    # 部门编码
    code = models.CharField(null=False, max_length=150, verbose_name="部门编码", help_text="部门编码")
    # 部门类型：1-公司 2-子公司 3-部门 4-小组
    type = models.IntegerField(null=False, default=0, verbose_name="部门类型：1-公司 2-子公司 3-部门 4-小组",
                               help_text="部门类型：1-公司 2-子公司 3-部门 4-小组")
    # 上级部门ID
    pid = models.IntegerField(default=0, verbose_name="上级部门ID", help_text="上级部门ID")
    # 部门排序
    sort = models.IntegerField(null=False, default=0, verbose_name="部门排序", help_text="部门排序")
    # 备注
    note = models.CharField(null=True, max_length=255, default='', verbose_name="备注", help_text="备注")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "dept"
        verbose_name = "部门表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)

    def __str__(self):
        return '部门{}'.format(self.name)
