# Generated by Django 2.0 on 2019-01-22 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0059_auto_20190118_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productegg',
            name='loss_insert',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='productegg',
            name='loss_openEgg',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='productegg',
            name='pastTank_amount',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='productegg',
            name='rawTank_amount',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='setproductmatch',
            name='setProductCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.SetProductCode'),
        ),
    ]
