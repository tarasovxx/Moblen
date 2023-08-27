# Generated by Django 4.2.1 on 2023-08-27 18:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=30)),
                ('student_surname', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('password_hash', models.BigIntegerField()),
                ('salt', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('group_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('list_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('list_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('tutor_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tutor_name', models.CharField(max_length=30)),
                ('tutor_surname', models.CharField(max_length=30)),
                ('tutor_photo', models.BinaryField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('has_access', models.BooleanField(default=False)),
                ('password_hash', models.BigIntegerField()),
                ('salt', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=50)),
                ('course_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.course')),
            ],
        ),
        migrations.CreateModel(
            name='TaskListGroupRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.studentgroup')),
                ('list_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.tasklist')),
            ],
        ),
        migrations.AddField(
            model_name='tasklist',
            name='topic_uuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.topic'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task_condition', models.TextField()),
                ('task_image', models.BinaryField(blank=True, null=True)),
                ('task_answer', models.CharField(max_length=50)),
                ('criteria', models.TextField()),
                ('topic_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.topic')),
            ],
        ),
        migrations.CreateModel(
            name='StudentTutorRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.student')),
                ('tutor_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='StudentGroupRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.studentgroup')),
                ('student_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.student')),
            ],
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='owner_uuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.tutor'),
        ),
        migrations.AddField(
            model_name='course',
            name='owner_uuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.tutor'),
        ),
    ]
