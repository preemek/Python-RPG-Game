#Dm1tro07

import random as r

hp=0
coins=0
damage=0
class Game:
     
    def printParametrs():
    print ("U ciebie {0} HP, {1} coins i {2}damage.".format(hp,coins,damage))

    def printHP():
    print("U ciebie", HP, "HP.")
    def printDamage():
    print("U ciebie", damage, "damage.")
    def printCoins():
    print("U ciebie", coins, "dollars.")
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
        Shop()
    
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
class sklep:
    def Shop():
    global hp
    global coins
    global damage
    def buy (dollars):
    global coins
    if coins >=dollars:
        dollars -= dollars
        return True
    else:
        print("U ciebie braknie dollars!")
        return False
    
weaponLVL = r.randint(1,3)
weaponDamage=r.randint(1,5)
weapons= ["AK-47","Iron Sword","Showel"]
weapondollars=r.randint(2,10)
weapon=r.choice(weapons)
OneHpDollars= 3
ThreeHpDollars=6
SixHpDollars=12
print("You met a merchant on the way ")
printParametrs()
while input("What will you do,(come in/come out?)").lower()== "come in":
    print("1) One unit of health", OneHpDollars ,"dollars")
    print("2) Two unit of health", TwoHpDollars ,"dollars")
    print("3) {0} {1} - {2} dollars".format(weaponRarity,weapon,weapondollars))

    Choice = input(" Co chcesz cupić:")
    if Choice == "1":
        if buy(OneHpDollars):
            HP +=1
            printHP()
    elif choice == "2":
        if buy (ThreeHpDollars):
            HP +=3
            printHP()
    elif choice == "3":
        if buy (weaponDollars):
            damage= weaponDamage
            printDamage()
    else:
        print("Nie spredaję tego")


    
    
  






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
        Shop()
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



