import asyncio

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

import json


class MyConsumer(AsyncWebsocketConsumer):
    async def receive(self, text_data):
        from application.study_chat.models import ChatSession, ChatMessage
        from application.user.models import User
        from application.ws_respon import GPT_generate, imageHandle

        try:
            # 解析请求体中的 JSON 数据
            data = json.loads(text_data)
            print(data)
            message_text = data.get('chat-text')
            session_id = data.get('session_id')
            user_id = data.get('user_id')
            image_url = data.get('image_url')
            if image_url:
                print("image_url = ", image_url)
                image_path = imageHandle.save_chat_image(image_url, "image")
                print(image_path)
                format_image =f"[这是一张照片url放在{image_path}]{message_text}"
                print(format_image)

            #
            # # ----------------------保存用户问题------------------------------------
            # # 使用 sync_to_async 包装同步的 ORM 调用
            # session = await sync_to_async(ChatSession.objects.get)(id=session_id)
            # userInfo = await sync_to_async(User.objects.filter(is_delete=False, id=user_id).first)()
            #
            # # 创建新的聊天消息实例
            # new_message = await sync_to_async(ChatMessage.objects.create)(
            #     session=session,
            #     sender=userInfo.realname,
            #     message_text=message_text,
            # )
            #
            # response_data = {
            #     "code": 0,
            #     "msg": "save confirmation",
            #     "response_type": "json",
            #     # 以历史信息的格式响应。参见 get_chat_messages_as_json
            #     "data": {
            #         "session_id": session_id,
            #         'message_text': new_message.message_text,
            #         'sender': new_message.sender,
            #         'timestamp': new_message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            #         "media_type": None,
            #         "media_url": None
            #     }
            # }
            # await self.send(text_data=json.dumps(response_data))
            #
            # # ----------------------通过GPT回答用户问题------------------------------------
            # chat_history = await sync_to_async(GPT_generate.get_chat_history)(user_id, session_id)
            #
            # gpt_response, chat_history = await GPT_generate.get_gpt_response(chat_history, message_text, websocket=self)
            # await sync_to_async(ChatMessage.objects.create)(
            #     session=session,
            #     sender="AI",
            #     message_text=gpt_response,
            # )
            # # ----------------------生成主题------------------------------------
            # if session.thematic == "新对话" or session.thematic == "no thematic":
            #     await GPT_generate.get_thimatic(chat_history,session,websocket=self)
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
