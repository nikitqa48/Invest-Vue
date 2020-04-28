from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from .choices import *

class Profile(User):
    GENDER = (
    ('male', "Мужчина"),
    ('female', 'Женщина'),
    )
    gender = models.CharField('Пол', choices=GENDER, max_length=6)
    phone = models.CharField('Телефон',max_length=20)
    address= models.CharField('Адрес', max_length=150)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.username


class Connect(models.Model):
    created = models.DateTimeField('Дата обращения',auto_now_add=True, db_index=True,null=True)
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    middle_name = models.CharField('Отчество', max_length=40, null=True)
    email = models.EmailField('Почта')
    phone = models.CharField('Телефон', max_length=30)
    organisation = models.CharField('Организация', max_length=50)
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


class InformationForRegion(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    power = models.CharField('Электроснабжение', max_length=20)
    water = models.CharField('Водоснабжение', max_length=20)
    gas = models.CharField('Газоснабжение', max_length=20)
    heat = models.CharField('Теплоснабжение', max_length=20)
    water_out = models.CharField('Теплоотведение', max_length=20)

    class Meta:
        verbose_name = 'Информация о районе'
        verbose_name_plural = 'Информация о районах'

    def __str__(self):
        return self.region.name


class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    image = models.ImageField(upload_to='News/img', height_field=None, width_field=None, null=True)
    slug = models.SlugField(max_length=250,unique_for_date='publish', null=True)
    body = models.TextField('Текст')
    publish = models.DateTimeField("Опубликован",default=timezone.now)
    created = models.DateTimeField("Создан",default=timezone.now, blank = False, null = True)
    updated = models.DateTimeField("Обновлен",auto_now=True)
        
    def get_absolute_url(self):
        return reverse('post_detail',
                        args=[self.slug])

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class Greenfield(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    number = models.CharField('Кадастровый номер', max_length=50)
    type = models.CharField('Тип участка', choices=choice_type, max_length=20, default=0)
    image = models.ImageField(upload_to='greenfield',height_field=None,width_field=None,null=True)
    square = models.CharField('Площадь(га)', max_length=10)
    form = models.CharField('Форма собственности', choices=private_choice,max_length=30)

    class Meta:
        ordering = ('number',)
        verbose_name = 'Земельный участок'
        verbose_name_plural = "Земельные участки"

    def __str__(self):
        return self.number


class Industry(models.Model):
    name = models.CharField('Название отрасли', max_length=100)

    class Meta:
        verbose_name = 'Отрасль'
        verbose_name_plural = 'Отрасли'

    def __str__(self):
        return self.name


class Support(models.Model):
    territory = models.CharField('Территория реализации проекта', choices=territory_choice, max_length=50, blank=True)
    recipient = models.CharField('Получатель', choices=recipient_choice, max_length=150)
    name = models.CharField('Имя поддержки', max_length=500)
    condition = models.TextField('Условия', blank=True)
    type = models.CharField('Тип поддержки', choices=choice, max_length=50)
    organisation = models.TextField('кто выдает меру поддержки')
    industry = models.ManyToManyField(Industry, verbose_name='Отрасль')
    implementation = models.CharField('Способ реализации проекта', choices=implementation_choice, max_length=50, blank=True)
    type_project = models.CharField('Тип проекта', choices=type_project_choices, max_length=50, blank=True)
    target = models.TextField('Цели/адресаты гос.поддержки', default=0, blank=True)
    authority = models.CharField('Куррирующий орган', choices=authority_choices, max_length=50, blank=True)
    project_name = models.TextField('Наименование национального проекта', blank=True, default=0)
    program_name = models.TextField('Наименование гос.программы', default=0)
    npa = models.TextField('НПА устанавливающий меры', default=0, blank=True)
    money = models.CharField('Объем меры гос.поддержки(млрд.руб.)', max_length=150, blank=True)
    category = models.CharField('Категория налогоплатильщика', max_length=300, blank=True)
    property_rate = models.TextField('Налоговая ставка на имущество', blank=True)
    profit = models.TextField('Налог на прибыль', blank=True)
    transport = models.TextField('Налоговая ставка по транспортному налогу', blank=True)
    land = models.TextField('Налоговая ставка по земельному налогу', blank=True)
    nds = models.TextField('Налоговая ставка НДС', blank=True)
    summ = models.CharField('Сумма займа', max_length=50, blank=True)
    expenses = models.TextField('Затраты подлежащие возмещению', blank=True)
    form = models.CharField('Категория получателя', choices=form_choice, max_length=20, default=0, blank=True)

    class Meta:
        verbose_name = 'Мера поддержки'
        verbose_name_plural = 'Меры поддержки'

    def __str__(self):
        return  self.name
