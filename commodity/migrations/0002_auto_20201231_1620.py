# Generated by Django 3.1.4 on 2020-12-31 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commodity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('Male Group', 'Male Group'), ('Female Group', 'Female Group'), ('Male SOLO', 'Male SOLO'), ('Female SOLO', 'Female SOLO')], max_length=100)),
                ('date', models.DateField()),
                ('content', models.TextField(max_length=500)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('music_files', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time_long', models.TimeField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.commodity')),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.singer')),
            ],
        ),
        migrations.AddField(
            model_name='commodity',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.singer'),
        ),
    ]
