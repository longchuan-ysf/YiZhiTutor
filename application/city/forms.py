from django import forms

# 城市表单验证
from application.city import models


class CityForm(forms.ModelForm):
    # 城市名称
    name = forms.CharField(
        required=True,
        max_length=150,
        error_messages={
            'required': '城市名称不能为空',
            'max_length': '城市名称长度不得超过150个字符'
        }
    )
    # 城市简称
    short_name = forms.CharField(
        required=True,
        max_length=150,
        error_messages={
            'required': '城市简称不能为空',
            'max_length': '城市简称长度不得超过150个字符'
        }
    )
    # # 城市全称
    # full_name = forms.CharField(
    #     required=True,
    #     max_length=150,
    #     error_messages={
    #         'required': '城市全称不能为空',
    #         'max_length': '城市全称长度不得超过150个字符'
    #     }
    # )
    # 城市拼音
    pinyin = forms.CharField(
        required=True,
        max_length=150,
        error_messages={
            'required': '城市拼音不能为空',
            'max_length': '城市拼音长度不得超过150个字符'
        }
    )
    # 城市区号
    city_code = forms.CharField(
        required=True,
        max_length=6,
        error_messages={
            'required': '城市区号不能为空',
            'max_length': '城市区号长度不得超过6个字符'
        }
    )
    # 行政编码
    area_code = forms.CharField(
        required=True,
        max_length=20,
        error_messages={
            'required': '行政编码不能为空',
            'max_length': '行政编码长度不得超过20个字符'
        }
    )
    # 城市邮编
    zip_code = forms.CharField(
        max_length=6,
        error_messages={
            'required': '城市邮编不能为空',
            'max_length': '城市邮编长度不得超过6个字符'
        }
    )
    # 城市级别
    level = forms.IntegerField(
        min_value=1,
        max_value=4,
        error_messages={
            'required': '城市级别不能为空',
            'min_value': '城市级别值在1~4之间',
            'max_value': '城市级别值在1~4之间',
        }
    )
    # 城市经度
    lng = forms.CharField(
        required=True,
        max_length=150,
        error_messages={
            'required': '城市经度不能为空',
            'max_length': '城市经度长度不得超过150个字符'
        }
    )
    # 城市纬度
    lat = forms.CharField(
        required=True,
        max_length=150,
        error_messages={
            'required': '城市纬度不能为空',
            'max_length': '城市纬度长度不得超过150个字符'
        }
    )
    # 上级城市ID
    pid = forms.IntegerField(
        min_value=0,
        error_messages={
            'required': '上级城市ID不能为空',
            'min_value': '上级城市ID不能小于0',
        }
    )

    class Meta:
        # 绑定模型
        model = models.City
        # 指定部分字段验证
        fields = ['name', 'city_code', 'area_code', 'parent_code', 'level', 'zip_code', 'short_name', 'pinyin', 'lng',
                  'lat']
