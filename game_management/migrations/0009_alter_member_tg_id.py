# Generated by Django 4.1.5 on 2023-01-27 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_management', '0008_alter_member_tg_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='tg_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
