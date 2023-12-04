from django import forms

from application.dict import models


# 字典表单验证
class DictForm(forms.ModelForm):
    # 字典名称
    name = forms.CharField(
        max_length=150,
        error_messages={
            'required': '字典名称不能为空',
            'max_length': '字典名称长度不得超过150个字符',
        }
    )
    # 字典编码
    code = forms.CharField(
        max_length=150,
        error_messages={
            'required': '字典编码不能为空',
            'max_length': '字典编码长度不得超过150个字符',
        }
    )
    # 字典排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '字典排序不能为空',
            'min_value': '字典排序值在0~99999之间',
            'max_value': '字典排序值在0~99999之间',
        }
    )
    # 字典备注
    note = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '字典备注长度不得超过255个字符',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Dict
        # 指定部分字段验证
        fields = ['name', 'code', 'sort', 'note']
