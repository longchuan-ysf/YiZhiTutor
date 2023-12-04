from django import forms

from application.user import models
from django.conf import settings

# 登录表单验证
class LoginForm(forms.ModelForm):
    # 登录名
    username = forms.CharField(
        max_length=20,
        error_messages={
            'required': '登录名不能为空',
            'max_length': '登录名长度不得超过20个字符',
        }
    )
    # 登录密码
    password = forms.CharField(
        min_length=6,
        max_length=12,
        error_messages={
            'required': '登录密码不能为空',
            'min_length': '登录密码长度为6~12个字符',
            'max_length': '登录密码长度为6~12个字符',
        }
    )
    # 验证码
    captcha = forms.CharField(
        min_length=settings.CAPTCHA_LENGTH,
        max_length=settings.CAPTCHA_LENGTH,
        error_messages={
            'required': '验证码不能为空',
            'min_length': f'验证码长度为{settings.CAPTCHA_LENGTH}个字符',
            'max_length': f'验证码长度为{settings.CAPTCHA_LENGTH}个字符',
        }
    )
    # 验证码KEY
    idKey = forms.CharField(
        error_messages={
            'required': '验证码KEY不能为空',
        }
    )

    class Meta:
        # 绑定模型
        model = models.User
        # 指定部分字段验证
        fields = ['username', 'password', 'captcha', 'idKey']
