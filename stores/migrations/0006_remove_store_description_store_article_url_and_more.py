# Generated by Django 5.0.1 on 2024-02-12 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_remove_store_true_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='description',
        ),
        migrations.AddField(
            model_name='store',
            name='article_url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='store',
            name='hash_tags',
            field=models.CharField(default='', max_length=300),
        ),
    ]
