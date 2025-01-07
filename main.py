#Dm1tro07

import random as r

hp=0
coins=0
damage=0

def printParametrs():
    print ("U ciebie {0} HP, {1} coins i {2}damage.".format(hp,coins,damage))

def printHP():
    print("U ciebie", HP, "HP.")
def printDamage():
    print("U ciebie", damage, "damage.")
    def printCoins():
    print("U ciebie", coins, "dollars.")

def meetShop():
    global hp
    global coins
    global damage
def buy (dollars):
    global coins
    if coins >=dollars:
        dollars -= dollars
        return True
    print("U ciebie braknie dollars!")
    return False
weaponLVL = r.randint(1,3)
weaponDamage=r.randint(1,5)
weapons= ["AK-47","Iron Sword","Showel"]
weapondollars=r.randint(2,10)
weapon=r.choice(weapons):
OneHpDollars= 3
ThreeHpDollars=6
SixHpDollars=12
print("")





def initGame(initHP,initCoins,initDamage):
    global hp
    global coins
    global damage
    hp=initHP
    coins=initCoins
    damage=initDamage
    print("Wyruszyłeś na prygodę.Dobrych przygod!")
    printParametrs()

def gameLoop():
    situation= r.randint(0,10)
    if situation == 0:
        input("Shop")
    elif situation == 1:
        input("monster")
    else:
        input("Wandering...")

initGame (3,5,1)
while True:
    gameLoop()
    if hp <=0:
        if input ("Want to start again(Yes/No):").lower() =="Yes":
            initGame(3,5,1)
    else:
        break 



