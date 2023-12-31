# Generated by Django 4.2.1 on 2023-09-15 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0012_alter_studenttutorrelationship_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
