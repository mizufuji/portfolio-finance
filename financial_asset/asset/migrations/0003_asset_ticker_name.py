# Generated by Django 3.2 on 2025-02-15 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_asset_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='ticker_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ティッカー'),
        ),
    ]
