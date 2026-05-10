# 『月の底で、息をする』Phase 3 MVP。
# プロローグから3エンディングまで、仮素材で通しプレイできる骨組み。

label start:
    show screen objective_overlay
    $ set_chapter(0, "プロローグ：シロワへようこそ", "徹との約束の時間まで、シロワの中を確認する")

    scene bg lander_interior
    show mio neutral at left
    show alma idle at right
    sysmsg "2056年。月面南極都市《白環市》。住民たちはその街を、短く『シロワ』と呼ぶ。"
    alma "ようこそ、佐伯監査官。都市管理AI、ALMAです。読みはアルマ。調査権限を確認しました。"
    m "ここでは、空気も水も記録も、誰かが守り続けているんですね。"

    scene bg shirowa_hab_ring
    show mio neutral at left
    show sena smile at right
    sena "シロワへようこそ。地球の監査官を迎えるには、少し狭い街ですが。"
    m "佐伯澪です。監査は手短に、でも正確に進めます。"
    sena "正確さは大切です。ここでは、小さな誤差が人の呼吸を止めますから。"

    scene bg core
    show toru gentle at center
    t "佐伯監査官。生命維持主任の檜山徹です。今夜22:30、少し話せませんか。"
    t "ALMAのログは正しい。けれど、正しいログだけでは見えないものがあります。"
    m "それは、監査に関わる話ですか？"
    t "シロワの空気に関わる話です。"

    jump chapter1


label chapter1:
    $ set_chapter(1, "第1章：息が止まった夜", "酸素工房R-7の事故現場を調べる")

    scene bg oxygen_workshop_r7
    show mio pained at left
    show alma alert at right
    sysmsg "22:31。酸素工房R-7で緊急減圧が発生。檜山徹は死亡した。"
    $ r7_log_lines = ["AREA: OXYGEN WORKSHOP R-7", "STATUS: DEPRESSURIZATION APPROVED", "HUMAN PRESENCE: NONE", "FATALITY: HIYAMA TORU"]
    call screen alma_log_screen("R-7 EMERGENCY EVENT", r7_log_lines)
    $ add_evidence("e_r7_decompression_log")

    m "R-7は無人判定。なのに、徹さんはここで死んでいる。"
    $ add_evidence("e_personnel_location_log")

    scene bg medbay
    show mio pained at left
    show akari doctor at right
    akari "死因は真空暴露による急性低酸素。外で倒れたのではなく、区画の中で空気を奪われた身体です。"
    $ add_evidence("e_autopsy_record")

    scene bg oxygen_workshop_r7
    show mio thinking at left
    sysmsg "手動隔壁レバーの根元に、乾いた血痕が残っていた。"
    m "徹さんは、最後に逃げようとしたんじゃない。隔壁を閉じようとした。"
    $ add_evidence("e_manual_bulkhead_blood")

    jump chapter2


label chapter2:
    $ set_chapter(2, "第2章：アルマは嘘をつかない", "ALMAの判断ログを確認する")

    scene bg core
    show mio thinking at left
    show ritsu neutral at right
    show alma speaking at center
    ritsu "ALMAの中核コードに改ざんはありません。アルマさんは規定通り動いています。"
    alma "記録上、檜山徹のビーコンは外口側へ移動。R-7内は無人と判定されました。"
    $ add_evidence("e_white_rabbit_usage_log")

    ritsu "保守モード中は、作業員ビーコンと外部カメラが優先されます。現場作業では安全な仕様なんです。"
    m "安全な仕様を、誰かが逆手に取った。"
    $ add_evidence("e_maintenance_admin_log")

    scene bg oxygen_workshop_r7
    show mio thinking at left
    show ritsu anxious at right
    ritsu "熱センサーに氷霜。自然結露にしては成分が変です。"
    $ add_evidence("e_thermal_sensor_frost")
    ritsu "それと、手動補助弁に新しい工具傷があります。自然故障だけでは説明できません。"
    $ add_evidence("e_manual_valve_scratch")

    jump chapter3_hub


