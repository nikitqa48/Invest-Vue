from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Profile(User):
    GENDER = (
    ('male',"Мужчина"),
    ('female','Женщина'),
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
    image = models.ImageField(upload_to='greenfield',height_field=None,width_field=None,null=True)
    square = models.CharField('Площадь(га)', max_length=10)
    choice = (
        ('goverment','государственная'),
        ('private','частная')
        )
    form = models.CharField('Форма собственности', choices=choice,max_length=30)

    class Meta:
        ordering = ('number',)
        verbose_name = 'Гринфилд'

    def __str__(self):
        return self.number


class Brownfield(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    number = models.CharField('Кадастровый номер', max_length=50)
    image = models.ImageField(upload_to='brownfield', height_field=None, width_field=None, null=True)
    square = models.CharField('Площадь(га)', max_length=15)

    class Meta:
        ordering = ('number',)
        verbose_name = 'Браунфилд'

    def __str__(self):
        return  self.number


class Industry(models.Model):
    name = models.CharField('Название отрасли', max_length=100)

    class Meta:
        verbose_name = 'Отрасль'
        verbose_name_plural = 'Отрасли'

    def __str__(self):
        return self.name


class Support(models.Model):
    recipient_choice = (
        ('small', 'Малый (1-100 чел.)'),
        ('average', 'Средний (100-250 чел.)'),
        ('big', "Крупный (от 251 чел.)"),
        ('all', 'Все')
    )
    territory_choice = (
        ('oez', 'ОЭЗ'),
        ('park', 'индустриальный парк'),
        ('mono', 'моногород'),
        ('vne', 'территория вне'),
        ('all', 'любая')
    )
    territory = models.CharField('Территория реализации проекта', choices=territory_choice, max_length=50, blank=True)
    recipient = models.CharField('Получатель', choices=recipient_choice, max_length=150)
    name = models.CharField('Имя поддержки', max_length=500)
    choice = (
        ('direct', 'Прямая финансовая поддержка'),
        ('loan', 'заемное финансирование')
    )
    condition = models.TextField('Условия', blank=True)
    type = models.CharField('Тип поддержки', choices= choice, max_length=50)
    organisation = models.TextField('кто выдает меру поддержки')
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, verbose_name='Отрасль')
    category = models.CharField('Категория налогоплатильщика', max_length=70, blank=True)
    property_rate = models.TextField('Налоговая ставка на имущество', blank=True)
    profit = models.TextField('Налог на прибыль', blank=True)
    transport = models.TextField('Налоговая ставка по транспортному налогу', blank=True)
    land = models.TextField('Налоговая ставка по земельному налогу', blank=True)
    nds = models.TextField('Налоговая ставка НДС', blank=True)
    expenses = models.TextField('Затраты подлежащие возмещению', blank=True)

    class Meta:
        verbose_name = 'Мера поддержки'
        verbose_name_plural = 'Меры поддержки'

    def __str__(self):
        return  self.name