# Generated by Django 3.0.2 on 2020-01-31 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_api', '0003_auto_20200129_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата обращения')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=40, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('organisation', models.CharField(max_length=50, verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Обращения',
            },
        ),
    ]
