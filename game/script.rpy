# 『月の底で、息をする』Phase 3 MVP。
# プロローグから3エンディングまで、仮素材で通しプレイできる骨組み。

label start:
    show screen objective_overlay
    $ set_chapter(0, "プロローグ：シロワへようこそ", "徹との約束の時間まで、シロワの中を確認する")

    scene bg lander_interior
    show mio neutral at left
    show alma idle at right
    sysmsg "2056年。月面南極都市《白環市》。住民たちはその街を、短く『シロワ』と呼ぶ。"
    sysmsg "降下船の窓の外で、太陽の光が氷の尾根を白く削っていた。ここでは、夜明けさえ機械の許可を待っている。"
    alma "ようこそ、佐伯監査官。都市管理AI、ALMAです。読みはアルマ。調査権限を確認しました。"
    m "声は落ち着いているのに、街全体から返事をされたみたいですね。"
    alma "生命維持、交通、区画圧、記録保全。私はそれらを管理します。判断は規定に従います。"
    m "ここでは、空気も水も記録も、誰かが守り続けている。……そういう街なんですね。"

    scene bg shirowa_hab_ring
    show mio neutral at left
    show sena smile at right
    sena "シロワへようこそ。地球の監査官を迎えるには、少し狭い街ですが。"
    m "佐伯澪です。監査は手短に、でも正確に進めます。"
    sena "正確さは大切です。ここでは、小さな誤差が人の呼吸を止めますから。"
    sysmsg "セナの笑みは柔らかい。けれど、その奥には都市全体を抱えて眠れない人の疲れがあった。"

    scene bg core
    show toru gentle at center
    t "佐伯監査官。生命維持主任の檜山徹です。今夜22:30、少し話せませんか。"
    t "ALMAのログは正しい。けれど、正しいログだけでは見えないものがあります。"
    m "それは、監査に関わる話ですか？"
    t "シロワの空気に関わる話です。嘘の混じった空気は、いつか誰かの肺を傷つける。"
    sysmsg "徹は冗談のように笑った。だが、その目だけは笑っていなかった。"

    jump chapter1


label chapter1:
    $ set_chapter(1, "第1章：息が止まった夜", "酸素工房R-7の事故現場を調べる")

    scene bg oxygen_workshop_r7
    show mio pained at left
    show alma alert at right
    sysmsg "22:31。酸素工房R-7で緊急減圧が発生。檜山徹は死亡した。"
    sysmsg "警報灯の赤が、白い壁を脈のように染めている。誰も叫ばない。ただ、空気だけが奪われた痕を残していた。"
    $ r7_log_lines = ["AREA: OXYGEN WORKSHOP R-7", "STATUS: DEPRESSURIZATION APPROVED", "HUMAN PRESENCE: NONE", "FATALITY: HIYAMA TORU"]
    call screen alma_log_screen("R-7 EMERGENCY EVENT", r7_log_lines)
    $ add_evidence("e_r7_decompression_log")

    m "R-7は無人判定。なのに、徹さんはここで死んでいる。"
    m "事故なら、記録と現場が同じ方向を向くはず。これは、どちらかが嘘をついている。"
    $ add_evidence("e_personnel_location_log")

    scene bg medbay
    show mio pained at left
    show akari doctor at right
    akari "死因は真空暴露による急性低酸素。外で倒れたのではなく、区画の中で空気を奪われた身体です。"
    akari "月の死は静かです。だから、記録より先に身体が話してくれることがあります。"
    $ add_evidence("e_autopsy_record")

    scene bg oxygen_workshop_r7
    show mio thinking at left
    sysmsg "手動隔壁レバーの根元に、乾いた血痕が残っていた。"
    m "徹さんは、最後に逃げようとしたんじゃない。隔壁を閉じようとした。"
    $ add_evidence("e_manual_bulkhead_blood")
    sysmsg "澪のメモ: 徹の死は減圧事故に見える。だが、位置ログと遺体の場所が噛み合わない。"
    sysmsg "澪のメモ: ALMAの判断そのものより、ALMAに届いた入力情報を疑う必要がある。"

    jump chapter2


