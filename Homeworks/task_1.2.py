my_favorite_songs = [['Waste a Moment', 3.03], ['New Salvation', 4.02], ['Staying\' Alive', 3.40], ['Out of Touch', 3.03], ['A Sorta Fairytale', 5.28], ['Easy', 4.15], ['Beautiful Day', 4.04], ['Nowhere to Run', 2.58], ['In This World', 4.02] ]
import random
#print(len(my_favorite_songs))
#print(random.choice(arr)*3)
time_song = (my_favorite_songs [0][1], my_favorite_songs [1][1], my_favorite_songs [2][1], my_favorite_songs [3][1],my_favorite_songs [4][1],my_favorite_songs [5][1],my_favorite_songs [6][1],my_favorite_songs [7][1], my_favorite_songs [8][1])
#print(time_song)
a = random.choice(time_song)
b = random.choice(time_song)
c = random.choice(time_song)
d = a + b + c
from datetime import datetime, date, time
def float_to_datetime(myfloat):
  minutes, seconds = str(myfloat).split('.')
  return datetime.combine(date.today(), time(0, int(minutes), int(seconds)))
d =float_to_datetime(d)
#print(a, b, c)
print("Три песни звучат", d, "минут")