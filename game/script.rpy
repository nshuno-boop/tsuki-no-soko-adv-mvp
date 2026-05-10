# 『月の底で、息をする』MVPプロトタイプ。
# 目的: 証拠入手、聞き込み、最終推理、エンディング分岐の骨組みを確認する。

label start:
    $ set_chapter(0, "プロローグ")

    scene bg lander_interior
    show mio neutral at left
    show alma idle at right
    sysmsg "2056年。月面南極都市《白環市》。住民たちはその街を、短く『シロワ』と呼ぶ。"
    sysmsg "地球監査局の新人監査官・佐伯澪は、生命維持主任・檜山徹の死亡事故を調査するため、シロワへ降り立った。"

    m "事故に見える。けれど、記録はいつも何かを隠している。"
    alma "ようこそ、佐伯監査官。都市管理AI、ALMAです。読みはアルマ。調査権限を確認しました。"

    scene bg shirowa_hab_ring
    show mio thinking at left
    show alma speaking at right
    sysmsg "中央居住環。冷たい機能美の中に、居住区の洗濯物と修理痕が混じっている。"
    noah "アルマさん、地球の監査官って本当に来たんだ。"
    m "あなたが雨宮ノア？"
    noah "うん。シロワで生まれた、ただの子ども。……たぶんね。"

    $ set_chapter(1, "白い事故")

    scene bg oxygen_workshop_r7
    show mio pained at left
    show alma alert at right
    sysmsg "酸素工房R-7。檜山徹は緊急減圧により死亡した。"
    $ r7_log_lines = ["AREA: OXYGEN WORKSHOP R-7", "STATUS: DEPRESSURIZATION APPROVED", "HUMAN PRESENCE: NONE", "OPERATOR NOTE: Hiyama Toru missing from visual feed"]
    call screen alma_log_screen("R-7 EMERGENCY EVENT", r7_log_lines)
    $ add_evidence("e_r7_decompression_log")

    m "R-7は『無人』と判定されている。でも、檜山主任はここにいた。"

    scene bg outer_port
    show mio thinking at left
    show ritsu anxious at right
    sysmsg "外口。事故当時に使われたとされる宇宙服、正式型番HAKU-3。通称『白兎3号』が保管されていた。"
    ritsu "白兎3号のログが、ほとんど空なんです。CO2吸収材も、交換された形跡がありません。"
    $ add_evidence("e_white_rabbit_co2_absorber")

    jump investigation_menu


label investigation_menu:
    scene bg shirowa_hab_ring
    show mio neutral at left
    sysmsg "聞き込み対象を選んでください。必要な証拠が揃ったと思ったら、最終推理へ進めます。"

    call screen investigation_hub_screen
    $ hub_choice = _return

    if hub_choice == "evidence":
        call screen evidence_screen
        jump investigation_menu
    elif hub_choice == "people":
        call screen person_memo_screen
        jump investigation_menu
    elif hub_choice == "alma":
        $ audit_log_lines = ["CITY: SHIROWA / OFFICIAL: HAKKAN CITY", "AI: ALMA", "PRIMARY INCIDENT: OXYGEN WORKSHOP R-7", "WARNING: sensor streams are not fully consistent"]
        call screen alma_log_screen("CURRENT AUDIT SNAPSHOT", audit_log_lines)
        jump investigation_menu
    elif hub_choice == "final":
        jump pre_final_reasoning
    elif hub_choice == "interview:noah":
        jump interview_noah
    elif hub_choice == "interview:sena":
        jump interview_sena
    elif hub_choice == "interview:ritsu":
        jump interview_ritsu
    elif hub_choice == "interview:luka":
        jump interview_luka
    elif hub_choice == "interview:akari":
        jump interview_akari
    elif hub_choice == "interview:jin":
        jump interview_jin
    else:
        jump investigation_menu


label interview_noah:
    $ set_chapter(2, "矛盾する目")
    scene bg core
    show mio thinking at left
    show noah rebellious at center
    show alma speaking at right

    noah "わたし、R-7を見てた。アルマさんが見ていたR-7と、補助センサーが見ていたR-7は違ったの。"
    m "映像では無人。生体センサーでは反応あり……。"
    noah "うん。誰かが、アルマさんに違う現実を見せた。"

    $ interview_done.add("noah")
    $ add_evidence("e_noah_testimony")
    call maybe_unlock_audit_file
    jump investigation_menu


label interview_sena:
    $ set_chapter(2, "都市の責任")
    scene bg sena_office
    show mio neutral at left
    show sena calm at right

    sena "シロワは、一度でも生命維持を止めれば終わります。地球の監査は、時に現場を殺す。"
    m "檜山主任は、都市運用に関する監査ファイルを準備していた。あなたは知っていましたか？"
    sena "監査官。都市を守る責任は、きれいな正義だけでは果たせません。"

    $ interview_done.add("sena")
    $ add_evidence("e_earth_meeting_audio")
    call maybe_unlock_audit_file
    jump investigation_menu


