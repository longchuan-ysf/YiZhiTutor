from django import forms

from application.ad import models


# 广告表单验证
class AdForm(forms.ModelForm):
    # 广告标题
    title = forms.CharField(
        max_length=255,
        error_messages={
            'required': '广告标题不能为空',
            'max_length': '广告标题长度不得超过255个字符',
        }
    )
    # 广告位ID
    sort_id = forms.IntegerField(
        min_value=0,
        error_messages={
            'required': '广告位ID不能为空',
            'min_value': '广告位ID不得小于0',
        }
    )
    # 广告类型：1图片 2文字 3视频 4推荐
    type = forms.IntegerField(
        min_value=1,
        max_value=4,
        error_messages={
            'required': '广告类型不能为空',
            'min_value': '广告类型值在1~4之间',
            'max_value': '广告类型值在1~4之间',
        }
    )
    # 广告封面
    cover = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '广告封面长度不得超过255个字符',
        }
    )
    # 广告URL
    url = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '广告URL长度不得超过255个字符',
        }
    )
    # 广告宽度
    width = forms.IntegerField(
        required=False,
        min_value=0,
        error_messages={
            'min_value': '广告宽度不得小于0',
        }
    )
    # 广告高度
    height = forms.IntegerField(
        required=False,
        min_value=0,
        error_messages={
            'min_value': '广告高度不得小于0',
        }
    )
    # 开始时间
    start_time = forms.DateTimeField(
        required=False,
    )
    # 结束时间
    end_time = forms.DateTimeField(
        required=False,
    )
    # 广告状态
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '广告状态值不能为空',
            'min_value': '广告状态值在1~2之间',
            'max_value': '广告状态值在1~2之间',
        }
    )
    # 广告排序
    sort = forms.IntegerField(
        min_value=0,
        max_value=99999,
        error_messages={
            'required': '栏目排序不能为空',
            'min_value': '栏目排序值在0~99999之间',
            'max_value': '栏目排序值在0~99999之间',
        }
    )
    # 广告备注
    note = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '广告备注长度不得超过255个字符',
        }
    )
    # 广告内容
    content = forms.CharField(
        required=False,
    )

    class Meta:
        # 绑定模型
        model = models.Ad
        # 指定部分字段验证
        fields = ['title', 'sort_id', 'type', 'cover', 'url', 'width', 'height', 'start_time', 'end_time', 'status',
                  'sort', 'note', 'content']


# 设置状态
class AdStatusForm(forms.ModelForm):
    # 广告状态
    id = forms.IntegerField(
        min_value=1,
        error_messages={
            'required': '广告ID不能为空',
            'min_value': '广告ID不能小于或等于0',
        }
    )
    # 广告状态
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '广告状态不能为空',
            'min_value': '广告状态值在1~2之间',
            'max_value': '广告状态值在1~2之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Ad
        # 指定部分字段验证
        fields = ["id", "status"]
