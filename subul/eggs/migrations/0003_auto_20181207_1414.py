# Generated by Django 2.0 on 2018-12-07 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eggs', '0002_auto_20181207_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='egg',
            old_name='eggLocationCode',
            new_name='locationCode',
        ),
        migrations.RenameField(
            model_name='egg',
            old_name='eggLocationName',
            new_name='locationCodeName',
        ),
    ]
