import json
import logging
from datetime import datetime, timedelta

from captcha.models import CaptchaStore

from application.login import forms
from application.user.models import User
from utils import R, regular, md5


# 用户登录
def Login(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
    except Exception as e:
        logging.info("错误信息：\n{}".format(e))
        return R.failed("参数错误")

    # 表单验证
    form = forms.LoginForm(data=dict_data)
    if form.is_valid():
        # 登录名
        username = form.cleaned_data.get("username")
        # 登录密码
        password = form.cleaned_data.get("password")
        # 验证码
        captcha = form.cleaned_data.get("captcha")
        # 验证码KEY
        idKey = int(form.cleaned_data.get("idKey"))
        # 验证码
        image_code = CaptchaStore.objects.filter(
            id=idKey
        ).first()
        five_minute_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
        if image_code and five_minute_ago > image_code.expiration.replace(tzinfo=None):
            image_code and image_code.delete()
            return R.failed(msg="验证码过期")
        else:
            if image_code and (
                    image_code.response == captcha
                    or image_code.challenge == captcha
            ):
                image_code and image_code.delete()
            else:
                image_code and image_code.delete()
                return R.failed(msg="图片验证码错误")

        # 根据用户名查询用户信息
        user = User.objects.filter(is_delete=False, username=username).first()
        if not user:
            return R.failed("用户不存在")

        # 密码MD5加密
        md5_pwd = md5.getPassword(password)

        # 比对密码是否相同
        if md5_pwd != user.password:
            return R.failed(msg="密码不正确")
        # 用户ID存入SESSION
        request.session['user_id'] = user.id

        # 返回结果
        return R.ok(msg="登录成功")
    else:
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)
