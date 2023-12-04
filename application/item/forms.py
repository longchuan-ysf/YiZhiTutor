from django import forms

from application.item import models


# 站点表单验证
class ItemForm(forms.ModelForm):
    # 站点名称
    name = forms.CharField(
        max_length=150,
        error_messages={
            'required': '站点名称不能为空',
            'max_length': '站点名称长度不得超过150个字符',
        }
    )
    # 站点类型：1普通站点 2其他站点
    type = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '站点类型不能为空',
            'min_value': '站点类型值在1~2之间',
            'max_value': '站点类型值在1~2之间',
        }
    )
    # 站点URL
    url = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'required': '站点URL不能为空',
            'max_length': '站点URL长度不得超过255个字符',
        }
    )
    # 站点图片
    image = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'required': '站点图片不能为空',
            'max_length': '站点图片长度不得超过255个字符',
        }
    )
    # 站点状态：1-正常 2-停用
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '站点状态不能为空',
            'min_value': '站点状态值在1~2之间',
            'max_value': '站点状态值在1~2之间',
        }
    )
    # 站点备注
    note = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '站点备注长度不得超过255个字符',
        }
    )
    # 站点排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '站点排序不能为空',
            'min_value': '站点排序值在0~99999之间',
            'max_value': '站点排序值在0~99999之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Item
        # 指定部分字段验证
        fields = ['name', 'type', 'status', 'sort']
