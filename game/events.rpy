label takeSavings:
    $ money += saving
    scene bank with Dissolve(0.3)
    "Kamu mengambil tabunganmu sejumlah [saving] karena uang yang kamu bawa telah habis" 
    $ saving = 0
    return

label takeCapitals:
    $ money += totalCapital
    scene bank with Dissolve(0.3)
    "Kamu mengambil uang modalmu sejumlah [totalCapital] karena uang yang kamu bawa dan uang di tanbunganmu telah habis" 
    $ totalCapital = 0
    return

label evaluasi:
    if (nilaiSemester >= 86):
        $ nilaiSKS += SKSAmbil
        $ SKSAmbil += 4
        $ stressModifier += 2
        if (SKSAmbil + 4 > 24):
            $ SKSAmbil = 24
            $ stressModifier -= 2
        "Kamu mendapat nilai A. Di semester berikutnya, SKSmu akan bertambah 4"
    elif(nilaiSemester >= 76):
        $ nilaiSKS += math.ceil(SKSAmbil * (3.5/4))
        $ SKSAmbil += 2
        $ stressModifier += 1
        if (SKSAmbil > 24):
            $ SKSAmbil = 24
            $ stressModifier -= 1
        "Kamu mendapat nilai AB. Di semester berikutnya, SKSmu akan bertambah 2"
    elif(nilaiSemester >= 66):
        $ nilaiSKS += math.ceil(SKSAmbil * (3/4))
        if (SKSAmbil > 24):
            $ SKSAmbil = 24
        "Kamu mendapat nilai B."
    elif(nilaiSemester >= 61):
        $ nilaiSKS += math.ceil(SKSAmbil * (2.5/4))
        $ SKSAmbil -= 2
        $ stressModifier -= 1
        if (SKSAmbil < 18):
            $ SKSAmbil = 18
            $ stressModifier += 1
        $ isEverGotCBelow =1
        "Kamu mendapat nilai BC. Di semester berikutnya, SKSmu akan berkurang 2"
    elif(nilaiSemester >= 56):
        $ nilaiSKS += math.ceil(SKSAmbil * (2/4))
        $ SKSAmbil -= 4
        $ stressModifier -= 2
        if (SKSAmbil < 18):
            $ SKSAmbil = 18
            $ stressModifier += 2
        $ isEverGotCBelow =1
        "Kamu mendapat nilai C. Di semester berikutnya, SKSmu akan berkurang 4"
    elif(nilaiSemester >= 41):
        $ nilaiSKS += math.ceil(SKSAmbil * (1/4))
        $ SKSAmbil -= 6
        $ stressModifier -= 3
        if (SKSAmbil < 18):
            $ SKSAmbil = 18
            $ stressModifier += 3
        $ isEverGotCBelow =1
        "Kamu mendapat nilai D. Di semester berikutnya, SKSmu akan berkurang 6"
    else:
        $ SKSAmbil -= 6
        $ stressModifier -= 3
        if (SKSAmbil < 18):
            $ SKSAmbil = 18
            $ stressModifier += 3
        
        $ isEverGotCBelow =1
        "Kamu mendapat nilai E. Di semester berikutnya, SKSmu akan berkurang 6"

    $ nilaiSemester = 0
    $ stress = 0
    jump endCheck

label pelatihanKewirausahaan:
    scene conference with Dissolve(0.3)
    "Kamu melihat sebuah acara tentang kewirausahaan"

    "Kamu tertarik untuk mengikuti acara itu, tetapi kamu takut acara itu mengganggu waktu istirahatmu"

    menu:
        "Apa yang akan kamu lakukan"

        "Tetap mengikuti acara itu":
            $ levelUsahaModifier += 2
            $ levelUsahaTotal = levelUsaha + levelUsahaModifier

            if(isIntrovert):
                $ stress += 6
            else:
                $ stress += 5
            "Kamu memutuskan untuk mengikuti acara itu"

            "Setelah acara, kamu merasa lelah. Tetapi, kamu merasa mendapat ilmu untuk membuka usaha"

            "Level Usahamu meningkat"
        
        "Lewati acara itu":
            "Kamu memutuskan untuk melewati acara itu"

    jump showKegiatan

