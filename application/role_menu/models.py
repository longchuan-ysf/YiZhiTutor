from django.db import models

# Create your models here.
from application.models import BaseModel

from config.env import TABLE_PREFIX


# 角色菜单模型
class RoleMenu(models.Model):
    # 角色ID
    role_id = models.IntegerField(default=0, verbose_name="角色ID", help_text="角色ID")
    # 菜单ID
    menu_id = models.IntegerField(default=0, verbose_name="菜单ID", help_text="菜单ID")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "role_menu"
        verbose_name = "角色菜单表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "角色菜单表{}".format(self.role_id)
