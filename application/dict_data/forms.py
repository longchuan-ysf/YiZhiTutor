from django import forms

from application.dict_data import models


# 字典项表单验证
class DictDataForm(forms.ModelForm):
    # 字典项名称
    name = forms.CharField(
        max_length=150,
        error_messages={
            'required': '字典项名称不能为空',
            'max_length': '字典项名称长度不得超过150个字符',
        }
    )
    # 字典项值
    value = forms.CharField(
        max_length=150,
        error_messages={
            'required': '字典项值不能为空',
            'max_length': '字典项值长度不得超过150个字符',
        }
    )
    # 字典ID
    dict_id = forms.IntegerField(
        min_value=0,
        error_messages={
            'required': '字典ID不能为空',
            'min_value': '字典ID不能小于0',
        }
    )
    # 字典项备注
    note = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '字典项备注长度不得超过255个字符',
        }
    )
    # 字典项排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '字典项排序不能为空',
            'min_value': '字典项排序值在0~99999之间',
            'max_value': '字典项排序值在0~99999之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.DictData
        # 指定部分字段验证
        fields = ['name', 'value', 'dict_id', 'sort', 'note']
