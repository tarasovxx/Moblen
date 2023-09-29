# Generated by Django 4.2.1 on 2023-09-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0013_alter_student_email_alter_student_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]