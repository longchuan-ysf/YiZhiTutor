import os
from openai import OpenAI, AsyncOpenAI
from application.study_chat import services
import json


def get_chat_history(user_id, session_id):
    # 初始化对话历史
    messages = []
    history_json = services.get_chat_messages_as_json(user_id, session_id)

    history_data = json.loads(history_json)
    messages = history_data["data"]["messages"]
    formatted_messages = []
    for msg in messages:
        formatted_message = {
            "role": "assistant" if msg["sender"] == "AI" else "user",
            "content": msg["message_text"]
        }
        formatted_messages.append(formatted_message)
    return formatted_messages


async def get_gpt_response(history, user_input, websocket=None, max_tokens=1024):
    api_key = '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'
    client = AsyncOpenAI(api_key=api_key)  # 使用异步客户端

    # 添加当前用户输入到历史
    history.append({"role": "user", "content": user_input})

    # 将历史对话转换为模型所需的格式
    formatted_history = [{"role": msg["role"], "content": msg["content"]} for msg in history]

    # 检查 token 数量并在必要时截断历史
    total_tokens = sum(len(msg["content"]) for msg in formatted_history)
    while total_tokens > max_tokens:
        # 移除最旧的消息
        removed_message = formatted_history.pop(0)
        total_tokens -= len(removed_message["content"])

    # 创建 GPT 请求
    stream = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=formatted_history,
        stream=True,
    )

    # 获取响应
    response = ""
    # 基本响应格式，包含code、msg、response_type、data
    response_data = {
        "code": 0,
        "msg": "ai response",
        "response_type": "json",
        "data": {
            "message_start_end": 'start',
            "message": "",
        }
    }
    await websocket.send(text_data=json.dumps(response_data))
    # 以下将回复
    response_data['data']['message_start_end'] = 'message'
    async for chunk in stream:
        response_content = chunk.choices[0].delta.content or ""
        print(response_content, end="")
        response_data['data']['message'] = response_content
        await websocket.send(text_data=json.dumps(response_data))
        response += response_content

    print(f"\r\n")
    response_data['data']['message_start_end'] = "end"
    response_data['data']['message'] = ""
    await websocket.send(text_data=json.dumps(response_data))
    # 更新历史记录
    history.append({"role": "assistant", "content": response})

    return response, history