label chapter2:
    $ set_chapter(2, "第2章：アルマは嘘をつかない", "ALMAの判断ログを確認する")

    scene bg core
    show mio thinking at left
    show ritsu neutral at right
    show alma speaking at center
    ritsu "ALMAの中核コードに改ざんはありません。アルマさんは規定通り動いています。"
    ritsu "だから厄介なんです。壊れていれば直せる。正しく動いた結果なら、何を正しいと見せられたかを見ないといけない。"
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
    sysmsg "澪のメモ: ALMAは嘘をついたのではなく、嘘の入力を正しく処理した可能性が高い。"
    sysmsg "澪のメモ: 保守モード、ビーコン優先、R-7の物理痕跡。この3つが同じ方向を示している。"

    jump chapter3_hub


label chapter3_hub:
    $ set_chapter(3, "第3章：影井戸の数字", "住民たちから徹の人間関係を聞き出す")
    $ synced_count = sync_story_evidence_for_chapter(3)

    scene bg shirowa_hab_ring
    show mio neutral at left
    sysmsg "徹が残した違和感は、シロワの人間関係と資源問題へつながっていく。"
    sysmsg "この街では、全員が空気を分け合っている。だからこそ、誰かの沈黙もまた、全員の肺に少しずつ溜まっていく。"
    if synced_count > 0:
        sysmsg "これまでの調査記録を証拠品一覧に同期した。"

    if has_enough_interviews_for_chapter4() and not has_evidence("e_toru_audit_file"):
        scene bg core
        show toru recording at center
        sysmsg "聞き込みで得た断片がつながり、徹の暗号化監査ファイルの一部が復号された。"
        sysmsg "ファイルには採掘量不足、セレネ社の圧力、そしてシロワを閉鎖させないための再建案が並んでいた。"
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
        $ audit_log_lines = ["CITY: SHIROWA", "OFFICIAL RECORD: 白環市", "COMMON NAME: シロワ", "AI: ALMA", "MODE: MAINTENANCE PRIORITY WINDOW FOUND", "WARNING: BEACON STREAM AND BIOMETRIC TRACE DO NOT MATCH"]
        call screen alma_log_screen("CURRENT AUDIT SNAPSHOT", audit_log_lines)
        jump chapter3_hub
    elif hub_choice == "timeline":
        call screen timeline_screen
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
        if has_enough_interviews_for_chapter4():
            jump chapter4
        else:
            $ done_count = interview_done_count()
            $ required_count = CHAPTER4_REQUIRED_INTERVIEWS
            $ missing_names = missing_interview_names()
            call screen interview_progress_warning_screen(done_count, required_count, missing_names)
            jump chapter3_hub
    else:
        jump chapter3_hub


label chapter4:
    $ set_chapter(4, "第4章：白兎は外へ出なかった", "白兎3号が本当に外へ出たのか確かめる")
    $ synced_count = sync_story_evidence_for_chapter(4)
    sysmsg "澪のメモ: 住民たちの証言はばらばらに見えたが、徹が都市を壊そうとしていなかったことだけは一致している。"
    sysmsg "澪のメモ: 次に確かめるべきは、ALMAに見えていた『徹の居場所』そのものだ。"

    scene bg outer_port
    show mio thinking at left
    show ritsu anxious at right
    if synced_count > 0:
        sysmsg "これまでの調査記録を証拠品一覧に同期した。"
    sysmsg "外口。正式型番HAKU-3、通称『白兎3号』は、事故当時に船外活動へ出たことになっている。"
    sysmsg "白いスーツは、使われたもののように記録されていた。だが表面は、あまりにも静かだった。"
    ritsu "CO2吸収材は未使用に近い。白兎3号は、徹さんを守るほど動いていません。"
    m "ログの上では外へ出た。でも、スーツの中では誰も息をしていない。"
    $ add_evidence("e_white_rabbit_co2_absorber")
    $ add_evidence("e_white_rabbit_dust_test")

    scene bg sena_office
    show mio neutral at left
    show jin irritated at right
    jin "地球会議の音声です。セレネ社としては、これ以上の提供はかなり譲歩しています。"
    jin "ただし、録音の空白まで当社の責任にされては困ります。沈黙は発言ではありませんから。"
    $ add_evidence("e_earth_meeting_audio")

    scene bg outer_port
    show mio thinking at left
    show noah tears at right
    noah "外口の近くで、足音を聞いた。母さんの歩き方に似てた。でも、言いたくなかった。"
    noah "言ったら、全部が壊れると思った。父さんのことも、母さんのことも、シロワのことも。"
    $ add_evidence("e_noah_testimony")

    scene bg shadow_well
    show mio thinking at left
    show luka sad at right
    luka "この粉塵は影井戸側のものだ。執務室だけにいた人間の袖につく粉じゃない。"
    $ add_evidence("e_sena_dust_trace")
    sysmsg "澪のメモ: 白兎3号は外へ出ていない。徹の居場所を示した入力は、誰かが作った偽の現実だった。"
    sysmsg "澪のメモ: 会議音声、ノアの証言、袖口の粉塵が、セナのアリバイに同じ傷をつけている。"

    jump chapter5_hub


