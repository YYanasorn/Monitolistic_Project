# Generated by Django 5.0.3 on 2024-04-04 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_parameter_stage_1_1_temp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parameter',
            old_name='inlet_puressure',
            new_name='inlet_pressure',
        ),
        migrations.RemoveField(
            model_name='parameter',
            name='stage_1_pressure',
        ),
    ]
