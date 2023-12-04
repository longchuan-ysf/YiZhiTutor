from django.db import models

# Create your models here.
from application.models import BaseModel

from config.env import TABLE_PREFIX


# 用户模型
class User(BaseModel):
    # 用户姓名
    realname = models.CharField(max_length=150, verbose_name="用户姓名", help_text="用户姓名")
    # 用户昵称
    nickname = models.CharField(max_length=150, verbose_name="用户昵称", help_text="用户昵称")
    # 性别：1-男 2-女 3-保密
    GENDER_CHOICES = (
        (1, "男"),
        (2, "女"),
        (3, "保密"),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1, verbose_name="性别：1-男 2-女 3-保密",
                                 help_text="性别：1-男 2-女 3-保密")
    # 用户头像
    avatar = models.CharField(max_length=255, verbose_name="用户头像", help_text="用户头像")
    # 手机号
    mobile = models.CharField(max_length=30, verbose_name="手机号", help_text="手机号")
    # 邮箱
    email = models.CharField(max_length=50, verbose_name="邮箱", help_text="邮箱")
    # 出生日期
    birthday = models.DateField(max_length=30, verbose_name="出生日期", help_text="出生日期")
    # 部门ID
    dept_id = models.IntegerField(default=0, verbose_name="部门ID", help_text="部门ID")
    # 职级ID
    level_id = models.IntegerField(default=0, verbose_name="职级ID", help_text="职级ID")
    # 岗位ID
    position_id = models.IntegerField(default=0, verbose_name="岗位ID", help_text="岗位ID")
    # 省份编码
    province_code = models.CharField(max_length=30, verbose_name="省份编码", help_text="省份编码")
    # 城市编码
    city_code = models.CharField(max_length=30, verbose_name="城市编码", help_text="城市编码")
    # 县区编码
    district_code = models.CharField(max_length=30, verbose_name="县区编码", help_text="县区编码")
    # 省市区信息
    address_info = models.CharField(max_length=255, verbose_name="省市区信息", help_text="省市区信息")
    # 详细地址
    address = models.CharField(max_length=255, verbose_name="详细地址", help_text="详细地址")
    # 用户名
    username = models.CharField(max_length=30, verbose_name="用户名", help_text="用户名")
    # 密码
    password = models.CharField(null=True, max_length=255, verbose_name="密码", help_text="密码")
    # 加密盐
    salt = models.CharField(null=True, max_length=30, verbose_name="加密盐", help_text="加密盐")
    # 个人简介
    intro = models.CharField(null=True, max_length=255, verbose_name="个人简介", help_text="个人简介")
    # 状态
    STATUS_CHOICES = (
        (1, "正常"),
        (2, "禁用"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="状态：1-正常 2-禁用",
                                 help_text="状态：1-正常 2-禁用")
    # 个人备注
    note = models.CharField(null=True, max_length=255, verbose_name="个人备注", help_text="个人备注")
    # 排序
    sort = models.IntegerField(default=0, verbose_name="排序", help_text="排序")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "user"
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户{}".format(self.id)
