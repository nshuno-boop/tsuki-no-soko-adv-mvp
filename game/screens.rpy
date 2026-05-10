# Phase 2 UI screens.
# 冷たい月面都市風の見た目に寄せつつ、Ren'Py標準機能だけで読める画面を優先する。

style tsuki_frame:
    background "#111827ee"
    padding (24, 20)

style tsuki_panel:
    background "#020617dd"
    padding (16, 14)

style tsuki_title_text:
    color "#f8fafc"
    size 34

style tsuki_subtle_text:
    color "#94a3b8"
    size 20

style tsuki_button:
    background "#1f2937"
    hover_background "#164e63"
    selected_background "#0e7490"
    padding (12, 9)

style tsuki_button_text:
    color "#f8fafc"
    hover_color "#ffffff"
    size 20

style alma_log_text:
    color "#bffcff"
    size 20


screen investigation_hub_screen():
    modal True

    add Solid("#030712")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 1180
        ysize 650

        vbox:
            spacing 18

            hbox:
                xfill True
                vbox:
                    spacing 2
                    text "聞き込み / 調査メニュー" style "tsuki_title_text"
                    text "第[chapter]章  [chapter_title]" style "tsuki_subtle_text"
                text "SHIROWA AUDIT" xalign 1.0 color "#67e8f9" size 18

            hbox:
                spacing 18

                viewport:
                    xsize 760
                    ysize 470
                    mousewheel True
                    scrollbars "vertical"

                    vbox:
                        spacing 10
                        for person_id in INTERVIEW_TARGETS:
                            $ person = person_profiles[person_id]
                            $ done = person_id in interview_done
                            frame:
                                style "tsuki_panel"
                                xfill True

                                hbox:
                                    spacing 14
                                    add person["image"] xysize (72, 112)
                                    vbox:
                                        xfill True
                                        spacing 4
                                        text person["name"] color "#f8fafc" size 24
                                        text person["label"] color "#93c5fd" size 18
                                        if done:
                                            text "聞き込み済み" color "#fbbf24" size 16
                                        else:
                                            text "未確認" color "#94a3b8" size 16
                                    textbutton "聞く":
                                        action Return("interview:" + person_id)
                                        xminimum 100

                vbox:
                    spacing 10
                    xsize 330
                    textbutton "証拠品一覧":
                        action Return("evidence")
                        xfill True
                    textbutton "人物メモ":
                        action Return("people")
                        xfill True
                    textbutton "ALMAログ":
                        action Return("alma")
                        xfill True
                    null height 12
                    textbutton "最終推理へ進む":
                        action Return("final")
                        xfill True


screen evidence_screen():
    tag menu
    modal True
    default selected_id = None

    add Solid("#030712")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 1160
        ysize 650

        vbox:
            spacing 18

            hbox:
                xfill True
                text "証拠品一覧" style "tsuki_title_text"
                text "第[chapter]章  [chapter_title]" xalign 1.0 color "#cbd5e1"

            if len(evidence_unlocked) == 0:
                text "まだ証拠品はありません。" color "#cbd5e1"
            else:
                hbox:
                    spacing 22

                    viewport:
                        xsize 450
                        ysize 490
                        mousewheel True
                        scrollbars "vertical"

                        vbox:
                            spacing 8
                            for evidence_id in ordered_unlocked_evidence():
                                $ item = evidence_catalog[evidence_id]
                                textbutton item["short_name"]:
                                    action SetScreenVariable("selected_id", evidence_id)
                                    xfill True

                    frame:
                        style "tsuki_panel"
                        xfill True
                        yfill True
                        background Frame("images/ui/ui_evidence_card.png", 24, 24)

                        if selected_id is None:
                            text "左のリストから証拠品を選択してください。" color "#cbd5e1"
                        else:
                            $ selected = evidence_catalog[selected_id]
                            $ selected_chapter = selected["chapter"]
                            $ selected_category = selected["category"]
                            $ selected_character = selected["related_character"]
                            $ selected_location = selected["related_location"]
                            vbox:
                                spacing 12
                                hbox:
                                    spacing 14
                                    add selected["icon"] xysize (52, 52)
                                    vbox:
                                        text selected["name"] size 28 color "#f8fafc"
                                        text "入手章: 第[selected_chapter]章 / [selected_category]" color "#93c5fd"
                                text selected["description"] color "#e5e7eb"
                                text selected["detail"] color "#cbd5e1"
                                null height 4
                                text "関連人物: [selected_character]" color "#fbbf24"
                                text "関連施設: [selected_location]" color "#67e8f9"

            textbutton "閉じる":
                action Return()
                xalign 1.0


