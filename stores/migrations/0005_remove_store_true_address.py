# Generated by Django 5.0.1 on 2024-02-12 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_remove_store_address_store_poi_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='true_address',
        ),
    ]
