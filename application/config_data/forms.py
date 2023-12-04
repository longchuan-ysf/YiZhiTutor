from django import forms

from application.config_data import models


# 配置项表单验证
class ConfigDataForm(forms.ModelForm):
    # 配置项标题
    title = forms.CharField(
        max_length=150,
        error_messages={
            'required': '配置项标题不能为空',
            'max_length': '配置项标题长度不得超过150个字符',
        }
    )
    # 配置项编码
    code = forms.CharField(
        max_length=150,
        error_messages={
            'required': '配置项编码不能为空',
            'max_length': '配置项编码长度不得超过150个字符',
        }
    )
    # 配置项值
    value = forms.CharField(
        required=False,
        max_length=1000,
        error_messages={
            'required': '配置项值不能为空',
            'min_length': '配置项值长度不得超过1000个字符',
            'max_length': '配置项值长度不得超过1000个字符',
        }
    )
    # 配置选项
    options = forms.CharField(
        required=False,
        max_length=150,
        error_messages={
            'required': '配置选项不能为空',
            'max_length': '配置选项长度不得超过150个字符',
        }
    )
    # 配置ID
    config_id = forms.IntegerField(
        min_value=0,
        error_messages={
            'required': '配置ID不能为空',
            'min_value': '配置ID不能小于0',
        }
    )
    # 配置类型
    type = forms.CharField(
        max_length=150,
        error_messages={
            'required': '配置类型不能为空',
            'max_length': '配置类型长度不得超过150个字符',
        }
    )
    # 配置项排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '配置项排序不能为空',
            'min_value': '配置项排序值在0~99999之间',
            'max_value': '配置项排序值在0~99999之间',
        }
    )
    # 配置项备注
    note = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '配置项备注长度不得超过255个字符',
        }
    )

    class Meta:
        # 绑定模型
        model = models.ConfigData
        # 指定部分字段验证
        fields = ['title', 'code', 'value', 'options', 'config_id', 'type', 'sort', 'note']


# 配置项状态设置
class ConfigDataStatusForm(forms.ModelForm):
    # 配置项状态
    id = forms.IntegerField(
        min_value=1,
        error_messages={
            'required': '配置项ID不能为空',
            'min_value': '配置项ID不能小于或等于0',
        }
    )
    # 配置项状态
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '配置项状态不能为空',
            'min_value': '配置项状态值在1~2之间',
            'max_value': '配置项状态值在1~2之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.ConfigData
        # 指定部分字段验证
        fields = ["id", "status"]
