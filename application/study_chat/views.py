from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from application.study_chat import services
from application.study_chat import tests
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired
from application.user.models import User
# 渲染角色首页
from utils import R
import json
from utils.utils import getImageURL
# 角色首页
@method_decorator(check_login, name='get')
class ChatIndexView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:chat:index',)

    # 接收GET请求
    def get(self, request):
        # 根据用户获取历史对话消息
        user_id = request.session.get('user_id')
        content = services.get_latest_chat_sessions_with_thematic(user_id)
        userInfo = User.objects.filter(is_delete=False, id=user_id).first()
        userInfo.avatar = getImageURL(userInfo.avatar)
        # 渲染HTML模板
        return render(request, "study_chat/index.html",{'content': content,'userInfo':userInfo})



# 前端提交谈话数据
@method_decorator(check_login, name='post')
class ChatSubmitView(PermissionRequired, View):
    permission_required = ('sys:chat:index',)
    def post(self,request):
        print("1111")
        return  R.ok()

class ThematicChangeView(PermissionRequired, View):
    permission_required = ('sys:chat:index',)
    def post(self, request):
        try:
            # 解析请求体中的JSON数据
            data = json.loads(request.body)
            session_id = data.get('session_id')
            user_id = request.session.get('user_id')
            print("Received session_id:", session_id)
            massage = services.get_chat_messages_as_json(user_id,session_id)
            # 以下是处理逻辑，例如更新会话主题等
            # ...

            return R.ok(data = massage)

        except json.JSONDecodeError:
            return R.failed()