# Generated by Django 4.0.2 on 2022-02-27 16:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_alter_bid_date_alter_comment_date_alter_listing_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 27, 13, 27, 31, 627127)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 27, 13, 27, 31, 627127)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 27, 13, 27, 31, 626127)),
        ),
    ]
