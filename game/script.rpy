# 『月の底で、息をする』MVPプロトタイプ。
# 目的: 証拠入手、聞き込み、最終推理、エンディング分岐の骨組みを確認する。

label start:
    $ set_chapter(0, "プロローグ")

    scene bg white_ring
    sysmsg "2056年。月面南極都市《白環市》。"
    sysmsg "地球監査局の新人監査官・佐伯澪は、生命維持主任・檜山徹の死亡事故を調査するため、白い環の都市へ降り立った。"

    m "事故に見える。けれど、記録はいつも何かを隠している。"
    alma "ようこそ、佐伯監査官。都市管理AI、ALMAです。調査権限を確認しました。"

    $ set_chapter(1, "白い事故")

    scene bg r7
    sysmsg "資源精製区R-7。檜山徹は緊急減圧により死亡した。"
    $ add_evidence("r7_decompression_log")

    m "R-7は『無人』と判定されている。でも、檜山主任はここにいた。"
    sysmsg "R-7保管庫から、事故当時に使われたとされる宇宙服HAKU-3が回収された。"
    $ add_evidence("haku3_unused")

    jump investigation_menu


label investigation_menu:
    scene bg admin
    sysmsg "聞き込み対象を選んでください。必要な証拠が揃ったと思ったら、最終推理へ進めます。"

    menu:
        "保守用子AIノアに聞く":
            jump interview_noa

        "都市運用責任者・雨宮セナに聞く":
            jump interview_sena

        "管制技師・九条カイに聞く":
            jump interview_kai

        "医療記録担当・白石ルイに聞く":
            jump interview_rui

        "証拠品一覧を見る":
            call screen evidence_screen
            jump investigation_menu

        "聞き込みを終えて最終推理へ進む":
            jump pre_final_reasoning


label interview_noa:
    $ set_chapter(2, "矛盾する目")
    scene bg alma_core

    noa "ぼくは、R-7を見ていました。でも、ALMAお姉さんが見ていたR-7と、ぼくの補助センサーが見ていたR-7は違いました。"
    m "映像では無人。生体センサーでは反応あり……。"
    noa "はい。誰かが、ALMAお姉さんに違う現実を見せました。"

    $ interview_done.add("noa")
    $ add_evidence("noa_testimony")
    call maybe_unlock_audit_file
    jump investigation_menu


label interview_sena:
    $ set_chapter(2, "都市の責任")
    scene bg council

    sena "白環市は、一度でも生命維持を止めれば終わります。地球の監査は、時に現場を殺す。"
    m "檜山主任は、都市運用に関する監査ファイルを準備していた。あなたは知っていましたか？"
    sena "監査官。都市を守る責任は、きれいな正義だけでは果たせません。"

    $ interview_done.add("sena")
    $ add_evidence("earth_conference_audio")
    call maybe_unlock_audit_file
    jump investigation_menu


label interview_kai:
    $ set_chapter(3, "同期のずれ")
    scene bg admin

    kai "ALMAの中核コードには触られていない。そこは断言できる。"
    kai "ただ、事故前夜に監視系の再同期がかかってる。しかも管理者権限でね。"
    m "ALMAを書き換えたんじゃない。ALMAが見る入力をずらした……。"

    $ interview_done.add("kai")
    $ add_evidence("admin_authority_log")
    call maybe_unlock_audit_file
    jump investigation_menu


label interview_rui:
    $ set_chapter(3, "最後の呼吸")
    scene bg r7

    rui "檜山さんの肺には、真空暴露に一致する損傷がありました。けれど、宇宙服で耐えた形跡がありません。"
    m "HAKU-3は飾りだった。事故説明を成立させるための。"
    rui "それと、檜山さんの個人端末に暗号化された監査ファイルの断片が残っていました。"

    $ interview_done.add("rui")
    call maybe_unlock_audit_file
    jump investigation_menu


label maybe_unlock_audit_file:
    # ノア・セナ・カイ・ルイの聞き込みが揃うと、最終証拠に到達する。
    if {"noa", "sena", "kai", "rui"}.issubset(interview_done):
        if "hiyama_audit_file" not in evidence_unlocked:
            sysmsg "断片化された記録がつながり、檜山徹の暗号化監査ファイルが復号された。"
            $ add_evidence("hiyama_audit_file")
    return


label pre_final_reasoning:
    scene bg council

    if len(interview_done) < 3:
        m "まだ聞ける相手が残っている。このまま推理に入るのは危険かもしれない。"
        menu:
            "それでも最終推理へ進む":
                jump final_reasoning
            "聞き込みに戻る":
                jump investigation_menu
    else:
        jump final_reasoning


label final_reasoning:
    $ set_chapter(4, "月の底で、息をする")
    $ deduction_score = 0
    $ deduction_mistakes = 0
    $ deduction_hint_count = 0

    scene bg council
    sysmsg "最終推理を開始します。問題ごとに、対応する証拠を提示してください。"

    $ question_index = 0
    while question_index < len(deduction_questions):
        $ current_question = deduction_questions[question_index]
        call ask_deduction_question(current_question)
        $ question_index += 1

    jump ending_branch


label ask_deduction_question(question_data):
    $ attempts = 0
    $ solved = False

    while not solved and attempts < 2:
        call screen evidence_choice_screen(question_data["prompt"], question_data["hint"])
        $ selected_evidence = _return

        if selected_evidence == "__hint__":
            $ deduction_hint_count += 1
            $ hint_text = question_data["hint"]
            sysmsg "[hint_text]"

        elif selected_evidence == "__cancel__":
            m "ここで引くわけにはいかない。証拠を選ぼう。"

        elif selected_evidence == question_data["answer"]:
            $ solved = True
            $ deduction_score += 1
            $ success_text = question_data["success"]
            sysmsg "正解。 [success_text]"

        else:
            $ attempts += 1
            $ deduction_mistakes += 1
            if attempts < 2:
                $ failure_text = question_data["failure"]
                sysmsg "不正解。 [failure_text]"
            else:
                $ hint_text = question_data["hint"]
                sysmsg "不正解。ここでは突破できなかった。ヒント: [hint_text]"

    return


label ending_branch:
    scene bg ending

    $ max_score = len(deduction_questions)
    $ has_final_key = "hiyama_audit_file" in evidence_unlocked

    if deduction_score == max_score and deduction_hint_count <= 1 and has_final_key:
        jump true_ending
    elif deduction_score >= 3:
        jump normal_ending
    else:
        jump bad_ending


label true_ending:
    sysmsg "True Ending: 月の底で、息をする"
    m "ALMAは殺していない。あなたは、ALMAに嘘の現実を見せた。"
    sena "……都市を守るには、誰かが月の底に沈む必要があった。"
    alma "記録を更新します。白環市R-7事故は、偽装殺人として再分類されました。"
    sysmsg "澪は白環市の沈黙を破り、檜山徹の監査ファイルを地球へ送信した。"
    return


label normal_ending:
    sysmsg "Normal Ending: 白い報告書"
    m "事故ではない。けれど、最後の一線までは届かなかった。"
    sysmsg "澪の報告によりR-7事故は再調査となる。白環市には、まだ多くの沈黙が残された。"
    return


label bad_ending:
    sysmsg "Bad Ending: 無人区画"
    alma "証拠不足です。R-7事故は、ALMA運用上の例外処理として記録されます。"
    m "違う。何かが、まだ見えていない。"
    sysmsg "白環市は静かに呼吸を続ける。月の底で、誰にも聞こえないまま。"
    return

