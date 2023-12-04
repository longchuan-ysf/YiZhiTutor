from django import forms

from application.level import models


# 职级表单验证
class LevelForm(forms.ModelForm):
    # 职级名称
    name = forms.CharField(
        max_length=150,
        error_messages={
            'required': '职级名称不能为空',
            'max_length': '职级名称长度不得超过150个字符',
        }
    )
    # 职级状态
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '职级状态不能为空',
            'min_value': '职级状态值在1~2之间',
            'max_value': '职级状态值在1~2之间',
        }
    )
    # 职级排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '排序不能为空',
            'min_value': '职级排序值在0~99999之间',
            'max_value': '职级排序值在0~99999之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Level
        # 全部字段验证
        # fields = '__all__'
        # # 除了id字段其他都验证
        # exclude = ['id']
        # 指定部分字段验证
        fields = ["name", "status", "sort"]

    # 使用局部钩子验证，clean_字段名
    def clean_sort(self):
        # 获取page字段
        sort = self.cleaned_data.get('sort')
        if sort > 99999:
            raise forms.ValidationError("排序值不能大于99999")
        else:
            return sort

    # # 可以定义全局钩子
    # def clean(self):
    #     return None


# 职级状态设置
class LevelStatusForm(forms.ModelForm):
    # 职级状态
    id = forms.IntegerField(
        min_value=1,
        error_messages={
            'required': '职级ID不能为空',
            'min_value': '职级ID不能小于或等于0',
        }
    )
    # 职级状态
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '职级状态不能为空',
            'min_value': '职级状态值在1~2之间',
            'max_value': '职级状态值在1~2之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Level
        # 指定部分字段验证
        fields = ["id", "status"]
