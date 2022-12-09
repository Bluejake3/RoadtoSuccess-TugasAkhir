screen map:
    imagemap: 
        ground "gui/maps.png"
        hover "gui/maps_hover.png"

        hotspot(331, 214, 354, 352) action Return("belajar")
        hotspot(1260, 213, 352, 354) action Return("bekerja")
        hotspot(335, 660, 353, 353) action Return("menabung")
        hotspot(1256, 660, 353, 350) action Return("rekreasi")
        hotspot(798, 440, 348, 352) action Return("Buka Usaha")

    add "statusback" xpos 0.0 ypos 0.0 
    text "Semester [Semester] Minggu [week]" xpos 0.0 ypos 0.0
    text "Uang: [money]" xpos 0.2 ypos 0.0
    text "Stress: [stress]/100" xpos 0.4 ypos 0.0
    text "Nilai: [nilaiSemester]/100" xpos 0.6 ypos 0.0
    text "SKS : [nilaiSKS]/144" xpos 0.8 ypos 0.0

    vbox:
        xalign 0.98
        yalign 0.07
        imagebutton:
            idle "gui/infoButton.png"
            hover "gui/infoButton_hover.png"
            action ui.callsinnewcontext("infoLengkapLabel")

label showKegiatan:
    scene maps with Dissolve(0.3)
    call screen map with Dissolve(0.3)

    if _return == "bekerja":
        jump bekerja
    elif _return == "belajar":
        jump belajar
    elif _return == "menabung":
        jump menabung
    elif _return == "rekreasi":
        jump rekreasi
    elif _return == "Buka Usaha":
        jump usaha
    