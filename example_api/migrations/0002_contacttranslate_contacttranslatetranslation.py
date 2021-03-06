# Generated by Django 3.1.5 on 2021-01-31 16:20

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('example_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactTranslate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300, verbose_name='Почта')),
                ('role', models.CharField(choices=[('leader', 'руководство'), ('agent', 'агенство')], max_length=300, null=True, verbose_name='Роль')),
                ('phone', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('image', models.ImageField(null=True, upload_to='contacts', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ContactTranslateTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=200, verbose_name='Фамилия, имя, отчество')),
                ('position', models.CharField(max_length=500, verbose_name='Должность')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='example_api.contacttranslate')),
            ],
            options={
                'verbose_name': 'Контакт Translation',
                'db_table': 'example_api_contacttranslate_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
