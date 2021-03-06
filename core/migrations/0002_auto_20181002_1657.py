# Generated by Django 2.0 on 2018-10-02 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='code_name',
            new_name='codeName',
        ),
        migrations.AddField(
            model_name='location',
            name='location_character',
            field=models.CharField(choices=[('01', 'B2B'), ('02', '급식'), ('03', '미군납'), ('04', '백화점'), ('05', '온라인'), ('06', '자사몰'), ('07', '직거래'), ('08', '특판'), ('09', '하이퍼'), ('99', '기타')], default='99', max_length=2),
        ),
        migrations.AddField(
            model_name='location',
            name='location_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location_manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='location',
            name='location_shoppingmall',
            field=models.CharField(choices=[('Y', '쇼핑몰'), ('2', '보관장소'), ('N', '기본장소')], default='N', max_length=2),
        ),
        migrations.AlterField(
            model_name='location',
            name='type',
            field=models.CharField(max_length=255),
        ),
    ]
