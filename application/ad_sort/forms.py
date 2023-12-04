from django import forms

from application.ad_sort import models


class AdSortForm(forms.ModelForm):
    # 广告位名称
    name = forms.CharField(
        max_length=255,
        error_messages={
            'required': '广告位名称不能为空',
            'max_length': '广告位名称长度不得超过255个字符',
        }
    )
    # 站点ID
    item_id = forms.IntegerField(
        required=False,
        min_value=0,
        error_messages={
            'required': '站点ID不能为空',
            'min_value': '站点ID不得小于0',
        }
    )
    # 栏目ID
    cate_id = forms.IntegerField(
        required=False,
        min_value=0,
        error_messages={
            'required': '栏目ID不能为空',
            'min_value': '栏目ID不得小于0',
        }
    )
    # 广告位位置
    loc_id = forms.IntegerField(
        required=False,
        min_value=0,
        error_messages={
            'required': '广告位位置不能为空',
            'min_value': '广告位位置不得小于0',
        }
    )
    # 投放平台：1PC站 2WAP站 3微信小程序 4APP应用
    platform = forms.IntegerField(
        min_value=1,
        max_value=4,
        error_messages={
            'required': '投放平台不能为空',
            'min_value': '投放平台的值在1~4之间',
            'max_value': '投放平台的值在1~4之间',
        }
    )
    # 广告位描述
    description = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '广告位描述长度不得超过255个字符',
        }
    )
    # 广告位排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '站点排序不能为空',
            'min_value': '站点排序值在0~99999之间',
            'max_value': '站点排序值在0~99999之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.AdSort
        # 指定部分字段验证
        fields = ['name', 'item_id', 'cate_id', 'loc_id', 'platform', 'description', 'sort']
