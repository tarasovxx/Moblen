# Generated by Django 4.1.10 on 2023-09-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_alter_studentgroup_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
