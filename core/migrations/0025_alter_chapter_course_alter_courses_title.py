# Generated by Django 4.1.3 on 2022-11-15 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_courses_content_courses_short_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Curso', to='core.courses'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
