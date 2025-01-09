class game:
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