from django.shortcuts import render

# Create your views here.


from django.utils.decorators import method_decorator
from django.views import View

from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired


# 渲染统计首页
@method_decorator(check_login, name="get")
class AnalysisView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:analysis:index",)

    # 接收GET请求
    def get(self, request):
        # 渲染模板
        return render(request, "analysis/index.html")
