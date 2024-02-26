import os
import django

# 设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "application.settings")

# 初始化Django
django.setup()

from application.study_chat import services
from application.ws_respon import GPT_generate
import sys
import json
import os
from openai import OpenAI,AsyncOpenAI





def get_chat_history(user_id, session_id):
    # 初始化对话历史
    messages = []
    history_json = services.get_chat_messages_as_json_messagesID(user_id, session_id)
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

def get_gpt_response(content):
    api_key = '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'

    client = OpenAI(api_key=api_key, )

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        stream=True,
    )
    response = ""
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
        response_content = chunk.choices[0].delta.content or ""
        response += response_content

    return response


def get_gpt_response_(history, user_input, max_tokens=1024):
    api_key = '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'
    client = OpenAI(api_key=api_key)

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

    print(formatted_history)
    # 创建 GPT 请求
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=formatted_history,
        stream=True,
    )

    # 获取响应
    response = ""
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
        response_content = chunk.choices[0].delta.content or ""
        response += response_content

    # 更新历史记录
    history.append({"role": "assistant", "content": response})

    return response, history


def main():
    chat_history = get_chat_history(1,2)
    try:
        while True:
            # 获取用户输入
            user_input = input("You: ")

            # 获取 GPT 响应
            gpt_response, chat_history = get_gpt_response_(chat_history, user_input)

            # 打印 GPT 响应
            print("history:", chat_history)
    except KeyboardInterrupt:
        # 当用户按下 Ctrl+C 时结束程序
        print("\nExiting.")
        sys.exit()



if __name__ == '__main__':
    main()


