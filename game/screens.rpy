# Phase 4 UI screens.
# 冷たい月面都市風の見た目に寄せつつ、Ren'Py標準機能だけで読める画面を優先する。

style tsuki_frame:
    background Frame("images/ui/ui_log_panel.png", 34, 34)
    padding (24, 20)

style tsuki_panel:
    background Frame("images/ui/ui_evidence_card.png", 24, 24)
    padding (16, 14)

style tsuki_title_text:
    color "#f8fafc"
    size 30

style tsuki_subtle_text:
    color "#94a3b8"
    size 18

style tsuki_button:
    background Frame("images/ui/ui_choice_button.png", 24, 24)
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


init python:
    def speaker_portrait(who):
        portrait_map = {
            "佐伯 澪": "images/portraits/portrait_mio.png",
            "雨宮 セナ": "images/portraits/portrait_sena.png",
            "檜山 徹": "images/portraits/portrait_toru.png",
            "北条 リツ": "images/portraits/portrait_ritsu.png",
            "ルカ・ナディム": "images/portraits/portrait_luka.png",
            "白石 アカリ": "images/portraits/portrait_akari.png",
            "雨宮 ノア": "images/portraits/portrait_noah.png",
            "鷹峰 ジン": "images/portraits/portrait_jin.png",
            "ALMA": "images/portraits/portrait_alma.png",
            "SYSTEM": "images/portraits/portrait_system.png",
        }
        return portrait_map.get(who, "images/portraits/portrait_system.png")


style playable_menu_button:
    background Frame("images/ui/ui_choice_button.png", 24, 24)
    hover_background "#164e63"
    padding (18, 10)
    xminimum 280

style playable_menu_button_text:
    color "#f8fafc"
    hover_color "#ffffff"
    size 24


screen main_menu():
    tag menu

    add "title background"
    add Solid("#02061733")

    add "title logo":
        xpos 56
        ypos 54

    text "月の底で、息をする":
        xpos 92
        ypos 166
        color "#f8fafc"
        size 52
        font gui.name_text_font
        outlines [(2, "#0e749099", 0, 0)]

    text "月面都市シロワの空気は、記録より先に嘘を吸い込んでいた。":
        xpos 98
        ypos 250
        xmaximum 640
        color "#cbd5e1"
        size 22

    vbox:
        xpos 96
        ypos 440
        spacing 12
        textbutton "はじめる" action Start() style "playable_menu_button" xsize 320
        textbutton "終了" action Quit(confirm=True) style "playable_menu_button" xsize 320

    text "PLAYABLE ART PASS / DRAFT":
        xpos 98
        ypos 642
        color "#67e8f9"
        size 15


screen say(who, what):
    zorder 10

    window:
        id "window"
        background Frame("images/ui/ui_textbox.png", 34, 34)
        xalign 0.5
        yalign 0.985
        xsize 1080
        ysize 190
        padding (0, 0)

        fixed:
            xfill True
            yfill True

            if who is not None:
                window:
                    id "namebox"
                    background Frame("images/ui/ui_nameplate.png", 22, 22)
                    xpos 205
                    ypos 18
                    xsize 334
                    ysize 38
                    padding (20, 0)
                    text who id "who":
                        color "#dff7ff"
                        size 18
                        font gui.text_font
                        yalign 0.5

                add speaker_portrait(who):
                    xpos 46
                    ypos 18
                    xysize (132, 132)

                text what id "what":
                    xpos 205
                    ypos 64
                    xmaximum 820
                    color "#f8fafc"
                    size 24
                    line_spacing 4

            else:
                text what id "what":
                    xpos 62
                    ypos 42
                    xmaximum 960
                    color "#f8fafc"
                    size 24
                    line_spacing 4


screen choice(items):
    zorder 100

    vbox:
        xalign 0.5
        yalign 0.52
        spacing 10

        for item in items:
            textbutton item.caption:
                action item.action
                style "playable_menu_button"
                xsize 760


screen objective_overlay():
    zorder 5

    frame:
        xalign 0.02
        yalign 0.025
        xmaximum 520
        padding (12, 7)
        background "#020617d8"

        vbox:
            spacing 2
            text "現在の目的" color "#67e8f9" size 14
            text current_objective color "#f8fafc" size 15 xmaximum 480


