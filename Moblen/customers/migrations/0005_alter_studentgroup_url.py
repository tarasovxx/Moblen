from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('customers', '0004_studentgroup_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='url',
            field=models.TextField(default='http://moblen.ru/ref/e8d7e6d9-e651-40bf-b2c0-fefe5f1fb257', unique=True),
        ),
    ]
