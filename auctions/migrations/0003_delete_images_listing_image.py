# Generated by Django 4.0.2 on 2022-02-09 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_images_listing'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
