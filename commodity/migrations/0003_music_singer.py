# Generated by Django 3.1.4 on 2021-01-02 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0002_auto_20201231_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='singer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='commodity.singer'),
        ),
    ]
