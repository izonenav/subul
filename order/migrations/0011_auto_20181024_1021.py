# Generated by Django 2.0 on 2018-10-24 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20181019_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='setProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.SetProductCode'),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='totalAmount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='totalCount',
            field=models.IntegerField(default=0),
        ),
    ]
