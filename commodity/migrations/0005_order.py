# Generated by Django 3.1.4 on 2021-01-05 01:48

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0004_commodity_iframe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact Phone Number', max_length=31)),
                ('address', models.CharField(max_length=100)),
                ('pay', models.CharField(choices=[('貨到付款', '貨到付款'), ('銀行轉帳', '銀行轉帳'), ('信用卡支付', '信用卡支付')], max_length=100)),
                ('status', models.CharField(choices=[('備貨中', '備貨中'), ('運貨中', '運貨中'), ('當天送達', '當天送達')], max_length=100)),
                ('progress', models.CharField(choices=[('未付款', '未付款'), ('已付款', '已付款'), ('交易完成', '交易完成')], max_length=100)),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='commodity.commodity')),
            ],
        ),
    ]
