# Generated by Django 4.0.2 on 2022-02-09 21:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_bid_date_alter_listing_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 9, 18, 42, 6, 280031))),
            ],
        ),
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 9, 18, 42, 6, 280031)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 9, 18, 42, 6, 278997)),
        ),
    ]
