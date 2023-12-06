import json
import logging
import re
import json
from django.core.serializers.json import DjangoJSONEncoder
from application.study_chat.models import ChatSession, ChatMessage, MediaRecord  # 替换为您的实际模型路径
from application.user.models import User
import datetime
from django.core.exceptions import ObjectDoesNotExist


from utils import R, regular
"""
获取聊天记录get_chat_messages_as_json
user_id:用户ID
session_id:会话id
"""
def get_chat_messages_as_json(user_id, session_id):
    try:
        # 确保会话存在
        ChatSession.objects.get(id=session_id, user_id=user_id)

        # 获取指定会话的所有消息
        messages = ChatMessage.objects.filter(session_id=session_id, session__user_id=user_id).order_by('timestamp')

        # 用于识别特定格式消息的正则表达式
        pattern = r'\[这是\w+url放在([^\]]+)\]'

        # 初始化响应数据结构
        response_data = {
            "date": "",  # 会话日期
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


