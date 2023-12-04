from django.shortcuts import render

# Create your views here.


from django.utils.decorators import method_decorator
from django.views import View

from application.config_web import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

from utils import R

from utils.utils import saveImage


# 渲染网站配置页
@method_decorator(check_login, name="get")
class ConfigWebView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:configweb:index",)

    # 接收GET请求
    def get(self, request):
        # 调用获取配置信息方法
        content = services.getConfigInfo(request)
        # 渲染模板
        return render(request, "config_web/index.html", content)

    # 接收POST请求与
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用保存配置信息方法
        result = services.saveConfigInfo(request)
        # 返回结果
        return result
