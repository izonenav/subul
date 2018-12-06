# Generated by Django 2.0 on 2018-11-06 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0015_auto_20181105_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='amount_kg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='release',
            name='releaseSetProductCode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.SetProductCode'),
        ),
        migrations.AlterField(
            model_name='release',
            name='type',
            field=models.CharField(choices=[('판매', '판매'), ('샘플', '샘플'), ('증정', '증정'), ('자손', '자손'), ('반품', '반품')], default='판매', max_length=10),
        ),
    ]