# Задача 1.3.
# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом
# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!


import calendar 
from calendar import monthrange
from datetime import datetime
import locale

locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"
)
num = int(input(" Введите номер месяца: "))
if num > 12:
    print("Такого месяца нет!")
else:
   
    current_year = datetime.now().year
    days = monthrange(current_year, num)[1]
    res = calendar.month_name[num]
    print("Вы ввели", str(res), days, "дней" )










