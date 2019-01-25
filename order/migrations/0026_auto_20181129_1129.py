# Generated by Django 2.0 on 2018-11-29 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0044_auto_20181129_1129'),
        ('order', '0025_auto_20181120_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='productCode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.ProductCode'),
        ),
        migrations.AlterField(
            model_name='order',
            name='setProduct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.SetProductCode'),
        ),
    ]