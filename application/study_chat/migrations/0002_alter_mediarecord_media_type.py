# Generated by Django 4.1.3 on 2023-12-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediarecord',
            name='media_type',
            field=models.IntegerField(choices=[(0, 'null'), (1, 'audio'), (2, 'image')], default=0, help_text='0-无媒体 1-音频 2-图片', verbose_name='0-无媒体 1-音频 2-图片'),
        ),
    ]