label pembukaanKader:
    scene field with Dissolve(0.3)
    show senior with Dissolve(0.3)

    senior "Selamat datang di pembukaan kaderisasi departemen"
    senior "Dalam acara kaderisasi ini, kalian akan belajar tentang norma-norma yang berlaku di departemen ini"
    senior "Kami tidak memaksa kalian untuk ikut dalam acara kaderisasi ini"
    senior "Tetapi, acara ini menjadi syarat untuk menjadi pengurus himpunan departemen ini"
    senior "Tenang saja, kami disini sebagai teman kalian. Jika ada dari kakak-kakak senior yang melakukan bullying terhadap kalian, mereka akan merasakan akibatnya"

    menu:
        senior "Jadi, apakah kalian bersedia ikut kaderisasi?"

        "Ya":
            $ kaderisasi = 1
            "Kamu memutuskan untuk mengikuti kaderisasi"
        "Tidak":
            "Kamu memutuskan untuk tidak mengikuti kaderisasi"

    scene bedroom with Dissolve(0.3)
    "Kamu membuka opsi bekerja 'Ambil Proyek'"

    jump showKegiatan

label kader:
    scene bedroom with Dissolve(0.3)

    "Minggu ini ada acara kaderisasi di departemen."
    menu:
        "Apakah kamu ingin hadir di acara kaderisasi?"

        "Ya":
            $ kaderisasi += 1
            $ stress += 3
            scene classroom with Dissolve(0.3)
            "Kamu memutuskan untuk mengikuti acara kaderisasi"
        "Tidak":
            "Kamu memutuskan untuk tidak mengikuti acara kaderisasi"

    jump showKegiatan

label pengangkatan:
    scene conference with Dissolve(0.3)
    show senior with Dissolve(0.3)
    "Kamu dan teman-temanmu diundang ke sebuah acara penting oleh seniormu"

    senior "Hari ini adalah hari yang spesial bagi kalian semua"
    senior "Kalian sudah bersedia mengikuti seluruh rangkaian acara kaderisasi dari awal sampai selesai"
    senior "Hari ini, kalian akan diangkat menjadi warga himpunan yang akan menerima tongkat estafet kepengurusan himpunan"
    senior "Tetapi, ada beberapa dari kalian yang kami rasa belum pantas untuk diangkat"
    senior "Kalian bisa melihat di daftar yang ada di layar. Jika nama kalian ada di daftar tersebut, kami ucapkan selamat karena kalian telah diangkat."

    if (kaderisasi >= 6):
        "Kamu melihat namamu ada di dalam daftar tersebut"
        "Kamu telah diangkat menjadi anggota himpunan"
        "Dengan ini, kamu dapat mendaftar menjadi pengurus himpunan"
    else:
        "Kamu tidak melihat namamu di dalam daftar tersebut"
        "Kamu tidak berhasil diangkat karena beberapa alasan"
        $ kaderisasi = 0
    
    jump showKegiatan

label studiMandiri:
    scene classroom with Dissolve(0.3)
    "Kamu diundang untuk melakukan studi mandiri dosenmu"
    "Dengan melakukan studi ini, diharapkan kamu dapat memahami materi yang sedang dipelajari semester ini"
    menu:
        "Apakah kamu tertarik untuk mengambil studi ini?"

        "Ya":
            if(isIntrovert):
                $ stress += 10
            else:
                $ stress += 15

            $ nilaiSemester += 20
            $ risetMandiri = 1
            "Kamu melakukan studi independen. Nilaimu bertambah karena studi yang kamu lakukan"
            "Kamu membuka opsi belajar 'Studi Independen'"
        "Tidak":
            "Kamu memutuskan untuk tidak mengikuti studi independen"
    jump showKegiatan

label penggunaNarkoba:
    scene city with Dissolve(0.3)
    show delinquent with Dissolve(0.3)

    bandar "Bro lu kenapa? lagi stress kah?"
    kamu "Iya bro. Banyak tugas nih"
    bandar "Wah kebetulan bro, ini aku ada barang buat nurunin stress"
    kamu "Barang apa bro?"
    "Bandar mengeluarkan sesuatu yang berbentuk seperti serbuk"
    bandar "Narkoboy bro. pakainya gampang, tinggal sedot lewat hidung"
    menu:
        bandar "Jadi gimana? mau nggak? ane kasih dah"

        "Boleh tuh ane coba":
            if (stressModifier <= 3):
                $ stressModifier = 0
            else:
                $ stressModifier -= 3

            bandar "Ini bro barangnya"
            kamu "Makasih bro. kayaknya bakal tenang malam ini"
            $ pakaiNarkoba += 1


        "Nggak ah, nggak mau aneh-aneh":
            bandar "yasudah kalau nggak mau"

    jump showKegiatan

