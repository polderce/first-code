day=int(input('Введите сегодняшний день:' ))
month=str(input('Введите сегодняшний месяц: '))
if month=='Декабрь':
    month=='Декабря'
elif month=='Январь':
    month=='Января'
elif month=='Февраль':
    month=='Февраля'
elif month=='Март':
    month=='Марта'
elif month=='Апрель':
    month=='Апреля'
elif month=='Май':
    month=='Мая'
elif month=='Июнь':
    month=='Июня'
elif month=='Июль':
    month=='Июля'
elif month=='Август':
    month=='Августа'
elif month=='Сентябрь':
    month=='Сентября'
elif month=='Октябрь':
    month=='Октября'
elif month=='Ноябрь':
    month=='Ноября'
print('Сегодня', day, month)