label chapter5_hub:
    $ set_chapter(5, "最終章：だれのための空", "証拠を揃え、最後の推理に進む")
    $ synced_count = sync_story_evidence_for_chapter(5)

    scene bg core
    show mio neutral at left
    show alma speaking at right
    if synced_count > 0:
        sysmsg "章の進行に合わせて、これまでの調査記録を証拠品一覧に同期した。"
    sysmsg "管制核。証拠はそろいつつある。あとは、誰のために空気が奪われたのかを示すだけだ。"
    sysmsg "セナを追及するには、手口だけでは足りない。"

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
    elif hub_choice == "timeline":
        call screen timeline_screen
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
        sena "でも、この街では薄い空気でも吸い続けるしかない。綺麗な正論だけでは、人は守れません。"
        $ mark_interview_flag("sena_initial")
        $ mark_interview_done("sena")
    elif "sena_additional" not in interview_flags and has_evidence("e_toru_audit_file"):
        sena "檜山さんが告発を準備していたことは知っていました。ですが、告発は都市を救うとは限りません。"
        m "隠すことも、救うこととは限らない。"
        sena "分かっています。分かっているからこそ、私は代表の顔を外せなかった。"
        $ mark_interview_flag("sena_additional")
    elif chapter >= 5 and "sena_core" not in interview_flags:
        show sena shaken at right
        sena "都市が閉じれば、ノアたちは地球で生きられない。私は代表で、母親でもあるんです。"
        m "その恐れが、徹さんを殺す理由にはなりません。"
        $ mark_interview_flag("sena_core")
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
        $ mark_interview_flag("ritsu_initial")
        $ mark_interview_done("ritsu")
    elif "ritsu_additional" not in interview_flags and has_evidence("e_maintenance_admin_log"):
        ritsu "保守モード中はビーコン優先です。現場の作業員を守るための仕様でした。"
        m "でも今回は、ビーコンが嘘の居場所を作った。"
        $ mark_interview_flag("ritsu_additional")
    elif chapter >= 5 and "ritsu_core" not in interview_flags:
        show ritsu relieved at right
        ritsu "ALMAは嘘をついていません。嘘の入力を、正しく信じたんです。"
        m "犯人はAIではなく、AIの目を塞いだ人間。"
        $ mark_interview_flag("ritsu_core")
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
        luka "俺は数字を誤魔化した。徹はそれを嫌った。だからって、あいつが嫌いだったわけじゃない。"
        $ mark_interview_flag("luka_initial")
        $ mark_interview_done("luka")
    elif "luka_additional" not in interview_flags and has_evidence("e_toru_audit_file"):
        show luka sad at right
        luka "採掘量不足は本当だ。セレネ社に見せる数字は、きれいに磨かれてた。"
        $ mark_interview_flag("luka_additional")
    elif chapter >= 5 and "luka_core" not in interview_flags:
        show luka sad at right
        luka "徹とは対立してた。でも友人でもあった。あいつは街を売る気なんかなかったよ。"
        $ mark_interview_flag("luka_core")
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
        $ mark_interview_flag("akari_initial")
        $ mark_interview_done("akari")
    elif "akari_additional" not in interview_flags:
        akari "月面生まれの世代は、急な地球移住に耐えられない子がいます。ノアも、その評価対象です。"
        akari "代表が恐れているのは、政治的な失点だけではありません。子どもたちの身体が、地球を拒むかもしれないんです。"
        $ add_evidence("e_lunarborn_medical_report")
        $ mark_interview_flag("akari_additional")
    elif chapter >= 5 and "akari_core" not in interview_flags:
        akari "徹さんは都市を壊したかったんじゃありません。嘘を外して、作り直したかったんです。"
        $ mark_interview_flag("akari_core")
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
        noah "嘘でも、街が残るならいいじゃん。……そう思っちゃだめなの？"
        $ mark_interview_flag("noah_initial")
        $ mark_interview_done("noah")
    elif "noah_additional" not in interview_flags and has_evidence("e_earth_meeting_audio"):
        show noah tears at right
        noah "外口の近くで足音を聞いた。母さんに似てた。でも、そうだって言いたくなかった。"
        $ mark_interview_flag("noah_additional")
    elif chapter >= 5 and "noah_core" not in interview_flags:
        show noah tears at right
        noah "父さんは、わたしを地球に捨てようとしてたんじゃないの？"
        m "違う。徹さんは、君が嘘のない街で息をできるようにしたかった。"
        $ mark_interview_flag("noah_core")
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
        jin "線を引かなければ、会社は何も認められません。認めた瞬間、ここにある生活全部が訴訟の材料になる。"
        $ mark_interview_flag("jin_initial")
        $ mark_interview_done("jin")
    elif "jin_additional" not in interview_flags and has_evidence("e_toru_audit_file"):
        show jin irritated at right
        jin "採掘量報告に問題があったことは認めます。ですが、それは殺人の指示ではありません。"
        $ mark_interview_flag("jin_additional")
    elif chapter >= 5 and "jin_core" not in interview_flags:
        show jin defeated at right
        jin "会社の圧力はありました。けれど、檜山徹を殺す判断は、企業会議の議事録にはない。"
        $ mark_interview_flag("jin_core")
    else:
        jin "言葉は便利です。責任を遠ざけるには、特に。"
    return


