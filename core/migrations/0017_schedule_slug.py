# Generated by Django 4.1 on 2022-10-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_schedule_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='slug',
            field=models.SlugField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]