screen confirm(message, yes_action, no_action):
    zorder 200
    modal True

    add Solid("#020617dd")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 720

        vbox:
            spacing 18
            text message color "#f8fafc" size 22 xmaximum 660

            hbox:
                spacing 12
                xalign 1.0
                textbutton "はい" action yes_action
                textbutton "いいえ" action no_action


screen investigation_hub_screen():
    zorder 20
    modal True

    add "ui_menu_background"
    add Solid("#02061799")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 1180
        ysize 650

        vbox:
            spacing 14

            $ done_count = interview_done_count()
            $ required_count = CHAPTER4_REQUIRED_INTERVIEWS
            $ missing_names = missing_interview_names()
            $ recommended_action = recommended_action_text()

            hbox:
                xfill True
                vbox:
                    spacing 2
                    text "聞き込み / 調査メニュー" style "tsuki_title_text"
                    text chapter_title style "tsuki_subtle_text"
                    text "目的: [current_objective]" color "#f8fafc" size 17 xmaximum 700
                    text recommended_action color "#fbbf24" size 15 xmaximum 740
                text "SHIROWA AUDIT" xalign 1.0 color "#67e8f9" size 18

            hbox:
                spacing 18

                frame:
                    style "tsuki_panel"
                    xsize 790
                    ysize 500

                    vbox:
                        spacing 7
                        text "聞き込み対象" color "#f8fafc" size 24
                        text "聞き込み進捗: [done_count] / [required_count]" color "#fbbf24" size 17
                        if chapter == 3:
                            text "第4章へ進むには4人以上への初回聞き込みが必要です。" color "#cbd5e1" size 15 xmaximum 730
                        else:
                            text "最終推理前に、核心に近い話も確認できます。" color "#cbd5e1" size 15 xmaximum 730

                        null height 2

                        frame:
                            background "#0f172acc"
                            padding (10, 6)
                            xfill True
                            hbox:
                                spacing 10
                                vbox:
                                    xsize 570
                                    spacing 1
                                    text "雨宮 セナ" color "#f8fafc" size 18
                                    text "シロワの代表 / [interview_status_text('sena')]" color "#93c5fd" size 14
                                textbutton "聞く":
                                    action Return("interview:sena")
                                    xminimum 92

                        frame:
                            background "#0f172acc"
                            padding (10, 6)
                            xfill True
                            hbox:
                                spacing 10
                                vbox:
                                    xsize 570
                                    spacing 1
                                    text "北条 リツ" color "#f8fafc" size 18
                                    text "アルマの技師 / [interview_status_text('ritsu')]" color "#93c5fd" size 14
                                textbutton "聞く":
                                    action Return("interview:ritsu")
                                    xminimum 92

                        frame:
                            background "#0f172acc"
                            padding (10, 6)
                            xfill True
                            hbox:
                                spacing 10
                                vbox:
                                    xsize 570
                                    spacing 1
                                    text "ルカ・ナディム" color "#f8fafc" size 18
                                    text "影井戸の採掘屋 / [interview_status_text('luka')]" color "#93c5fd" size 14
                                textbutton "聞く":
                                    action Return("interview:luka")
                                    xminimum 92

                        frame:
                            background "#0f172acc"
                            padding (10, 6)
                            xfill True
                            hbox:
                                spacing 10
                                vbox:
                                    xsize 570
                                    spacing 1
                                    text "白石 アカリ" color "#f8fafc" size 18
                                    text "月生まれを診る医師 / [interview_status_text('akari')]" color "#93c5fd" size 14
                                textbutton "聞く":
                                    action Return("interview:akari")
                                    xminimum 92

                        frame:
                            background "#0f172acc"
                            padding (10, 6)
                            xfill True
                            hbox:
                                spacing 10
                                vbox:
                                    xsize 570
                                    spacing 1
                                    text "雨宮 ノア" color "#f8fafc" size 18
                                    text "月で生まれた娘 / [interview_status_text('noah')]" color "#93c5fd" size 14
                                textbutton "聞く":
                                    action Return("interview:noah")
                                    xminimum 92

                        frame:
                            background "#0f172acc"
                            padding (10, 6)
                            xfill True
                            hbox:
                                spacing 10
                                vbox:
                                    xsize 570
                                    spacing 1
                                    text "鷹峰 ジン" color "#f8fafc" size 18
                                    text "セレネ社の広報法務 / [interview_status_text('jin')]" color "#93c5fd" size 14
                                textbutton "聞く":
                                    action Return("interview:jin")
                                    xminimum 92

                vbox:
                    spacing 10
                    xsize 330
                    textbutton "証拠品を確認":
                        action Return("evidence")
                        xfill True
                    textbutton "人物メモを見る":
                        action Return("people")
                        xfill True
                    textbutton "ALMAログ":
                        action Return("alma")
                        xfill True
                    textbutton "事件タイムライン":
                        action Return("timeline")
                        xfill True
                    null height 12
                    if chapter < 4:
                        textbutton "第4章へ進む: 白兎3号を調べる":
                            action Return("final")
                            xfill True
                        if chapter == 3 and done_count < required_count:
                            text "不足: [done_count] / [required_count]" color "#fbbf24" size 15
                            if len(missing_names) > 0:
                                $ missing_text = "、".join(missing_names)
                                text "未聞き込み: [missing_text]" color "#94a3b8" size 14 xmaximum 310
                    else:
                        textbutton "最終推理へ進む":
                            action Return("final")
                            xfill True


