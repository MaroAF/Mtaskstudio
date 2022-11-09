# Generated by Django 4.1 on 2022-08-15 19:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/PersonalInfo')),
                ('listOfHabilities', ckeditor.fields.RichTextField()),
                ('personalData', ckeditor.fields.RichTextField()),
                ('dedication', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
