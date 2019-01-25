# Generated by Django 2.0 on 2019-01-17 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0058_auto_20190117_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='purchaseSupplyPrice',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='purchaseVat',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('제품생산', '제품생산'), ('미출고품사용', '미출고품사용'), ('OEM', 'OEM')], default='제품생산', max_length=30),
        ),
        migrations.AlterField(
            model_name='setproductmatch',
            name='setProductCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.SetProductCode'),
        ),
    ]