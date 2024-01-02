# Generated by Django 4.1.3 on 2023-12-25 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study_chat', '0003_chatsession_thematic'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summaries', to='study_chat.chatsession')),
            ],
            options={
                'verbose_name': '会话摘要表',
                'db_table': 'django_Chat_Summary',
            },
        ),
    ]