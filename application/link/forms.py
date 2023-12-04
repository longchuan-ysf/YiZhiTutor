from django import forms

from application.link import models


# 友链表单验证
class LinkForm(forms.ModelForm):
    # 友链名称
    name = forms.CharField(
        max_length=255,
        error_messages={
            'required': '友链名称不能为空',
            'max_length': '友链名称长度不得超过255个字符',
        }
    )
    # 友链类型：1友情链接 2合作伙伴
    type = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '友链类型不能为空',
            'min_value': '友链类型的值在1~2之间',
            'max_value': '友链类型的值在1~2之间',
        }
    )
    # 友链URL
    url = forms.CharField(
        max_length=255,
        error_messages={
            'required': '友链URL不能为空',
            'max_length': '友链URL长度不得超过255个字符',
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
    # 友链形式：1文字链接 2图片链接
    form = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '友链形式不能为空',
            'min_value': '友链形式的值在1~2之间',
            'max_value': '友链形式的值在1~2之间',
        }
    )
    # 友链图片
    image = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '友链图片长度不得超过255个字符',
        }
    )
    # 友链状态
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '友链状态不能为空',
            'min_value': '友链状态值在1~2之间',
            'max_value': '友链状态值在1~2之间',
        }
    )
    # 友链排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '站点排序不能为空',
            'min_value': '站点排序值在0~99999之间',
            'max_value': '站点排序值在0~99999之间',
        }
    )
    # 友链备注
    note = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '友链备注长度不得超过255个字符',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Link
        # 指定部分字段验证
        fields = ['name', 'type', 'url', 'item_id', 'cate_id', 'platform', 'form', 'image', 'status', 'sort', 'note']


# 友链状态设置
class LevelStatusForm(forms.ModelForm):
    # 友链状态
    id = forms.IntegerField(
        min_value=1,
        error_messages={
            'required': '友链ID不能为空',
            'min_value': '友链ID不能小于或等于0',
        }
    )
    # 友链状态
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '友链状态不能为空',
            'min_value': '友链状态值在1~2之间',
            'max_value': '友链状态值在1~2之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Link
        # 指定部分字段验证
        fields = ["id", "status"]
