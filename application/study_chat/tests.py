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










def main():
    # 示例调用函数
    json_response = get_latest_chat_sessions_with_thematic(1)  # 假设的用户ID和会话ID
    print(json_response)
    print(f"get {len(json_response['data'])} data")


if __name__ == '__main__':
    main()
