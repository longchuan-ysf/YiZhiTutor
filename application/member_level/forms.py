from django import forms

from application.member_level import models


# 会员等级表单验证
class MemberLevelForm(forms.ModelForm):
    # 会员等级名称
    name = forms.CharField(
        max_length=255,
        error_messages={
            'required': '会员等级名称不能为空',
            'max_length': '会员等级名称长度不得超过255个字符',

        }
    )
    # 会员等级排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '会员等级排序不能为空',
            'min_value': '会员等级排序值在0~99999之间',
            'max_value': '会员等级排序值在0~99999之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.MemberLevel
        # 指定部分字段验证
        fields = ['name', 'sort']
