# Generated by Django 4.2.1 on 2023-10-08 21:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0002_remove_task_topic_uuid_task_list_uuid"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="format",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="task",
            name="max_ball",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]