# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

words = {  'один': 1,
           'два': 2,
           'три': 3,
           'четыре': 4,
           'пять': 5,
           'шесть': 6,
           'семь': 7,
           'восемь': 8,
           'девять': 9
            }

def switch_it_up(number):
    try:
        for i in range(1,10):
            words_keys = list(words.keys())
            words_values = list(words.values())
            val_index = words_values.index(number)
            write_num = words_keys[val_index]
        print(number, "-->", write_num)
    except ValueError:
            print(number, "-->", None)

switch_it_up(9)



