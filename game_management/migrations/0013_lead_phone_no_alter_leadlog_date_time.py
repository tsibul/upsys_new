# Generated by Django 4.1.5 on 2023-01-28 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_management', '0012_alter_lead_tg_name_alter_leadlog_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='phone_no',
            field=models.CharField(default='', max_length=14),
        ),
        migrations.AlterField(
            model_name='leadlog',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 20, 13, 18, 393450)),
        ),
    ]
