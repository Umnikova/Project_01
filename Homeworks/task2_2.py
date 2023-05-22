monthes = {
    'Январь': 1,
    'Февраль': 2,
    'Март': 3,
    'Апрель': 4,
    'Май': 5,
    'Июнь': 6,
    'Июль': 7,
    'Август': 8,
    'Сентябрь': 9,
    'Октябрь': 10,
    'Ноябрь': 11,
    'Декабрь': 12}

quarters = {
    'Первый_квартал': [1, 2, 3],
    'Второй_квартал': [4, 5, 6],
    'Третий_квартал': [7, 8, 9],
    'Четвертый_квартал': [10, 11, 12]
}

def quarter_of(month):
    for k, v in quarters.items():
        for a, b in monthes.items():
            if b == month:
                if (isinstance(v, list) and month in v) or month == v:
                    print(f'Месяц {month} ({a}) является частью "{k}"')
                break
    else:
        print(f'Нет такого месяца {month}')

quarter_of(78)













































