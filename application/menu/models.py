from django.db import models

# Create your models here.
from application.models import BaseModel

from config.env import TABLE_PREFIX


# 菜单模型
class Menu(BaseModel):
    # 菜单名称
    name = models.CharField(max_length=150, verbose_name="菜单名称", help_text="菜单名称")
    # 菜单图标
    icon = models.CharField(max_length=50, verbose_name="菜单图标", help_text="菜单图标")
    # 菜单URL
    url = models.CharField(max_length=255, verbose_name="菜单URL", help_text="菜单URL")
    # 上级ID
    pid = models.IntegerField(default=0, verbose_name="上级ID", help_text="上级ID")
    # 菜单类型：0-菜单 1-节点
    type = models.IntegerField(default=0, verbose_name="菜单类型：0-菜单 1-节点",
                               help_text="菜单类型：0-菜单 1-节点")
    # 权限节点
    permission = models.CharField(max_length=150, verbose_name="权限节点", help_text="权限节点")
    # 状态选项
    STATUS_CHOICES = (
        (1, "正常"),
        (2, "停用"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="菜单状态：1-正常 2-停用",
                                 help_text="菜单状态：1-正常 2-停用")
    # 打开方式：1-内部打开 2-外部打开
    TARGET_CHOICES = (
        (1, "内部打开"),
        (2, "外部打开"),
    )
    target = models.IntegerField(choices=TARGET_CHOICES, default=1, verbose_name="打开方式：1-内部打开 2-外部打开",
                                 help_text="打开方式：1-内部打开 2-外部打开")
    # 排序
    sort = models.IntegerField(default=0, verbose_name="排序", help_text="排序")
    # 备注
    note = models.CharField(null=True, max_length=255, verbose_name="备注", help_text="备注")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "menu"
        verbose_name = "菜单表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "菜单{}".format(self.id)
