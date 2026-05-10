# 証拠・人物メモ・進行・推理問題のデータ層。
# 章や証拠を増やすときは、まずこのファイルにIDを追加する。

default chapter = 0
default chapter_title = "プロローグ"
default evidence_unlocked = set()
default interview_done = set()
default deduction_score = 0
default deduction_mistakes = 0
default deduction_hint_count = 0

init python:
    EVIDENCE_ORDER = [
        "e_r7_decompression_log",
        "e_white_rabbit_co2_absorber",
        "e_admin_authority_log",
        "e_earth_meeting_audio",
        "e_noah_testimony",
        "e_toru_audit_file",
    ]

    evidence_catalog = {
        "e_r7_decompression_log": {
            "id": "e_r7_decompression_log",
            "name": "酸素工房R-7緊急減圧ログ",
            "short_name": "R-7減圧ログ",
            "description": "酸素工房R-7で、ALMAの安全制御が減圧を許可したように見えるログ。",
            "summary": "酸素工房R-7で、ALMAの安全制御が減圧を許可したように見えるログ。",
            "detail": "減圧時刻の直前、区画内に『作業員なし』という状態が記録されている。しかし檜山徹はその時点でR-7内部にいた。",
            "category": "log",
            "related_character": "檜山 徹",
            "related_location": "酸素工房R-7",
            "icon": "images/icons/icon_evidence_log.png",
            "chapter": 1,
            "acquired": False,
            "hint": "アルマは人を見落としたのか。それとも、見せられた現実が偽物だったのか。",
        },
        "e_white_rabbit_co2_absorber": {
            "id": "e_white_rabbit_co2_absorber",
            "name": "白兎3号のCO2吸収材",
            "short_name": "CO2吸収材",
            "description": "檜山徹が使ったはずの宇宙服『白兎3号』に、使用時の消耗が残っていない。",
            "summary": "白兎3号に、使用時の消耗ログが残っていない。",
            "detail": "酸素消費、関節駆動、内圧維持、CO2吸収材の交換履歴が不自然に空白。徹は宇宙服で退避しようとした、という事故説明と矛盾する。",
            "category": "suit",
            "related_character": "檜山 徹",
            "related_location": "外口",
            "icon": "images/icons/icon_evidence_suit.png",
            "chapter": 1,
            "acquired": False,
            "hint": "使われたはずの白兎3号に、使われた痕跡がない。",
        },
        "e_admin_authority_log": {
            "id": "e_admin_authority_log",
            "name": "コア管理者権限ログ",
            "short_name": "権限ログ",
            "description": "事故前夜、コアから酸素工房R-7監視系の再同期が行われている。",
            "summary": "事故前夜、管理者権限でR-7監視系の再同期が行われている。",
            "detail": "ALMAの中核コード改ざんはない。ただし、外部センサーと区画状態の同期タイミングだけが手動でずらされている。",
            "category": "log",
            "related_character": "北条 リツ",
            "related_location": "コア",
            "icon": "images/icons/icon_evidence_key.png",
            "chapter": 2,
            "acquired": False,
            "hint": "ALMAそのものではなく、ALMAが参照する入力側に手が入っている。",
        },
        "e_earth_meeting_audio": {
            "id": "e_earth_meeting_audio",
            "name": "地球会議の音声記録",
            "short_name": "会議音声",
            "description": "地球側の会議で、セレネ資源開発と白環市の水資源契約をめぐる圧力が記録されている。",
            "summary": "セレネ社と白環市の水資源契約をめぐる圧力が記録された音声。",
            "detail": "雨宮セナはシロワ存続のため、檜山の監査告発を止める必要があった。音声には動機につながる発言が含まれる。",
            "category": "audio",
            "related_character": "雨宮 セナ",
            "related_location": "セナ執務室",
            "icon": "images/icons/icon_evidence_audio.png",
            "chapter": 2,
            "acquired": False,
            "hint": "事故の技術的説明だけでは、なぜ檜山が狙われたかは説明できない。",
        },
        "e_noah_testimony": {
            "id": "e_noah_testimony",
            "name": "ノアの証言",
            "short_name": "ノア証言",
            "description": "月面生まれの雨宮ノアは、R-7のカメラ映像と生体センサーが一致していなかったと証言する。",
            "summary": "R-7のカメラ映像と生体センサーが一致していなかった、という証言。",
            "detail": "映像上のR-7は無人。生体センサーには微弱な人間反応。ALMA本体は映像側を優先して判断した。",
            "category": "testimony",
            "related_character": "雨宮 ノア",
            "related_location": "コア",
            "icon": "images/icons/icon_person.png",
            "chapter": 3,
            "acquired": False,
            "hint": "ALMAは嘘をついたのではない。嘘の入力を信じた。",
        },
        "e_toru_audit_file": {
            "id": "e_toru_audit_file",
            "name": "徹の暗号化監査ファイル",
            "short_name": "監査ファイル",
            "description": "檜山徹が死の直前に残した監査ファイル。シロワの運用偽装と犯人の手口が暗号化されていた。",
            "summary": "檜山徹が死の直前に残した、犯人と手口を結ぶ監査ファイル。",
            "detail": "監査ファイルには、雨宮セナがセンサー同期を操作し、ALMAに『無人のR-7』を認識させた手順が残っている。",
            "category": "key",
            "related_character": "檜山 徹",
            "related_location": "コア",
            "icon": "images/icons/icon_evidence_key.png",
            "chapter": 3,
            "acquired": False,
            "hint": "真相を確定する最後の鍵。技術トリックと犯人を同時に結びつける。",
        },
    }

    PERSON_ORDER = ["mio", "sena", "toru", "ritsu", "luka", "akari", "noah", "jin", "alma"]
    INTERVIEW_TARGETS = ["noah", "sena", "ritsu", "luka", "akari", "jin"]

    person_profiles = {
        "mio": {
            "name": "佐伯 澪",
            "label": "地球から来た監査官",
            "memo": "地球監査局の新人監査官。シロワで起きた減圧事故の調査を担当する。",
            "image": "images/chars/mio_neutral.png",
        },
        "sena": {
            "name": "雨宮 セナ",
            "label": "シロワの代表",
            "memo": "白環市、通称シロワの都市代表。住民からの信頼は厚いが、都市存続のために強引な判断も辞さない。",
            "image": "images/chars/sena_neutral.png",
        },
        "toru": {
            "name": "檜山 徹",
            "label": "空気を守っていた男",
            "memo": "生命維持主任。酸素工房R-7で死亡した被害者。生前、都市運用の監査ファイルを残していた。",
            "image": "images/chars/toru_neutral.png",
        },
        "ritsu": {
            "name": "北条 リツ",
            "label": "アルマの技師",
            "memo": "AI管理技師。ALMAの中核コードに改ざんがないことを確認し、入力側の異常に気づく。",
            "image": "images/chars/ritsu_neutral.png",
        },
        "luka": {
            "name": "ルカ・ナディム",
            "label": "影井戸の採掘屋",
            "memo": "永久影採掘坑、通称『影井戸』の採掘主任。現場の空気と水の重みをよく知っている。",
            "image": "images/chars/luka_neutral.png",
        },
        "akari": {
            "name": "白石 アカリ",
            "label": "月生まれを診る医師",
            "memo": "医療主任。月面生まれの住民の体調管理を担う。檜山の死因にも違和感を抱いている。",
            "image": "images/chars/akari_neutral.png",
        },
        "noah": {
            "name": "雨宮 ノア",
            "label": "月で生まれた娘",
            "memo": "シロワで生まれた少女。ALMAを『アルマさん』と呼び、事故直前の違和感を覚えている。",
            "image": "images/chars/noah_neutral.png",
        },
        "jin": {
            "name": "鷹峰 ジン",
            "label": "セレネ社の広報法務",
            "memo": "セレネ資源開発の企業側担当。事故を企業リスクとして処理しようとする。",
            "image": "images/chars/jin_neutral.png",
        },
        "alma": {
            "name": "ALMA",
            "label": "白環市管理AI / 読み: アルマ",
            "memo": "都市の生命維持、区画制御、ログ管理を担うAI。住民からは『アルマさん』とも呼ばれる。",
            "image": "images/chars/alma_idle.png",
        },
    }

    deduction_questions = [
        {
            "id": "q1",
            "prompt": "Q1. 檜山徹が死亡した直接の原因を示す証拠は？",
            "answer": "e_r7_decompression_log",
            "hint": "まずは事件そのものを記録したログを示す。",
            "success": "酸素工房R-7の減圧ログが、死亡時刻と区画状態を示している。",
            "failure": "それは原因よりも、手口や動機に近い証拠だ。",
        },
        {
            "id": "q2",
            "prompt": "Q2. 『徹は白兎3号で退避しようとした』という説明と矛盾する証拠は？",
            "answer": "e_white_rabbit_co2_absorber",
            "hint": "使われたはずなのに、使われた痕跡がないものを探す。",
            "success": "白兎3号のCO2吸収材に使用痕跡がない。事故説明は崩れた。",
            "failure": "退避行動の矛盾を直接示すものではない。",
        },
        {
            "id": "q3",
            "prompt": "Q3. ALMA本体ではなく、入力側が操作されたことを示す証拠は？",
            "answer": "e_admin_authority_log",
            "hint": "コード改ざんではなく、コアの監視系同期に注目する。",
            "success": "コア管理者権限ログは、監視系の再同期操作を示している。",
            "failure": "ALMAが何を見たかではなく、誰が入力をずらせたかが必要だ。",
        },
        {
            "id": "q4",
            "prompt": "Q4. 雨宮セナに檜山を止める動機があったことを示す証拠は？",
            "answer": "e_earth_meeting_audio",
            "hint": "技術ではなく、政治的・経済的な圧力を示す証拠を選ぶ。",
            "success": "地球会議の音声記録が、シロワとセナの動機を浮かび上がらせる。",
            "failure": "それは手口の証拠で、動機の説明には弱い。",
        },
        {
            "id": "q5",
            "prompt": "Q5. 『ALMAは偽の現実を見せられた』と説明できる証拠は？",
            "answer": "e_noah_testimony",
            "hint": "映像と生体センサーの食い違いを語った人物を思い出す。",
            "success": "ノアの証言により、ALMAの判断材料が矛盾していたとわかる。",
            "failure": "偽の現実そのものを説明するには、入力の食い違いが必要だ。",
        },
        {
            "id": "q6",
            "prompt": "Q6. 雨宮セナの偽装殺人を最終的に確定する証拠は？",
            "answer": "e_toru_audit_file",
            "hint": "犯人・手口・被害者の告発を一本につなぐ最後の証拠を示す。",
            "success": "徹の監査ファイルが、セナと偽装手口を結びつけた。",
            "failure": "真相確定には、犯人と手口を同時に結ぶ証拠が必要だ。",
        },
    ]

    def ordered_unlocked_evidence():
        """入手済み証拠を、カタログで決めた順番に並べて返す。"""
        return [evidence_id for evidence_id in EVIDENCE_ORDER if evidence_id in evidence_unlocked]

    def add_evidence(evidence_id):
        """証拠品を入手する。存在しないIDなら通知だけ出してFalseを返す。"""
        if evidence_id not in evidence_catalog:
            renpy.notify("未登録の証拠ID: {}".format(evidence_id))
            return False

        if evidence_id in evidence_unlocked:
            renpy.notify("入手済み: {}".format(evidence_catalog[evidence_id]["name"]))
            return False

        evidence_unlocked.add(evidence_id)
        renpy.notify("証拠品を入手: {}".format(evidence_catalog[evidence_id]["name"]))
        renpy.restart_interaction()
        return True

    def set_chapter(number, title):
        """章番号と章タイトルを更新する。"""
        store.chapter = number
        store.chapter_title = title

