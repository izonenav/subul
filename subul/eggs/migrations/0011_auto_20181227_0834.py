# Generated by Django 2.0 on 2018-12-26 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eggs', '0010_egg_in_ymd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egg',
            name='in_ymd',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
