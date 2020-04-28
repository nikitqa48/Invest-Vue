# Generated by Django 2.2.6 on 2020-04-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('example_api', '0037_auto_20200427_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greenfield',
            name='form',
            field=models.CharField(choices=[('goverment', 'государственная'), ('private', 'частная')], max_length=30, verbose_name='Форма собственности'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
