# Generated by Django 3.0.4 on 2020-06-17 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_api', '0066_auto_20200617_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='nalog',
            field=models.TextField(blank=True, null=True, verbose_name='Налоговые льготы'),
        ),
        migrations.AlterField(
            model_name='greenfield',
            name='form',
            field=models.ManyToManyField(to='example_api.PrivateForm', verbose_name='Форма владения'),
        ),
        migrations.AlterField(
            model_name='greenfield',
            name='water_out',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Водоотведение'),
        ),
        migrations.AlterField(
            model_name='project',
            name='body',
            field=models.TextField(blank=True, null=True, verbose_name='Описание проекта проекта'),
        ),
        migrations.AlterField(
            model_name='support',
            name='form',
            field=models.CharField(blank=True, choices=[('lawyer', 'Юр.лицо'), ('ip', 'ИП'), ('municipality', 'Муниципалитет')], default=0, max_length=20, null=True, verbose_name='Категория получателя'),
        ),
        migrations.AlterField(
            model_name='support',
            name='summ',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Сумма займа'),
        ),
    ]
