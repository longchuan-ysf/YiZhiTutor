from django.db import models

# Create your models here.
from application.models import BaseModel

from config.env import TABLE_PREFIX


# 城市模型
class City(BaseModel):
    # 城市区号
    city_code = models.CharField(null=False, max_length=6, verbose_name="城市区号", help_text="城市区号")
    # 行政编码
    area_code = models.CharField(null=False, max_length=20, verbose_name="行政编码", help_text="行政编码")
    # 上级行政编码
    parent_code = models.CharField(null=True, max_length=20, verbose_name="上级行政编码", help_text="上级行政编码")
    # 邮政编码
    zip_code = models.CharField(null=False, max_length=6, verbose_name="邮政编码", help_text="邮政编码")
    # 城市级别
    level = models.IntegerField(default=0, verbose_name="城市级别：1-省份 2-城市 3-县区 4-街道",
                                help_text="城市级别：1-省份 2-城市 3-县区 4-街道")
    # 上级城市ID
    pid = models.IntegerField(null=False, default=0, verbose_name="上级城市ID", help_text="上级城市ID")
    # 城市名称
    name = models.CharField(null=False, max_length=150, verbose_name="城市名称", help_text="城市名称")
    # 城市简称
    short_name = models.CharField(null=False, max_length=150, verbose_name="城市简称", help_text="城市简称")
    # 城市全称
    full_name = models.CharField(null=True, max_length=150, verbose_name="城市全称", help_text="城市全称")
    # 城市拼音
    pinyin = models.CharField(null=True, max_length=150, verbose_name="城市拼音", help_text="城市拼音")
    # 城市经度
    lng = models.CharField(null=True, max_length=150, verbose_name="城市经度", help_text="城市经度")
    # 城市纬度
    lat = models.CharField(null=True, max_length=150, verbose_name="城市纬度", help_text="城市纬度")

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + "city"
        verbose_name = "城市表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '城市{}'.format(self.id)
