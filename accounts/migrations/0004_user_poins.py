# Generated by Django 4.1.3 on 2022-11-25 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='poins',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
