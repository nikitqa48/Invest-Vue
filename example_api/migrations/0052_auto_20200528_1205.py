# Generated by Django 3.0.4 on 2020-05-28 09:05

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('example_api', '0051_auto_20200528_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='type',
            field=models.CharField(choices=[('direct', 'инвестиции'), ('loan_funding', 'Заемное финансирование'), ('loan', 'Налоговые льготы по налогу на займ'), ('subsidies', 'субсидии'), ('profit', 'Налоговые льготы по налогу на прибыль'), ('property', 'Налоговые льготы по налогу на имущество'), ('grant', 'Гранты'), ('rent', 'льготы по аренде'), ('garant', 'гарантии'), ('transport', 'Налоговые льготы по транспортному налогу'), ('earth', 'налоговые льготы по земельному налогу'), ('nds', 'налоговые льготы по уплате НДС'), ('customs', 'таможенные льготы'), ('infrastructure', 'Субсидии на инфраструктуру'), ('loan_profit', 'кредиты под залог создаваемого имущества')], max_length=50, verbose_name='Тип поддержки'),
        ),
        migrations.AlterField(
            model_name='support',
            name='type_project',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('new', 'Новое строительство'), ('reconstuction', 'Реконструкция'), ('modernisation', 'Модернизация'), ('all', 'любой')], max_length=50, verbose_name='Тип проекта'),
        ),
    ]
