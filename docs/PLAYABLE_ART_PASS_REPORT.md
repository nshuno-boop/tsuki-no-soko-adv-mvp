# Phase 6 Playable Art Pass Report

## アート全体方針

Phase 6は、本素材化の前段として「通しプレイ中に場所・人物・証拠・感情の変化が即座に読める」状態を目指した。既存の軸である「冷たい月面都市に残る人間の体温」は維持し、派手なサイバーパンクではなく、生活感、補修跡、職能差、操作端末の実在感を増やした。

基本色は暗い紺、青みの灰、白、淡いシアン。警告・証拠・危険にはアンバーを限定使用した。背景の下部はテキストボックスの可読性を優先して暗く落とし、左右の立ち絵領域に強すぎる縦線や高輝度モチーフを置きすぎない方針にした。

Reference Polishでは、提示された生成画像を基準に、澪の立ち絵、タイトル背景、調査ハブ背景、最終推理背景、UIフレーム、証拠アイコンを再制作した。前回の単純図形ベースから、ノベルゲームの完成画面に近い密度と余白へ寄せている。

Player View QA後の追加修正では、目的表示と左立ち絵の顔が重なる問題を優先修正した。Ren'Py標準の `left` / `center` / `right` 配置を作品用transformで置き換え、キャラが上端に寄りすぎない腰上構図として見えるようにした。あわせて、澪はセナと同じ画面密度になるよう腰上寄りに再生成し、セナの立ち絵は澪の色替えに見えないよう、顔立ち、目元、髪型、衣装シルエットから再生成した。背景も施設ごとのモチーフが読めるよう再ブラッシュアップした。

## サブエージェントごとの判断

### A. Art Director Agent

- シロワを清潔な未来都市ではなく、生命維持と資源契約に縛られた閉鎖都市として見せる。
- 色だけでなく、配管、隔壁、保守表示、補修跡、都市運用UIで場所の差を出す。
- UIは未来感より、推理ADVとしての読みやすさと階層整理を優先する。

### B. Character Art Agent

- 全立ち絵は既存の `520x760` 透明PNGを維持し、Ren'Py上の `left` / `center` / `right` 配置を壊さない。
- 澪は腰上から太もも上までの構図で再生成し、セナと並べたときのサイズ差が出にくいようにした。表情差分は同一ポーズを保ちつつ、目元、口元、端末の発光差で最小限の感情差を追加した。
- セナは追加生成対象として、都市代表らしい柔らかさと疲弊を持つ別デザインへ再制作した。澪とは顔型、目元、髪型、服装の役割記号を分け、表情差分は `neutral` / `smile` / `calm` / `shaken` / `broken` を維持した。
- 職能差を小物と色で分けた。澪は監査、セナは代表、徹は生命維持、リツは技師、ルカは採掘、アカリは医療、ノアは月生まれ、ジンは企業法務。
- ALMAは人型化せず、波形・リング・警告表示で状態差を出した。

### C. Background Art Agent

- 9背景はすべて1920x1080で制作し、Ren'Py側で1280x720へスケールする。
- R-7、外口、影井戸、夜明けの窓は特に固有モチーフを強めた。Player View QA後、端末UI壁紙に見えすぎる背景は、窓、タンク、医療ベッド、外口、採掘坑などの施設モチーフを追加して再生成した。
- 重要CGはR-7事故、True Ending夜明け、徹の監査ファイル、白兎3号検証の4枚を追加した。

### D. UI / Graphic Design Agent

- タイトル画面を専用化し、タイトル背景とロゴを追加した。
- 会話ウィンドウ、名前欄、選択肢に制作済みUI画像を接続した。Player View QA後は、左端の見切れリスクを直し、会話窓左側へ話者の顔アップを追加した。
- 調査系UIは過剰装飾を避け、文字階層とボタンの見え方を優先した。Reference Polish後は、調査ハブ/証拠一覧/人物メモ/タイムライン/ALMAログに暗い調査画面背景を敷き、最終推理系には専用の推理背景を敷いた。
- Referoは、情報密度の高いUIで「装飾より階層」を優先する参考として軽く確認した。

### E. Ren'Py Integration Agent

- 既存のimage名とファイル名を維持し、進行・証拠・推理構造を触らない方針で統合した。
- `images.rpy` で背景とCGを1280x720にスケール表示するよう定義した。
- `transforms.rpy` で立ち絵の `left` / `center` / `right` を腰上構図に調整し、目的表示との重なりを避けた。
- `generate_placeholder_assets.py` は既存PNGを上書きせず、欠損補完専用に変更した。

