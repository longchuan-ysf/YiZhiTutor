from django.db import models
from django.conf import settings
from config.env import TABLE_PREFIX

from application.user.models import User
# Create your models here.

class ChatSession(models.Model):
    # 使用ForeignKey一对多的依据：每个聊天会话属于一个用户但是用户可以有多个会话
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    thematic = models.CharField(max_length=50,default="no thematic")
    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + 'Chat_Session'
        verbose_name = '会话对照表'

    def __str__(self):
        return f"Session {self.id} - User {self.user.username}"


class ChatMessage(models.Model):
    # 使用ForeignKey一对多的依据：每条消息属于一个聊天会话但是一个聊天会话可以包含多条消息
    session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE)
    sender = models.CharField(max_length=100)
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + 'Chat_Message'
        verbose_name = '会话记录表'

    def __str__(self):
        return f"Message {self.id} - Session {self.session.id}"

class ChatSummary(models.Model):
    session = models.ForeignKey(ChatSession, related_name='summaries', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        db_table = TABLE_PREFIX + 'Chat_Summary'
        verbose_name = '会话摘要表'

    def __str__(self):
        return f"Summary {self.id} - Session {self.session.id}"

class MediaRecord(models.Model):
    # 使用ForeignKey一对多的依据：每个媒体记录属于一条消息但是一条消息可以包含一个或多个媒体记录
    message = models.ForeignKey(ChatMessage, related_name='media', on_delete=models.CASCADE)

    MEDIA_CHOICES = (
        (0, "null"),
        (1, "audio"),
        (2, "image"),
    )
    media_type = models.IntegerField(choices=MEDIA_CHOICES, default=0, verbose_name="0-无媒体 1-音频 2-图片",
                                 help_text="0-无媒体 1-音频 2-图片")
    media_url = models.URLField()
    upload_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 数据表名
        db_table = TABLE_PREFIX + 'Chat_Media_Record'
        verbose_name = '会话多媒体记录表'

    def __str__(self):
        return f"Media {self.id} - Message {self.message.id}"







