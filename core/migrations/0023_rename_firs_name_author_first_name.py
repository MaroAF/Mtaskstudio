# Generated by Django 4.1.3 on 2022-11-12 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_remove_courses_video_chapter_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='firs_name',
            new_name='first_name',
        ),
    ]