label interview_ritsu:
    $ set_chapter(3, "同期のずれ")
    scene bg core
    show mio thinking at left
    show ritsu angry at right
    show alma idle at center

    ritsu "ALMAの中核コードには触られていません。そこは断言できます。"
    ritsu "ただ、事故前夜に監視系の再同期がかかってる。しかもコアの管理者権限で。"
    m "ALMAを書き換えたんじゃない。ALMAが見る入力をずらした……。"

    $ interview_done.add("ritsu")
    $ add_evidence("e_admin_authority_log")
    call maybe_unlock_audit_file
    jump investigation_menu


label interview_luka:
    $ set_chapter(3, "影井戸の水")
    scene bg shadow_well
    show mio neutral at left
    show luka sarcastic at right

    luka "影井戸の水を地球に売れば、シロワは延命できる。売らなければ、次の冬で詰む。"
    m "セレネ社は、その契約を急いでいた？"
    luka "急いでいたなんてもんじゃない。鷹峰は、事故も契約リスクの一部として見てたよ。"

    $ interview_done.add("luka")
    call maybe_unlock_audit_file
    jump investigation_menu


label interview_akari:
    $ set_chapter(3, "最後の呼吸")
    scene bg medbay
    show mio pained at left
    show akari doctor at right

    akari "檜山さんの肺には、真空暴露に一致する損傷がありました。けれど、宇宙服で耐えた形跡がありません。"
    m "白兎3号は飾りだった。事故説明を成立させるための。"
    akari "それと、檜山さんの個人端末に暗号化された監査ファイルの断片が残っていました。"

    $ interview_done.add("akari")
    call maybe_unlock_audit_file
    jump investigation_menu


label interview_jin:
    $ set_chapter(3, "セレネ社の線引き")
    scene bg sena_office
    show mio neutral at left
    show jin business_smile at right

    jin "セレネ資源開発としては、事故調査に全面的に協力します。もちろん、契約情報には守秘義務がありますが。"
    m "檜山主任の監査ファイルも、守秘義務の中ですか？"
    jin "監査官。言葉は選んだ方がいい。月では、沈黙も資源です。"

    $ interview_done.add("jin")
    call maybe_unlock_audit_file
    jump investigation_menu


label maybe_unlock_audit_file:
    # ノア・セナ・リツ・アカリの聞き込みが揃うと、最終証拠に到達する。
    if {"noah", "sena", "ritsu", "akari"}.issubset(interview_done):
        if "e_toru_audit_file" not in evidence_unlocked:
            scene bg core
            show toru recording at center
            sysmsg "断片化された記録がつながり、檜山徹の暗号化監査ファイルが復号された。"
            $ add_evidence("e_toru_audit_file")
    return


label pre_final_reasoning:
    scene bg core
    show mio thinking at left
    show alma alert at right

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

    scene bg core
    show mio neutral at left
    show sena neutral at right
    show alma speaking at center
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
    scene bg dawn_window
    show mio neutral at left

    $ max_score = len(deduction_questions)
    $ has_final_key = "e_toru_audit_file" in evidence_unlocked

    if deduction_score == max_score and deduction_hint_count <= 1 and has_final_key:
        jump true_ending
    elif deduction_score >= 3:
        jump normal_ending
    else:
        jump bad_ending


label true_ending:
    scene bg dawn_window
    show mio neutral at left
    show sena broken at right
    sysmsg "True Ending: 月の底で、息をする"
    m "ALMAは殺していない。あなたは、ALMAに嘘の現実を見せた。"
    sena "……都市を守るには、誰かが月の底に沈む必要があった。"
    alma "記録を更新します。白環市R-7事故は、偽装殺人として再分類されました。"
    sysmsg "澪はシロワの沈黙を破り、檜山徹の監査ファイルを地球へ送信した。"
    return


label normal_ending:
    scene bg dawn_window
    show mio pained at left
    sysmsg "Normal Ending: 白い報告書"
    m "事故ではない。けれど、最後の一線までは届かなかった。"
    sysmsg "澪の報告によりR-7事故は再調査となる。シロワには、まだ多くの沈黙が残された。"
    return


label bad_ending:
    scene bg dawn_window
    show mio pained at left
    show alma alert at right
    sysmsg "Bad Ending: 無人区画"
    alma "証拠不足です。R-7事故は、ALMA運用上の例外処理として記録されます。"
    m "違う。何かが、まだ見えていない。"
    sysmsg "シロワは静かに呼吸を続ける。月の底で、誰にも聞こえないまま。"
    return
