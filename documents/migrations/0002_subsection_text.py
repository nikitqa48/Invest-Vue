# Generated by Django 3.1.5 on 2021-03-13 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsection',
            name='text',
            field=models.TextField(default='', verbose_name='Текст'),
        ),
    ]
