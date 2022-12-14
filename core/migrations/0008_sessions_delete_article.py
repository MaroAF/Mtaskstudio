# Generated by Django 4.1 on 2022-10-21 10:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/Sessions')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
