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
        if(turnsCounter <= 136 and getScholarship):
            jump lanjutKuliah
        elif (levelUsaha >=30):
            if (levelRelasi >=25):
                jump bukaStartup
            else:
                jump pengusahaKecil
        elif (turnsCounter <= 136 and (not isEverGotCBelow)):
            jump cumLaude
        else:
            jump Lulus
    elif(turnsCounter >= 238 or (turnsCounter==34 and nilaiSKS <18)):
        jump gagal
    jump routinesMenu
