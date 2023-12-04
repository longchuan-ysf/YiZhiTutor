from django import forms

from application.dept import models


# 部门表单验证
class DeptForm(forms.ModelForm):
    # 部门名称
    name = forms.CharField(
        max_length=150,
        error_messages={
            'required': '部门名称不能为空',
            'min_length': '部门名称长度不得超过150个字符',
            'max_length': '部门名称长度不得超过150个字符',
        }
    )
    # 部门编码
    code = forms.CharField(
        max_length=150,
        error_messages={
            'required': '部门编码不能为空',
            'min_length': '部门编码长度不得超过150个字符',
            'max_length': '部门编码长度不得超过150个字符',
        }
    )
    # 部门类型
    type = forms.IntegerField(
        min_value=1,
        max_value=4,
        error_messages={
            'required': '部门类型不能为空',
            'min_value': '部门类型值在1~4之间',
            'max_value': '部门类型值在1~4之间',
        }
    )
    # 上级ID
    pid = forms.IntegerField(
        min_value=0,
        error_messages={
            'min_value': '上级部门ID不能小于0'
        }
    )
    # 部门排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '部门排序不能为空',
            'min_value': '部门排序值在0~99999之间',
            'max_value': '部门排序值在0~99999之间',
        }
    )
    # 部门备注
    note = forms.CharField(
        # #required不写默认=True
        required=False,
        max_length=255,
        error_messages={
            'max_length': '部门备注长度不能大于255个字符'
        }
    )

    class Meta:
        # 绑定模型
        model = models.Dept
        # 指定部分字段验证
        fields = ['name', 'code', 'type', 'pid', 'sort', 'note']
