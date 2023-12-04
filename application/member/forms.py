from django import forms

from application.member import models


# 会员表单验证
class MemberForm(forms.ModelForm):
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
    # 头像
    avatar = forms.CharField(
        max_length=255,
        error_messages={
            'required': '头像不能为空',
            'max_length': '头像长度不得超过255个字符',
        }
    )
    # 出生日期
    birthday = forms.CharField(
        max_length=30,
        error_messages={
            'required': '出生日期不能为空',
            'max_length': '出生日期长度不得超过30个字符',
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
    # 省份编码
    province_code = forms.CharField(
        max_length=30,
        error_messages={
            'required': '省份编码不能为空',
            'max_length': '省份编码长度不得超过30个字符',
        }
    )
    # 城市编码
    city_code = forms.CharField(
        max_length=30,
        error_messages={
            'required': '城市编码不能为空',
            'max_length': '城市编码长度不得超过30个字符',
        }
    )
    # 县区编码
    district_code = forms.CharField(
        max_length=30,
        error_messages={
            'required': '县区编码不能为空',
            'max_length': '县区编码长度不得超过30个字符',
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
    # 用户名
    username = forms.CharField(
        max_length=30,
        error_messages={
            'required': '用户名不能为空',
            'max_length': '用户名长度不得超过30个字符',
        }
    )
    # 密码
    password = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'required': '密码不能为空',
            'max_length': '密码长度不得超过255个字符',
        }
    )
    # 会员等级
    member_level = forms.IntegerField(
        min_value=0,
        error_messages={
            'required': '会员等级不能为空',
            'min_value': '会员等级值不得小于0',
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
    # 个人签名
    signature = forms.CharField(
        required=False,
        max_length=255,
        error_messages={
            'required': '个人签名不能为空',
            'max_length': '个人签名长度不得超过255个字符',
        }
    )
    # 注册来源：1-网站注册 2-客户端注册 3-小程序注册 4-手机站注册 5-后台添加
    source = forms.IntegerField(
        min_value=1,
        max_value=5,
        error_messages={
            'required': '注册来源不能为空',
            'min_value': '注册来源在1~5之间',
            'max_value': '注册来源在1~5之间',
        }
    )
    # 用户状态：1-正常 2-禁用
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '用户状态不能为空',
            'min_value': '用户状态值在1~2之间',
            'max_value': '用户状态值在1~2之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Member
        # 指定部分字段验证
        fields = ['realname', 'nickname', 'gender', 'avatar', 'birthday', 'province_code', 'city_code',
                  'district_code', 'address', 'username', 'password', 'member_level', 'intro', 'signature', 'source',
                  'status']


# 会员状态设置
class MemberStatusForm(forms.ModelForm):
    # 会员状态
    id = forms.IntegerField(
        min_value=1,
        error_messages={
            'required': '会员ID不能为空',
            'min_value': '会员ID不能小于或等于0',
        }
    )
    # 会员状态
    status = forms.IntegerField(
        min_value=1,
        max_value=2,
        error_messages={
            'required': '会员状态不能为空',
            'min_value': '会员状态值在1~2之间',
            'max_value': '会员状态值在1~2之间',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Member
        # 指定部分字段验证
        fields = ["id", "status"]
