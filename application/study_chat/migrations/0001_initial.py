# Generated by Django 4.1.3 on 2023-12-05 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('message_text', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '会话记录表',
                'db_table': 'django_Chat_Message',
            },
        ),
        migrations.CreateModel(
            name='MediaRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(max_length=50)),
                ('media_url', models.URLField()),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='study_chat.chatmessage')),
            ],
            options={
                'verbose_name': '会话多媒体记录表',
                'db_table': 'django_Chat_Media_Record',
            },
        ),
        migrations.CreateModel(
            name='ChatSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'verbose_name': '会话对照表',
                'db_table': 'django_Chat_Session',
            },
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='study_chat.chatsession'),
        ),
    ]
