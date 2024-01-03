import os
from openai import OpenAI, AsyncOpenAI
from application.study_chat import services
import json
import re
from asgiref.sync import sync_to_async
import secret_key
# api_key = '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'
api_key = secret_key.gpt_api_key
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


async def get_thimatic(historys, session, websocket=None):
    client = AsyncOpenAI(api_key=api_key)  # 使用异步客户端
    text = "帮我给这段对话起个标题,不超过8个字。回复的格式严格固定为：标题：XXXXX\n\n"
    pattern = r"标题.*?：(.+)"
    # 将每个字典格式化为指定的字符串格式
    formatted_strings = ['"role": "{}",\n"content":"{}"'.format(history["role"], history["content"]) for history in
                         historys]
    # 将格式化的字符串用逗号连接
    resulting_string = ",\n".join(formatted_strings)
    text = text + resulting_string

    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        model="gpt-3.5-turbo",
    )
    title = chat_completion.choices[0].message.content
    print(title)
    # 尝试匹配特定的"标题"模式
    match = re.search(pattern, title)
    if match:
        # 提取并清理标题
        found_title = match.group(1).strip()
    else:
        # 如果没有匹配到特定模式，将整个响应作为标题
        found_title = title.strip()

    print("找到标题:", found_title)
    # 基本响应格式，包含code、msg、response_type、data
    response_data = {
        "code": 0,
        "msg": "thematic change",
        "response_type": "json",
        "data": {
            'newThematic': found_title,
            'sessionId': session.id
        }
    }
    if websocket:
        await websocket.send(text_data=json.dumps(response_data))

    session.thematic = found_title
    await sync_to_async(session.save)()


async def get_highlight(historys, session):
    client = AsyncOpenAI(api_key=api_key)  # 使用异步客户端
    text = '提取这段对话重点，如果有小学知识，重点放在小学知识上比如工作效率=工作总量/时间、圆的面积s=πr^2、分数换算百分数等。' \
           '回答的格式为：重点为1、标题:内容,2、标题:内容,3、标题:内容...等等' \
           '回答时，其中标题要换成实际重点的标题，内容换成实际重点的内容' \
           '内容在50到100字之间\n\n'
    # 将每个字典格式化为指定的字符串格式
    formatted_strings = ['"role": "{}",\n"content":"{}"'.format(history["role"], history["content"]) for history in
                         historys]
    # 将格式化的字符串用逗号连接
    resulting_string = ",\n".join(formatted_strings)
    text = text + resulting_string

    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        model="gpt-3.5-turbo",
    )
    highlight = chat_completion.choices[0].message.content
    print(highlight)
