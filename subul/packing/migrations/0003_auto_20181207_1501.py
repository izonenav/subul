# Generated by Django 2.0 on 2018-12-07 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packing', '0002_auto_20181207_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packingcode',
            name='size',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