screen person_memo_screen():
    tag menu
    modal True
    default selected_person = "mio"

    add Solid("#020617")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 1160
        ysize 650

        fixed:
            hbox:
                spacing 22

                viewport:
                    xsize 360
                    ysize 560
                    mousewheel True
                    scrollbars "vertical"

                    vbox:
                        spacing 8
                        text "人物メモ" style "tsuki_title_text"
                        for person_id in PERSON_ORDER:
                            $ person = person_profiles[person_id]
                            textbutton person["name"]:
                                action SetScreenVariable("selected_person", person_id)
                                xfill True

                frame:
                    style "tsuki_panel"
                    xfill True
                    yfill True

                    $ person = person_profiles[selected_person]
                    hbox:
                        spacing 22
                        add person["image"] xysize (250, 390)
                        vbox:
                            spacing 14
                            text person["name"] size 34 color "#f8fafc"
                            text person["label"] size 22 color "#67e8f9"
                            text person["memo"] color "#cbd5e1"
                            if selected_person in interview_done:
                                text "聞き込み済み" color "#fbbf24"
                            elif selected_person in INTERVIEW_TARGETS:
                                text "未聞き込み" color "#94a3b8"
                            else:
                                text "参考人物" color "#94a3b8"

            textbutton "閉じる":
                action Return()
                xalign 0.96
                yalign 0.95


screen evidence_choice_screen(question, hint_text):
    modal True

    add Solid("#020617")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 1180
        ysize 660

        vbox:
            spacing 16

            text question size 28 color "#f8fafc"
            text "提示する証拠を選んでください。" color "#cbd5e1"

            if len(evidence_unlocked) == 0:
                text "提示できる証拠がありません。" color "#fecaca"
            else:
                viewport:
                    xfill True
                    ysize 455
                    mousewheel True
                    scrollbars "vertical"

                    vbox:
                        spacing 10
                        for evidence_id in ordered_unlocked_evidence():
                            $ item = evidence_catalog[evidence_id]
                            $ related_character = item["related_character"]
                            $ related_location = item["related_location"]
                            frame:
                                style "tsuki_panel"
                                xfill True
                                background Frame("images/ui/ui_choice_button.png", 20, 20)

                                hbox:
                                    spacing 16
                                    add item["icon"] xysize (46, 46)
                                    vbox:
                                        xfill True
                                        spacing 5
                                        text item["name"] size 22 color "#f8fafc"
                                        text item["description"] color "#cbd5e1"
                                        text "[related_character] / [related_location]" color "#67e8f9" size 16

                                    textbutton "提示":
                                        action Return(evidence_id)
                                        xminimum 100

            hbox:
                spacing 12
                textbutton "ヒントを見る":
                    action Return("__hint__")

                textbutton "考え直す":
                    action Return("__cancel__")


screen alma_log_screen(title, lines):
    modal True

    add Solid("#01050a")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 590
        padding (24, 22)
        background Frame("images/ui/ui_alma_panel.png", 24, 24)

        vbox:
            spacing 12
            text title color "#67e8f9" size 28
            text "ALMA / CITY OPERATIONS LOG" color "#94a3b8" size 18
            null height 8
            for line in lines:
                text "> [line]" style "alma_log_text"
            null height 14
            textbutton "ログを閉じる":
                action Return()
                xalign 1.0
