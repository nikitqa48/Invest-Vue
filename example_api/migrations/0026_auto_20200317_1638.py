# Generated by Django 2.2.6 on 2020-03-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_api', '0025_support'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='territory',
            field=models.CharField(blank=True, choices=[('oez', 'ОЭЗ'), ('park', 'индустриальный парк'), ('mono', 'моногород'), ('vne', 'территория вне'), ('all', 'любая')], max_length=50, verbose_name='Территория реализации проекта'),
        ),
        migrations.AlterField(
            model_name='support',
            name='recipient',
            field=models.CharField(choices=[('small', 'Малый (1-100 чел.)'), ('average', 'Средний (100-250 чел.)'), ('big', 'Крупный (от 251 чел.)'), ('all', 'Все')], max_length=150, verbose_name='Получатель'),
        ),
    ]