screen evidence_screen():
    tag menu
    zorder 20
    modal True
    default selected_id = None

    add "ui_menu_background"
    add Solid("#020617aa")

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
                text chapter_title xalign 1.0 color "#cbd5e1"
            text "目的: [current_objective]" color "#f8fafc" size 17 xmaximum 1040

            if len(evidence_unlocked) == 0:
                text "まだ証拠品はありません。" color "#cbd5e1"
            else:
                hbox:
                    spacing 22

                    frame:
                        style "tsuki_panel"
                        xsize 500
                        yfill True

                        hbox:
                            spacing 8
                            vbox:
                                spacing 4
                                xsize 235
                                if has_evidence("e_r7_decompression_log"):
                                    textbutton "R-7減圧ログ" action SetScreenVariable("selected_id", "e_r7_decompression_log") xfill True
                                if has_evidence("e_personnel_location_log"):
                                    textbutton "位置ログ" action SetScreenVariable("selected_id", "e_personnel_location_log") xfill True
                                if has_evidence("e_autopsy_record"):
                                    textbutton "検案記録" action SetScreenVariable("selected_id", "e_autopsy_record") xfill True
                                if has_evidence("e_manual_bulkhead_blood"):
                                    textbutton "隔壁の血痕" action SetScreenVariable("selected_id", "e_manual_bulkhead_blood") xfill True
                                if has_evidence("e_white_rabbit_usage_log"):
                                    textbutton "白兎使用ログ" action SetScreenVariable("selected_id", "e_white_rabbit_usage_log") xfill True
                                if has_evidence("e_white_rabbit_co2_absorber"):
                                    textbutton "CO2吸収材" action SetScreenVariable("selected_id", "e_white_rabbit_co2_absorber") xfill True
                                if has_evidence("e_white_rabbit_dust_test"):
                                    textbutton "関節粉塵検査" action SetScreenVariable("selected_id", "e_white_rabbit_dust_test") xfill True
                                if has_evidence("e_thermal_sensor_frost"):
                                    textbutton "氷霜成分" action SetScreenVariable("selected_id", "e_thermal_sensor_frost") xfill True
                            vbox:
                                spacing 4
                                xsize 235
                                if has_evidence("e_manual_valve_scratch"):
                                    textbutton "補助弁の傷" action SetScreenVariable("selected_id", "e_manual_valve_scratch") xfill True
                                if has_evidence("e_maintenance_admin_log"):
                                    textbutton "重要: 保守モード記録" action SetScreenVariable("selected_id", "e_maintenance_admin_log") xfill True
                                if has_evidence("e_earth_meeting_audio"):
                                    textbutton "会議音声" action SetScreenVariable("selected_id", "e_earth_meeting_audio") xfill True
                                if has_evidence("e_noah_testimony"):
                                    textbutton "重要: ノア証言" action SetScreenVariable("selected_id", "e_noah_testimony") xfill True
                                if has_evidence("e_toru_audit_file"):
                                    textbutton "重要: 監査ファイル" action SetScreenVariable("selected_id", "e_toru_audit_file") xfill True
                                if has_evidence("e_lunarborn_medical_report"):
                                    textbutton "重要: 月生まれ医療評価" action SetScreenVariable("selected_id", "e_lunarborn_medical_report") xfill True
                                if has_evidence("e_sena_dust_trace"):
                                    textbutton "袖口の粉塵" action SetScreenVariable("selected_id", "e_sena_dust_trace") xfill True

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
                            $ selected_is_key = selected_id in FINAL_REQUIRED_EVIDENCE
                            vbox:
                                spacing 12
                                hbox:
                                    spacing 14
                                    add selected["icon"] xysize (52, 52)
                                    vbox:
                                        text selected["name"] size 25 color "#f8fafc" xmaximum 560
                                        text "入手章: 第[selected_chapter]章 / [selected_category]" color "#93c5fd" size 17
                                        if selected_is_key:
                                            text "重要証拠: 最終推理の核心に関わる" color "#fbbf24" size 16
                                text selected["description"] color "#e5e7eb" size 18 xmaximum 600
                                text selected["detail"] color "#cbd5e1" size 17 xmaximum 600
                                null height 4
                                text "関連人物: [selected_character]" color "#fbbf24"
                                text "関連施設: [selected_location]" color "#67e8f9"

            textbutton "閉じる":
                action Return()
                xalign 1.0


