from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from application.study_chat import services
from application.study_chat import tests
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染角色首页
from utils import R


# 角色首页
@method_decorator(check_login, name='get')
class ChatIndexView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:chat:index',)

    # 接收GET请求
    def get(self, request):
        # 根据用户获取历史对话消息
        user_id = request.session.get('user_id')

        # 渲染HTML模板
        return render(request, "study_chat/index.html")



# 前端提交谈话数据
@method_decorator(check_login, name='post')
class ChatSubmitView(PermissionRequired, View):
    permission_required = ('sys:chat:index',)
    def post(self,request):
        print("1111")
        return  R.ok()