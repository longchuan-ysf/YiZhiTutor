from django.db import models

# Create your models here.


from config.env import TABLE_PREFIX


# 用户角色模型
class UserRole(models.Model):
    # 用户ID
    user_id = models.IntegerField(default=0, verbose_name="用户ID", help_text="用户ID")
    # 角色ID
    role_id = models.IntegerField(default=0, verbose_name="角色ID", help_text="角色ID")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "user_role"
        verbose_name = "用户角色表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户角色表{}".format(self.user_id)
