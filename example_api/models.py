from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from .choices import *
from django.conf import settings


class Connect(models.Model):
    created = models.DateTimeField('Дата обращения', auto_now_add=True, db_index=True, null=True)
    name = models.CharField('Имя', max_length=30, )
    surname = models.CharField('Фамилия', max_length=30)
    middle_name = models.CharField('Отчество', max_length=40, null=True, blank=True)
    email = models.EmailField('Почта')
    phone = models.CharField('Телефон', max_length=30, blank=True, null=True)
    organisation = models.CharField('Организация', max_length=50, blank=True, null=True)
    text = models.TextField('Текст сообщения', blank=True)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField('Имя района', max_length=30)

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    image = models.ImageField(upload_to='News/img', height_field=None, width_field=None, null=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish', null=True)
    body = models.TextField('Текст')
    publish = models.DateTimeField("Опубликован", default=timezone.now)
    created = models.DateTimeField("Создан", default=timezone.now, blank=False, null=True)
    updated = models.DateTimeField("Обновлен", auto_now=True)

    def get_absolute_url(self):
        return reverse('post_detail',
                       args=[self.slug])

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class PrivateForm(models.Model):
    title = models.CharField('Форма собственности', max_length=150)

    class Meta:
        verbose_name = 'Форма собственности'
        verbose_name_plural = 'Форма собственности'

    def __str__(self):
        return self.title


class Greenfield(models.Model):
    ''' Модель участка '''
    territory = models.CharField('Территория участка', choices=greenfield_choice, max_length=50, )
    number_territory = models.CharField('Номер участка', max_length=100, default='')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Район')
    number = models.CharField('Кадастровый номер', max_length=50)
    type = models.CharField('Тип участка', choices=choice_type, max_length=20, default=0)
    image = models.ImageField(upload_to='greenfield', height_field=None, width_field=None, null=True,
                              verbose_name='Фотография участка')
    square = models.CharField('Площадь(га)', max_length=10)
    form = models.ManyToManyField(PrivateForm, verbose_name="Форма сделки")
    power = models.CharField('Электроснабжение', max_length=500, blank=True, null=True)
    water = models.CharField('Водоснабжение', max_length=500, blank=True, null=True)
    gas = models.CharField('Газоснабжение', max_length=500, blank=True, null=True)
    heat = models.CharField('Теплоснабжение', max_length=500, blank=True, null=True)
    water_out = models.CharField('Водоотведение', max_length=500, blank=True, null=True)
    description = models.TextField('Описание участка', blank=True, null=True)
    danger = models.CharField('Класс опасности', max_length=500, choices=danger_choices, default='1')
    category = models.CharField('Категория замель', max_length=50, choices=category_choices, default='0')
    desired = models.CharField('Форма собственности', max_length=50, choices=desired_choices, null=True)
    customs_priveleges = models.CharField('Таможенные льготы', max_length=100, default='', blank=True, null=True)
    territory_priveleges = models.CharField('Льготная стоимость земли', max_length=100, default='', null=True,
                                            blank=True)
    nalog = models.TextField('Налоговые льготы', blank=True, null=True)

    class Meta:
        ordering = ('number',)
        verbose_name = 'Земельный участок'
        verbose_name_plural = "Земельные участки"

    def __str__(self):
        return self.number


class Industry(models.Model):
    name = models.CharField('Название отрасли', max_length=100)
    slug = models.SlugField('Адрес', max_length=250, null=True, unique=True)

    class Meta:
        verbose_name = 'Отрасль'
        verbose_name_plural = 'Отрасли'

    def __str__(self):
        return self.name


class TypeProject(models.Model):
    description = models.CharField('Тип проекта', max_length=100)

    class Neta:
        verbose_name = 'Тип проекта'

    def __str__(self):
        return self.description


class Support(models.Model):
    territory = models.CharField('Территория реализации проекта', choices=territory_choice, max_length=50, blank=True)
    recipient = models.CharField('Получатель', choices=recipient_choice, max_length=150)
    name = models.CharField('Имя поддержки', max_length=500)
    condition = models.TextField('Условия', blank=True)
    type = models.CharField('Вид поддержки', choices=choice, max_length=50)
    organisation = models.TextField('кто выдает меру поддержки')
    industry = models.ManyToManyField(Industry, verbose_name='Отрасль')
    implementation = models.CharField('Способ реализации проекта', choices=implementation_choice, max_length=50,
                                      blank=True)
    type_project = models.ManyToManyField(TypeProject, blank=True, verbose_name='Тип проекта')
    target = models.TextField('Цели/адресаты гос.поддержки', default=0, blank=True)
    authority = models.CharField('Куррирующий орган', choices=authority_choices, max_length=50, blank=True)
    project_name = models.TextField('Наименование национального проекта', blank=True, default=0)
    program_name = models.TextField('Наименование гос.программы', default=0, blank=True)
    npa = models.TextField('НПА устанавливающий меры', default=0, blank=True)
    money = models.CharField('Объем меры гос.поддержки(млн.руб.)', max_length=150, blank=True)
    loan_time = models.CharField('Сроки займа', max_length=150, blank=True, default=0)
    category = models.CharField('Категория налогоплатильщика', max_length=300, blank=True)
    property_rate = models.TextField('Налоговая ставка на имущество', blank=True)
    profit = models.TextField('Налог на прибыль', blank=True)
    transport = models.TextField('Налоговая ставка по транспортному налогу', blank=True)
    land = models.TextField('Налоговая ставка по земельному налогу', blank=True)
    nds = models.TextField('Налоговая ставка НДС', blank=True)
    summ = models.CharField('Сумма займа', max_length=50, blank=True, null=True)
    expenses = models.TextField('Затраты подлежащие возмещению', blank=True)
    form = models.CharField('Категория получателя', choices=form_choice, max_length=20, default=0, blank=True,
                            null=True)
    nalog = models.TextField('Налоговые льготы', null=True, blank=True)
    percent = models.CharField('Процентная ставка', null=True, blank=True, max_length=200)

    class Meta:
        verbose_name = 'Мера поддержки'
        verbose_name_plural = 'Меры поддержки'

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField('Название документа', max_length=5000)
    url = models.CharField('УРЛ', max_length=50, default='')
    file = models.FileField(upload_to='Documents', null=True)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'



class Project(models.Model):
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, null=True, verbose_name='Отрасль')
    name = models.CharField('Наименование проекта', max_length=100)
    start = models.IntegerField('Начало реализации проекта', null=True)
    finish = models.IntegerField('Конец реализации проекта', null=True)
    body = models.TextField('Описание проекта проекта', null=True, blank=True)
    sum = models.IntegerField('Сумма инвестиций(млн.руб)')
    now = models.TextField('Текущее состояние проекта')
    image = models.ImageField(upload_to='Project', height_field=None, width_field=None, null=True,
                              verbose_name='Фотография проекта')
    help = models.BooleanField('Нуждается в финансировании',  default=False)
    # invest = models.ForeignKey(ProjectRequest, null=True, on_delete = models.CASCADE, blank=True, verbose_name='Заявление для финансирования')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '{0}{1}'.format(settings.MEDIA_URL, self.image.url)

