# Generated by Django 5.0.7 on 2024-08-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_user_id_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='employee_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
