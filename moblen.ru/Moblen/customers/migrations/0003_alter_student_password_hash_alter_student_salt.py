# Generated by Django 4.2.1 on 2023-09-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_tutor_email_alter_tutor_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password_hash',
            field=models.CharField(max_length=257),
        ),
        migrations.AlterField(
            model_name='student',
            name='salt',
            field=models.CharField(max_length=36),
        ),
    ]
