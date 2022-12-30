screen infoUpdate:
    add "statusback" xpos 0.0 ypos 0.0 
    text "Sem. [Semester] Mingg. [week]" xpos 0.0 ypos 0.0
    text "Uang: [money]" xpos 0.2 ypos 0.0
    text "Stress: [stress]/100" xpos 0.4 ypos 0.0
    text "Nilai: [nilaiSemester]/100" xpos 0.6 ypos 0.0
    text "SKS : [nilaiSKS]/144" xpos 0.8 ypos 0.0
    
return


label infoLengkapLabel:
    show screen infoUpdate
    call screen infoLengkapScreen with Dissolve(0.3)

screen infoLengkapScreen:
    add "status_background"
    add "statusback" xpos 0.0 ypos 0.0 
    text "Sem. [Semester] Ming.[week]" xpos 0.0 ypos 0.0
    text "Uang: [money]" xpos 0.2 ypos 0.0
    text "Stress: [stress]/100" xpos 0.4 ypos 0.0
    text "Nilai: [nilaiSemester]/100" xpos 0.6 ypos 0.0
    text "SKS : [nilaiSKS]/144" xpos 0.8 ypos 0.0

    vbox:
        xalign 0.98
        yalign 0.07
        imagebutton:
            idle "gui/backButton.png"
            hover "gui/backButton_hover.png"
            action ui.jumps("showKegiatan")

    text "Level Usaha: [levelUsahaTotal] ([levelUsahaEXP]%)" xpos 0.1 ypos 0.2
    text "Total Modal Usaha: [totalCapital]" xpos 0.1 ypos 0.25
    text "Keuntungan usaha Mingguan: [profit] ([profitMultiplier]%)" xpos 0.1 ypos 0.3
    text "Saldo di bank: [saldo]" xpos 0.1 ypos 0.35
    text "Level relasi: [levelRelasi]" xpos 0.1 ypos 0.40
    
    
