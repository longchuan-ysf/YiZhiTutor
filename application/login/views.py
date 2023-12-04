import base64

from captcha.models import CaptchaStore
from captcha.views import captcha_image
from django.shortcuts import render

# Create your views here.

from django.utils.decorators import method_decorator
from django.views import View

from application.login import services
from middleware.login_middleware import check_login

from utils import R


# 渲染登录页
@method_decorator(check_login, name='dispatch')
class LoginView(View):

    # GET请求渲染HTML模板
    def get(self, request):
        # 使用render渲染方式
        return render(request, 'login.html')

    # POST接收登录请求
    def post(self, request):
        # 调用添加友链服务方法
        result = services.Login(request)
        # 返回结果
        return result


# 获取验证码
@method_decorator(check_login, name='get')
class CaptchaView(View):
    def get(self, request):
        hashkey = CaptchaStore.generate_key()
        # KEY值
        idKey = CaptchaStore.objects.filter(hashkey=hashkey).first().id
        image = captcha_image(request, hashkey)
        # 将图片转换为base64
        base64Image = base64.b64encode(image.content)
        imgStr = "data:image/png;base64," + base64Image.decode("utf-8")
        return R.ok(idkey=idKey, data=imgStr)
