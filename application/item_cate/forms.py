from django import forms

from application.item_cate import models


# 栏目表单验证
class ItemCateForm(forms.ModelForm):
    # 栏目名称
    name = forms.CharField(
        max_length=150,
        error_messages={
            'required': '站点名称不能为空',
            'max_length': '站点名称长度不得超过150个字符',
        }
    )
    # 上级ID
    pid = forms.IntegerField(
        min_value=0,
        error_messages={
            'required': '上级ID不能为空',
            'min_value': '上级ID不能小于0'
        }
    )
    # 站点ID
    item_id = forms.IntegerField(
        min_value=1,
        error_messages={
            'required': '站点ID不能为空',
            'min_value': '站点ID必须大于0',
        }
    )
    # 拼音全称
    pinyin = forms.CharField(
        max_length=150,
        error_messages={
            'required': '拼音全称不能为空',
            'max_length': '拼音全称长度不得超过150个字符',
        }
    )
    # 拼音简称
    code = forms.CharField(
        max_length=150,
        error_messages={
            'required': '拼音简称不能为空',
            'max_length': '拼音简称长度不得超过150个字符',
        }
    )
    # 是否有封面：1是 2否
    is_cover = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '是否有封面不能为空',
            'min_value': '是否有封面的值在1~2之间',
            'max_value': '是否有封面的值在1~2之间',
        }
    )
    # 封面
    cover = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'required': '封面不能为空',
            'max_length': '封面长度不得超过255个字符',
        }
    )
    # 栏目状态
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '栏目状态不能为空',
            'min_value': '栏目状态值在1~2之间',
            'max_value': '栏目状态值在1~2之间',
        }
    )
    # 栏目备注
    note = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '栏目备注长度不得超过255个字符',
        }
    )
    # 栏目排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '栏目排序不能为空',
            'min_value': '栏目排序值在0~99999之间',
            'max_value': '栏目排序值在0~99999之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.ItemCate
        # 指定部分字段验证
        fields = ['name', 'pid', 'item_id', 'pinyin', 'code', 'is_cover', 'cover', 'status', 'note', 'sort']
