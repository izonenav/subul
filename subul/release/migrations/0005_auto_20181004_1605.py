# Generated by Django 2.0 on 2018-10-04 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0004_auto_20181004_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='releaseSetProductCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.SetProductCode'),
        ),
    ]
