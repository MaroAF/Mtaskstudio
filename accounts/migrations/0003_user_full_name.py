# Generated by Django 4.1.3 on 2022-11-17 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_perfil_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]