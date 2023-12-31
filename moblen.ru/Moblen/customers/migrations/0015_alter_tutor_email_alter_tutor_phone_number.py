# Generated by Django 4.2.1 on 2023-09-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0014_alter_tutor_email_alter_tutor_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
