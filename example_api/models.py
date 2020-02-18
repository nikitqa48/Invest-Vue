from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

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
    created = models.DateTimeField("Создан",auto_now_add=True)
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