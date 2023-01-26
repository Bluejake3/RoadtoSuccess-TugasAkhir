label endCheck:

    if(money < 0):
        if (saving > 0):
            call takeSavings
        elif (totalCapital > 0):
            call takeCapitals
        else:
            jump miskin
    elif (stress >= 100):
        jump gila 
    elif (nilaiSKS >= 144):
        jump lulus
    elif(turnsCounter >= 238 or (turnsCounter==34 and nilaiSKS <18)):
        jump gagal
    jump routinesMenu
