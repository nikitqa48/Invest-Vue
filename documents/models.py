from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=5000)
    text = models.TextField('Описание раздела', null=True, default='', blank=False)
    slug = models.SlugField(max_length=250, null=True)
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Раздел'
    
    def __str__(self):
        return self.name

class SubSection(models.Model):
    name = models.CharField('Название', max_length=5000)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Раздел')
    text = models.TextField('Текст', default='')
    class Meta:
        verbose_name = 'Подраздел'
        verbose_name_plural = 'Подразделы'
    
    def __str__(self):
        return self.name

class File(models.Model):
    name = models.TextField('Имя файла')
    subsection = models.ForeignKey(SubSection, verbose_name='Подраздел', on_delete=models.CASCADE)
    file = models.FileField(upload_to='Documents', null=True, max_length=100000000)
    
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.name

