#Wiktor
from Player import *
import json
from tkinter import *
import random



# class rpg_game:
#     Player1 = create_player()
player1 = Player()
player1.create_player(mode="new_player",file_number=2)

print(player1.name)
player1.save_player_data(2)






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