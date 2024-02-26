import json
import logging
import re
import json
from django.core.serializers.json import DjangoJSONEncoder
from application.study_chat.models import ChatSession, ChatMessage, MediaRecord, ChatSummary  # 替换为您的实际模型路径
from application.user.models import User
import datetime
from django.core.exceptions import ObjectDoesNotExist

from utils import R, regular

"""
创建新的会话
"""


def create_new_chat_session(user_id):
    try:
        user = User.objects.get(pk=user_id)
        chat_session = ChatSession(user=user)
        chat_session.thematic = "新对话"
        chat_session.save()
        return chat_session

    except ObjectDoesNotExist:
        # 用户不存在
        raise Exception("User not found.")


"""
获取聊天记录get_chat_messages_as_json
user_id:用户ID
session_id:会话id
"""
def get_chat_messages_as_json(user_id, session_id):
    try:
        # 确保会话存在
        chat_session = ChatSession.objects.get(id=session_id, user_id=user_id)

        # 获取指定会话的所有消息
        messages = ChatMessage.objects.filter(session_id=session_id, session__user_id=user_id).order_by('timestamp')

        summaries = ChatSummary.objects.filter(session_id=session_id)
        # 用于识别特定格式消息的正则表达式
        pattern = r'\[这是\w+url放在([^\]]+)\](.*)'
        # 初始化响应数据结构
        response_data = {
            "date": chat_session.start_time.strftime("%Y-%m-%d"),  # 会话日期
            "thematic": chat_session.thematic,
            "summary": [
                {
                    "title": f"{index + 1}、{summary.title}",
                    "content": summary.content
                } for index, summary in enumerate(summaries)
            ],
            "messages": [],
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
                    message_data["message_text"] = ''
                    message_data["media_type"] = media_record.media_type
                    message_data["media_url"] = media_record.media_url
                    if media_record.media_type and match.group(2).strip():
                        audio_text = match.group(2).strip()
                        message_data["message_text"] = audio_text
            response_data["messages"].append(message_data)

        # 更新会话日期
        # print(response_data)
        return json.dumps({"status": True, "message": "Query successful.", "data": response_data},
                          cls=DjangoJSONEncoder)

    except ObjectDoesNotExist:
        return json.dumps({
            "status": False,
            "message": "Chat session not found or user not associated with session.",
            "data": {}
        }, cls=DjangoJSONEncoder)
    except Exception as e:
        return json.dumps({
            "status": False,
            "message": f"An error occurred: {str(e)}",
            "data": {}
        }, cls=DjangoJSONEncoder)

def check_string_format(input_string):
    pattern = r"(\[这是.+url放在.+\])\S*"
    match = re.match(pattern, input_string)
    if match:
        return True,  input_string.replace(match.group(1),'')
    else:
        return False, None
"""
获取聊天记录get_chat_messages_as_json_messagesID
user_id:用户ID
session_id:会话id

因为发现上面的代码有点问题当语音识别或者图片识别的文本中存在换行符就得多处理，想了下还是通过外键去查询更合理
"""
def get_chat_messages_as_json_messagesID(user_id, session_id):
    try:
        # 确保会话存在
        chat_session = ChatSession.objects.get(id=session_id, user_id=user_id)

        # 获取指定会话的所有消息
        messages = ChatMessage.objects.filter(session_id=session_id, session__user_id=user_id).order_by('timestamp')

        summaries = ChatSummary.objects.filter(session_id=session_id)

        # 初始化响应数据结构
        response_data = {
            "date": chat_session.start_time.strftime("%Y-%m-%d"),  # 会话日期
            "thematic": chat_session.thematic,
            "summary": [
                {
                    "title": f"{index + 1}、{summary.title}",
                    "content": summary.content
                } for index, summary in enumerate(summaries)
            ],
            "messages": [],
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
            result, extracted_content = check_string_format(message.message_text)
            if result:
                media_record = MediaRecord.objects.filter(message=message).first()
                message_data["media_type"] = media_record.media_type
                message_data["media_url"] = media_record.media_url
                message_data["message_text"] = extracted_content

            response_data["messages"].append(message_data)

        # 更新会话日期
        # print(response_data)
        return json.dumps({"status": True, "message": "Query successful.", "data": response_data},
                          cls=DjangoJSONEncoder)

    except ObjectDoesNotExist:
        return json.dumps({
            "status": False,
            "message": "Chat session not found or user not associated with session.",
            "data": {}
        }, cls=DjangoJSONEncoder)
    except Exception as e:
        return json.dumps({
            "status": False,
            "message": f"An error occurred: {str(e)}",
            "data": {}
        }, cls=DjangoJSONEncoder)
"""
获取用户最新记录完整get_latest_chat_sessions
user_id:用户ID
n:多少条
"""
def get_latest_chat_sessions(user_id, n=8):
    try:
        # 获取用户的最新n个会话
        latest_sessions = ChatSession.objects.filter(user_id=user_id).order_by('-start_time')[:n]

        all_sessions_data = []

        for session in latest_sessions:
            # 获取每个会话的消息
            session_messages = get_chat_messages_as_json_messagesID(user_id, session.id)
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


"""
获取用户最新会话主题get_latest_chat_sessions_with_thematic
user_id:用户ID
n:多少条
"""


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
