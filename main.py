#Wiktor
from Classes import *
import json
from tkinter import *
import random



# class rpg_game:
#     Player1 = create_player()

player1 = create_player(mode="from_save_file",file_number=1)

print(player1.name)
# save_player_data(player1,1)


"""
random.choices(mylist, weights = [10, 1, 1], k = 14)
weights - szansa na wylosowanie tej rzeczy
k - ile wartości jest zwróconych

do zrobienia funkcja do wyświetlania tekstu (taki print ale w tkinter)

git checkout -b Wiktor

git add .

git commit -m "komunikat "

git push


git status

"""