label chapter3_hub:
    $ set_chapter(3, "第3章：影井戸の数字", "住民たちから徹の人間関係を聞き出す")

    scene bg shirowa_hab_ring
    show mio neutral at left
    sysmsg "徹が残した違和感は、シロワの人間関係と資源問題へつながっていく。"

    if len(interview_done) >= 4 and not has_evidence("e_toru_audit_file"):
        scene bg core
        show toru recording at center
        sysmsg "聞き込みで得た断片がつながり、徹の暗号化監査ファイルの一部が復号された。"
        $ add_evidence("e_toru_audit_file")
        scene bg shirowa_hab_ring
        show mio neutral at left

    call screen investigation_hub_screen
    $ hub_choice = _return

    if hub_choice == "evidence":
        call screen evidence_screen
        jump chapter3_hub
    elif hub_choice == "people":
        call screen person_memo_screen
        jump chapter3_hub
    elif hub_choice == "alma":
        $ audit_log_lines = ["CITY: SHIROWA / OFFICIAL: HAKKAN CITY", "AI: ALMA", "MODE: MAINTENANCE PRIORITY WINDOW FOUND", "WARNING: BEACON STREAM AND BIOMETRIC TRACE DO NOT MATCH"]
        call screen alma_log_screen("CURRENT AUDIT SNAPSHOT", audit_log_lines)
        jump chapter3_hub
    elif hub_choice == "interview:sena":
        call interview_sena
        jump chapter3_hub
    elif hub_choice == "interview:ritsu":
        call interview_ritsu
        jump chapter3_hub
    elif hub_choice == "interview:luka":
        call interview_luka
        jump chapter3_hub
    elif hub_choice == "interview:akari":
        call interview_akari
        jump chapter3_hub
    elif hub_choice == "interview:noah":
        call interview_noah
        jump chapter3_hub
    elif hub_choice == "interview:jin":
        call interview_jin
        jump chapter3_hub
    elif hub_choice == "final":
        if len(interview_done) >= 4:
            jump chapter4
        else:
            m "まだ聞ける相手が多い。このまま白兎3号へ進むには、材料が足りない。"
            jump chapter3_hub
    else:
        jump chapter3_hub


label chapter4:
    $ set_chapter(4, "第4章：白兎は外へ出なかった", "白兎3号が本当に外へ出たのか確かめる")

    scene bg outer_port
    show mio thinking at left
    show ritsu anxious at right
    sysmsg "外口。正式型番HAKU-3、通称『白兎3号』は、事故当時に船外活動へ出たことになっている。"
    ritsu "CO2吸収材は未使用に近い。白兎3号は、徹さんを守るほど動いていません。"
    $ add_evidence("e_white_rabbit_co2_absorber")
    $ add_evidence("e_white_rabbit_dust_test")

    scene bg sena_office
    show mio neutral at left
    show jin irritated at right
    jin "地球会議の音声です。セレネ社としては、これ以上の提供はかなり譲歩しています。"
    $ add_evidence("e_earth_meeting_audio")

    scene bg outer_port
    show mio thinking at left
    show noah tears at right
    noah "外口の近くで、足音を聞いた。母さんの歩き方に似てた。でも、言いたくなかった。"
    $ add_evidence("e_noah_testimony")

    scene bg shadow_well
    show mio thinking at left
    show luka sad at right
    luka "この粉塵は影井戸側のものだ。執務室だけにいた人間の袖につく粉じゃない。"
    $ add_evidence("e_sena_dust_trace")

    jump chapter5_hub


