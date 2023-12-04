from django import forms

# 菜单表单验证
from application.menu import models


# 菜单表单验证
class MenuForm(forms.ModelForm):
    # 菜单名称
    name = forms.CharField(
        max_length=150,
        error_messages={
            'required': '菜单名称不能为空',
            'max_length': '菜单名称长度不得超过150个字符',
        }
    )
    # 菜单图标
    icon = forms.CharField(
        required=False,
        max_length=50,
        error_messages={
            'required': '菜单图标不能为空',
            'max_length': '菜单图标长度不得超过50个字符',
        }
    )
    # 菜单URL
    url = forms.CharField(
        max_length=255,
        error_messages={
            'required': '菜单URL不能为空',
            'max_length': '菜单URL长度不得超过255个字符',
        }
    )
    # 上级ID
    pid = forms.IntegerField(
        required=False,
        min_value=0,
        error_messages={
            'min_value': '上级菜单ID不能小于0'
        }
    )
    # 菜单类型：0-菜单 1-节点
    type = forms.IntegerField(
        min_value=0,
        max_value=1,
        error_messages={
            'required': '菜单类型不能为空',
            'min_value': '菜单类型值在0~1之间',
            'max_value': '菜单类型值在0~1之间',
        }
    )
    # 权限节点
    permission = forms.CharField(
        required=False,
        max_length=150,
        error_messages={
            'required': '权限节点不能为空',
            'max_length': '权限节点长度不得超过150个字符',
        }
    )
    # 打开方式：1-内部打开 2-外部打开
    target = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '打开方式不能为空',
            'min_value': '打开方式值在1~2之间',
            'max_value': '打开方式值在1~2之间',
        }
    )
    # 菜单状态：1-正常 2-禁用
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '菜单状态不能为空',
            'min_value': '菜单状态值在1~2之间',
            'max_value': '菜单状态值在1~2之间',
        }
    )
    # 菜单排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '菜单排序不能为空',
            'min_value': '菜单排序值在0~99999之间',
            'max_value': '菜单排序值在0~99999之间',
        }
    )
    # 菜单备注
    note = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '菜单备注长度不能大于255个字符'
        }
    )
    # 菜单节点
    func = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '菜单节点长度不能大于255个字符'
        }
    )

    class Meta:
        # 绑定模型
        model = models.Menu
        # 指定部分字段验证
        fields = ['name', 'icon', 'url', 'pid', 'type', 'permission', 'target', 'status', 'sort', 'note', 'func']
