# Generated by Django 3.0.4 on 2020-06-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_api', '0062_auto_20200614_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='time',
            field=models.IntegerField(verbose_name='Сроки реализации'),
        ),
    ]
