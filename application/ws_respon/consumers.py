import asyncio

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

import json


class MyConsumer(AsyncWebsocketConsumer):
    async def receive(self, text_data):
        from application.study_chat.models import ChatSession, ChatMessage, MediaRecord
        from application.user.models import User
        from application.ws_respon import GPT_generate, imageHandle

        try:
            # 解析请求体中的 JSON 数据 打印分割线,好知道这部分的打印是从哪开始的
            print("---------------------")
            data = json.loads(text_data)
            print(f"data = {data}")

            # 提取数据
            message_text = data.get('chat-text')
            session_id = data.get('session_id')
            user_id = data.get('user_id')
            image_url = data.get('image_url')
            audio_url = data.get("audio_url")

            # 初始化变量
            media_url = ''
            formatted_message = message_text
            media_type = 0

            # 处理媒体上传和消息格式化
            if image_url or audio_url:
                media_kind = "image" if image_url else "audio"
                media_url = imageHandle.save_chat_image(image_url or audio_url, media_kind)
                media_prefix = "[这是一张照片" if media_kind == "image" else "[这是一段语音"
                formatted_message = f"{media_prefix}url放在{media_url}]{message_text}"
                media_type = 2 if media_kind == "image" else 1

            print(f'message_text={message_text}\n'
                  f'formatted_message={formatted_message}\n'
                  f'media_type={media_type}   media_url={media_url}\n')

            # 保存用户问题
            session = await sync_to_async(ChatSession.objects.get)(id=session_id)
            userInfo = await sync_to_async(User.objects.filter(is_delete=False, id=user_id).first)()

            # 创建新的聊天消息实例
            new_message = await sync_to_async(ChatMessage.objects.create)(
                session=session,
                sender=userInfo.realname,
                message_text=formatted_message,
            )

            # 如果有媒体文件，则创建媒体记录
            if media_url:
                new_media_record = await sync_to_async(MediaRecord.objects.create)(
                    media_type=media_type,
                    media_url=media_url,
                    message=new_message,
                )

            response_data = {
                "code": 0,
                "msg": "save confirmation",
                "response_type": "json",
                "data": {
                    "session_id": session_id,
                    'message_text': message_text,
                    'sender': new_message.sender,
                    'timestamp': new_message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    "media_type": media_type,
                    "media_url": media_url
                }
            }
            await self.send(text_data=json.dumps(response_data))

            # ----------------------通过GPT回答用户问题------------------------------------
            chat_history = await sync_to_async(GPT_generate.get_chat_history)(user_id, session_id)

            gpt_response, chat_history = await GPT_generate.get_gpt_response(chat_history, message_text, websocket=self)
            await sync_to_async(ChatMessage.objects.create)(
                session=session,
                sender="AI",
                message_text=gpt_response,
            )
            # ----------------------生成主题------------------------------------
            if session.thematic == "新对话" or session.thematic == "no thematic":
                await GPT_generate.get_thimatic(chat_history,session,websocket=self)
            # ----------------------提取关键字------------------------------------
        except Exception as e:
            print(f'file = {__file__},err = {str(e)}')
            response_data = {
                "code": -1,
                "msg": str(e),
                "response_type": "err msg",
                "data": {

                }
            }
            await self.send(text_data=json.dumps(response_data))
