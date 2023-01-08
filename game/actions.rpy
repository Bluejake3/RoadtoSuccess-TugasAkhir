label bekerja:
    show screen infoUpdate
    scene bedroom with Dissolve(0.3)
    menu:
        "Apa yang akan kamu kerjakan pada minggu ini?"
        "Jasa joki game online":
            scene cafe with Dissolve(0.3)
            $ stress += (1 + usahaStressModifier)
            $ money += 100
            "Kamu membuka jasa joki game online untuk seminggu"

        "Jual makanan ringan":
            scene city with Dissolve(0.3)
            $ stress += (4 + usahaStressModifier)
            $ money += 300
            "Kamu berjualan makanan ringan selama seminggu"

        "Ambil proyek" if turnsCounter >=18:
            scene office with Dissolve(0.3)
            $ stress += (9 + usahaStressModifier)
            $ money += 750
            "Kamu mengambil sebuah proyek yang kamu selesaikan dalam seminggu"

        "Kembali":
            jump showKegiatan

    jump endCheck

label rekreasi:
    scene bedroom with Dissolve(0.3)
    show screen infoUpdate

    menu:
        "Mau rekreasi yang seperti apa?"
        "Main di rumah saja":
            if(isIntrovert):
                $ stress -= 20
            else:
                $ stress -= 15
            $ money -= 500
            "Kamu bermain sendiri di kos"
        "Nongkrong bersama teman-teman":
            scene cafe with Dissolve(0.3)
            if(isIntrovert):
                $ stress -=15
            else:
                $ stress -= 25
            $ money -= 1000
            if (stress<0):
                $ stress = 0
            "Kamu bercengkrama dengan temanmu dan membeli beberapa kopi"
        "Pergi ke Mall" if turnsCounter >= 34:
            scene mall with Dissolve(0.3)
            $ stress -= 80
            $ money -= 5000
            if (stress<0):
                $ stress = 0
            "Kamu pergi ke mall untuk melepas penat"
        "Kembali":
            jump showKegiatan
    
    jump endCheck

label menabung:
    show screen infoUpdate
    scene bank with Dissolve(0.3)
   
    menu:
        teller "Selamat datang di bank, ada yang bisa kami bantu"
        "Tarik Tunai":
            python:
                try:
                    saving = int(renpy.input("Berapa uang yang ingin kamu ambil?", length=10))
                except ValueError:
                    saving = 0

            
            if (saving>saldo):
                teller "Mohon maaf, saldo anda kurang"
            else:
                play sound "audio/kaching.mp3"
                $ saldo -= saving
                $ money += saving
                teller "Penarikan sejumlah [saving] berhasil. Saldomu sekarang [saldo]"
        "Setor Tunai":
            python:
                try:
                    saving = int(renpy.input("Berapa uang yang ingin kamu setor?", length=10))
                except ValueError:
                    saving = 0

            if (saving>money):
                teller "Mohon maaf, uang anda kurang"
            else:
                play sound "audio/kaching.mp3"
                $ saldo += saving
                $ money -= saving
                teller "Setoran sejumlah [saving] berhasil"
        "Kembali":
            "Terima kasih"

    jump showKegiatan

label usaha:
    show screen infoUpdate
    scene office with Dissolve(0.3)
    python:
        try: 
            capital = int(renpy.input("Kamu mau mengembangkan usaha dengan modal berapa?", length=10))
        except ValueError:
            capital = 0
    

    if (capital <= money):
        $ totalCapital += capital
        $ money -= capital
        $ levelUsaha = totalCapital // 1000
        $ levelUsahaEXP = (totalCapital % 1000) / 10   
        $ levelUsahaTotal = levelUsahaModifier + levelUsaha
        $ profitMultiplier = (10+(levelUsahaTotal*0.5))/4
        $ profit = math.floor(totalCapital * profitMultiplier/100)
        $ usahaStressModifier = totalCapital // 5000
        
        "Kamu memasukkan modal sejumlah [capital], jumlah keuntunganmu setiap minggu akan bertambah menjadi [profit]"

    else:
        "Maaf, uangmu kurang untuk memasukkan modal sebanyak [capital]"
    
    jump showKegiatan

label belajar:
    show screen infoUpdate
    scene bedroom with Dissolve(0.3)
    menu:
        "Kamu mau belajar seperti apa?"
        "Belajar sendiri":
            if (isIntrovert):
                $ nilaiSemester += 7
                $ stress += (4 + stressModifier + usahaStressModifier)
            else:
                $ nilaiSemester += 6
                $ stress += (5 + stressModifier + usahaStressModifier)
            if (nilaiSemester >100):
                $ nilaiSemester = 100  
            "Kamu memilih untuk belajar sendiri"
        "Belajar bersama teman":
            if (isIntrovert):
                $ nilaiSemester += 6
                $ stress += (5 + stressModifier + usahaStressModifier)
            else:
                $ nilaiSemester += 7
                $ stress += (4 + stressModifier + usahaStressModifier)
            if (nilaiSemester >100):
                $ nilaiSemester = 100
            "Kamu memilih untuk belajar bersama teman"
        "Riset Mandiri" if risetMandiri:
            $ nilaiSemester += 10
            $ stress += (7 + stressModifier + usahaStressModifier)
            if (nilaiSemester >100):
                $ nilaiSemester = 100  
            "Kamu memilih untuk melakukan riset"
        "Kembali":
            jump showKegiatan
 
    jump endCheck

