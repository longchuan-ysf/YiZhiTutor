# Generated by Django 4.1.3 on 2023-12-05 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_chat', '0002_alter_mediarecord_media_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatsession',
            name='thematic',
            field=models.CharField(default='no thematic', max_length=50),
        ),
    ]
