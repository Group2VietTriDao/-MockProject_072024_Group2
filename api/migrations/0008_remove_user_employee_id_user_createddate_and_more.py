# Generated by Django 5.0.7 on 2024-08-12 18:38

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_createrole_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='employee_id',
        ),
        migrations.AddField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='deletedAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='updatedDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='api.user')),
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            bases=('api.user',),
        ),
    ]
