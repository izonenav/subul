# Generated by Django 2.0 on 2018-10-04 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20181004_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='setProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.SetProductCode'),
        ),
    ]