label pre_final_reasoning:
    $ set_chapter(5, "最終章：だれのための空", "証拠を揃え、最後の推理に進む")
    $ synced_count = sync_story_evidence_for_chapter(5)
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
        jump ending_branch
    else:
        $ final_forced_bad = False

    jump final_reasoning


label final_reasoning:
    $ set_chapter(5, "最終章：だれのための空", "証拠を提示し、事件の構造を明らかにする")
    $ deduction_score = 0
    $ deduction_mistakes = 0
    $ deduction_hint_count = 0
    $ deduction_key_failures = 0
    $ deduction_correct_ids = set()

    scene bg core
    show mio neutral at left
    show sena neutral at right
    show alma speaking at center
    sysmsg "最終推理を開始します。問題ごとに、対応する証拠または人物を提示してください。"
    sysmsg "これは犯人当てでは終わらない。"

    $ question_index = 0
    while question_index < len(deduction_questions):
        $ current_question = deduction_questions[question_index]
        call ask_deduction_question(current_question)
        if _return == "back_to_investigation":
            jump chapter5_hub
        $ question_index += 1

    jump ending_branch


label ask_deduction_question(question_data):
    $ attempts = 0
    $ solved = False

    while not solved and attempts < 2:
        if question_data["kind"] == "person":
            call screen person_choice_screen(question_data["prompt"], question_data["hint"])
        elif question_data["kind"] == "multi_evidence":
            call screen multi_evidence_choice_screen(question_data["prompt"], question_data["hint"], len(question_data["required_answers"]))
        else:
            call screen evidence_choice_screen(question_data["prompt"], question_data["hint"])
        $ selected_answer = _return

        if selected_answer == "__hint__":
            $ deduction_hint_count += 1
            $ hint_text = question_data["hint"]
            sysmsg "[hint_text]"

        elif selected_answer == "__cancel__":
            m "ここで引くわけにはいかない。もう一度考えよう。"

        elif selected_answer == "__back_to_investigation__":
            m "証拠が足りないまま押し切るより、もう一度記録を洗い直そう。"
            return "back_to_investigation"

        elif question_data["kind"] == "person" and selected_answer == question_data["answer_person"]:
            $ solved = True
            $ deduction_score += 1
            $ mark_deduction_correct(question_data["id"])
            $ success_text = question_data["success"]
            sysmsg "正解。 [success_text]"

        elif question_data["kind"] == "multi_evidence" and set(selected_answer) == set(question_data["required_answers"]):
            $ solved = True
            $ deduction_score += 1
            $ mark_deduction_correct(question_data["id"])
            $ success_text = question_data["success"]
            sysmsg "正解。 [success_text]"

        elif question_data["kind"] == "evidence" and selected_answer in question_data["answers"]:
            $ solved = True
            $ deduction_score += 1
            $ mark_deduction_correct(question_data["id"])
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

    $ true_required_questions = {"q6", "q8", "q9"}
    $ true_question_ok = true_required_questions.issubset(deduction_correct_ids)
    if final_forced_bad:
        $ ending_name = "Bad Ending"
    elif deduction_score >= 8 and deduction_key_failures == 0 and true_question_ok and has_final_required_evidence():
        $ ending_name = "True Ending"
    elif deduction_score >= 5 and deduction_key_failures <= 2:
        $ ending_name = "Normal Ending"
    else:
        $ ending_name = "Bad Ending"

    $ result_text = "正解 {} / 不正解 {} / ヒント {} / 重要失敗 {}".format(deduction_score, deduction_mistakes, deduction_hint_count, deduction_key_failures)
    call screen deduction_result_screen(result_text, ending_name)

    if final_forced_bad:
        jump bad_ending
    elif ending_name == "True Ending":
        jump true_ending
    elif ending_name == "Normal Ending":
        jump normal_ending
    else:
        jump bad_ending