screen person_memo_screen():
    tag menu
    zorder 20
    modal True
    default selected_person = "mio"

    add "ui_menu_background"
    add Solid("#020617aa")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 1160
        ysize 650

        fixed:
            hbox:
                spacing 22

                vbox:
                    spacing 8
                    xsize 360
                    ysize 560
                    text "人物メモ" style "tsuki_title_text"
                    textbutton "佐伯 澪" action SetScreenVariable("selected_person", "mio") xfill True
                    textbutton "雨宮 セナ" action SetScreenVariable("selected_person", "sena") xfill True
                    textbutton "檜山 徹" action SetScreenVariable("selected_person", "toru") xfill True
                    textbutton "北条 リツ" action SetScreenVariable("selected_person", "ritsu") xfill True
                    textbutton "ルカ・ナディム" action SetScreenVariable("selected_person", "luka") xfill True
                    textbutton "白石 アカリ" action SetScreenVariable("selected_person", "akari") xfill True
                    textbutton "雨宮 ノア" action SetScreenVariable("selected_person", "noah") xfill True
                    textbutton "鷹峰 ジン" action SetScreenVariable("selected_person", "jin") xfill True
                    textbutton "ALMA" action SetScreenVariable("selected_person", "alma") xfill True

                frame:
                    style "tsuki_panel"
                    xfill True
                    yfill True

                    $ person = person_profiles[selected_person]
                    $ person_focus = person["focus"]
                    hbox:
                        spacing 22
                        add person["image"] xysize (250, 390)
                        vbox:
                            spacing 14
                            text person["name"] size 30 color "#f8fafc"
                            text person["label"] size 20 color "#67e8f9"
                            text person["memo"] color "#cbd5e1" size 18 xmaximum 485
                            text "現在の印象: [person_focus]" color "#fbbf24" size 17 xmaximum 500
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
    zorder 30
    modal True

    add "ui_deduction_background"
    add Solid("#02061799")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 1180
        ysize 660

        vbox:
            spacing 16

            text question size 25 color "#f8fafc" xmaximum 1080
            text "提示する証拠を選んでください。" color "#cbd5e1" size 18

            if len(evidence_unlocked) == 0:
                text "提示できる証拠がありません。調査に戻って、証拠品一覧や聞き込みを確認してください。" color "#fecaca" size 20 xmaximum 1020
            else:
                hbox:
                    spacing 10
                    vbox:
                        spacing 4
                        xsize 545
                        if has_evidence("e_r7_decompression_log"):
                            textbutton "R-7減圧ログ: 酸素工房R-7緊急減圧ログ" action Return("e_r7_decompression_log") xfill True
                        if has_evidence("e_personnel_location_log"):
                            textbutton "位置ログ: 人員位置ログ" action Return("e_personnel_location_log") xfill True
                        if has_evidence("e_autopsy_record"):
                            textbutton "検案記録: 徹の遺体検案記録" action Return("e_autopsy_record") xfill True
                        if has_evidence("e_manual_bulkhead_blood"):
                            textbutton "隔壁の血痕: 手動隔壁レバーの血痕" action Return("e_manual_bulkhead_blood") xfill True
                        if has_evidence("e_white_rabbit_usage_log"):
                            textbutton "白兎使用ログ: 白兎3号の使用ログ" action Return("e_white_rabbit_usage_log") xfill True
                        if has_evidence("e_white_rabbit_co2_absorber"):
                            textbutton "CO2吸収材: 白兎3号のCO2吸収材" action Return("e_white_rabbit_co2_absorber") xfill True
                        if has_evidence("e_white_rabbit_dust_test"):
                            textbutton "関節粉塵検査: 白兎3号関節部の粉塵検査" action Return("e_white_rabbit_dust_test") xfill True
                        if has_evidence("e_thermal_sensor_frost"):
                            textbutton "氷霜成分: 熱センサーの氷霜成分" action Return("e_thermal_sensor_frost") xfill True
                    vbox:
                        spacing 4
                        xsize 545
                        if has_evidence("e_manual_valve_scratch"):
                            textbutton "補助弁の傷: 手動補助弁の微細傷" action Return("e_manual_valve_scratch") xfill True
                        if has_evidence("e_maintenance_admin_log"):
                            textbutton "保守モード記録: 管理者権限の保守モード記録" action Return("e_maintenance_admin_log") xfill True
                        if has_evidence("e_earth_meeting_audio"):
                            textbutton "会議音声: 地球会議の音声記録" action Return("e_earth_meeting_audio") xfill True
                        if has_evidence("e_noah_testimony"):
                            textbutton "ノア証言: ノアの証言メモ" action Return("e_noah_testimony") xfill True
                        if has_evidence("e_toru_audit_file"):
                            textbutton "監査ファイル: 徹の暗号化監査ファイル" action Return("e_toru_audit_file") xfill True
                        if has_evidence("e_lunarborn_medical_report"):
                            textbutton "月生まれ医療評価: 月面生まれ世代の医療評価" action Return("e_lunarborn_medical_report") xfill True
                        if has_evidence("e_sena_dust_trace"):
                            textbutton "袖口の粉塵: セナの袖口に残る極地粉塵" action Return("e_sena_dust_trace") xfill True

            hbox:
                spacing 12
                textbutton "ヒントを見る":
                    action Return("__hint__")

                textbutton "考え直す":
                    action Return("__cancel__")

                textbutton "調査に戻る":
                    action Return("__back_to_investigation__")