label chapter5_hub:
    $ set_chapter(5, "最終章：だれのための空", "証拠を揃え、最後の推理に進む")

    scene bg core
    show mio neutral at left
    show alma speaking at right
    sysmsg "管制核。証拠はそろいつつある。あとは、誰のために空気が奪われたのかを示すだけだ。"

    call screen investigation_hub_screen
    $ hub_choice = _return

    if hub_choice == "evidence":
        call screen evidence_screen
        jump chapter5_hub
    elif hub_choice == "people":
        call screen person_memo_screen
        jump chapter5_hub
    elif hub_choice == "alma":
        $ final_log_lines = ["FINAL AUDIT READY", "ALMA CORE INTEGRITY: CLEAN", "INPUT REALITY: COMPROMISED", "RECOMMENDATION: HUMAN DEDUCTION REQUIRED"]
        call screen alma_log_screen("FINAL ALMA LOG", final_log_lines)
        jump chapter5_hub
    elif hub_choice == "interview:sena":
        call interview_sena
        jump chapter5_hub
    elif hub_choice == "interview:ritsu":
        call interview_ritsu
        jump chapter5_hub
    elif hub_choice == "interview:luka":
        call interview_luka
        jump chapter5_hub
    elif hub_choice == "interview:akari":
        call interview_akari
        jump chapter5_hub
    elif hub_choice == "interview:noah":
        call interview_noah
        jump chapter5_hub
    elif hub_choice == "interview:jin":
        call interview_jin
        jump chapter5_hub
    elif hub_choice == "final":
        jump pre_final_reasoning
    else:
        jump chapter5_hub


label interview_sena:
    scene bg sena_office
    show mio neutral at left
    show sena calm at right

    if "sena_initial" not in interview_flags:
        sena "事故として処理できるなら、それが一番です。シロワに長い停止は許されません。"
        m "事故と決めるには早すぎます。徹さんは22:30に、私へ話したいと言っていました。"
        sena "……檜山さんは、いつも空気の薄い話をする人でした。"
        $ interview_flags.add("sena_initial")
        $ interview_done.add("sena")
    elif "sena_additional" not in interview_flags and has_evidence("e_toru_audit_file"):
        sena "檜山さんが告発を準備していたことは知っていました。ですが、告発は都市を救うとは限りません。"
        m "隠すことも、救うこととは限らない。"
        $ interview_flags.add("sena_additional")
    elif chapter >= 5 and "sena_core" not in interview_flags:
        show sena shaken at right
        sena "都市が閉じれば、ノアたちは地球で生きられない。私は代表で、母親でもあるんです。"
        m "その恐れが、徹さんを殺す理由にはなりません。"
        $ interview_flags.add("sena_core")
    else:
        sena "監査官。シロワには、正しさだけでは守れない空気があります。"
    return


label interview_ritsu:
    scene bg core
    show mio thinking at left
    show ritsu neutral at right
    show alma idle at center

    if "ritsu_initial" not in interview_flags:
        ritsu "ALMAは規定通り動きました。少なくとも、ログを自分で書き換えるようなAIではありません。"
        alma "自己改ざんの記録はありません。"
        $ interview_flags.add("ritsu_initial")
        $ interview_done.add("ritsu")
    elif "ritsu_additional" not in interview_flags and has_evidence("e_maintenance_admin_log"):
        ritsu "保守モード中はビーコン優先です。現場の作業員を守るための仕様でした。"
        m "でも今回は、ビーコンが嘘の居場所を作った。"
        $ interview_flags.add("ritsu_additional")
    elif chapter >= 5 and "ritsu_core" not in interview_flags:
        show ritsu relieved at right
        ritsu "ALMAは嘘をついていません。嘘の入力を、正しく信じたんです。"
        m "犯人はAIではなく、AIの目を塞いだ人間。"
        $ interview_flags.add("ritsu_core")
    else:
        ritsu "アルマさんを疑うなら、まず入力の流れを見てください。"
    return


