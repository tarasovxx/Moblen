# Generated by Django 4.2.1 on 2023-09-13 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0010_alter_studentgrouprelationship_unique_together_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studenttutorrelationship',
            old_name='student_uuid',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='studenttutorrelationship',
            old_name='tutor_uuid',
            new_name='tutor',
        ),
    ]
