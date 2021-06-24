from django.db import models
from parler.models import TranslatableModelMixin, TranslatedFields, TranslatableModel
from example_api.models import Region, PrivateForm



# Create your models here.
# class Territory(TranslatableModel):
#     region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Район', null=True)
#     number_territory = models.CharField('Номер участка', max_length=100, default='')
#     number = models.CharField('Кадастровый номер', max_length=50, default=0)
#     image = models.ImageField(upload_to='greenfield', height_field=None, width_field=None, null=True,
#                               verbose_name='Фотография участка')

#     form = models.ManyToManyField(PrivateForm, verbose_name="Форма сделки")
#     translations = TranslatedFields(
#     description = models.TextField('Описание участка', blank=True, null=True),
#     territory = models.CharField('Территория участка', choices=greenfield_choice, max_length=50, null=True),
#     type = models.CharField('Тип участка', choices=choice_type, max_length=20, default=0),
#     square = models.CharField('Площадь(га)', max_length=10, default=''),
#     power = models.CharField('Электроснабжение', max_length=500, blank=True, null=True),
#     water = models.CharField('Водоснабжение', max_length=500, blank=True, null=True),
#     gas = models.CharField('Газоснабжение', max_length=500, blank=True, null=True),
#     heat = models.CharField('Теплоснабжение', max_length=500, blank=True, null=True),
#     water_out = models.CharField('Водоотведение', max_length=500, blank=True, null=True),
#     danger = models.CharField('Класс опасности', max_length=500, choices=danger_choices, default='1'),
#     category = models.CharField('Категория замель', max_length=50, choices=category_choices, default='0'),
#     desired = models.CharField('Форма собственности', max_length=50, choices=desired_choices, null=True),
#     customs_priveleges = models.CharField('Таможенные льготы', max_length=100, default='', blank=True, null=True),
#     territory_priveleges = models.CharField('Льготная стоимость земли', max_length=100, default='', null=True,
#                                             blank=True),
#     nalog = models.TextField('Налоговые льготы', blank=True, null=True)
#     )
#     class Meta:
#         verbose_name = 'Земельный участок'
#         verbose_name_plural = 'Земельные участки'

#     def __str__(self):
#         return self.number_territory