### F. Playtest Presentation QA Agent

- Phase 6後はタイトル、プロローグ、第3章ハブ、証拠一覧、タイムライン、最終推理、True/Bad Endingを重点確認する。
- 特に、背景の情報量が会話文や目的表示を邪魔しないか、CG挿入でテンポが崩れないかを確認する。
- タイムラインは手書き表示と `case_timeline` データのズレが将来リスクとして残る。

## 追加/更新した本素材一覧

### 背景

- `bg_lander_interior.png`
- `bg_shirowa_hab_ring.png`
- `bg_core.png`
- `bg_oxygen_workshop_r7.png`
- `bg_outer_port.png`
- `bg_medbay.png`
- `bg_sena_office.png`
- `bg_dawn_window.png`
- `bg_shadow_well.png`

### 立ち絵

- 佐伯澪: `mio_neutral.png`, `mio_thinking.png`, `mio_surprised.png`, `mio_pained.png`
- 雨宮セナ: `sena_neutral.png`, `sena_smile.png`, `sena_calm.png`, `sena_shaken.png`, `sena_broken.png`
- 檜山徹: `toru_neutral.png`, `toru_tired.png`, `toru_gentle.png`, `toru_recording.png`
- 北条リツ: `ritsu_neutral.png`, `ritsu_anxious.png`, `ritsu_angry.png`, `ritsu_relieved.png`
- ルカ・ナディム: `luka_neutral.png`, `luka_sarcastic.png`, `luka_angry.png`, `luka_sad.png`
- 白石アカリ: `akari_neutral.png`, `akari_doctor.png`, `akari_worried.png`
- 雨宮ノア: `noah_neutral.png`, `noah_rebellious.png`, `noah_tears.png`, `noah_smile.png`
- 鷹峰ジン: `jin_neutral.png`, `jin_business_smile.png`, `jin_irritated.png`, `jin_defeated.png`
- ALMA: `alma_idle.png`, `alma_alert.png`, `alma_speaking.png`

### CG

- `cg_r7_incident.png`
- `cg_dawn_window_ending.png`
- `cg_toru_recording.png`
- `cg_outer_port_reveal.png`

### UI / Icons

- `title_background.png`
- `title_logo.png`
- `ui_textbox.png`
- `ui_nameplate.png`
- `ui_choice_button.png`
- `ui_evidence_card.png`
- `ui_log_panel.png`
- `ui_timeline_panel.png`
- `ui_alma_panel.png`
- `ui_menu_background.png`
- `ui_deduction_background.png`
- `portraits/portrait_*.png` 10点
- 証拠・人物・場所・警告アイコン8点

## 画面ごとの改善点

- タイトル画面: 参照画像ベースの完成画面風背景、ロゴ、縦並びメニューを追加した。
- 会話画面: テキストボックスと名前欄を細線・角飾り・シアン発光のUIに再接続した。名前欄と本文を画面内へ収め、左側に顔アップを出すことで、本文と表情を同時に追いやすくした。
- 第1章: R-7事故CGを追加し、事件発生の第一印象を強めた。
- 第3章: 徹の監査ファイル復号CGを追加し、真相接近の手応えを強めた。
- 第4章: 白兎3号検証CGを追加し、ログと物理証拠の矛盾を視覚化した。
- True Ending: 夜明けCGを追加し、タイトル回収の余韻を強めた。
- 調査UI: 証拠カード、タイムライン、ALMAログのフレーム画像を高密度化し、背景つきの端末画面として見えるようにした。
- 立ち絵配置: 目的表示との重なりを避けるため、全体配置を腰上構図寄りに変更した。

## まだプレースホルダーのままのもの

- BGM/SEは未実装。
- セーブ/ロード/設定画面はRen'Py標準寄りのまま。
- 立ち絵は同一生成方針で揃えたプレイアブル素材であり、商業完成版の最終手描き素材ではない。澪はReference Polish済みだが、他キャラは最終版で個別に描き直したい。
- タイムライン画面はまだ手書き表示で、`case_timeline` データ駆動化は未対応。

## 今後の最終仕上げポイント

- 実機スクリーンショットで、背景下部と会話ウィンドウのコントラストを確認する。
- 立ち絵の表情差分を、会話上の感情変化に合わせてさらに調整する。
- 重要証拠の表示統一、証拠詳細・人物メモ・タイムラインのスクロール対応を進める。
- BGM/SEプレースホルダーを追加し、証拠入手・ALMAログ・選択決定の手触りを上げる。
- Beta前に、CG挿入箇所のテンポと読後感を実機で確認する。
