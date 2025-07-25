# Generated by Django 5.0 on 2025-05-21 21:22

import django.db.models.deletion
import iranian_cities.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_module', '0001_initial'),
        ('home_module', '0001_initial'),
        ('iranian_cities', '0009_rename_iranian_cit_code_1c3b38_idx_sage_city_code_8db749_idx_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InsurancePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_value_day', models.SmallIntegerField(verbose_name='تعداد روز برای محاسبه تمام بها')),
                ('all_value_price', models.CharField(max_length=50, verbose_name='قیمت تمام بها')),
                ('other_day_price', models.CharField(max_length=50, verbose_name='قیمت بقیه روز ها')),
            ],
            options={
                'verbose_name': 'نرخ بیمه',
                'verbose_name_plural': 'نرخ بیمه ها',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, editable=False, max_length=9, verbose_name='کددرخواست')),
                ('insurance_maneger', models.BooleanField(default=False, verbose_name='مدیر گروه بیمه شود / نشود')),
                ('total_price', models.CharField(default=0, max_length=100, verbose_name='مبلغ قابل پرداخت')),
                ('pay_status', models.CharField(choices=[('0', 'پرداخت نشده'), ('1', 'پرداخت شده')], default=0, max_length=220, verbose_name='وضعیت پرداخت')),
                ('status', models.CharField(choices=[('0', 'پرداخت نشده'), ('1', 'درحال رسیدگی'), ('2', 'رسیدگی شده'), ('3', 'ردشده')], default=0, max_length=255, verbose_name='وضعیت درخواست')),
                ('start_date', models.DateField(verbose_name='تاریخ شروع به حرکت')),
                ('end_date', models.DateField(verbose_name='تاریخ بازگشت')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='زمان ثبت درخواست')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='آخرین ویرایش درخواست')),
                ('insurance_file', models.FileField(blank=True, null=True, upload_to='insurance/', verbose_name='بیمه نامه')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_module.pilgrimagedestination', verbose_name='مقصد زیارتی')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurances', to=settings.AUTH_USER_MODEL, verbose_name='مدیر گروه')),
                ('origin_county', iranian_cities.fields.CountyField(on_delete=django.db.models.deletion.CASCADE, to='iranian_cities.county', verbose_name='شهر مبدا')),
                ('origin_province', iranian_cities.fields.ProvinceField(on_delete=django.db.models.deletion.CASCADE, to='iranian_cities.province', verbose_name='استان مبدا')),
                ('subsets', models.ManyToManyField(blank=True, null=True, to='account_module.subuser', verbose_name='همراهان')),
                ('insuranceprice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance_module.insuranceprice', verbose_name='تعرفه محاسبه قیمت')),
            ],
            options={
                'verbose_name': 'بیمه',
                'verbose_name_plural': 'بیمه ها',
            },
        ),
    ]
