# Generated by Django 2.0 on 2018-12-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eggs', '0004_auto_20181207_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egg',
            name='type',
            field=models.CharField(choices=[('입고', '입고'), ('생산', '생산'), ('폐기', '폐기'), ('판매', '판매')], default='생산', max_length=10),
        ),
    ]
