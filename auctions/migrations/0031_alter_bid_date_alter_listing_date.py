# Generated by Django 4.0.3 on 2022-03-11 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_alter_bid_date_alter_listing_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 11, 16, 58, 18, 641288)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 11, 16, 58, 18, 640513)),
        ),
    ]
