# Generated by Django 3.1.5 on 2021-01-31 16:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Дата обращения')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Телефон')),
                ('organisation', models.CharField(blank=True, max_length=50, null=True, verbose_name='Организация')),
                ('text', models.TextField(blank=True, verbose_name='Текст сообщения')),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Фамилия, имя, отчество')),
                ('email', models.EmailField(max_length=300, verbose_name='Почта')),
                ('role', models.CharField(choices=[('leader', 'руководство'), ('agent', 'агенство')], max_length=300, null=True, verbose_name='Роль')),
                ('phone', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('position', models.CharField(max_length=500, verbose_name='Должность')),
                ('image', models.ImageField(null=True, upload_to='contacts', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5000, verbose_name='Название документа')),
                ('url', models.CharField(default='', max_length=50, verbose_name='УРЛ')),
                ('file', models.FileField(null=True, upload_to='Documents')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300, null=True, verbose_name='Почта')),
                ('name', models.CharField(max_length=300, null=True, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=300, null=True, verbose_name='Фармилия')),
                ('phone', models.CharField(max_length=30, null=True, verbose_name='Номер телефона')),
                ('organisation', models.CharField(blank=True, max_length=500, null=True, verbose_name='Название компании')),
                ('profile', models.TextField(null=True, verbose_name='Профиль деятельности')),
                ('role', models.TextField(null=True, verbose_name='Ваша должность')),
                ('registration', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Зарегестрирован')),
                ('transfer', models.BooleanField(null=True, verbose_name='Нужен ли трансфер из города?')),
            ],
            options={
                'verbose_name': 'Cобытие',
                'verbose_name_plural': 'Событие',
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название отрасли')),
                ('slug', models.SlugField(max_length=250, null=True, unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Отрасль',
                'verbose_name_plural': 'Отрасли',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('image', models.ImageField(null=True, upload_to='News/img')),
                ('slug', models.SlugField(max_length=250, null=True, unique_for_date='publish')),
                ('body', models.TextField(verbose_name='Текст')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Опубликован')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='NewsTranslate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Опубликован')),
                ('image', models.ImageField(null=True, upload_to='News/img')),
                ('slug', models.SlugField(max_length=250, null=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ('-publish',),
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PrivateForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Форма собственности')),
            ],
            options={
                'verbose_name': 'Форма собственности',
                'verbose_name_plural': 'Форма собственности',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование проекта')),
                ('start', models.IntegerField(null=True, verbose_name='Начало реализации проекта')),
                ('finish', models.IntegerField(null=True, verbose_name='Конец реализации проекта')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Описание проекта проекта')),
                ('sum', models.IntegerField(verbose_name='Сумма инвестиций(млн.руб)')),
                ('now', models.TextField(verbose_name='Текущее состояние проекта')),
                ('image', models.ImageField(null=True, upload_to='Project', verbose_name='Фотография проекта')),
                ('help', models.BooleanField(default=False, verbose_name='Нуждается в финансировании')),
                ('industry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example_api.industry', verbose_name='Отрасль')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='ProjectTranslate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField(null=True, verbose_name='Начало реализации проекта')),
                ('finish', models.IntegerField(null=True, verbose_name='Конец реализации проекта')),
                ('sum', models.IntegerField(blank=True, null=True, verbose_name='Сумма инвестиций(млн.руб)')),
                ('image', models.ImageField(null=True, upload_to='Project', verbose_name='Фотография проекта')),
                ('help', models.BooleanField(default=False, verbose_name='Нуждается в финансировании')),
                ('industry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example_api.industry', verbose_name='Отрасль')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя района')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='TypeProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Тип проекта')),
            ],
        ),
        migrations.CreateModel(
            name='SupportTranslate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('territory', models.CharField(blank=True, choices=[('without', 'Без ограничений'), ('park', 'индустриальные парки'), ('mono', 'моногород'), ('techno', 'технопарк'), ('oez', 'ОЭЗ ппт '), ('oezru', 'ОЭЗРУ'), ('cluster', 'Участник кластера'), ('all', 'Любая')], max_length=50, verbose_name='Территория реализации проекта')),
                ('recipient', models.CharField(choices=[('small', 'МСП'), ('innovation', 'Инновации'), ('all', 'Все'), ('municipality', 'муниципалитет'), ('industrial', 'Резиденты индустриальных парков'), ('developers', 'Разработчики ПО'), ('resident_oez', 'Резиденты ОЭЗРУ Липецк'), ('subject', 'Субъект'), ('legally', 'Юридические лица'), ('cooperatives', 'Кооперативы'), ('not_msp', 'Все кроме МСП')], max_length=150, verbose_name='Получатель')),
                ('type', models.CharField(choices=[('direct', 'Инвестиции'), ('loan_funding', 'Заемное финансирование'), ('loan', 'Налоговые льготы по налогу на займ'), ('subsidies', 'субсидии'), ('profit', 'Налоговые льготы по налогу на прибыль'), ('property', 'Налоговые льготы по налогу на имущество'), ('grant', 'Гранты'), ('rent', 'льготы по аренде'), ('garant', 'гарантии'), ('transport', 'Налоговые льготы по транспортному налогу'), ('earth', 'налоговые льготы по земельному налогу'), ('nds', 'налоговые льготы по уплате НДС'), ('customs', 'таможенные льготы'), ('infrastructure', 'Субсидии на инфраструктуру'), ('loan_profit', 'кредиты под залог создаваемого имущества')], max_length=50, verbose_name='Вид поддержки')),
                ('implementation', models.CharField(blank=True, choices=[('agreement', 'Соглашение'), ('gchp', 'ГЧП'), ('any', 'Любой')], max_length=50, verbose_name='Способ реализации проекта')),
                ('authority', models.CharField(blank=True, choices=[('uilo', 'УИиИ ЛО'), ('min', 'Минпромторг России'), ('bank', 'Уполномоченные банки'), ('fond', 'Фонд содействия инновациям'), ('rvk', 'АО "РВК"'), ('business', 'Центры "мой бизнес", Управляющие компании')], max_length=50, verbose_name='Куррирующий орган')),
                ('form', models.CharField(blank=True, choices=[('lawyer', 'Юр.лицо'), ('ip', 'ИП'), ('municipality', 'Муниципалитет')], default=0, max_length=20, null=True, verbose_name='Категория получателя')),
                ('industry', models.ManyToManyField(related_name='industry', to='example_api.Industry', verbose_name='Отрасль')),
                ('type_project', models.ManyToManyField(blank=True, to='example_api.TypeProject', verbose_name='Тип проекта')),
            ],
            options={
                'verbose_name': 'Мера поддержки',
                'verbose_name_plural': 'Меры поддержки',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('territory', models.CharField(blank=True, choices=[('without', 'Без ограничений'), ('park', 'индустриальные парки'), ('mono', 'моногород'), ('techno', 'технопарк'), ('oez', 'ОЭЗ ппт '), ('oezru', 'ОЭЗРУ'), ('cluster', 'Участник кластера'), ('all', 'Любая')], max_length=50, verbose_name='Территория реализации проекта')),
                ('recipient', models.CharField(choices=[('small', 'МСП'), ('innovation', 'Инновации'), ('all', 'Все'), ('municipality', 'муниципалитет'), ('industrial', 'Резиденты индустриальных парков'), ('developers', 'Разработчики ПО'), ('resident_oez', 'Резиденты ОЭЗРУ Липецк'), ('subject', 'Субъект'), ('legally', 'Юридические лица'), ('cooperatives', 'Кооперативы'), ('not_msp', 'Все кроме МСП')], max_length=150, verbose_name='Получатель')),
                ('name', models.CharField(max_length=500, verbose_name='Имя поддержки')),
                ('condition', models.TextField(blank=True, verbose_name='Условия')),
                ('type', models.CharField(choices=[('direct', 'Инвестиции'), ('loan_funding', 'Заемное финансирование'), ('loan', 'Налоговые льготы по налогу на займ'), ('subsidies', 'субсидии'), ('profit', 'Налоговые льготы по налогу на прибыль'), ('property', 'Налоговые льготы по налогу на имущество'), ('grant', 'Гранты'), ('rent', 'льготы по аренде'), ('garant', 'гарантии'), ('transport', 'Налоговые льготы по транспортному налогу'), ('earth', 'налоговые льготы по земельному налогу'), ('nds', 'налоговые льготы по уплате НДС'), ('customs', 'таможенные льготы'), ('infrastructure', 'Субсидии на инфраструктуру'), ('loan_profit', 'кредиты под залог создаваемого имущества')], max_length=50, verbose_name='Вид поддержки')),
                ('organisation', models.TextField(verbose_name='кто выдает меру поддержки')),
                ('implementation', models.CharField(blank=True, choices=[('agreement', 'Соглашение'), ('gchp', 'ГЧП'), ('any', 'Любой')], max_length=50, verbose_name='Способ реализации проекта')),
                ('target', models.TextField(blank=True, default=0, verbose_name='Цели/адресаты гос.поддержки')),
                ('authority', models.CharField(blank=True, choices=[('uilo', 'УИиИ ЛО'), ('min', 'Минпромторг России'), ('bank', 'Уполномоченные банки'), ('fond', 'Фонд содействия инновациям'), ('rvk', 'АО "РВК"'), ('business', 'Центры "мой бизнес", Управляющие компании')], max_length=50, verbose_name='Куррирующий орган')),
                ('project_name', models.TextField(blank=True, default=0, verbose_name='Наименование национального проекта')),
                ('program_name', models.TextField(blank=True, default=0, verbose_name='Наименование гос.программы')),
                ('npa', models.TextField(blank=True, default=0, verbose_name='НПА устанавливающий меры')),
                ('money', models.CharField(blank=True, max_length=150, verbose_name='Объем меры гос.поддержки(млн.руб.)')),
                ('loan_time', models.CharField(blank=True, default=0, max_length=150, verbose_name='Сроки займа')),
                ('category', models.CharField(blank=True, max_length=300, verbose_name='Категория налогоплатильщика')),
                ('property_rate', models.TextField(blank=True, verbose_name='Налоговая ставка на имущество')),
                ('profit', models.TextField(blank=True, verbose_name='Налог на прибыль')),
                ('transport', models.TextField(blank=True, verbose_name='Налоговая ставка по транспортному налогу')),
                ('land', models.TextField(blank=True, verbose_name='Налоговая ставка по земельному налогу')),
                ('nds', models.TextField(blank=True, verbose_name='Налоговая ставка НДС')),
                ('summ', models.CharField(blank=True, max_length=50, null=True, verbose_name='Сумма займа')),
                ('expenses', models.TextField(blank=True, verbose_name='Затраты подлежащие возмещению')),
                ('form', models.CharField(blank=True, choices=[('lawyer', 'Юр.лицо'), ('ip', 'ИП'), ('municipality', 'Муниципалитет')], default=0, max_length=20, null=True, verbose_name='Категория получателя')),
                ('nalog', models.TextField(blank=True, null=True, verbose_name='Налоговые льготы')),
                ('percent', models.CharField(blank=True, max_length=200, null=True, verbose_name='Процентная ставка')),
                ('industry', models.ManyToManyField(to='example_api.Industry', verbose_name='Отрасль')),
                ('type_project', models.ManyToManyField(blank=True, to='example_api.TypeProject', verbose_name='Тип проекта')),
            ],
            options={
                'verbose_name': 'Мера поддержки',
                'verbose_name_plural': 'Меры поддержки',
            },
        ),
        migrations.CreateModel(
            name='ProjectRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='ФИО')),
                ('organisation', models.CharField(blank=True, max_length=500, null=True, verbose_name='Организация')),
                ('phone', models.CharField(blank=True, max_length=500, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example_api.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Заявка  финансирования проекта',
                'verbose_name_plural': 'Заявки финансирования проектов',
            },
        ),
        migrations.CreateModel(
            name='GreenfieldTranslate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_territory', models.CharField(default='', max_length=100, verbose_name='Номер участка')),
                ('number', models.CharField(default=0, max_length=50, verbose_name='Кадастровый номер')),
                ('image', models.ImageField(null=True, upload_to='greenfield', verbose_name='Фотография участка')),
                ('form', models.ManyToManyField(to='example_api.PrivateForm', verbose_name='Форма сделки')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example_api.region', verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Земельный участок',
                'verbose_name_plural': 'Земельные участки',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Greenfield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('territory', models.CharField(choices=[('oez', 'ОЭЗ ППТ'), ('oezru', 'ОЭЗ Ру'), ('industrial', 'Индустриальный парк'), ('any', 'Иная площадка')], max_length=50, verbose_name='Территория участка')),
                ('number_territory', models.CharField(default='', max_length=100, verbose_name='Номер участка')),
                ('number', models.CharField(max_length=50, verbose_name='Кадастровый номер')),
                ('type', models.CharField(choices=[('greenfield', 'Гринфилд'), ('brownfield', 'Браунфилд')], default=0, max_length=20, verbose_name='Тип участка')),
                ('image', models.ImageField(null=True, upload_to='greenfield', verbose_name='Фотография участка')),
                ('square', models.CharField(max_length=10, verbose_name='Площадь(га)')),
                ('power', models.CharField(blank=True, max_length=500, null=True, verbose_name='Электроснабжение')),
                ('water', models.CharField(blank=True, max_length=500, null=True, verbose_name='Водоснабжение')),
                ('gas', models.CharField(blank=True, max_length=500, null=True, verbose_name='Газоснабжение')),
                ('heat', models.CharField(blank=True, max_length=500, null=True, verbose_name='Теплоснабжение')),
                ('water_out', models.CharField(blank=True, max_length=500, null=True, verbose_name='Водоотведение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание участка')),
                ('danger', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=500, verbose_name='Класс опасности')),
                ('category', models.CharField(choices=[('0', 'Земли сельского назначения'), ('1', 'Земли  населенных пунктов'), ('2', 'Земли для промышленности'), ('3', 'Земли для энергетики'), ('4', 'Земли для транспорта'), ('5', 'Земли для связи'), ('6', 'Земли для радиовещания'), ('7', 'Земли для телевидения'), ('8', 'Земли для информатики'), ('9', 'Земли для обеспечения космической деятельности'), ('10', 'Земли для обороны'), ('11', 'Земли для безопасности и иного специального назначения'), ('12', 'Земли особо охраняемых территорий и объектов'), ('13', 'Земли лесного фонда'), ('14', 'Земли водного фонда')], default='0', max_length=50, verbose_name='Категория замель')),
                ('desired', models.CharField(choices=[('goverment', 'Государственная'), ('private', 'Частная')], max_length=50, null=True, verbose_name='Форма собственности')),
                ('customs_priveleges', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Таможенные льготы')),
                ('territory_priveleges', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Льготная стоимость земли')),
                ('nalog', models.TextField(blank=True, null=True, verbose_name='Налоговые льготы')),
                ('form', models.ManyToManyField(to='example_api.PrivateForm', verbose_name='Форма сделки')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_api.region', verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Земельный участок',
                'verbose_name_plural': 'Земельные участки',
                'ordering': ('number',),
            },
        ),
        migrations.CreateModel(
            name='SupportTranslateTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=5000, verbose_name='Имя поддержки')),
                ('target', models.TextField(blank=True, default=0, verbose_name='Цели/адресаты гос.поддержки')),
                ('nalog', models.TextField(blank=True, null=True, verbose_name='Налоговые льготы')),
                ('expenses', models.TextField(blank=True, verbose_name='Затраты подлежащие возмещению')),
                ('project_name', models.TextField(blank=True, default=0, verbose_name='Наименование национального проекта')),
                ('program_name', models.TextField(blank=True, default=0, verbose_name='Наименование гос.программы')),
                ('npa', models.TextField(blank=True, default=0, verbose_name='НПА устанавливающий меры')),
                ('organisation', models.TextField(verbose_name='кто выдает меру поддержки')),
                ('condition', models.TextField(blank=True, verbose_name='Условия')),
                ('category', models.CharField(blank=True, max_length=300, verbose_name='Категория налогоплатильщика')),
                ('loan_time', models.CharField(blank=True, default=0, max_length=150, verbose_name='Сроки займа')),
                ('property_rate', models.TextField(blank=True, verbose_name='Налоговая ставка на имущество')),
                ('profit', models.TextField(blank=True, verbose_name='Налог на прибыль')),
                ('transport', models.TextField(blank=True, verbose_name='Налоговая ставка по транспортному налогу')),
                ('land', models.TextField(blank=True, verbose_name='Налоговая ставка по земельному налогу')),
                ('nds', models.TextField(blank=True, verbose_name='Налоговая ставка НДС')),
                ('money', models.CharField(blank=True, max_length=150, verbose_name='Объем меры гос.поддержки(млн.руб.)')),
                ('summ', models.CharField(blank=True, max_length=50, null=True, verbose_name='Сумма займа')),
                ('percent', models.CharField(blank=True, max_length=200, null=True, verbose_name='Процентная ставка')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='example_api.supporttranslate')),
            ],
            options={
                'verbose_name': 'Мера поддержки Translation',
                'db_table': 'example_api_supporttranslate_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProjectTranslateTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование проекта')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Описание проекта проекта')),
                ('now', models.TextField(verbose_name='Текущее состояние проекта')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='example_api.projecttranslate')),
            ],
            options={
                'verbose_name': 'Проект Translation',
                'db_table': 'example_api_projecttranslate_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NewsTranslateTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Текст')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='example_api.newstranslate')),
            ],
            options={
                'verbose_name': 'Новость Translation',
                'db_table': 'example_api_newstranslate_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GreenfieldTranslateTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание участка')),
                ('territory', models.CharField(choices=[('oez', 'ОЭЗ ППТ'), ('oezru', 'ОЭЗ Ру'), ('industrial', 'Индустриальный парк'), ('any', 'Иная площадка')], max_length=50, null=True, verbose_name='Территория участка')),
                ('type', models.CharField(choices=[('greenfield', 'Гринфилд'), ('brownfield', 'Браунфилд')], default=0, max_length=20, verbose_name='Тип участка')),
                ('square', models.CharField(default='', max_length=10, verbose_name='Площадь(га)')),
                ('power', models.CharField(blank=True, max_length=500, null=True, verbose_name='Электроснабжение')),
                ('water', models.CharField(blank=True, max_length=500, null=True, verbose_name='Водоснабжение')),
                ('gas', models.CharField(blank=True, max_length=500, null=True, verbose_name='Газоснабжение')),
                ('heat', models.CharField(blank=True, max_length=500, null=True, verbose_name='Теплоснабжение')),
                ('water_out', models.CharField(blank=True, max_length=500, null=True, verbose_name='Водоотведение')),
                ('danger', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=500, verbose_name='Класс опасности')),
                ('category', models.CharField(choices=[('0', 'Земли сельского назначения'), ('1', 'Земли  населенных пунктов'), ('2', 'Земли для промышленности'), ('3', 'Земли для энергетики'), ('4', 'Земли для транспорта'), ('5', 'Земли для связи'), ('6', 'Земли для радиовещания'), ('7', 'Земли для телевидения'), ('8', 'Земли для информатики'), ('9', 'Земли для обеспечения космической деятельности'), ('10', 'Земли для обороны'), ('11', 'Земли для безопасности и иного специального назначения'), ('12', 'Земли особо охраняемых территорий и объектов'), ('13', 'Земли лесного фонда'), ('14', 'Земли водного фонда')], default='0', max_length=50, verbose_name='Категория замель')),
                ('desired', models.CharField(choices=[('goverment', 'Государственная'), ('private', 'Частная')], max_length=50, null=True, verbose_name='Форма собственности')),
                ('customs_priveleges', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Таможенные льготы')),
                ('territory_priveleges', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Льготная стоимость земли')),
                ('nalog', models.TextField(blank=True, null=True, verbose_name='Налоговые льготы')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='example_api.greenfieldtranslate')),
            ],
            options={
                'verbose_name': 'Земельный участок Translation',
                'db_table': 'example_api_greenfieldtranslate_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