label jadiBandarNarkoba:
    scene city with Dissolve(0.3)
    show delinquent with Dissolve(0.3)

    bandar "Gimana barangnya, enak kan?"
    kamu "Wah enak bro"
    bandar "Dibilangin, kalau gitu mau beli lagi nggak?"
    kamu "Mau sih bro, tapi lagi nggak ada uang nih"
    bandar "Kebetulan nih bro, ane lagi cari distributor baru"
    bandar "Nanti kamu bisa dapet uang hasil jualan narkoboy. Ane ambil sedikit aja kok bro"
    menu:
        bandar "Gimana, mau join nggak bro?"

        "Boleh bro":
            $ pakaiNarkoba +=1
            $ salary += 500
            bandar "wah mantap bro, entar malem barangnya ane kirim ya bro"
            kamu "Siap bro"
        "Nggak dulu bro":
            bandar "Yasudah bro, padahal pasarnya luas loh."
        
    kamu "Aku beli barang biasanya ya bro"
    $ money -= 1000
    bandar "Siap bro"

    jump showKegiatan

label bertemuPolisi:
    scene bedroom with Dissolve(0.3)
    
    "Tok tok tok"
    "Kamu mendengar suara itu dan membuka pintu"

    show detective with Dissolve(0.3)
    agent "Selamat siang"
    kamu "Iya pak, ada apa ya?"
    agent "Kami melacak adanya penggunaan obat terlarang di daerah ini"
    agent "Salah satu bandar yang ada di daerah ini telah kami ringkus dan dia memberi tahu kami bahwa anda merupakan salah satu pengguna"

    menu:
        agent "Sekarang, anda harus ikut kami ke kantor polisi"

        "Serahkan diri":
            agent "Terima kasih atas kooperasinya"
            if (pakaiNarkoba == 1):
                jump rehabilitasi
            elif (pakaiNarkoba == 2):
                jump penjara
        "Kabur":
            hide detective with Dissolve(0.3)
            "Kamu memutuskan untuk melarikan diri"
            if (pakaiNarkoba == 1):
                show city with Dissolve(0.3)
                "Setelah berlari cukup jauh, kamu tidak melihat agen itu lagi"
                $ stress += 10
                jump showKegiatan

            elif (pakaiNarkoba == 2):
                show detective with Dissolve(0.3)
                agent "Kamu tidak bisa lari. Kamu terindikasi sebagai asalah satu dari jaringan bandar narkoba"
                agent "Bawa dia ke dalam mobil!"
                "Kamu dibawa masuk ke mobil polisi"
                jump penjara

label daftarOrganisasi:
    scene bedroom with Dissolve(0.3)
    
    hp "Mari bergabung bersama kami dalam Himpunan Mahasiswa Jurusan"
    hp "Bersama kami, mari majukan kehidupan mahasiswa intra kampus"
    hp "dan dapatkan pengalaman yang akan berguna setelah lulus"
    hp "Untuk pendaftaran dan wawancara dapat dilakukan di selasar gedung jurusan"
    
    menu:
        "Setelah menerima pesan itu, Kamu memutuskan untuk:"
        "Ikut organisasi intra kampus":
            "Kamu berangkat ke kampus untuk kuliah dan mendaftar ke organisasi"
            scene campus with Dissolve(0.3)
            "Setelah kuliah"
            show senior with Dissolve(0.3)
            senior "Halo, apakah kamu mau mendaftar ke organisasi ini?"
            kamu "Iya kak"
            senior "Oke, kalau begitu kita lakukan wawancara ya"
            kamu "Baik kak"
            "Kamu melakukan wawancara untuk mendaftar organisasi"
            $ masukOrganisasi = 1

        "Tidak ikut organisasi":
            "Kamu menutup pesan itu dan berangkat ke kampus untuk kuliah"

    jump showKegiatan

