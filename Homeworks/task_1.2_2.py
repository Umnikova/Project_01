my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

time_value_list = list(my_favorite_songs_dict.values()) 
print(time_value_list)
from random import sample
total_time = sample(time_value_list, 3)
summa = str(sum(total_time))
print(type(summa))
print(summa)

from datetime import datetime
total = datetime.strptime(summa, "%M.%S")
print(type(total)) 
print("Три песни звучат:", total.time(), "минут")



 
 












