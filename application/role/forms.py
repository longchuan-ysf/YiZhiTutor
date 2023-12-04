from django import forms

from application.role import models


# 角色表单验证
class RoleForm(forms.ModelForm):
    # 角色名称
    name = forms.CharField(
        max_length=150,
        error_messages={
            'required': '角色名称不能为空',
            'max_length': '角色名称长度不得超过150个字符',
        }
    )
    # 角色编码
    code = forms.CharField(
        max_length=30,
        error_messages={
            'required': '角色编码不能为空',
            'max_length': '角色编码长度不得超过30个字符',
        }
    )
    # 角色状态：1-正常 2-停用
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '角色状态不能为空',
            'min_value': '角色状态值在1~2之间',
            'max_value': '角色状态值在1~2之间',
        }
    )
    # 角色排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '角色排序不能为空',
            'min_value': '角色排序值在0~99999之间',
            'max_value': '角色排序值在0~99999之间',
        }
    )
    # 角色备注
    note = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '角色备注长度不能大于255个字符'
        }
    )

    class Meta:
        # 绑定模型
        model = models.Role
        # 指定字段验证
        fields = ['name', 'code', 'status', 'sort', 'note']


# 设置状态
class RoleStatusForm(forms.ModelForm):
    # 角色状态
    id = forms.IntegerField(
        min_value=1,
        error_messages={
            'required': '角色ID不能为空',
            'min_value': '角色ID最小值不能小于1',
        }
    )
    # 角色状态
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '角色状态不能为空',
            'min_value': '角色状态值在1~2之间',
            'max_value': '角色状态值在1~2之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Role
        # 指定部分字段验证
        fields = ["id", "status"]
