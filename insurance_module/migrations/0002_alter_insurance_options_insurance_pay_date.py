# Generated by Django 5.0 on 2025-05-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='insurance',
            options={'ordering': ['-created_at'], 'verbose_name': 'بیمه', 'verbose_name_plural': 'بیمه ها'},
        ),
        migrations.AddField(
            model_name='insurance',
            name='pay_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت'),
        ),
    ]
