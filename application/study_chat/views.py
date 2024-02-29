from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from application.study_chat import services, ocr,asr
from application.study_chat.models import ChatSession, ChatMessage
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired
from application.user.models import User
# 渲染角色首页
from utils import R
import json
from utils.utils import getImageURL, URL2DiskPath
from config.env import IMAGE_URL
import os


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

    # 由于现在不使用http改为websocket，所以现在不用这个函数
    def post(self, request):
        return R.ok()


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
            massage = services.get_chat_messages_as_json_messagesID(user_id, session_id)
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


@method_decorator(check_login, name='post')
class OCRView(PermissionRequired, View):
    permission_required = ('sys:chat:index',)

    def post(self, request):
        image_url = request.POST.get('imageUrl', '')
        DiskPath = URL2DiskPath(image_url)
        if os.path.exists(DiskPath):
            ocr_text = ocr.get_ocr_results(DiskPath)
        else:
            return R.failed(msg="解析图片url有误")

        if ocr_text["code"]:
            return R.failed(code=ocr_text["code"],msg=ocr_text["msg"])
        else:
            return R.ok(data=ocr_text["data"],msg=ocr_text["msg"])


@method_decorator(check_login, name='post')
class ASRView(PermissionRequired, View):
    permission_required = ('sys:chat:index',)

    def post(self, request):
        audio_file = request.FILES['audio_file']
        audio_url, audio_file_path = asr.saveAudio(audio_file)
        result = asr.asr_request(audio_file_path)  # 假设这个函数接受一个文件对象，并返回识别结果
        print(f'audio_url = {audio_url}\naudio_file_path = {audio_file_path}\n,asr result = {result}')
        return R.ok(data={'audio_url':audio_url,'asr_result':result})

