class enemy:
  def enemy:

    global HP 
    global dollars 
    enemyLvl = r.randit(2,3)
    enemyHP = enemyLvl
    enemyDamage = enemyLvl
    monstersName = ["Groow","Madrock"]
    monster = r.choice(monsters)
    print("Ty znalazłeś potwore - (0) u niego (1) lvl,(2) HP (3)Damage.".format(enemy,enemyLvl,enemyDamage)
    printparametrs()

    while enemyHp >0
    choice = input("")

    if choice =="Fight":
        enemyHP -=Damege
        print("zaatakowałeś potwore i został z nim",enemyHp,"życie")

    elif choice == "biegać"
    
    chance=r.randit(0,enemyLvl)
    if chance ==0:
        print("udało ci się uciec z pola bitwy!")
        break
     else:
      
        print("enemy okazał się bardzo silny!")
      else:
        continue
      if enemyhp>0:
        hp=-enemyDamage
        print("")
      if hp<0:
        break
  
  def initGame(initHp,InitDollars,initDmg):
    global help
    global dollars
    global enemyDamage

    hp=initHp
    dollars=initdollars
    dmg=initdmg


    .......