label diterimaOrganisasi:
    scene bedroom with Dissolve(0.3)
    $stressModifier += 2
    hp "Selamat, kamu telah diterima di himpunan mahasiswa jurusan"
    hp "Untuk itu, mari datang ke Welcome party yang akan dilakukan di kampus"
    menu:
        "Kamu menutup pesan itu dan memutuskan untuk"
        "Datang ke Welcome Party":
            scene conference with Dissolve(0.3)
            show senior with Dissolve(0.3)
            $ levelRelasi += 2

            senior "Selamat datang di Himpunan Mahasiswa Jurusan"
            senior "Tenang saja, kami disini akan menjadi teman kalian untuk menyejahterakan kehidupan mahasiswa di dalam kampus"
            senior "Mari bekerja sama untuk mencapai tujuan kita"

            if (isIntrovert):
                $ stress -= 15
            else:
                $stress -= 20
            "Kamu menikmati malam itu untuk berkenalan dengan rekan-rekan di himpunan"
        "Lewati Welcome Party":
            if (isIntrovert):
                $ stress -= 15
            else:
                $stress -= 10
            "Kamu melanjutkan aktivitas seperti biasa"

    jump showKegiatan

label eventOrganisasi:
    scene campus with Dissolve(0.3)
    "Kamu melihat ada brosur mengenai perekrutan panitia acara besar di jurusanmu"
    "Acara itu akan mengundang artis dari ibukota"
    "Tetapi, kamu melihat bahwa acara itu dilaksanakan dalam 3 minggu"
    menu:
        "Kamu memutuskan untuk"

        "Ikut kepanitiaan":
            scene classroom with Dissolve(0.3)
            show senior with Dissolve(0.3)
            senior "Selamat datang di kepanitiaan acara"
            senior "Mulai saat ini, mari kita membuat acara yang meriah"
            $ panitiaAcara = 1
        "Tidak ikut kepanitiaan":
            "Kamu memutuskan untuk tidak menjadi panitia"
    jump showKegiatan

label persiapanAcara:
    scene classroom with Dissolve(0.3)
    "Kamu bekerja sama dengan temanmu untuk mempersiapkan acara besar organisasi agar berjalan dengan baik"
    $ stress +=3

    jump showKegiatan

label acaraBesar:
    scene conference with Dissolve(0.3)
    "Setelah persiapan selama 3 bulan, acara yang kamu buat siap untuk dilaksanakan"
    show senior with Dissolve(0.3)
    senior "Dengan pembunyian gong ini, maka acara resmi dibuka"
    hide senior with Dissolve(0.3)
    play sound "audio/gong.mp3"
    "Gong telah dibunyikan. para penampil sudah siap memasuki panggung"
    "Kamu melihat penampilan artis langsung dari belakang panggung"
    "Malam itu berjalan dengan sukses dan meriah"
    scene classroom with Dissolve(0.3)
    senior "Terima kasih bagi kalian yang sudah membantu untuk memeriahkan acara kita"
    senior "Semoga kepengurusan berikutnya bisa lebih meriah dari tahun ini"
    $ stress -= 30

    if (kaderisasi):
        $ levelRelasi += 5
    else:
        $ levelRelasi += 3

    jump showKegiatan

label nontonAcaraBesar:
    scene bedroom with Dissolve(0.3)
    "Kamu mendapat pengumuman tentang acara besar di jurusanmu yang mengundang artis ibukota favoritmu"
    menu:
        "Kamu memutuskan untuk..."

        "Beli tiket":
            scene conference with Dissolve(0.3)
            $ money -= 1500
            "Kamu membeli tiket untuk memasuki acara itu"
            "Setelah itu, kamu menonton acara itu sampai selesai"
            "Acara itu berlangsung sangat meriah"
            if (isIntrovert):
                $ stress -= 10
            else:
                $ stress -= 15
    jump showKegiatan

