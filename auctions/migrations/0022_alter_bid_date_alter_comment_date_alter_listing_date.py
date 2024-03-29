# Generated by Django 4.0.2 on 2022-03-01 02:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_bid_valid_alter_bid_date_alter_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 28, 23, 0, 27, 576341)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 28, 23, 0, 27, 577337)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 28, 23, 0, 27, 575343)),
        ),
    ]