label interview_luka:
    scene bg shadow_well
    show mio neutral at left
    show luka sarcastic at right

    if "luka_initial" not in interview_flags:
        luka "徹とは口論したよ。影井戸の採掘量を盛るなって、あいつは何度も言った。"
        m "あなたには、徹さんを黙らせる理由があった？"
        luka "あったかもな。でも殺す理由はない。空気を守るやつを殺して、誰が得する。"
        $ interview_flags.add("luka_initial")
        $ interview_done.add("luka")
    elif "luka_additional" not in interview_flags and has_evidence("e_toru_audit_file"):
        show luka sad at right
        luka "採掘量不足は本当だ。セレネ社に見せる数字は、きれいに磨かれてた。"
        $ interview_flags.add("luka_additional")
    elif chapter >= 5 and "luka_core" not in interview_flags:
        show luka sad at right
        luka "徹とは対立してた。でも友人でもあった。あいつは街を売る気なんかなかったよ。"
        $ interview_flags.add("luka_core")
    else:
        luka "影井戸は嘘を嫌う。暗い場所ほど、数字だけは正直でないと死ぬ。"
    return


label interview_akari:
    scene bg medbay
    show mio pained at left
    show akari doctor at right

    if "akari_initial" not in interview_flags:
        akari "徹さんの死因は真空暴露。宇宙服で耐えた痕跡はありません。"
        m "外で倒れたのではなく、R-7の中で空気を奪われた。"
        $ interview_flags.add("akari_initial")
        $ interview_done.add("akari")
    elif "akari_additional" not in interview_flags:
        akari "月面生まれの世代は、急な地球移住に耐えられない子がいます。ノアも、その評価対象です。"
        $ add_evidence("e_lunarborn_medical_report")
        $ interview_flags.add("akari_additional")
    elif chapter >= 5 and "akari_core" not in interview_flags:
        akari "徹さんは都市を壊したかったんじゃありません。嘘を外して、作り直したかったんです。"
        $ interview_flags.add("akari_core")
    else:
        akari "医療記録は、政治より残酷です。でも、ときどき政治より優しい。"
    return


label interview_noah:
    scene bg dawn_window
    show mio neutral at left
    show noah rebellious at right

    if "noah_initial" not in interview_flags:
        noah "父さんはシロワを壊そうとしてた。母さんは街を守ってる。だから、わたしは母さんの味方。"
        m "徹さんが本当に壊そうとしていたのは、街ではなく嘘かもしれない。"
        $ interview_flags.add("noah_initial")
        $ interview_done.add("noah")
    elif "noah_additional" not in interview_flags and has_evidence("e_earth_meeting_audio"):
        show noah tears at right
        noah "外口の近くで足音を聞いた。母さんに似てた。でも、そうだって言いたくなかった。"
        $ interview_flags.add("noah_additional")
    elif chapter >= 5 and "noah_core" not in interview_flags:
        show noah tears at right
        noah "父さんは、わたしを地球に捨てようとしてたんじゃないの？"
        m "違う。徹さんは、君が嘘のない街で息をできるようにしたかった。"
        $ interview_flags.add("noah_core")
    else:
        noah "アルマさんは、嘘を嫌うよ。人間よりずっと。"
    return


label interview_jin:
    scene bg sena_office
    show mio neutral at left
    show jin business_smile at right

    if "jin_initial" not in interview_flags:
        jin "セレネ資源開発としては、事故調査に全面的に協力します。企業責任とは別の話ですが。"
        m "その線引きで、人が死んでも？"
        $ interview_flags.add("jin_initial")
        $ interview_done.add("jin")
    elif "jin_additional" not in interview_flags and has_evidence("e_toru_audit_file"):
        show jin irritated at right
        jin "採掘量報告に問題があったことは認めます。ですが、それは殺人の指示ではありません。"
        $ interview_flags.add("jin_additional")
    elif chapter >= 5 and "jin_core" not in interview_flags:
        show jin defeated at right
        jin "会社の圧力はありました。けれど、檜山徹を殺す判断は、企業会議の議事録にはない。"
        $ interview_flags.add("jin_core")
    else:
        jin "言葉は便利です。責任を遠ざけるには、特に。"
    return


