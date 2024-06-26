# Generated by Django 3.2.13 on 2024-06-15 20:29

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('helpdeskbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='question',
            table='help_desk_questions',
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('telegram_data', models.JSONField()),
                ('question',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='helpdeskbot.question')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user')),
            ],
            options={
                'db_table': 'help_desk_answers',
            },
        ),
    ]
