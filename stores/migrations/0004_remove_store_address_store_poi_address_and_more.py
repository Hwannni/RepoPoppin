# Generated by Django 5.0.1 on 2024-02-12 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_remove_store_price_store_img_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='address',
        ),
        migrations.AddField(
            model_name='store',
            name='poi_address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='store',
            name='true_address',
            field=models.CharField(default='', max_length=250),
        ),
    ]
