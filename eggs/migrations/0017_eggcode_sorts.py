# Generated by Django 2.0 on 2019-02-26 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eggs', '0016_auto_20190122_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='eggcode',
            name='sorts',
            field=models.IntegerField(default=10),
        ),
    ]