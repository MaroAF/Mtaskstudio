# Generated by Django 4.1.3 on 2022-11-12 11:29

import core.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_placeholder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firs_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='schedule',
            name='image_h',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.schedule_directory_path, verbose_name='Imagen Banner(Si se requiere)'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='image_v',
            field=models.ImageField(upload_to=core.models.schedule_directory_path, verbose_name='Imagen vertical(Portada del Set)'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='image_v1',
            field=models.ImageField(upload_to=core.models.schedule_directory_path, verbose_name='Imagen vertical Foto demostrativa 1'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='image_v2',
            field=models.ImageField(upload_to=core.models.schedule_directory_path, verbose_name='Imagen vertical Foto demostrativa 2'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='image_v3',
            field=models.ImageField(upload_to=core.models.schedule_directory_path, verbose_name='Imagen vertical Foto demostrativa 3'),
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Link Automatico (NO MODIFICAR)')),
                ('image', models.ImageField(upload_to=core.models.user_directory_path, verbose_name='Imagen de portada del curso')),
                ('video', models.FileField(upload_to='video/courses', verbose_name='Video Demo')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('authors', models.ManyToManyField(to='core.author')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_number', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=core.models.chapter_directory_path, verbose_name='Imagen de portada del capitulo')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.courses')),
            ],
        ),
    ]
