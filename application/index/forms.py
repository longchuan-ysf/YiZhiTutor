from django import forms

from application.user import models


# 用户基本信息
class UserForm(forms.ModelForm):
    # 用户姓名
    realname = forms.CharField(
        max_length=150,
        error_messages={
            'required': '用户姓名不能为空',
            'max_length': '用户姓名长度不得超过150个字符',
        }
    )
    # 用户昵称
    nickname = forms.CharField(
        max_length=150,
        error_messages={
            'required': '用户昵称不能为空',
            'max_length': '用户昵称长度不得超过150个字符',
        }
    )
    # 性别：1-男 2-女 3-保密
    gender = forms.IntegerField(
        min_value=1,
        max_value=3,
        error_messages={
            'required': '性别不能为空',
            'min_value': '性别值在1~3之间',
            'max_value': '性别值在1~3之间',
        }
    )
    # 手机号
    mobile = forms.CharField(
        max_length=30,
        error_messages={
            'required': '手机号不能为空',
            'max_length': '手机号长度不得超过30个字符',
        }
    )
    # 邮箱
    email = forms.CharField(
        max_length=30,
        error_messages={
            'required': '邮箱不能为空',
            'max_length': '邮箱长度不得超过30个字符',
        }
    )
    # 详细地址
    address = forms.CharField(
        max_length=255,
        error_messages={
            'required': '详细地址不能为空',
            'max_length': '详细地址长度不得超过255个字符',
        }
    )
    # 个人简介
    intro = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'required': '个人简介不能为空',
            'max_length': '个人简介长度不得超过255个字符',
        }
    )

    class Meta:
        # 绑定模型
        model = models.User
        # 指定部分字段验证
        fields = ['realname', 'nickname', 'gender', 'mobile', 'email', 'address', 'intro']


# 更新密码
class UpdatePwdForm(forms.ModelForm):
    # 原始密码
    oldPassword = forms.CharField(
        min_length=6,
        max_length=12,
        error_messages={
            'required': '原始密码不能为空',
            'min_length': '原始密码长度为6~12个字符',
            'max_length': '原始密码长度为6~12个字符',
        }
    )
    # 新密码
    newPassword = forms.CharField(
        min_length=6,
        max_length=12,
        error_messages={
            'required': '新密码不能为空',
            'min_length': '新密码长度为6~12个字符',
            'max_length': '新密码长度为6~12个字符',
        }
    )
    # 确认新密码
    rePassword = forms.CharField(
        min_length=6,
        max_length=12,
        error_messages={
            'required': '确认新密码不能为空',
            'min_length': '确认新密码长度为6~12个字符',
            'max_length': '确认新密码长度为6~12个字符',
        }
    )

    class Meta:
        # 绑定模型
        model = models.User
        # 指定部分字段验证
        fields = ['oldPassword', 'newPassword', 'rePassword']
