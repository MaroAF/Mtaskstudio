# Generated by Django 4.1.3 on 2022-11-26 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_pricing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='stripe_price_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
