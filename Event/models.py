from django.db import models

class Organisation(models.Model):
    name = models.CharField('Название организации', max_length=5000)
    description = models.TextField('Описание компании')
    logo = models.ImageField('Логотип компании', upload_to = 'Company/logo', height_field=None, width_field=None, null=True)
    site = models.URLField('Сайт компании')
    
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField('Название победителя', max_length=500 , )
    video = models.URLField('Видео')

    class Meta:
        verbose_name = 'Поздравление'
        verbose_name_plural = 'Поздравления'

    def __str__(self):
        return self.name    

class Event(models.Model):
    title = models.CharField('Название События', max_length=800, null=True)
    description = models.TextField('Описание', null=True)
    translation = models.URLField('Трансляция', null=True)
    date = models.DateTimeField('Дата и время проведения', null=True)
    partner = models.ManyToManyField(Organisation, verbose_name='Учаcтники')
    draft = models.BooleanField('добавить в архив', null= True, blank=True)
    video = models.ManyToManyField(Video, blank=True, null=True, verbose_name='Призеры')
    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
    
    def __str__(self):
        return self.title


class Winners(models.Model):
    company = models.ManyToManyField(Organisation, verbose_name='Победитель')
    reward = models.TextField('Награждение')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Событие', null=True)
    
    class Meta:
        verbose_name = 'Призер'
        verbose_name_plural = 'Призеры'
    
    def __str__(self):
        return self.event.title
