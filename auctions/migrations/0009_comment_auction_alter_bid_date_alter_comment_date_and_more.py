# Generated by Django 4.0.2 on 2022-02-09 21:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_comment_alter_bid_date_alter_listing_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='auction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 9, 18, 43, 43, 20874)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 9, 18, 43, 43, 20874)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 9, 18, 43, 43, 19865)),
        ),
    ]