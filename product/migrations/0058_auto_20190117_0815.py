# Generated by Django 2.0 on 2019-01-16 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0057_auto_20190116_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productegg',
            name='memo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setproductmatch',
            name='setProductCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.SetProductCode'),
        ),
    ]