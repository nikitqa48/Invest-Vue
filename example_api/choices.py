choice_type = (
    ('greenfield', 'Гринфилд'),
    ('brownfield', 'Браунфилд')
)
private_choice = (
    ('goverment', 'государственная'),
    ('private', 'частная')
)
recipient_choice = (
    ('small', 'МСП'),
    ('innovation', "Инновации"),
    ('all', 'Все'),
    ('municipality', 'муниципалитет'),
    ('industrial', 'Резиденты индустриальных парков'),
    ('developers', 'Разработчики ПО'),
    ('resident_oez', 'Резиденты ОЭЗРУ Липецк'),
    ('subject', 'Субъект'),
    ('legally', 'Юридические лица'),
    ('cooperatives', 'Кооперативы'),
    ('not_msp', 'Все кроме МСП')
)
territory_choice = (
    ('without', 'Без ограничений'),
    ('park', 'индустриальные парки'),
    ('mono', 'моногород'),
    ('techno', 'технопарк'),
    ('oez', 'ОЭЗ ппт '),
    ('oezru', 'ОЭЗРУ'),
    ('cluster', 'Участник кластера'),
    ('all', 'Любая')
)
choice = (
    ('direct', 'Инвестиции'),
    ('loan_funding', 'Заемное финансирование'),
    ('loan', 'Налоговые льготы по налогу на займ'),
    ('subsidies', 'субсидии'),
    ('profit', 'Налоговые льготы по налогу на прибыль'),
    ('property', 'Налоговые льготы по налогу на имущество'),
    ('grant', 'Гранты'),
    ('rent', 'льготы по аренде'),
    ('garant', 'гарантии'),
    ('transport', 'Налоговые льготы по транспортному налогу'),
    ('earth', 'налоговые льготы по земельному налогу'),
    ('nds', 'налоговые льготы по уплате НДС'),
    ('customs', 'таможенные льготы'),
    ('infrastructure', 'Субсидии на инфраструктуру'),
    ('loan_profit', 'кредиты под залог создаваемого имущества'),
)
form_choice = (
    ('lawyer', 'Юр.лицо'),
    ('ip', 'ИП'),
    ('municipality', 'Муниципалитет')
)
implementation_choice = (
    ('agreement', 'Соглашение'),
    ('gchp', 'ГЧП'),
    ('any', 'Любой')
)
type_project_choices = (
    ('new', 'Новое строительство'),
    ('reconstuction', 'Реконструкция'),
    ('modernisation', 'Модернизация'),
    ('all', 'любой')
)
authority_choices = (
    ('uilo', 'УИиИ ЛО'),
    ('min', 'Минпромторг России'),
    ('bank', 'Уполномоченные банки'),
    ('fond', 'Фонд содействия инновациям'),
    ('rvk', 'АО "РВК"'),
    ('business', 'Центры "мой бизнес", Управляющие компании')
)
danger_choices = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)
category_choices = (
    ('0', 'Земли сельского назначения'),
    ('1', 'Земли  населенных пунктов'),
    ('2', 'Земли для промышленности'),
    ('3', 'Земли для энергетики'),
    ('4', 'Земли для транспорта'),
    ('5', 'Земли для связи'),
    ('6', 'Земли для радиовещания'),
    ('7', 'Земли для телевидения'),
    ('8', 'Земли для информатики'),
    ('9', 'Земли для обеспечения космической деятельности'),
    ('10', 'Земли для обороны'),
    ('11', 'Земли для безопасности и иного специального назначения'),
    ('12', 'Земли особо охраняемых территорий и объектов'),
    ('13', 'Земли лесного фонда'),
    ('14', 'Земли водного фонда')
)
desired_choices = (
    ('arend', 'Аренда'),
    ('buy', 'Выкуп')
)
greenfield_choice = (
    ('oez', 'ОЭЗ ППТ'),
    ('oezru', 'ОЭЗ Ру'),
    ('industrial', 'Индустриальный парк'),
    ('any', 'Иная площадка')
)
