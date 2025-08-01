# Generated by Django 5.0 on 2025-06-03 07:57

import django.db.models.deletion
import iranian_cities.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0003_alter_user_phone'),
        ('insurance_module', '0002_alter_insurance_options_insurance_pay_date'),
        ('iranian_cities', '0009_rename_iranian_cit_code_1c3b38_idx_sage_city_code_8db749_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='code',
            field=models.CharField(db_index=True, editable=False, max_length=9, verbose_name='کد رهگیری'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='origin_county',
            field=iranian_cities.fields.CountyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='iranian_cities.county', verbose_name='شهر مبدا'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='subsets',
            field=models.ManyToManyField(blank=True, null=True, related_name='insurances', to='account_module.subuser', verbose_name='همراهان'),
        ),
    ]
