# Generated by Django 5.0.3 on 2024-04-04 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_parameter_inlet_alter_parameter_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='stage_1_pressure',
            field=models.FloatField(default=0.0),
        ),
    ]
