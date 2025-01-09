class monster:
def monster()
    global HP 
    global dollars 
    monsterLvl = r.randit(2,3)
    monsterHP = monsterLvl
    monsterDamage = monsterLvl
    monstersName = ["Groow","Madrock"]
    monster = r.choice(monsters)
    print("Ty znalazłeś potwore - (0) u niego (1) lvl,(2) HP (3)Damage.".format(monster,monsterLvl,monsterDamage))
    printparametrs()

    while monsterHp >0
    choice = input("")

    if choice =="Fight":
        monsterHP -=Damege
        print("")
    elif choice == ""
    .......
