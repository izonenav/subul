# Generated by Django 2.0 on 2018-10-07 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20181004_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmaster',
            name='total_eggUse',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productmaster',
            name='total_openEgg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productmaster',
            name='total_produceStore',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productmaster',
            name='total_productAmount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productmaster',
            name='total_productCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productmaster',
            name='total_storeInsert',
            field=models.IntegerField(default=0),
        ),
    ]