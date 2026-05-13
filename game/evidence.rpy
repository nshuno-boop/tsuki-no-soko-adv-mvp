# 証拠・人物メモ・進行・推理問題のデータ層。
# Phase 3では「最初から最後まで遊べるMVP」を優先し、章と証拠の導線をここで一元管理する。

default chapter = 0
default chapter_title = "プロローグ：シロワへようこそ"
default current_objective = "徹との約束の時間まで、シロワの中を確認する"
default evidence_unlocked = set()
default interview_done = set()
default interview_flags = set()
default deduction_score = 0
default deduction_mistakes = 0
default deduction_hint_count = 0
default deduction_key_failures = 0
default deduction_correct_ids = set()
default final_forced_bad = False

init python:
    REQUIRED_EVIDENCE_IDS = [
        "e_r7_decompression_log",
        "e_personnel_location_log",
        "e_autopsy_record",
        "e_manual_bulkhead_blood",
        "e_white_rabbit_usage_log",
        "e_white_rabbit_co2_absorber",
        "e_white_rabbit_dust_test",
        "e_thermal_sensor_frost",
        "e_manual_valve_scratch",
        "e_maintenance_admin_log",
        "e_earth_meeting_audio",
        "e_noah_testimony",
        "e_toru_audit_file",
        "e_lunarborn_medical_report",
        "e_sena_dust_trace",
    ]

    EVIDENCE_ORDER = REQUIRED_EVIDENCE_IDS

    evidence_catalog = {
        "e_r7_decompression_log": {
            "id": "e_r7_decompression_log",
            "name": "酸素工房R-7緊急減圧ログ",
            "short_name": "R-7減圧ログ",
            "description": "22:31に酸素工房R-7の緊急減圧が承認された記録。",
            "summary": "R-7で緊急減圧が起きたことを示す一次ログ。",
            "detail": "ログ上はALMAが『区画内に人員なし』と判断し、緊急減圧を許可している。檜山徹の死亡時刻と一致する。",
            "category": "log",
            "related_character": "檜山 徹",
            "related_location": "酸素工房R-7",
            "icon": "images/icons/icon_evidence_log.png",
            "chapter": 1,
            "hint": "事件の発生時刻と直接の危険を示す。",
        },
        "e_personnel_location_log": {
            "id": "e_personnel_location_log",
            "name": "人員位置ログ",
            "short_name": "位置ログ",
            "description": "事故時刻、徹のビーコンが外口側にあると記録されたログ。",
            "summary": "徹がR-7ではなく外口側にいるように見えた記録。",
            "detail": "保守モード中はビーコンと外部カメラが優先され、R-7内の弱い生体反応は後解析で矛盾として浮かんだ。ALMAが無人判定した根拠のひとつ。",
            "category": "log",
            "related_character": "檜山 徹",
            "related_location": "コア",
            "icon": "images/icons/icon_evidence_log.png",
            "chapter": 1,
            "hint": "ALMAが誰をどこにいると見なしたかを見る。",
        },
        "e_autopsy_record": {
            "id": "e_autopsy_record",
            "name": "徹の遺体検案記録",
            "short_name": "検案記録",
            "description": "徹の死因が真空暴露による急性低酸素であると示す医療記録。",
            "summary": "死亡原因を医学的に裏づける記録。",
            "detail": "白兎3号で一定時間耐えた痕跡はなく、R-7内で直接減圧に巻き込まれた可能性が高い。",
            "category": "medical",
            "related_character": "白石 アカリ",
            "related_location": "医療室",
            "icon": "images/icons/icon_evidence_medical.png",
            "chapter": 1,
            "hint": "死因をログだけでなく身体の記録から確認する。",
        },
        "e_manual_bulkhead_blood": {
            "id": "e_manual_bulkhead_blood",
            "name": "手動隔壁レバーの血痕",
            "short_name": "隔壁の血痕",
            "description": "R-7内の手動隔壁レバーに残った徹の血痕。",
            "summary": "徹が最後にR-7の隔壁を閉じようとした痕跡。",
            "detail": "徹は逃げるためではなく、隣接区画へ減圧が広がるのを止めるためにレバーへ手を伸ばしていた。",
            "category": "physical",
            "related_character": "檜山 徹",
            "related_location": "酸素工房R-7",
            "icon": "images/icons/icon_evidence_medical.png",
            "chapter": 1,
            "hint": "徹が最後に守ろうとしたものを示す。",
        },
        "e_white_rabbit_usage_log": {
            "id": "e_white_rabbit_usage_log",
            "name": "白兎3号の使用ログ",
            "short_name": "白兎使用ログ",
            "description": "白兎3号が事故時刻に外へ出たように見える運用ログ。",
            "summary": "宇宙服の使用記録。ただし入力元がビーコン情報に偏っている。",
            "detail": "ログは『外口を通過』と読めるが、スーツ本体の消耗記録とは一致しない。ALMAがビーコン優先仕様で判断した可能性を示す。",
            "category": "suit",
            "related_character": "北条 リツ",
            "related_location": "外口",
            "icon": "images/icons/icon_evidence_suit.png",
            "chapter": 2,
            "hint": "ALMAが無人と判断した入力のひとつ。",
        },
        "e_white_rabbit_co2_absorber": {
            "id": "e_white_rabbit_co2_absorber",
            "name": "白兎3号のCO2吸収材",
            "short_name": "CO2吸収材",
            "description": "白兎3号のCO2吸収材が未使用に近い状態で残っていた。",
            "summary": "白兎3号が実際には使われていなかったことを示す。",
            "detail": "宇宙服で船外活動を行えば必ず消耗するはずの吸収材が、事故前点検時とほぼ同じ状態だった。",
            "category": "suit",
            "related_character": "檜山 徹",
            "related_location": "外口",
            "icon": "images/icons/icon_evidence_suit.png",
            "chapter": 4,
            "hint": "使われたはずなのに消耗していないもの。",
        },
        "e_white_rabbit_dust_test": {
            "id": "e_white_rabbit_dust_test",
            "name": "白兎3号関節部の粉塵検査",
            "short_name": "関節粉塵検査",
            "description": "白兎3号の関節部から、外口通過時につくはずの月面粉塵が検出されなかった。",
            "summary": "白兎3号が外へ出ていないことを示す検査。",
            "detail": "影井戸や外口の粉塵は細かく関節部に残りやすい。だが白兎3号にはそれがない。",
            "category": "suit",
            "related_character": "ルカ・ナディム",
            "related_location": "外口",
            "icon": "images/icons/icon_evidence_suit.png",
            "chapter": 4,
            "hint": "実際に外へ出たなら、関節部に粉塵が残る。",
        },
        "e_thermal_sensor_frost": {
            "id": "e_thermal_sensor_frost",
            "name": "熱センサーの氷霜成分",
            "short_name": "氷霜成分",
            "description": "R-7熱センサーに付着していた、自然結露では説明しづらい氷霜成分。",
            "summary": "センサーを一時的に鈍らせた痕跡。",
            "detail": "冷却剤と影井戸由来の微細粉塵が混ざっている。自然故障ではなく、人の手でセンサーに干渉した可能性が高い。",
            "category": "physical",
            "related_character": "ルカ・ナディム",
            "related_location": "酸素工房R-7",
            "icon": "images/icons/icon_warning.png",
            "chapter": 2,
            "hint": "自然故障ではない異物の痕跡。",
        },
        "e_manual_valve_scratch": {
            "id": "e_manual_valve_scratch",
            "name": "手動補助弁の微細傷",
            "short_name": "補助弁の傷",
            "description": "R-7の手動補助弁に、新しい工具傷が残っていた。",
            "summary": "減圧を人為的に誘導した可能性を示す傷。",
            "detail": "補助弁は通常ALMAの監視対象だが、保守モード中は人間の手動操作が優先される。",
            "category": "physical",
            "related_character": "北条 リツ",
            "related_location": "酸素工房R-7",
            "icon": "images/icons/icon_warning.png",
            "chapter": 2,
            "hint": "人が触った痕跡がある操作部を見る。",
        },
        "e_maintenance_admin_log": {
            "id": "e_maintenance_admin_log",
            "name": "管理者権限の保守モード記録",
            "short_name": "保守モード記録",
            "description": "事故前夜、管理者権限でALMAの区画監視が保守モードへ切り替えられていた記録。",
            "summary": "ALMAの中核ではなく、入力と優先順位を変えた記録。",
            "detail": "保守モードでは作業員ビーコンと外部カメラが優先される。切替は代表権限IDから発行され、会議音声の空白時間と重なる。ALMAは嘘をついたのではなく、偽の入力を規定通り処理した。",
            "category": "log",
            "related_character": "雨宮 セナ",
            "related_location": "コア",
            "icon": "images/icons/icon_evidence_key.png",
            "chapter": 2,
            "hint": "犯人がALMAを騙すために利用した仕様。",
        },
        "e_earth_meeting_audio": {
            "id": "e_earth_meeting_audio",
            "name": "地球会議の音声記録",
            "short_name": "会議音声",
            "description": "セレネ資源開発と地球側会議で、シロワの採掘量不足が問題視されていた音声。",
            "summary": "セナのアリバイと動機に関わる遠隔会議の音声。",
            "detail": "音声にはセナの応答があるが、発言間隔に長い空白がある。遠隔出席を続けながら現場へ移動できた余地が残る。",
            "category": "audio",
            "related_character": "雨宮 セナ",
            "related_location": "セナ執務室",
            "icon": "images/icons/icon_evidence_audio.png",
            "chapter": 4,
            "hint": "セナのアリバイを完全には支えない音声。",
        },
        "e_noah_testimony": {
            "id": "e_noah_testimony",
            "name": "ノアの証言メモ",
            "short_name": "ノア証言",
            "description": "ノアが外口近くで聞いた足音と、ALMAの見ていたR-7の違和感をまとめたメモ。",
            "summary": "映像と生体センサー、外口付近の足音が食い違う証言。",
            "detail": "ノアは母をかばいながらも、事故直前に外口へ向かう足音を聞いていたと認める。",
            "category": "testimony",
            "related_character": "雨宮 ノア",
            "related_location": "外口",
            "icon": "images/icons/icon_person.png",
            "chapter": 4,
            "hint": "アリバイの空白を人の記憶で埋める。",
        },
        "e_toru_audit_file": {
            "id": "e_toru_audit_file",
            "name": "徹の暗号化監査ファイル",
            "short_name": "監査ファイル",
            "description": "檜山徹が死の直前に残した、シロワ再建のための監査ファイル。",
            "summary": "セレネ社の圧力、採掘量不足、ALMA運用の抜け穴をつなぐ資料。",
            "detail": "徹は都市を壊すためではなく、嘘のない再建のために告発を準備していた。",
            "category": "key",
            "related_character": "檜山 徹",
            "related_location": "コア",
            "icon": "images/icons/icon_evidence_key.png",
            "chapter": 3,
            "hint": "動機と徹の本心を同時に示す。",
        },
        "e_lunarborn_medical_report": {
            "id": "e_lunarborn_medical_report",
            "name": "月面生まれ世代の医療評価",
            "short_name": "月生まれ医療評価",
            "description": "月面生まれの世代が急な地球移住に耐えにくいことを示す医療評価。",
            "summary": "セナが都市閉鎖を恐れた理由に関わる資料。",
            "detail": "ノアを含む月面生まれ世代は、重力・免疫・循環器の面で地球移住に高いリスクを抱えている。",
            "category": "medical",
            "related_character": "白石 アカリ",
            "related_location": "医療室",
            "icon": "images/icons/icon_evidence_medical.png",
            "chapter": 3,
            "hint": "セナの動機を、政治ではなく家族と住民の身体から見る。",
        },
        "e_sena_dust_trace": {
            "id": "e_sena_dust_trace",
            "name": "セナの袖口に残る極地粉塵",
            "short_name": "袖口の粉塵",
            "description": "セナの袖口から、外口と影井戸周辺に特有の微細粉塵が検出された。",
            "summary": "セナが会議中に外口近くへ移動した可能性を示す。",
            "detail": "執務室だけにいたなら付着しない粉塵。ノアの証言と組み合わせることで、セナのアリバイが崩れる。",
            "category": "physical",
            "related_character": "雨宮 セナ",
            "related_location": "外口",
            "icon": "images/icons/icon_warning.png",
            "chapter": 4,
            "hint": "セナがどこにいたかを衣服の痕跡で見る。",
        },
    }

    PERSON_ORDER = ["mio", "sena", "toru", "ritsu", "luka", "akari", "noah", "jin", "alma"]
    INTERVIEW_TARGETS = ["sena", "ritsu", "luka", "akari", "noah", "jin"]
    CHAPTER4_REQUIRED_INTERVIEWS = 4

    person_profiles = {
        "mio": {
            "name": "佐伯 澪",
            "label": "地球から来た監査官",
            "memo": "地球監査局の新人監査官。シロワで起きた減圧事故の調査を担当する。",
            "focus": "外から来た立場だからこそ、街の常識に飲み込まれず違和感を拾える。",
            "image": "images/chars/mio_neutral.png",
        },
        "sena": {
            "name": "雨宮 セナ",
            "label": "シロワの代表",
            "memo": "白環市、通称シロワの代表。住民の未来を背負うあまり、真実を押し潰そうとしている。",
            "focus": "都市を守る責任と、ノアを守りたい母親としての恐れが重なっている。",
            "image": "images/chars/sena_neutral.png",
        },
        "toru": {
            "name": "檜山 徹",
            "label": "空気を守っていた男",
            "memo": "生命維持主任。酸素工房R-7で死亡した被害者。都市を壊すのではなく再建するため、監査ファイルを残した。",
            "focus": "告発は破壊ではなく、嘘のない再建のためだった可能性が高い。",
            "image": "images/chars/toru_neutral.png",
        },
        "ritsu": {
            "name": "北条 リツ",
            "label": "アルマの技師",
            "memo": "AI管理技師。ALMAは嘘をつかない、だからこそ入力の嘘に気づく。",
            "focus": "ALMAの中核ではなく、ALMAに渡された入力を疑う視点を持っている。",
            "image": "images/chars/ritsu_neutral.png",
        },
        "luka": {
            "name": "ルカ・ナディム",
            "label": "影井戸の採掘屋",
            "memo": "影井戸の採掘主任。徹とは口論していたが、同じ危機を別の角度から見ていた。",
            "focus": "採掘量不足を知る人物。徹と対立していたが、殺意とは別の感情がある。",
            "image": "images/chars/luka_neutral.png",
        },
        "akari": {
            "name": "白石 アカリ",
            "label": "月生まれを診る医師",
            "memo": "医療主任。死者の身体と、月面生まれ世代の未来を同じ重さで見ている。",
            "focus": "徹の死因と、月面生まれ世代が抱える身体的リスクをつなぐ。",
            "image": "images/chars/akari_neutral.png",
        },
        "noah": {
            "name": "雨宮 ノア",
            "label": "月で生まれた娘",
            "memo": "シロワで生まれた少女。母をかばい、父の本心を知らないまま傷ついている。",
            "focus": "母を信じたい気持ちと、外口で聞いた足音の記憶の間で揺れている。",
            "image": "images/chars/noah_neutral.png",
        },
        "jin": {
            "name": "鷹峰 ジン",
            "label": "セレネ社の広報法務",
            "memo": "セレネ資源開発の企業側担当。会社を守る言葉で、現場の痛みを薄めようとする。",
            "focus": "企業の圧力は示せるが、殺人の実行者とは切り分けて考える必要がある。",
            "image": "images/chars/jin_neutral.png",
        },
        "alma": {
            "name": "ALMA",
            "label": "白環市管理AI / 読み: アルマ",
            "memo": "都市の生命維持、区画制御、ログ管理を担うAI。住民からは『アルマさん』とも呼ばれる。",
            "focus": "嘘をつく存在ではなく、与えられた入力を規定通り処理する都市の目。",
            "image": "images/chars/alma_idle.png",
        },
    }

    def interview_done_count():
        return len([person_id for person_id in INTERVIEW_TARGETS if person_id in interview_done])

    def missing_interview_names():
        return [
            person_profiles[person_id]["name"]
            for person_id in INTERVIEW_TARGETS
            if person_id not in interview_done
        ]

    def has_enough_interviews_for_chapter4():
        return interview_done_count() >= CHAPTER4_REQUIRED_INTERVIEWS

    def interview_status_text(person_id):
        if person_id in interview_done:
            return "聞き込み済み"
        return "未聞き込み"

    def recommended_action_text():
        if chapter == 3:
            if not has_enough_interviews_for_chapter4():
                return "おすすめ: まずは4人以上に初回聞き込みを行い、徹の監査ファイルへ近づく。"
            if not has_evidence("e_lunarborn_medical_report"):
                return "おすすめ: 白石アカリにもう一度話を聞き、月面生まれ世代の医療評価を確認する。"
            return "おすすめ: 証拠品一覧を確認してから、白兎3号の調査へ進む。"
        if chapter >= 5:
            missing_ids = missing_final_evidence()
            if len(missing_ids) > 0:
                if "e_lunarborn_medical_report" in missing_ids:
                    return "おすすめ: 白石アカリにもう一度話を聞き、月生まれ世代の医療評価を確認する。"
                return "おすすめ: 不足している重要証拠を確認し、人物メモと証拠品一覧を見直す。"
            return "おすすめ: セナのアリバイ、動機、徹の最後の行動を証拠品一覧で整理する。"
        if chapter == 4:
            return "おすすめ: 白兎3号の消耗、会議音声、ノアの証言、袖口の粉塵をつなげる。"
        return "おすすめ: 現在の目的に沿って、証拠品一覧と人物メモを確認する。"

    FINAL_REQUIRED_EVIDENCE = [
        "e_toru_audit_file",
        "e_lunarborn_medical_report",
        "e_noah_testimony",
        "e_maintenance_admin_log",
        "e_white_rabbit_co2_absorber",
        "e_earth_meeting_audio",
        "e_sena_dust_trace",
        "e_manual_bulkhead_blood",
    ]

    STORY_EVIDENCE_BY_PHASE = {
        1: [
            "e_r7_decompression_log",
            "e_personnel_location_log",
            "e_autopsy_record",
            "e_manual_bulkhead_blood",
        ],
        2: [
            "e_white_rabbit_usage_log",
            "e_maintenance_admin_log",
            "e_thermal_sensor_frost",
            "e_manual_valve_scratch",
        ],
        4: [
            "e_white_rabbit_co2_absorber",
            "e_white_rabbit_dust_test",
            "e_earth_meeting_audio",
            "e_noah_testimony",
            "e_sena_dust_trace",
        ],
    }

    case_timeline = [
        {
            "time": "19:10",
            "title": "澪がシロワに到着",
            "description": "地球から来た監査官として白環市に入る。",
            "related_evidence": [],
            "chapter": 0,
        },
        {
            "time": "19:40",
            "title": "セナが監査予定を確認",
            "description": "セナは都市停止リスクを理由に、調査の短縮を求める。",
            "related_evidence": ["e_earth_meeting_audio"],
            "chapter": 0,
        },
        {
            "time": "20:20",
            "title": "徹とルカが口論",
            "description": "影井戸の採掘量報告をめぐって対立。",
            "related_evidence": ["e_toru_audit_file"],
            "chapter": 3,
        },
        {
            "time": "21:05",
            "title": "ALMA保守モード開始",
            "description": "管理者権限でR-7周辺の監視優先順位が切り替わる。",
            "related_evidence": ["e_maintenance_admin_log"],
            "chapter": 2,
        },
        {
            "time": "21:32",
            "title": "熱センサーに氷霜が付着",
            "description": "R-7熱センサーに、自然結露では説明しにくい成分が残る。",
            "related_evidence": ["e_thermal_sensor_frost"],
            "chapter": 2,
        },
        {
            "time": "21:46",
            "title": "手動補助弁が操作される",
            "description": "R-7の補助弁に新しい工具傷が残る。",
            "related_evidence": ["e_manual_valve_scratch"],
            "chapter": 2,
        },
        {
            "time": "21:52",
            "title": "ノアが外口付近で足音を聞く",
            "description": "母セナに似た歩き方だったが、ノアは言い出せなかった。",
            "related_evidence": ["e_noah_testimony"],
            "chapter": 4,
        },
        {
            "time": "22:03",
            "title": "白兎3号のビーコンが移動",
            "description": "白兎3号が外口側へ移動したようにALMAへ入力される。",
            "related_evidence": ["e_white_rabbit_usage_log", "e_personnel_location_log"],
            "chapter": 2,
        },
        {
            "time": "22:08",
            "title": "セナの会議音声に空白",
            "description": "地球会議の応答に、移動可能な長い無音が残る。",
            "related_evidence": ["e_earth_meeting_audio"],
            "chapter": 4,
        },
        {
            "time": "22:31",
            "title": "酸素工房R-7が緊急減圧",
            "description": "ALMAは無人区画と判断し、R-7を隔離・減圧した。",
            "related_evidence": ["e_r7_decompression_log", "e_personnel_location_log"],
            "chapter": 1,
        },
        {
            "time": "22:32",
            "title": "徹が隔壁レバーへ手を伸ばす",
            "description": "徹は隣接区画を守るため、最後に手動隔壁を閉じようとした。",
            "related_evidence": ["e_manual_bulkhead_blood"],
            "chapter": 1,
        },
        {
            "time": "22:40",
            "title": "白兎3号に未使用痕跡",
            "description": "CO2吸収材と関節粉塵が、船外活動の説明と矛盾する。",
            "related_evidence": ["e_white_rabbit_co2_absorber", "e_white_rabbit_dust_test"],
            "chapter": 4,
        },
        {
            "time": "23:20",
            "title": "徹の監査ファイルが復号",
            "description": "徹が都市を壊すのではなく、嘘のない再建を目指していたとわかる。",
            "related_evidence": ["e_toru_audit_file", "e_lunarborn_medical_report"],
            "chapter": 5,
        },
    ]

    deduction_questions = [
        {
            "id": "q1",
            "kind": "evidence",
            "prompt": "Q1. 徹が何によって命を落としたのか、直接示す証拠は？",
            "answers": ["e_r7_decompression_log", "e_autopsy_record"],
            "hint": "まずは手口や犯人ではなく、死亡の原因そのものを見よう。",
            "success": "減圧の発生と真空暴露の記録が、徹の死因をまっすぐ示している。",
            "failure": "今は『誰が』ではなく、『何が徹を死なせたか』を示す証拠が必要だ。",
            "key": True,
        },
        {
            "id": "q2",
            "kind": "evidence",
            "prompt": "Q2. ALMAがR-7を無人だと信じた判断材料は？",
            "answers": ["e_personnel_location_log", "e_white_rabbit_usage_log"],
            "hint": "ALMAが見ていたのは、現場そのものではなく位置と運用の入力だ。",
            "success": "ALMAは位置や白兎3号の運用記録を材料に、徹がR-7にいないと判断した。",
            "failure": "ALMAを責める前に、ALMAが何を材料に判断したかを示そう。",
            "key": True,
        },
        {
            "id": "q3",
            "kind": "multi_evidence",
            "prompt": "Q3. 徹が白兎3号で船外活動をしていなかったと示す組み合わせは？",
            "required_answers": ["e_white_rabbit_co2_absorber", "e_white_rabbit_dust_test"],
            "hint": "実際に外へ出たスーツなら、内部と関節部の両方に痕跡が残る。",
            "success": "白兎3号には、外へ出たスーツにあるはずの消耗と粉塵がない。",
            "failure": "ログではなく、白兎3号の実物に残った痕跡を組み合わせよう。",
            "key": True,
        },
        {
            "id": "q4",
            "kind": "multi_evidence",
            "prompt": "Q4. R-7の異常が自然故障ではなく、人の手で起こされたと示す組み合わせは？",
            "required_answers": ["e_thermal_sensor_frost", "e_manual_valve_scratch"],
            "hint": "自然現象だけでは説明しにくい、機器側の痕跡に注目する。",
            "success": "センサーの氷霜と補助弁の傷が、R-7への人為的な干渉を示している。",
            "failure": "まだ事故の説明に寄っている。操作された場所に残った痕跡を見よう。",
            "key": True,
        },
        {
            "id": "q5",
            "kind": "evidence",
            "prompt": "Q5. 犯人がALMAに偽の現実を見せるため、利用した仕様は？",
            "answers": ["e_maintenance_admin_log"],
            "hint": "ALMAを書き換えたのではなく、ALMAが優先する入力を変えた。",
            "success": "保守モード中の優先仕様が、ALMAに偽の現実を信じさせた。",
            "failure": "改ざんではない。ALMAが正しく従ったルールを示す証拠が必要だ。",
            "key": True,
        },
        {
            "id": "q6",
            "kind": "multi_evidence",
            "prompt": "Q6. セナが会議中ずっと執務室にいた、というアリバイを崩す組み合わせは？",
            "required_answers": ["e_earth_meeting_audio", "e_noah_testimony", "e_sena_dust_trace"],
            "hint": "ひとつの記録だけではなく、時間の空白と現場に残った痕跡を重ねて見る。",
            "success": "会議の空白、ノアの証言、袖口の粉塵が、セナの移動を浮かび上がらせた。",
            "failure": "ひとつでは足りない。セナが外口へ行けたことを、別々の角度から重ねよう。",
            "key": True,
        },
        {
            "id": "q7",
            "kind": "person",
            "prompt": "Q7. 動機の全体像は次に詰める。まず、権限と移動痕跡が指す実行者は誰か？",
            "answer_person": "sena",
            "hint": "権限、動機、移動の痕跡が同じ人物に集まっている。",
            "success": "雨宮セナ。権限と移動痕跡は、実行者として彼女を指している。",
            "failure": "疑わしさだけでは足りない。権限、動機、アリバイ崩しが揃う人物を選ぼう。",
            "key": True,
        },
        {
            "id": "q8",
            "kind": "multi_evidence",
            "prompt": "Q8. セナがそこまで追い詰められた理由を示す組み合わせは？",
            "required_answers": ["e_toru_audit_file", "e_lunarborn_medical_report"],
            "hint": "都市の嘘と、月で生まれた子どもたちの身体。その両方を見る。",
            "success": "監査ファイルと医療評価が、セナの恐れを動機として説明する。ただし、それは罪を軽くするものではない。",
            "failure": "手口ではなく、セナが何を恐れていたかを示す証拠を組み合わせよう。",
            "key": True,
        },
        {
            "id": "q9",
            "kind": "evidence",
            "prompt": "Q9. 徹が最後に守ろうとしたものを示す証拠は？",
            "answers": ["e_manual_bulkhead_blood"],
            "hint": "徹が最後に向かったのは、逃げ道ではなく、被害を止めるための場所だった。",
            "success": "徹は最後に、自分ではなく隣の区画の空気を守ろうとしていた。",
            "failure": "徹の本心は、最後の行動に残っている。手が届いた場所を見よう。",
            "key": True,
        },
    ]

    def ordered_unlocked_evidence():
        """入手済み証拠を、カタログで決めた順番に並べて返す。"""
        unlocked = set(store.evidence_unlocked)
        return [evidence_id for evidence_id in EVIDENCE_ORDER if evidence_id in unlocked]

    def has_evidence(evidence_id):
        return evidence_id in set(store.evidence_unlocked)

    def missing_final_evidence():
        unlocked = set(store.evidence_unlocked)
        return [evidence_id for evidence_id in FINAL_REQUIRED_EVIDENCE if evidence_id not in unlocked]

    def has_final_required_evidence():
        return len(missing_final_evidence()) == 0

    def evidence_names(evidence_ids):
        return [evidence_catalog[evidence_id]["name"] for evidence_id in evidence_ids if evidence_id in evidence_catalog]

    def add_to_store_set(store_name, value):
        current = set(getattr(store, store_name))
        current.add(value)
        setattr(store, store_name, current)

    def mark_interview_flag(flag_id):
        add_to_store_set("interview_flags", flag_id)

    def mark_interview_done(person_id):
        add_to_store_set("interview_done", person_id)

    def mark_deduction_correct(question_id):
        add_to_store_set("deduction_correct_ids", question_id)

    def sync_story_evidence_for_chapter(target_chapter):
        """章進行上すでに入手済みであるべき証拠を復元する。

        セーブ互換、デバッグジャンプ、途中修正後の再開で証拠セットだけが空に
        なると最終推理で詰むため、章到達時に安全側へ同期する。
        """
        unlocked = set(store.evidence_unlocked)
        before_count = len(unlocked)

        if target_chapter >= 3:
            for evidence_id in STORY_EVIDENCE_BY_PHASE[1] + STORY_EVIDENCE_BY_PHASE[2]:
                unlocked.add(evidence_id)

        if target_chapter >= 4 and has_enough_interviews_for_chapter4():
            unlocked.add("e_toru_audit_file")

        if target_chapter >= 5:
            for evidence_id in STORY_EVIDENCE_BY_PHASE[1] + STORY_EVIDENCE_BY_PHASE[2] + STORY_EVIDENCE_BY_PHASE[4]:
                unlocked.add(evidence_id)
            if has_enough_interviews_for_chapter4():
                unlocked.add("e_toru_audit_file")
            if "akari_additional" in interview_flags:
                unlocked.add("e_lunarborn_medical_report")

        store.evidence_unlocked = unlocked
        return len(unlocked) - before_count

    def add_evidence(evidence_id):
        """証拠品を入手する。存在しないIDなら通知だけ出してFalseを返す。"""
        if evidence_id not in evidence_catalog:
            renpy.notify("未登録の証拠ID: {}".format(evidence_id))
            return False

        unlocked = set(store.evidence_unlocked)
        if evidence_id in unlocked:
            renpy.notify("入手済み: {}".format(evidence_catalog[evidence_id]["name"]))
            return False

        unlocked.add(evidence_id)
        store.evidence_unlocked = unlocked
        renpy.notify("証拠品を入手: {}".format(evidence_catalog[evidence_id]["name"]))
        renpy.restart_interaction()
        return True

    def set_chapter(number, title, objective):
        """章番号・章タイトル・現在目的を更新する。"""
        store.chapter = number
        store.chapter_title = title
        store.current_objective = objective

