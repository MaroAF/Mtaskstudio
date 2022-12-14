# Generated by Django 4.1 on 2022-10-21 10:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_sessions_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='logo',
            field=models.ImageField(upload_to='images/main', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido'),
        ),
    ]
