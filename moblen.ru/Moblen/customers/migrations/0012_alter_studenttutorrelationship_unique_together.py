# Generated by Django 4.2.1 on 2023-09-13 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0011_rename_student_uuid_studenttutorrelationship_student_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studenttutorrelationship',
            unique_together={('student', 'tutor')},
        ),
    ]
