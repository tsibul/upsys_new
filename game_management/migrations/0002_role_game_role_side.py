# Generated by Django 4.1.5 on 2023-01-22 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game_management.gametype'),
        ),
        migrations.AddField(
            model_name='role',
            name='side',
            field=models.CharField(default='', max_length=100),
        ),
    ]