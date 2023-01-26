label lulus:
    scene conference with Dissolve(0.3)
    hide screen info_Update

    "Kamu telah menyelesaikan studimu di kampus ini"
    "Kamu menunggu namamu dipanggil ke atas panggung"
    if (not isEverGotCBelow and turnsCounter <= 136):
        announcer "[nama], Lulus dengan status cum laude"
    else:
        announcer "[nama], Lulus"
    "Kamu naik ke atas panggung"
    show professor with Dissolve(0.3)
    rektor "Selamat ya nak"
    kamu "Terima kasih pak"
    hide professor with Dissolve(0.3)
    "Kamu lega bahwa studimu telah selesai dan berharap agar ilmu yang kamu dapatkan bermanfaat"

    if(getScholarship and turnsCounter <= 136):
        scene airport with Dissolve(0.3)
        "Beberapa hari setelah wisuda, kamu langsung berangkat ke luar negeri untuk melanjutkan kuliah"
        "Kamu sudah meninggalkan pesan untuk keluarga dan teman-temanmu dan meminta mereka untuk mendoakanmu"
        "Ending 3 - 'Lanjut kuliah' tercapai"
        return
    
    else if (levelUsaha >=30):
        if (levelRelasi >=25):
            scene cooperation with Dissolve(0.3)

            "Kamu dan teman-temanmu ingin membuka lapangan pekerjaan baru sesuai dengan keahlian yang dimiliki"
            "Kamu dan temanmu sepakat bahwa kalian akan membuat startup baru"
            "Dengan modal yang sudah kamu kumpulkan, kamu membantu menanam modal di perusahaan barumu"
            "Ending 11 - 'Buka Startup' Tercapai"

        else:
            scene enterpreneur with Dissolve(0.3)

            "Kamu ingin membuka usaha baru dengan keahlian yang kamu miliki"
            "Modal yang kamu kumpulkan selama kuliah juga sudah mencukupi untuk membuat usaha baru"
            "Walaupun begitu, kamu masih harus mencari orang untuk mengisi posisi penting di usaha kecilmu"
            "Ending 12- 'Usaha Kecil' Tercapai"

    else:
        if (not isEverGotCBelow):
            "Ending 1 - 'Lulus dengan sempurna' tercapai"
        else:
            "Ending 2 - 'Lulus Kuliah' tercapai"

    return 

label gagal:
    scene messy with Dissolve(0.3)
    hide screen info_Update

    "Kamu gagal mencapai target yang ditentukan oleh kampusmu"
    "Akibatnya, kamu terkena evaluasi oleh kampus"
    "Ending 4 - 'Terkena Evaluasi' tercapai"

    return

label miskin:
    scene homeless with Dissolve(0.3)
    hide screen info_Update

    "Kamu menggunakan seluruh uangmu hingga suatu hari kau menyadari bahwa uangmu sudah habis"
    "Kamu menjual semua yang kamu punya untuk memuaskan nafsumu"
    "Suatu hari, kau didatangi oleh penagih hutang. Kamu tidak memiliki uang sekarang"
    "Penagih utang itu menyita barangmu untuk menutupi hutang yang kamu miliki"

    "Ending 5 -'Bangkrut' tercapai"

    return

label gila:
    scene street with Dissolve(0.3)
    hide screen info_Update

    "Kamu tidak dapat menahan beratnya tekanan dalam kuliah"
    "Kamu mulai berteriak dengan kencang dan melempar barang-barang yang ada di sekitarmu"
    "Orang-orang yang berada di sekitarmu mulai memanggil polisi"
    "Tiga puluh menit kemudian, orang-orang dari rumah sakit jiwa datang dan menyeretmu ke ambulans"

    "Ending 6 - 'Sakit Jiwa' tercapai"
    return

label penjara:
    scene jail with Dissolve(0.3)
    hide screen info_Update

    "Kamu dibawa ke pengadilan atas tuntutan pengedaran obat terlarang"
    "Semua bukti mengarah kepadamu dan kamu tidak dapat membantah bukti yang diberikan"
    "Pada akhirnya, hakim memutuskan bahwa kamu bersalah dan memberi hukuman maksimal"
    "Ending 7 - 'Masuk Penjara' tecapai"

    return

label rehabilitasi:
    scene rehab with Dissolve(0.3)
    hide screen info_Update

    "Kamu dibawa ke pengadilan atas tuntutan penggunaan obat terlarang"
    "Semua bukti mengarah kepadamu dan kamu tidak dapat membantah bukti yang diberikan"
    "Hakim memberimu pilihan untuk melakukan rehabilitasi dan kamu menerimanya"
    "Ending 8 - 'Rehabilitasi' tecapai"

    return

label overdosis:
    scene grave with Dissolve(0.3)
    hide screen info_Update

    "Kamu terus memakai narkoba karena kamu merasa butuh untuk memakai narkoba"
    "Hingga suatu hari, tiba-tiba kamu jatuh tidak sadarkan diri di dekat tempat tinggalmu"
    "Orang yang ada di dekatmu memanggil ambulans"
    "Tetapi sayang nyawamu tidak dapat terselamatkan"

    "Ending 9 - 'Overdosis Narkoba' tercapai"

    return

label mencobaHalBaru:
    
    scene franchise with Dissolve(0.3)
    hide screen info_Update

    "Kamu memutuskan untuk berhenti kuliah"
    "Setelah berhenti kuliah, kamu menggunakan waktumu untuk mencari tahu tentang dunia bisnis"
    "Kamu mempelajari hal baru yang tidak diajarkan selama kamu bekuliah dan mempraktekannya di dunia bisnis"
    "Ending 10 - 'Pengusaha Otodidak' tercapai"

    return
