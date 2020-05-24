# Generated by Django 3.0.4 on 2020-05-21 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_api', '0044_auto_20200513_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='greenfield',
            name='number_territory',
            field=models.CharField(default=0, max_length=100, verbose_name='Номер участка'),
        ),
        migrations.AlterField(
            model_name='support',
            name='territory',
            field=models.CharField(blank=True, choices=[('without', 'Без ограничений'), ('park', 'индустриальные парки'), ('mono', 'моногород'), ('techno', 'технопарк'), ('oez', 'ОЭЗ ппт '), ('oezru', 'ОЭЗРУ'), ('cluster', 'Участник кластера'), ('all', 'Любая')], max_length=50, verbose_name='Территория реализации проекта'),
        ),
    ]
