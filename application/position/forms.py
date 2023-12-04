from django import forms

from application.position import models


# 岗位表单验证
class PositionForm(forms.ModelForm):
    # 岗位名称
    name = forms.CharField(
        max_length=150,
        error_messages={
            'required': '岗位名称不能为空',
            'max_length': '岗位名称长度不得超过150个字符',
        }
    )
    # 岗位状态
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '岗位状态不能为空',
            'min_value': '岗位状态值在1~2之间',
            'max_value': '岗位状态值在1~2之间',
        }
    )
    # 岗位排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '岗位排序不能为空',
            'min_value': '岗位排序值在0~99999之间',
            'max_value': '岗位排序值在0~99999之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Position
        # 指定部分字段验证
        fields = ['name', 'status', 'sort']


# 岗位状态设置
class PositionStatusForm(forms.ModelForm):
    # 岗位状态
    id = forms.IntegerField(
        min_value=1,
        error_messages={
            'min_value': '岗位ID最小值不能小于1',
            'required': '岗位ID不能为空'
        }
    )
    # 岗位状态
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '岗位状态不能为空',
            'min_value': '岗位状态值在1~2之间',
            'max_value': '岗位状态值在1~2之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Position
        # 指定部分字段验证
        fields = ["id", "status"]