screen multi_evidence_choice_screen(question, hint_text, required_count=0):
    zorder 30
    modal True
    default selected_ids = set()

    add "ui_deduction_background"
    add Solid("#02061799")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 1180
        ysize 660

        vbox:
            spacing 14
            text question size 24 color "#f8fafc" xmaximum 1080
            if required_count > 0:
                text "この問題は[required_count]つの証拠を組み合わせます。関係する証拠だけを選んで提示してください。" color "#cbd5e1" size 18
            else:
                text "この問題は複数の証拠を組み合わせます。関係する証拠だけを選んで提示してください。" color "#cbd5e1" size 18
            $ selected_count = len(selected_ids)
            if required_count > 0:
                text "選択中: [selected_count] / [required_count]件" color "#fbbf24" size 17
            else:
                text "選択中: [selected_count]件" color "#fbbf24" size 17

            if len(evidence_unlocked) == 0:
                text "提示できる証拠がありません。調査に戻って、必要な証拠を集めてください。" color "#fecaca" size 20 xmaximum 1020
                null height 360
            else:
                hbox:
                    spacing 10
                    vbox:
                        spacing 4
                        xsize 545
                        if has_evidence("e_r7_decompression_log"):
                            textbutton ("選択中: R-7減圧ログ" if "e_r7_decompression_log" in selected_ids else "R-7減圧ログ") action If("e_r7_decompression_log" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_r7_decompression_log"])), SetScreenVariable("selected_ids", selected_ids | set(["e_r7_decompression_log"]))) xfill True
                        if has_evidence("e_personnel_location_log"):
                            textbutton ("選択中: 位置ログ" if "e_personnel_location_log" in selected_ids else "位置ログ") action If("e_personnel_location_log" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_personnel_location_log"])), SetScreenVariable("selected_ids", selected_ids | set(["e_personnel_location_log"]))) xfill True
                        if has_evidence("e_autopsy_record"):
                            textbutton ("選択中: 検案記録" if "e_autopsy_record" in selected_ids else "検案記録") action If("e_autopsy_record" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_autopsy_record"])), SetScreenVariable("selected_ids", selected_ids | set(["e_autopsy_record"]))) xfill True
                        if has_evidence("e_manual_bulkhead_blood"):
                            textbutton ("選択中: 隔壁の血痕" if "e_manual_bulkhead_blood" in selected_ids else "隔壁の血痕") action If("e_manual_bulkhead_blood" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_manual_bulkhead_blood"])), SetScreenVariable("selected_ids", selected_ids | set(["e_manual_bulkhead_blood"]))) xfill True
                        if has_evidence("e_white_rabbit_usage_log"):
                            textbutton ("選択中: 白兎使用ログ" if "e_white_rabbit_usage_log" in selected_ids else "白兎使用ログ") action If("e_white_rabbit_usage_log" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_white_rabbit_usage_log"])), SetScreenVariable("selected_ids", selected_ids | set(["e_white_rabbit_usage_log"]))) xfill True
                        if has_evidence("e_white_rabbit_co2_absorber"):
                            textbutton ("選択中: CO2吸収材" if "e_white_rabbit_co2_absorber" in selected_ids else "CO2吸収材") action If("e_white_rabbit_co2_absorber" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_white_rabbit_co2_absorber"])), SetScreenVariable("selected_ids", selected_ids | set(["e_white_rabbit_co2_absorber"]))) xfill True
                        if has_evidence("e_white_rabbit_dust_test"):
                            textbutton ("選択中: 関節粉塵検査" if "e_white_rabbit_dust_test" in selected_ids else "関節粉塵検査") action If("e_white_rabbit_dust_test" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_white_rabbit_dust_test"])), SetScreenVariable("selected_ids", selected_ids | set(["e_white_rabbit_dust_test"]))) xfill True
                        if has_evidence("e_thermal_sensor_frost"):
                            textbutton ("選択中: 氷霜成分" if "e_thermal_sensor_frost" in selected_ids else "氷霜成分") action If("e_thermal_sensor_frost" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_thermal_sensor_frost"])), SetScreenVariable("selected_ids", selected_ids | set(["e_thermal_sensor_frost"]))) xfill True
                    vbox:
                        spacing 4
                        xsize 545
                        if has_evidence("e_manual_valve_scratch"):
                            textbutton ("選択中: 補助弁の傷" if "e_manual_valve_scratch" in selected_ids else "補助弁の傷") action If("e_manual_valve_scratch" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_manual_valve_scratch"])), SetScreenVariable("selected_ids", selected_ids | set(["e_manual_valve_scratch"]))) xfill True
                        if has_evidence("e_maintenance_admin_log"):
                            textbutton ("選択中: 保守モード記録" if "e_maintenance_admin_log" in selected_ids else "保守モード記録") action If("e_maintenance_admin_log" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_maintenance_admin_log"])), SetScreenVariable("selected_ids", selected_ids | set(["e_maintenance_admin_log"]))) xfill True
                        if has_evidence("e_earth_meeting_audio"):
                            textbutton ("選択中: 会議音声" if "e_earth_meeting_audio" in selected_ids else "会議音声") action If("e_earth_meeting_audio" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_earth_meeting_audio"])), SetScreenVariable("selected_ids", selected_ids | set(["e_earth_meeting_audio"]))) xfill True
                        if has_evidence("e_noah_testimony"):
                            textbutton ("選択中: ノア証言" if "e_noah_testimony" in selected_ids else "ノア証言") action If("e_noah_testimony" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_noah_testimony"])), SetScreenVariable("selected_ids", selected_ids | set(["e_noah_testimony"]))) xfill True
                        if has_evidence("e_toru_audit_file"):
                            textbutton ("選択中: 監査ファイル" if "e_toru_audit_file" in selected_ids else "監査ファイル") action If("e_toru_audit_file" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_toru_audit_file"])), SetScreenVariable("selected_ids", selected_ids | set(["e_toru_audit_file"]))) xfill True
                        if has_evidence("e_lunarborn_medical_report"):
                            textbutton ("選択中: 月生まれ医療評価" if "e_lunarborn_medical_report" in selected_ids else "月生まれ医療評価") action If("e_lunarborn_medical_report" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_lunarborn_medical_report"])), SetScreenVariable("selected_ids", selected_ids | set(["e_lunarborn_medical_report"]))) xfill True
                        if has_evidence("e_sena_dust_trace"):
                            textbutton ("選択中: 袖口の粉塵" if "e_sena_dust_trace" in selected_ids else "袖口の粉塵") action If("e_sena_dust_trace" in selected_ids, SetScreenVariable("selected_ids", selected_ids - set(["e_sena_dust_trace"])), SetScreenVariable("selected_ids", selected_ids | set(["e_sena_dust_trace"]))) xfill True

            hbox:
                spacing 12
                textbutton "提示する":
                    action Return(selected_ids)
                    sensitive len(evidence_unlocked) > 0 and len(selected_ids) > 0

                textbutton "ヒントを見る":
                    action Return("__hint__")

                textbutton "考え直す":
                    action Return("__cancel__")

                textbutton "調査に戻る":
                    action Return("__back_to_investigation__")


screen person_choice_screen(question, hint_text):
    zorder 30
    modal True

    add "ui_deduction_background"
    add Solid("#02061799")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 1080
        ysize 620

        vbox:
            spacing 16
            text question size 26 color "#f8fafc" xmaximum 980
            text "人物を選んでください。" color "#cbd5e1" size 18

            grid 2 3:
                spacing 12
                frame:
                    style "tsuki_panel"
                    xsize 490
                    ysize 145
                    vbox:
                        spacing 4
                        text "雨宮 セナ" color "#f8fafc" size 20
                        text "シロワの代表" color "#93c5fd" size 15
                        textbutton "指摘する" action Return("sena")
                frame:
                    style "tsuki_panel"
                    xsize 490
                    ysize 145
                    vbox:
                        spacing 4
                        text "北条 リツ" color "#f8fafc" size 20
                        text "アルマの技師" color "#93c5fd" size 15
                        textbutton "指摘する" action Return("ritsu")
                frame:
                    style "tsuki_panel"
                    xsize 490
                    ysize 145
                    vbox:
                        spacing 4
                        text "ルカ・ナディム" color "#f8fafc" size 20
                        text "影井戸の採掘屋" color "#93c5fd" size 15
                        textbutton "指摘する" action Return("luka")
                frame:
                    style "tsuki_panel"
                    xsize 490
                    ysize 145
                    vbox:
                        spacing 4
                        text "白石 アカリ" color "#f8fafc" size 20
                        text "月生まれを診る医師" color "#93c5fd" size 15
                        textbutton "指摘する" action Return("akari")
                frame:
                    style "tsuki_panel"
                    xsize 490
                    ysize 145
                    vbox:
                        spacing 4
                        text "雨宮 ノア" color "#f8fafc" size 20
                        text "月で生まれた娘" color "#93c5fd" size 15
                        textbutton "指摘する" action Return("noah")
                frame:
                    style "tsuki_panel"
                    xsize 490
                    ysize 145
                    vbox:
                        spacing 4
                        text "鷹峰 ジン" color "#f8fafc" size 20
                        text "セレネ社の広報法務" color "#93c5fd" size 15
                        textbutton "指摘する" action Return("jin")

            hbox:
                spacing 12
                textbutton "ヒントを見る":
                    action Return("__hint__")

                textbutton "考え直す":
                    action Return("__cancel__")

                textbutton "調査に戻る":
                    action Return("__back_to_investigation__")


screen timeline_screen():
    tag menu
    zorder 20
    modal True

    add "ui_menu_background"
    add Solid("#020617aa")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 1160
        ysize 650
        background Frame("images/ui/ui_timeline_panel.png", 24, 24)

        vbox:
            spacing 12
            hbox:
                xfill True
                text "事件タイムライン" style "tsuki_title_text"
                text chapter_title xalign 1.0 color "#cbd5e1"
            text "事件の流れを時刻順に確認できます。" color "#94a3b8" size 18

            vbox:
                spacing 5
                text "19:10  澪がシロワに到着 - 地球から来た監査官として白環市に入る。" color "#cbd5e1" size 17
                text "19:40  セナが監査予定を確認 - 都市停止リスクを理由に調査短縮を求める。" color "#cbd5e1" size 17
                text "20:20  徹とルカが口論 - 影井戸の採掘量報告をめぐって対立。" color "#cbd5e1" size 17
                text "21:05  ALMA保守モード開始 - 管理者権限で監視優先順位が切り替わる。" color "#cbd5e1" size 17
                text "21:32  熱センサーに氷霜 - 自然結露では説明しにくい成分が残る。" color "#cbd5e1" size 17
                text "21:46  手動補助弁が操作 - R-7の補助弁に新しい工具傷が残る。" color "#cbd5e1" size 17
                text "21:52  ノアが外口付近で足音を聞く - 母に似た歩き方だった。" color "#cbd5e1" size 17
                text "22:08  地球会議の長い空白 - セナの遠隔出席に移動の余地が残る。" color "#cbd5e1" size 17
                text "22:31  酸素工房R-7が緊急減圧 - ALMAは無人区画と判断した。" color "#cbd5e1" size 17
                text "22:32  徹が隔壁レバーへ手を伸ばす - 隣接区画を守ろうとした。" color "#cbd5e1" size 17
                text "22:34  徹の死亡を確認 - 死因は真空暴露による急性低酸素。" color "#cbd5e1" size 17
                text "翌朝   白兎3号の未使用痕跡 - 船外活動は偽装だったと分かる。" color "#cbd5e1" size 17

            textbutton "閉じる":
                action Return()
                xalign 1.0


screen missing_evidence_screen(missing_names):
    zorder 20
    modal True

    add "ui_deduction_background"
    add Solid("#020617aa")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 980
        ysize 560

        vbox:
            spacing 14
            text "証拠が不足しています" style "tsuki_title_text"
            text "このまま進むとBad Endingへ分岐します。戻って不足証拠を確認できます。" color "#fecaca" size 19 xmaximum 880
            text "不足している重要証拠:" color "#fbbf24"

            $ missing_text = "、".join(missing_names)
            if missing_text == "":
                text "不足証拠の名前を取得できませんでした。調査ハブへ戻って証拠品一覧を確認してください。" color "#e5e7eb" size 18 xmaximum 880
            else:
                text missing_text color "#e5e7eb" size 18 xmaximum 880

            hbox:
                spacing 12
                textbutton "調査に戻る":
                    action Return("back")
                textbutton "証拠不足のまま進む":
                    action Return("continue")


screen interview_progress_warning_screen(done_count, required_count, missing_names):
    zorder 20
    modal True

    add "ui_menu_background"
    add Solid("#020617aa")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 420

        vbox:
            spacing 18
            text "聞き込みが不足しています" style "tsuki_title_text"
            text "第4章へ進むには、最低4人への初回聞き込みが必要です。" color "#f8fafc" size 20 xmaximum 820
            text "現在の聞き込み済み: [done_count] / [required_count]" color "#fbbf24" size 20

            if len(missing_names) > 0:
                $ missing_text = "、".join(missing_names)
                text "未聞き込み: [missing_text]" color "#cbd5e1" size 18 xmaximum 820

            textbutton "聞き込みに戻る":
                action Return("back")
                xalign 0.5


screen deduction_result_screen(result_text, ending_name):
    zorder 20
    modal True

    add "ui_deduction_background"
    add Solid("#02061799")

    frame:
        style "tsuki_frame"
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 390

        vbox:
            spacing 14
            text "推理結果" style "tsuki_title_text"
            text result_text color "#f8fafc" size 24
            text "到達予定: [ending_name]" color "#fbbf24" size 22
            if ending_name == "True Ending":
                text "動機と最後の行動まで示せました。真相は、夜明けの窓へ向かいます。" color "#cbd5e1"
            elif ending_name == "Normal Ending":
                text "犯人と手口は示せましたが、すべての痛みまではすくいきれていません。" color "#cbd5e1"
            else:
                text "重要な証拠が欠けています。真相は記録の底へ沈みます。" color "#cbd5e1"
            textbutton "エンディングへ":
                action Return()
                xalign 1.0


screen alma_log_screen(title, lines):
    zorder 20
    modal True

    add "ui_menu_background"
    add Solid("#01050abb")

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
