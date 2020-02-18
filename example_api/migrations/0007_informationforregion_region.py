# Generated by Django 3.0.2 on 2020-02-02 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('example_api', '0006_connect_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя района')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='InformationForRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.CharField(max_length=20, verbose_name='Электроснабжение')),
                ('water', models.CharField(max_length=20, verbose_name='Водоснабжение')),
                ('gas', models.CharField(max_length=20, verbose_name='Газоснабжение')),
                ('heat', models.CharField(max_length=20, verbose_name='Теплоснабжение')),
                ('water_out', models.CharField(max_length=20, verbose_name='Теплоотведение')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_api.Region')),
            ],
            options={
                'verbose_name': 'Информация о районе',
                'verbose_name_plural': 'Информация о районах',
            },
        ),
    ]
