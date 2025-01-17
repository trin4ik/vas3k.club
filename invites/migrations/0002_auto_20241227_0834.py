# Generated by Django 3.2.13 on 2024-12-27 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_auto_20200721_1043'),
        ('invites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invite',
            name='status',
        ),
        migrations.AddField(
            model_name='invite',
            name='payment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='payments.payment'),
            preserve_default=False,
        ),
    ]