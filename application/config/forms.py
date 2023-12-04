from django import forms

from application.config import models


# 配置表单验证
class ConfigForm(forms.ModelForm):
    # 配置名称
    name = forms.CharField(
        max_length=150,
        error_messages={
            'required': '配置名称不能为空',
            'max_length': '配置名称长度不得超过150个字符',
        }
    )
    # 配置排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '配置排序不能为空',
            'min_value': '配置排序值在0~99999之间',
            'max_value': '配置排序值在0~99999之间',
        }
    )
    # 配置备注
    note = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '配置备注长度不得超过255个字符',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Config
        # 指定部分字段验证
        fields = ['name', 'sort', 'note']
