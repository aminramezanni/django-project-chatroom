# Generated by Django 4.0.3 on 2023-12-07 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
