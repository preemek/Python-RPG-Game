class shop:
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
    elif Choice == "2":
        if buy (ThreeHpDollars):
            HP +=3
            printHP()
    elif Choice == "3":
        if buy (weaponDollars):
            damage= weaponDamage
            printDamage()
    else:
        print("Nie spredaję tego")
