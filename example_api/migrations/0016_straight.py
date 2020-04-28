# Generated by Django 2.2.6 on 2020-03-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_api', '0015_brownfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='Straight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(max_length=150, verbose_name='Получатель')),
                ('name', models.CharField(max_length=500, verbose_name='Имя поддержки')),
                ('body', models.TextField(blank=True, verbose_name='Текст')),
                ('type', models.CharField(choices=[('grant', 'грант'), ('direct', 'Прямая финансовая поддержка'), ('loan', 'заемное финансирование')], max_length=50, verbose_name='Тип поддержки')),
                ('organisation', models.TextField(verbose_name='кто выдает меру поддержки')),
                ('industry', models.CharField(choices=[('industry', 'промышленность'), ('tourism', 'культура и туризм'), ('education', 'образование'), ('agriculture', 'сельское хозяйство'), ('trade', 'торговля'), ('ecology', 'экология')], max_length=20, verbose_name='Отрасль')),
            ],
        ),
    ]
