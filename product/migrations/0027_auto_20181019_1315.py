# Generated by Django 2.0 on 2018-10-19 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_auto_20181019_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='memo',
            field=models.TextField(blank=True),
        ),
    ]