label pameranUsaha:
    scene campus with Dissolve(0.3)
    "Kamu menerima pesan di HP-mu"
    hp "Selamat siang, saya mewakili sebuah organisasi kewirausahaan mengundang anda untuk mengikuti pameran usaha yang akan dilaksanakan minggu ini"
    hp "Acara ini dapat mengenalkan produk anda pada pasar yang anda inginkan dan akan mengembangkan usaha anda"
    hp "Ada biaya pendaftaran sejumlah 1000 unntuk membuka stand di pameran ini"
    menu:
        hp "Apakah anda bersedia untuk mengikuti pameran kewirausahaan yang akan di"

        "Bersedia":
            $ money -= 1000
            $ levelUsahaModifier += 3
            $ levelUsahaTotal = levelUsaha + levelUsahaModifier
            hp "Baik. kami tunggu anda di hari pameran."
            hp "Terima kasih"
            scene exhibition with Dissolve(0.3)
            "Di hari pameran"
            "Kamu membuka stand untuk menjual produkmu"
            $ money += (300 * levelUsahaTotal)
            if(isIntrovert):
                $ stress += 10
            else:
                $ stress += 8
            $ levelRelasi += (levelUsahaTotal // 2)
            "Kamu mendapatkan keuntungan, pengalaman, dan relasi dari pameran ini"
        "Tidak Bersedia":
            hp "Baik, mohon maaf sudah mengganggu."

    jump showKegiatan

label pencalonanKetua:
    scene campus with Dissolve(0.3)
    hp "Telah dibuka pendaftaran calon ketua himpunan"
    hp "Syarat utama dari menjadi ketua adalah bebas narkoba dan pernah menjadi pengurus di acara kampus"
    hp "Bagi kalian yang ingin meneruskan perjuangan kami, silahkan mendaftar"

    menu:
        "Setelah menerima pesan itu, apa yang ingin kamu lakukan?"

        "Mendaftar calon ketua":
            scene classroom with Dissolve(0.3)
            "Kamu menemui seniormu untuk melakukan tes"
            senior "Nanti ditunggu ya hasil tesnya"
        "Tidak mendaftar":
            $ kaderisasi = 0
            "Kamu memutuskan untuk tidak mendaftar menjadi calon ketua"

    jump showKegiatan

label pengumumanCalon:
    scene campus with Dissolve(0.3)
    show senior with Dissolve(0.3)

    senior "Setelah melalui tahap seleksi, tersisalah beberapa kandidat yang memenuhi semua persyaratan yang kami ajukan"
    senior "Pada hari ini, kami akan mengumumkan siapa calon ketua himpunan periode berikutnya"
    "Kamu menyimak siapa saja yang berhasil menjadi ketua"
    "Selamat kepada Yusuf Fabriansyah sebagai calon ketua himpunan"

    if (panitiaAcara):
        senior "Selamat kepada [nama] sebagai calon ketua himpunan"
        senior "Apakah ada sepatah kata dari para calon untuk para hadirin?"
        "Kamu memberikan kata-kata sambutan sebagai calon ketua himpunan yang baru"
    else:
        $ kaderisasi = 0
        "Namamu tidak disebutkan oleh pengawas pemilu"
        "Kamu gagal menjadi calon ketua himpunan periode berikutnya"

    jump showKegiatan

label kampanyePemilu:
    show campus with Dissolve(0.3)

    menu:
        "Apakah kamu akan melakukan kampanye sebagai calon ketua himpunan minggu ini?"
        "Ya":
            $ levelRelasi += 1
            $ stress += 2
            "Kamu melakukan kampanye agar kamu dapat terpilih menjadi ketua himpunan"
        "Tidak":
            "Kamu tidak melakukan kampanya pada minggu ini"
    jump showKegiatan

label pemiluJurusan:
    show campus with Dissolve(0.3)

    "Setelah melalui minggu kampanye, tibalah hari pemilu"
    "Kamu melihat para mahasiswa mengisi balot pemilihan umum"
    "Setelah waktu pemungutan selesai, kamu mengikuti perhitungan suara"

    show classroom with Dissolve(0.3)

    if (levelRelasi >= 8):
        $stressModifier += 2
        $ levelRelasi += 4
        senior "Pemenang pemilu kali ini adalah [nama]"
        senior "Kepada saudara [nama], apakah ada sambutan sebagai ketua terpilih?"
        "Kamu memberikan ungkapan terima kasih dan keinginan untuk bekerja sama sebagai ketua organisasi"
    else:
        $stressModifier -= 2
        $ kaderisasi = 0
        senior "Pemenang pemilu kali ini adalah Yusuf Fabriansyah"
        "Kamu gagal memenangi pemilu himpunan"
        senior "Bagi saudara [nama], terima kasih atas semangat dan partisipasinya dalam pemilu kali ini"
        "Kamu meninggalkan ruangan perhitungan suara"

    jump showKegiatan

label berhentiKuliah:
    scene bedroom with Dissolve(0.3)
    jump showKegiatan

    
