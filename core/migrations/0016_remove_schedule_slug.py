# Generated by Django 4.1 on 2022-10-25 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_schedule_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='slug',
        ),
    ]
