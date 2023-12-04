from django.db import models

# Create your models here.
from application.models import BaseModel
from config.env import TABLE_PREFIX


# 栏目模型
class ItemCate(BaseModel):
    # 栏目名称
    name = models.CharField(null=False, max_length=150, verbose_name="栏目名称", help_text="栏目名称")
    # 上级ID
    pid = models.IntegerField(null=False, default=0, verbose_name="上级ID", help_text="上级ID")
    # 站点ID
    item_id = models.IntegerField(null=False, default=0, verbose_name="站点ID", help_text="站点ID")
    # 拼音(全拼)
    pinyin = models.CharField(null=False, max_length=150, verbose_name="拼音(全拼)", help_text="拼音(全拼)")
    # 拼音(简拼)
    code = models.CharField(null=False, max_length=150, verbose_name="拼音(简拼)", help_text="拼音(简拼)")
    # 是否有封面：1是 2否
    is_cover = models.IntegerField(null=False, default=2, verbose_name="是否有封面：1是 2否", help_text="是否有封面：1是 2否")
    # 封面地址
    cover = models.CharField(null=False, max_length=255, verbose_name="封面地址", help_text="封面地址")
    # 栏目状态
    STATUS_CHOICES = (
        (1, "正常"),
        (2, "停用"),
    )
    status = models.IntegerField(null=False, choices=STATUS_CHOICES, default=1, verbose_name="栏目状态：1-正常 2-停用",
                                 help_text="栏目状态：1-正常 2-停用")
    # 栏目备注
    note = models.CharField(null=True, max_length=255, verbose_name="栏目备注", help_text="栏目备注")
    # 栏目排序
    sort = models.IntegerField(default=0, verbose_name="栏目排序", help_text="栏目排序")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "item_cate"
        verbose_name = "栏目表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "栏目{}".format(self.name)
