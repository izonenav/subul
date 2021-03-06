# Generated by Django 2.0 on 2018-12-26 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eggs', '0007_auto_20181226_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egg',
            name='locationCode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Location'),
        ),
        migrations.AlterField(
            model_name='egg',
            name='locationCodeName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
