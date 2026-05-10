# 証拠・進行・推理問題の最小データ層。
# 章や証拠を増やすときは、基本的にここへ追記する。

default chapter = 0
default chapter_title = "プロローグ"
default evidence_unlocked = set()
default interview_done = set()
default deduction_score = 0
default deduction_mistakes = 0
default deduction_hint_count = 0

init python:
    # 表示順を固定するためのリスト。辞書だけに頼ると後で並び替えが面倒になる。
    EVIDENCE_ORDER = [
        "r7_decompression_log",
        "haku3_unused",
        "admin_authority_log",
        "earth_conference_audio",
        "noa_testimony",
        "hiyama_audit_file",
    ]

    # 証拠品カタログ。
    # idはゲーム内ロジックで使うため、英数字・snake_caseで固定する。
    evidence_catalog = {
        "r7_decompression_log": {
            "name": "R-7緊急減圧ログ",
            "chapter": 1,
            "summary": "資源精製区R-7で、ALMAの安全制御が減圧を許可したように見えるログ。",
            "detail": "減圧時刻の直前、区画内に『作業員なし』という状態が記録されている。しかし檜山徹はその時点でR-7内部にいた。",
            "hint": "ALMAは人を見落としたのか。それとも、見せられた現実が偽物だったのか。",
        },
        "haku3_unused": {
            "name": "宇宙服HAKU-3の未使用痕跡",
            "chapter": 1,
            "summary": "檜山徹が着用していたはずの宇宙服に、使用時の消耗ログが残っていない。",
            "detail": "酸素消費、関節駆動、内圧維持の記録が不自然に空白。徹は宇宙服で退避しようとした、という事故説明と矛盾する。",
            "hint": "被害者が本当に宇宙服を使えたなら、痕跡が残るはず。",
        },
        "admin_authority_log": {
            "name": "管理者権限ログ",
            "chapter": 2,
            "summary": "事故前夜、都市運用責任者の管理権限でR-7監視系の再同期が行われている。",
            "detail": "ALMAの中核コード改ざんはない。ただし、外部センサーと区画状態の同期タイミングだけが手動でずらされている。",
            "hint": "ALMAそのものではなく、ALMAが参照する入力側に手が入っている。",
        },
        "earth_conference_audio": {
            "name": "地球会議音声",
            "chapter": 2,
            "summary": "地球側の会議で、白環市の水資源契約をめぐる圧力が記録されている。",
            "detail": "雨宮セナは都市存続のため、檜山の監査告発を止める必要があった。音声には動機につながる発言が含まれる。",
            "hint": "事故の技術的説明だけでは、なぜ檜山が狙われたかは説明できない。",
        },
        "noa_testimony": {
            "name": "ノアの証言",
            "chapter": 3,
            "summary": "保守用子AIノアは、事故直前にR-7のカメラ映像と生体センサーが一致していなかったと証言する。",
            "detail": "映像上のR-7は無人。生体センサーには微弱な人間反応。ALMA本体は映像側を優先して判断した。",
            "hint": "ALMAは嘘をついたのではない。嘘の入力を信じた。",
        },
        "hiyama_audit_file": {
            "name": "徹の暗号化監査ファイル",
            "chapter": 3,
            "summary": "檜山徹が死の直前に残した監査ファイル。白環市の運用偽装と犯人の手口が暗号化されていた。",
            "detail": "監査ファイルには、雨宮セナがセンサー同期を操作し、ALMAに『無人のR-7』を認識させた手順が残っている。",
            "hint": "真相を確定する最後の鍵。技術トリックと犯人を同時に結びつける。",
        },
    }

    deduction_questions = [
        {
            "id": "q1",
            "prompt": "Q1. 檜山徹が死亡した直接の原因を示す証拠は？",
            "answer": "r7_decompression_log",
            "hint": "まずは事件そのものを記録したログを示す。",
            "success": "R-7の減圧ログが、死亡時刻と区画状態を示している。",
            "failure": "それは原因よりも、手口や動機に近い証拠だ。",
        },
        {
            "id": "q2",
            "prompt": "Q2. 『徹は宇宙服で退避しようとした』という説明と矛盾する証拠は？",
            "answer": "haku3_unused",
            "hint": "使われたはずなのに、使われた痕跡がないものを探す。",
            "success": "HAKU-3に使用痕跡がない。事故説明は崩れた。",
            "failure": "退避行動の矛盾を直接示すものではない。",
        },
        {
            "id": "q3",
            "prompt": "Q3. ALMA本体ではなく、入力側が操作されたことを示す証拠は？",
            "answer": "admin_authority_log",
            "hint": "コード改ざんではなく、監視系の同期に注目する。",
            "success": "管理者権限ログは、監視系の再同期操作を示している。",
            "failure": "ALMAが何を見たかではなく、誰が入力をずらせたかが必要だ。",
        },
        {
            "id": "q4",
            "prompt": "Q4. 雨宮セナに檜山を止める動機があったことを示す証拠は？",
            "answer": "earth_conference_audio",
            "hint": "技術ではなく、政治的・経済的な圧力を示す証拠を選ぶ。",
            "success": "地球会議音声が、白環市とセナの動機を浮かび上がらせる。",
            "failure": "それは手口の証拠で、動機の説明には弱い。",
        },
        {
            "id": "q5",
            "prompt": "Q5. 『ALMAは偽の現実を見せられた』と説明できる証拠は？",
            "answer": "noa_testimony",
            "hint": "映像と生体センサーの食い違いを語った人物を思い出す。",
            "success": "ノアの証言により、ALMAの判断材料が矛盾していたとわかる。",
            "failure": "偽の現実そのものを説明するには、入力の食い違いが必要だ。",
        },
        {
            "id": "q6",
            "prompt": "Q6. 雨宮セナの偽装殺人を最終的に確定する証拠は？",
            "answer": "hiyama_audit_file",
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

