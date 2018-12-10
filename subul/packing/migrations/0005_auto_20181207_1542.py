# Generated by Django 2.0 on 2018-12-07 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packing', '0004_packing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packing',
            name='type',
            field=models.CharField(choices=[('입고', '입고'), ('생산', '생산'), ('폐기', '폐기'), ('조정', '조정')], default='입고', max_length=10),
        ),
    ]
