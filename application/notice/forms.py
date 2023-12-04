from django import forms

from application.notice import models


# 通知公告表单验证
class NoticeForm(forms.ModelForm):
    # 通知公告标题
    title = forms.CharField(
        max_length=255,
        error_messages={
            'required': '通知公告标题不能为空',
            'max_length': '通知公告标题长度不得超过255个字符',
        }
    )
    # 通知公告来源：1官方平台 2开源中国 3CSDN官方 4新浪微博
    source = forms.IntegerField(
        min_value=1,
        max_value=4,
        error_messages={
            'required': '通知公告来源不能为空',
            'min_value': '通知公告来源值在1~4之间',
            'max_value': '通知公告来源值在1~4之间',
        }
    )
    # 通知公告URL
    url = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'max_length': '通知公告URL长度不得超过255个字符',
        }
    )
    # 通知公告状态
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '通知公告状态不能为空',
            'min_value': '通知公告状态值在1~2之间',
            'max_value': '通知公告状态值在1~2之间',
        }
    )
    # 是否置顶
    is_top = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '是否置顶不能为空',
            'min_value': '是否置顶值在1~2之间',
            'max_value': '是否置顶值在1~2之间',

        }
    )
    # 点击率
    click = forms.IntegerField(
        min_value=0,
        error_messages={
            'required': '点击率不能为空',
            'min_value': '点击率不能小于0',
        }
    )
    # 通知公告内容
    content = forms.CharField(
        required=False,
        error_messages={
            'required': '通知公告内容不能为空',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Notice
        # 指定部分字段验证
        fields = ['title', 'source', 'url', 'status', 'is_top', 'click', 'content']
