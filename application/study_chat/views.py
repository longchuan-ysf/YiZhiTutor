from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from application.study_chat import services
from application.study_chat.models import ChatSession,ChatMessage
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired
from application.user.models import User
# 渲染角色首页
from utils import R
import json
from utils.utils import getImageURL
from config.env import IMAGE_URL


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
        return render(request, "study_chat/index.html",
                      {'content': content, 'userInfo': userInfo, "NGINX_URL": IMAGE_URL})


# 前端提交谈话数据
@method_decorator(check_login, name='post')
class ChatSubmitTxtView(PermissionRequired, View):
    permission_required = ('sys:chat:index',)

    def post(self, request):
        try:
            # 解析请求体中的 JSON 数据
            data = json.loads(request.body)
            print(data)
            # 假设请求体中包含了 'message_text' 和 'session_id'
            message_text = data.get('chat-text')
            session_id = data.get('session_id')
            # 获取相关的聊天会话
            session = ChatSession.objects.get(id=session_id)
            user_id = request.session.get('user_id')
            userInfo = User.objects.filter(is_delete=False, id=user_id).first()
            # 创建新的聊天消息实例
            new_message = ChatMessage.objects.create(
                session=session,
                sender=userInfo.realname,  # 假设发送者是当前登录用户
                message_text=message_text,
            )
            print(new_message)
            response_data = {
                "session_id":session_id,
                'message_text': new_message.message_text,
                'sender': new_message.sender,
                'timestamp': new_message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                "media_type": None,
                "media_url": None
            }
            # 返回成功响应
            return R.ok(data=response_data)

        except Exception as e:
            # 发生错误时返回错误响应
            return R.failed(message=str(e))



@method_decorator(check_login, name='post')
class ThematicChangeView(PermissionRequired, View):
    permission_required = ('sys:chat:index',)

    def post(self, request):
        try:
            # 解析请求体中的JSON数据
            data = json.loads(request.body)
            session_id = data.get('session_id')
            user_id = request.session.get('user_id')
            print("Received session_id:", session_id)
            massage = services.get_chat_messages_as_json(user_id, session_id)
            return R.ok(data=massage)

        except json.JSONDecodeError:
            return R.failed()


@method_decorator(check_login, name='post')
class ThematicAddView(PermissionRequired, View):
    permission_required = ('sys:chat:index',)
    def post(self, request):
        try:
            # 解析请求体中的JSON数据
            user_id = request.session.get('user_id')
            if not user_id:
                return R.failed(faild_msg='User ID not found in session')
            chat_session = services.create_new_chat_session(user_id)

            if not isinstance(chat_session, ChatSession):
                return R.failed(faild_msg='Failed to create chat session')

            return R.ok(session_id=chat_session.id)

        except Exception as e:
            return R.failed(faild_msg=str(e))
