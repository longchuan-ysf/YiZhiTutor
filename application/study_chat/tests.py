import os
import django
import re
import json
from django.core.serializers.json import DjangoJSONEncoder
# 设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "application.settings")

# 初始化Django
django.setup()

from application.study_chat.models import ChatSession, ChatMessage, MediaRecord  # 替换为您的实际模型路径
from application.user.models import User
import datetime
from django.core.exceptions import ObjectDoesNotExist

def test_create_chat_session(user_id):

    user = User.objects.get(id=user_id)
    realname = user.realname if hasattr(user, 'realname') else "Unknown User"
    print(f"realname = {realname}")

    # 创建新的聊天会话
    session = ChatSession.objects.filter(
        user_id=user_id
    ).first()




def get_chat_messages_as_json(user_id, session_id):
    try:
        # 确保会话存在
        chat_session = ChatSession.objects.get(id=session_id, user_id=user_id)

        # 获取指定会话的所有消息
        messages = ChatMessage.objects.filter(session_id=session_id, session__user_id=user_id).order_by('timestamp')

        # 用于识别特定格式消息的正则表达式
        pattern = r'\[这是\w+url放在([^\]]+)\]'

        # 初始化响应数据结构
        response_data = {
            "date": "",  # 会话日期
            "thematic": chat_session.thematic,
            "messages": []
        }

        # 处理每条消息
        for message in messages:
            message_data = {
                "session_id": message.session.id,
                "sender": message.sender,
                "message_text": message.message_text,
                "timestamp": message.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "media_type": None,
                "media_url": None
            }

            match = re.search(pattern, message.message_text)
            if match:
                media_url = match.group(1)
                media_record = MediaRecord.objects.filter(message=message, media_url=media_url).first()
                if media_record:
                    message_data["media_type"] = media_record.media_type
                    message_data["media_url"] = media_record.media_url

            response_data["messages"].append(message_data)

            # 更新会话日期
            if not response_data["date"]:
                response_data["date"] = message.timestamp.strftime("%Y-%m-%d")

        return {
            "status": True,
            "message": "Query successful.",
            "data": json.dumps(response_data, cls=DjangoJSONEncoder)
        }

    except ObjectDoesNotExist:
        return {
            "status": False,
            "message": "Chat session not found or user not associated with session.",
            "data": {}
        }
    except Exception as e:
        return {
            "status": False,
            "message": f"An error occurred: {str(e)}",
            "data": {}
        }


def get_latest_chat_sessions(user_id, n=8):
    try:
        # 获取用户的最新n个会话
        latest_sessions = ChatSession.objects.filter(user_id=user_id).order_by('-start_time')[:n]

        all_sessions_data = []

        for session in latest_sessions:
            # 获取每个会话的消息
            session_messages = get_chat_messages_as_json(user_id, session.id)
            if session_messages['status']:
                all_sessions_data.append(session_messages['data'])

        return {
            "status": True,
            "message": "Latest chat sessions fetched successfully.",
            "data": all_sessions_data
        }

    except Exception as e:
        return {
            "status": False,
            "message": f"An error occurred: {str(e)}",
            "data": {}
        }




def get_latest_chat_sessions_with_thematic(user_id, n=8):
    try:
        # 获取用户的最新n个会话
        latest_sessions = ChatSession.objects.filter(user_id=user_id).order_by('-start_time')[:n]

        # 使用values()来选择特定的字段
        sessions_data = latest_sessions.values('id', 'thematic')

        thematic_data = []

        for session in sessions_data:
            session_id = session['id']
            thematic = session['thematic']

            thematic_data.append({
                "session_id": session_id,
                "thematic": thematic,
            })

        return {
            "status": True,
            "message": "Latest chat sessions with thematics fetched successfully.",
            "data": thematic_data
        }

    except Exception as e:
        return {
            "status": False,
            "message": f"An error occurred: {str(e)}",
            "data": {}
        }

def main():
    # 示例调用函数
    json_response = get_latest_chat_sessions_with_thematic(1)  # 假设的用户ID和会话ID
    print(json_response)
    print(f"get {len(json_response['data'])} data")


if __name__ == '__main__':
    main()
