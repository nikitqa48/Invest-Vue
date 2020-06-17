# Generated by Django 3.0.4 on 2020-06-17 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('example_api', '0064_auto_20200617_1248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
        migrations.AddField(
            model_name='industry',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='project',
            name='industry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example_api.Industry', verbose_name='Отрасль'),
        ),
    ]