class ProjectRequest(models.Model):
    name = models.CharField('ФИО', max_length=500, blank=True, null=True)
    organisation = models.CharField('Организация', max_length=500, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=500, blank=True, null=True)
    email = models.EmailField('Почта', blank=True, null=True)
    comment = models.TextField('Комментарий', blank=True, null=True)
    project = models.ForeignKey(Project, verbose_name = 'Проект', on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = 'Заявка  финансирования проекта'
        verbose_name_plural = 'Заявки финансирования проектов'

class Contact(models.Model):
    name = models.CharField('Фамилия, имя, отчество', max_length=200)
    email = models.EmailField('Почта', max_length=300)
    role = models.CharField('Роль', max_length=300, choices=contact_role_choice,  null=True)
    phone = models.CharField('Номер телефона', max_length=30)
    position = models.CharField('Должность', max_length=500)
    image = models.ImageField(upload_to='contacts', height_field=None, width_field=None, null=True,
                              verbose_name='Фотография')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name

class Event(models.Model):
    email = models.EmailField('Почта', max_length=300, null=True)
    name = models.CharField('Имя', max_length=300, null=True)
    second_name = models.CharField('Фармилия', max_length=300, null=True)
    phone = models.CharField('Номер телефона', max_length=30, null=True)
    organisation = models.CharField('Название компании', max_length=500, blank=True, null=True)
    profile = models.TextField('Профиль деятельности', null=True)
    role = models.TextField('Ваша должность', null=True)
    registration = models.DateTimeField('Зарегестрирован', default=timezone.now, null=True)
    transfer = models.BooleanField('Нужен ли трансфер из города?', null=True)
    
    class Meta:
        verbose_name = 'Cобытие'
        verbose_name_plural = 'Событие'

    def __str__(self):
        return self.organisation 