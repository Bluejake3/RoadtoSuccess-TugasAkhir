# The script of the game goes in this file.
init python:
    import math
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kamu = Character("[nama]")
define senior = Character("Kakak Tingkat")
define teller = Character("Teller Bank")
define bandar = Character("Bandar Narkoba")
define agent = Character("Agen Anti-narkotika")
define hp = Character("Pesan di HP")

# The game starts here.

label start:
    $ SKSAmbil = 18
    $ isIntrovert = 0
    $ turnsCounter = 0
    $ stress = 0
    $ money = 300
    $ nilaiSemester = 0
    $ risetMandiri = 0
    $ nilaiSKS = 0
    $ saving = 0
    $ saldo = 0
    $ salary = 100
    $ stressModifier = 0
    $ usahaStressModifier = 0
    $ nilaiModifier = 0
    $ totalCapital = 0
    $ profit = 0
    $ pakaiNarkoba = 0
    $ getScholarship = 0
    $ levelUsaha = 1
    $ levelUsahaModifier = 0
    $ levelUsahaEXP = 0
    $ levelUsahaTotal = 0
    $ kaderisasi = 0
    $ mingguKader = [22, 26, 30, 35, 39, 43, 47]
    $ masukOrganisasi = 0
    $ panitiaAcara = 0
    $ persiapanAcaraOrganisasi = [78, 80, 82, 84, 86]
    $ levelRelasi = 0
    scene city with fade
    play music "audio/song1.mp3"

    "Setelah mencari pekerjaan, akhirnya kamu mendapat sebuah pekerjaan yang kamu impikan"

    "Dengan dukungan dari orang tua, kamu menatap kehidupan baru yang lebih berat dari kehidupan kuliah"

    python:
        nama = renpy.input("Omong-omong, siapa namamu?", length=32)
        nama = nama.strip()

        if not nama:
            nama ="Yohan Luis Sukma"

    kamu "Namaku [nama]!"
    menu:
        "Apakah kau membutuhkan tutorial cara bermain?"
        "Ya":
            "Setiap hari, kamu akan diberikan 4 opsi kegiatan"
            "Opsi pertama adalah belajar. Opsi ini akan menambah nilaimu, tetapi akan menambah stress"
            "Opsi bekerja berfungsi untuk menambah uang selain dari uang yang didapatkan tiap giliran. Opsi ini akan menambah stres"
            "Opsi berikutnya adalah opsi menabung. Di sini kamu dapat menginvestasikan uangmu dan menerima bunga dari bank"
            "Opsi terakhir adalah Pergi Rekreasi. Opsi ini mengurangi banyak stres dengan menggunakan sejumlah uang"
            "Nilai yang kamu dapatkan pada semester ini akan berpengaruh pada total nilai yang kamu dapat di game"
            "Pertimbangkan uang, stress, dan nilai dalam memilih opsi yang ada"
        "Tidak":
            "Baik, karena kamu sudah paham, ke pertanyaan selanjutnya ya"

    menu:
        "Sebelum itu, kamu termasuk orang yang ...."
        "Introvert":
            "Kamu memilih untuk menjadi Introvert, Kamu merasa lebih nyaman jika kamu sendiri"
            $ isIntrovert = 1
        "Extrovert":
            "Kamu memilih untuk menjadi Extrovert, Kamu merasa lebih nyaman jika kamu bersama orang lain"
            $ isIntrovert = 0

    "Oke, mari kita mulai"
    jump routinesMenu

label routinesMenu:
    $ turnsCounter += 1
    $ Semester = (turnsCounter // 17) + 1
    $ week = turnsCounter % 17
    $ money += (salary + profit)
    $ saldo += math.floor(saldo * 0.001)

    scene bedroom with dissolve

    if (not (turnsCounter % 17)):
        jump evaluasi
    elif (turnsCounter == 14):
        jump pelatihanKewirausahaan
    elif (turnsCounter == 18):
        jump pembukaanKader
    elif (kaderisasi >= 1 and (turnsCounter in mingguKader)):
        jump kader
    elif (turnsCounter == 35):
        jump unlockKeMall
    elif (turnsCounter == 37):
        jump penggunaNarkoba
    elif (turnsCounter == 45 and pakaiNarkoba):
        jump jadiBandarNarkoba
    elif (turnsCounter == 52 and kaderisasi >= 1):
        jump pengangkatan
    elif (turnsCounter == 64 and pakaiNarkoba):
        jump bertemuPolisi
    elif (turnsCounter == 67 and kaderisasi):
        jump daftarOrganisasi
    elif(turnsCounter == 69):
        jump studiMandiri
    elif(turnsCounter == 73 and masukOrganisasi):
        jump diterimaOrganisasi
    elif (turnsCounter == 76):
        if(pakaiNarkoba):
            jump overdosis
        else:
            jump acaraOrganisasi
    elif((turnsCounter in persiapanAcaraOrganisasi) and panitiaAcara):
        jump persiapanAcara
    elif(turnsCounter == 88):
        if (panitiaAcara):
            jump acaraBesar
        else:
            jump nontonAcaraBesar
    elif(turnsCounter == 95 and capital):
        jump pameranUsaha
    
    jump showKegiatan

label unlockKeMall:
    scene bedroom with dissolve
    "Kamu membuka opsi rekreasi 'Pergi ke Mall'"
    jump showKegiatan
        
