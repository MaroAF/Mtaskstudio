# Generated by Django 4.1.3 on 2022-11-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_alter_pricing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=99),
        ),
    ]
