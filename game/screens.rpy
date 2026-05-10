# MVP用の簡易スクリーン。
# 本格UI化するときも、証拠IDを返す設計はそのまま使える。

screen evidence_screen():
    tag menu
    modal True
    default selected_id = None

    add Solid("#030712")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1120
        ysize 620
        padding (28, 24)
        background "#111827ee"

        vbox:
            spacing 18

            hbox:
                xfill True
                text "証拠品一覧" size 34 color "#f8fafc"
                text "第[chapter]章  [chapter_title]" xalign 1.0 color "#cbd5e1"

            if len(evidence_unlocked) == 0:
                text "まだ証拠品はありません。" color "#cbd5e1"
            else:
                hbox:
                    spacing 22

                    viewport:
                        xsize 390
                        ysize 470
                        mousewheel True
                        scrollbars "vertical"

                        vbox:
                            spacing 8
                            for evidence_id in ordered_unlocked_evidence():
                                $ item = evidence_catalog[evidence_id]
                                textbutton item["name"]:
                                    action SetScreenVariable("selected_id", evidence_id)
                                    xfill True

                    frame:
                        xfill True
                        yfill True
                        padding (20, 18)
                        background "#020617"

                        if selected_id is None:
                            text "左のリストから証拠品を選択してください。" color "#cbd5e1"
                        else:
                            $ selected = evidence_catalog[selected_id]
                            $ selected_chapter = selected["chapter"]
                            vbox:
                                spacing 12
                                text selected["name"] size 28 color "#f8fafc"
                                text "入手章: 第[selected_chapter]章" color "#93c5fd"
                                null height 4
                                text selected["summary"] color "#e5e7eb"
                                text selected["detail"] color "#cbd5e1"

            textbutton "閉じる":
                action Return()
                xalign 1.0


screen evidence_choice_screen(question, hint_text):
    modal True

    add Solid("#020617")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1160
        ysize 650
        padding (28, 24)
        background "#111827ee"

        vbox:
            spacing 18

            text question size 28 color "#f8fafc"
            text "提示する証拠を選んでください。" color "#cbd5e1"

            if len(evidence_unlocked) == 0:
                text "提示できる証拠がありません。" color "#fecaca"
            else:
                viewport:
                    xfill True
                    ysize 450
                    mousewheel True
                    scrollbars "vertical"

                    vbox:
                        spacing 10
                        for evidence_id in ordered_unlocked_evidence():
                            $ item = evidence_catalog[evidence_id]
                            frame:
                                xfill True
                                padding (16, 14)
                                background "#020617"

                                hbox:
                                    spacing 18
                                    vbox:
                                        xfill True
                                        spacing 5
                                        text item["name"] size 22 color "#f8fafc"
                                        text item["summary"] color "#cbd5e1"

                                    textbutton "提示":
                                        action Return(evidence_id)
                                        xminimum 100

            hbox:
                spacing 12
                textbutton "ヒントを見る":
                    action Return("__hint__")

                textbutton "考え直す":
                    action Return("__cancel__")
