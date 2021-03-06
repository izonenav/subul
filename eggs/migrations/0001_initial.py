# Generated by Django 2.0 on 2018-12-07 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0006_location_location_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Egg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ymd', models.CharField(max_length=8)),
                ('code', models.CharField(max_length=255)),
                ('codeName', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('amount', models.FloatField()),
                ('amount_kg', models.FloatField(blank=True, null=True)),
                ('memo', models.TextField(blank=True)),
                ('delete_state', models.CharField(choices=[('Y', 'deleted'), ('N', 'notDeleted')], default='N', max_length=2)),
                ('type', models.CharField(choices=[('입고', '입고'), ('생산', '생산'), ('폐기', '폐기'), ('판매', '판매')], default='판매', max_length=10)),
                ('price', models.IntegerField()),
                ('eggLocationName', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EggCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('codeName', models.CharField(max_length=255)),
                ('delete_state', models.CharField(choices=[('Y', 'deleted'), ('N', 'notDeleted')], default='N', max_length=2)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('size', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='egg',
            name='eggCode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eggs.EggCode'),
        ),
        migrations.AddField(
            model_name='egg',
            name='eggLocationCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location'),
        ),
    ]
