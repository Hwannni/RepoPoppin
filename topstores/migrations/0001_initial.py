# Generated by Django 5.0.1 on 2024-03-16 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0004_store_stores_stor_news_id_3a1c0b_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rank', models.IntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.store')),
            ],
        ),
    ]