label pre_final_reasoning:
    $ set_chapter(5, "最終章：だれのための空", "証拠を揃え、最後の推理に進む")
    scene bg core
    show mio thinking at left
    show alma alert at right

    $ missing_ids = missing_final_evidence()
    if len(missing_ids) > 0:
        $ missing_names = evidence_names(missing_ids)
        call screen missing_evidence_screen(missing_names)
        $ missing_choice = _return
        if missing_choice == "back":
            jump chapter5_hub
        $ final_forced_bad = True
    else:
        $ final_forced_bad = False

    jump final_reasoning


label final_reasoning:
    $ set_chapter(5, "最終章：だれのための空", "証拠を提示し、事件の構造を明らかにする")
    $ deduction_score = 0
    $ deduction_mistakes = 0
    $ deduction_hint_count = 0
    $ deduction_key_failures = 0

    scene bg core
    show mio neutral at left
    show sena neutral at right
    show alma speaking at center
    sysmsg "最終推理を開始します。問題ごとに、対応する証拠または人物を提示してください。"

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
        if question_data["kind"] == "person":
            call screen person_choice_screen(question_data["prompt"], question_data["hint"])
        else:
            call screen evidence_choice_screen(question_data["prompt"], question_data["hint"])
        $ selected_answer = _return

        if selected_answer == "__hint__":
            $ deduction_hint_count += 1
            $ hint_text = question_data["hint"]
            sysmsg "[hint_text]"

        elif selected_answer == "__cancel__":
            m "ここで引くわけにはいかない。もう一度考えよう。"

        elif question_data["kind"] == "person" and selected_answer == question_data["answer_person"]:
            $ solved = True
            $ deduction_score += 1
            $ success_text = question_data["success"]
            sysmsg "正解。 [success_text]"

        elif question_data["kind"] == "evidence" and selected_answer in question_data["answers"]:
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

    if not solved and question_data["key"]:
        $ deduction_key_failures += 1

    return


label ending_branch:
    $ set_chapter(6, "エンディング", "澪の報告が、シロワの明日を決める")
    scene bg dawn_window
    show mio neutral at left

    if final_forced_bad:
        jump bad_ending
    elif deduction_score >= 8 and deduction_key_failures == 0 and deduction_mistakes <= 3 and has_final_required_evidence():
        jump true_ending
    elif deduction_score >= 5 and deduction_key_failures <= 2:
        jump normal_ending
    else:
        jump bad_ending


label true_ending:
    scene bg dawn_window
    show mio neutral at left
    show sena broken at right
    sysmsg "True Ending: 月の底で、息をする"
    m "ALMAは殺していない。あなたは、ALMAに偽の現実を見せた。"
    sena "都市が閉じれば、ノアたちは生きる場所を失う。私は、それが怖かった。"
    noah "父さんは、シロワを壊そうとしてたんじゃないんだね。"
    m "嘘を取り除いて、作り直そうとしていた。君たちが、ここで息を続けられるように。"
    sysmsg "シロワは閉鎖されず、住民自治と安全監査の道へ進む。夜明けの窓に、細い光が差した。"
    return


label normal_ending:
    scene bg dawn_window
    show mio pained at left
    show sena shaken at right
    sysmsg "Normal Ending: 白い報告書"
    m "犯人と手口は示せた。けれど、徹さんが何を守ろうとしたのかまでは届かなかった。"
    sysmsg "セナは拘束される。だが、セレネ社の責任追及は曖昧なまま、シロワの住民には重い沈黙が残った。"
    return


label bad_ending:
    scene bg outer_port
    show noah tears at left
    show alma alert at right
    sysmsg "Bad Ending: 無人区画"
    alma "R-7事故はALMA運用上の重大エラーとして処理されます。停止手続きに入ります。"
    sysmsg "真犯人は明らかにならない。外口の床に残る粉塵を、ノアだけが見つめていた。"
    noah "……母さんの足跡、どうしてここにあるの。"
    sysmsg "プレイヤーだけが、届かなかった真相の形を知っている。"
    return