label true_ending:
    scene bg dawn_window
    show mio pained at left
    show noah tears at center
    show sena broken at right
    sysmsg "True Ending: 月の底で、息をする"
    m "ALMAは殺していない。あなたは、ALMAに偽の現実を見せた。"
    sena "都市が閉じれば、ノアたちは生きる場所を失う。私は、それが怖かった。"
    sena "ノア、私は……。"
    sysmsg "セナの言葉は、夜明けの窓の前で途切れた。"
    sena "怖さを理由にして、取り返しのつかないことをした。代表としても、母親としても。"
    sysmsg "徹の監査ファイルには、最後の一文が残されていた。"
    t "シロワを告発する。シロワを終わらせるためではない。嘘の上では、誰も長く息をできないから。"
    noah "父さんは、シロワを壊そうとしてたんじゃないんだね。"
    m "違う。徹さんは、嘘を取り除いて、君たちがここで息を続けられるようにしようとしていた。"
    alma "登録住民数386。呼吸確認385。"
    alma "檜山徹。生命維持主任。最終作業、居住区隔壁保護。記録しました。"
    noah "……ひとりぶん、忘れないで。"
    alma "記録しました。"
    sysmsg "夜明けの窓に、細い光が差した。誰もすぐには話さず、ただ同じ空気を吸った。"
    sysmsg "月の底で、人々はもう一度、嘘のない空気を吸う練習を始める。"
    return


label normal_ending:
    scene bg dawn_window
    show mio pained at left
    show sena shaken at right
    sysmsg "Normal Ending: 白い報告書"
    m "犯人と手口は示せた。けれど、徹さんが何を守ろうとしたのかまでは届かなかった。"
    sysmsg "ノアは報告書を閉じたまま、父の名前だけを何度も見ていた。"
    sysmsg "澪はページをめくれず、薄い紙の重さだけを指先に感じていた。"
    sysmsg "セナは拘束される。だが、セレネ社の責任追及は曖昧なまま、シロワの住民には重い沈黙が残った。"
    sysmsg "事件は解決した。それでも、夜明けの窓に立つ人々の呼吸は、まだ少し浅い。"
    return


label bad_ending:
    scene bg outer_port
    show noah tears at left
    show alma alert at right
    sysmsg "Bad Ending: 無人区画"
    alma "R-7事故はALMA運用上の重大エラーとして処理されます。停止手続きに入ります。"
    sysmsg "真犯人は明らかにならない。外口の床に残る粉塵を、ノアだけが見つめていた。"
    noah "……母さんの足跡、どうしてここにあるの。"
    sysmsg "誰も答えないまま、警告灯だけが白い床を赤く染めていた。"
    sysmsg "外口の足跡も、ノアの疑問も、シロワの公式記録には残らない。"
    return


label debug_menu:
    if not config.developer:
        sysmsg "このメニューは開発用です。"
        return

    sysmsg "開発用デバッグメニュー"
    menu:
        "すべての証拠を入手":
            $ evidence_unlocked = set(evidence_unlocked) | set(REQUIRED_EVIDENCE_IDS)
            $ renpy.notify("すべての証拠を入手しました")
            jump debug_menu

        "重要証拠だけ入手":
            $ evidence_unlocked = set(evidence_unlocked) | set(FINAL_REQUIRED_EVIDENCE)
            $ renpy.notify("重要証拠を入手しました")
            jump debug_menu

        "第3章へジャンプ":
            jump chapter3_hub

        "第5章へジャンプ":
            jump chapter5_hub

        "最終推理へジャンプ":
            jump pre_final_reasoning

        "True Endingへジャンプ":
            jump true_ending

        "Normal Endingへジャンプ":
            jump normal_ending

        "Bad Endingへジャンプ":
            jump bad_ending

        "戻る":
            return
