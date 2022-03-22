# Generated by Django 4.0.2 on 2022-02-09 21:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_bid_user_comment_user_alter_bid_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 9, 18, 46, 52, 905288)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 9, 18, 46, 52, 905288)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 9, 18, 46, 52, 904291)),
        ),
    ]