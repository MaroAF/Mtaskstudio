# Generated by Django 4.1.3 on 2022-11-24 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_alter_pricing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='price',
            field=models.IntegerField(),
        ),
    ]
