# Generated by Django 4.1.3 on 2022-11-16 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_alter_pricing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]
