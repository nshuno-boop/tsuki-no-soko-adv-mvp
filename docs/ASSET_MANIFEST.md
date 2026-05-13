# ASSET MANIFEST

Phase 6 Playable Art Pass時点では、通しプレイMVPで参照している主要画像を playable art として更新した。追加のReference Polishでは、提示された生成画像の方向性をもとに、澪の立ち絵、タイトル/メニュー背景、推理画面背景、UIフレーム、証拠アイコンを再ブラッシュアップした。

MVP表示基準は1280x720。背景とCGは1920x1080で制作し、Ren'Py側で1280x720へスケールして表示する。立ち絵とALMA UI画像は520x760の透明PNGとして維持する。

今回の素材は商業完成版の最終素材ではないが、プレイテスト中にplaceholder感が主役にならない水準を目指した。

状態:

- placeholder: 今回生成した仮素材
- playable: 本素材寄りのプレイテスト用素材
- needed: まだ必要
- final: 本素材化済み
- unused: 未使用候補

## Backgrounds

| File | Description | Status |
| --- | --- | --- |
| game/images/bg/bg_lander_interior.png | 月面降下船内部 | playable |
| game/images/bg/bg_shirowa_hab_ring.png | シロワ中央居住環 | playable |
| game/images/bg/bg_core.png | コア | playable |
| game/images/bg/bg_oxygen_workshop_r7.png | 酸素工房R-7 | playable |
| game/images/bg/bg_outer_port.png | 外口 | playable |
| game/images/bg/bg_medbay.png | 医療室 | playable |
| game/images/bg/bg_sena_office.png | セナ執務室 | playable |
| game/images/bg/bg_dawn_window.png | 夜明けの窓 | playable |
| game/images/bg/bg_shadow_well.png | 影井戸 | playable |

## CG

| File | Description | Status |
| --- | --- | --- |
| game/images/cg/cg_r7_incident.png | R-7事故直後 | playable |
| game/images/cg/cg_dawn_window_ending.png | True Ending夜明け | playable |
| game/images/cg/cg_toru_recording.png | 徹の監査ファイル復号 | playable |
| game/images/cg/cg_outer_port_reveal.png | 白兎3号検証 | playable |

## Character Sprites

| Character | Files | Status |
| --- | --- | --- |
| 佐伯澪 | mio_neutral.png, mio_thinking.png, mio_surprised.png, mio_pained.png | reference-polished |
| 雨宮セナ | sena_neutral.png, sena_smile.png, sena_calm.png, sena_shaken.png, sena_broken.png | playable |
| 檜山徹 | toru_neutral.png, toru_tired.png, toru_gentle.png, toru_recording.png | playable |
| 北条リツ | ritsu_neutral.png, ritsu_anxious.png, ritsu_angry.png, ritsu_relieved.png | playable |
| ルカ・ナディム | luka_neutral.png, luka_sarcastic.png, luka_angry.png, luka_sad.png | playable |
| 白石アカリ | akari_neutral.png, akari_doctor.png, akari_worried.png | playable |
| 雨宮ノア | noah_neutral.png, noah_rebellious.png, noah_tears.png, noah_smile.png | playable |
| 鷹峰ジン | jin_neutral.png, jin_business_smile.png, jin_irritated.png, jin_defeated.png | playable |
| ALMA | alma_idle.png, alma_alert.png, alma_speaking.png | playable |

## UI

| File | Description | Status |
| --- | --- | --- |
| game/images/ui/title_background.png | タイトル背景 | playable |
| game/images/ui/title_logo.png | タイトルロゴ | playable |
| game/images/ui/ui_textbox.png | テキストボックス | playable |
| game/images/ui/ui_nameplate.png | 名前表示 | playable |
| game/images/ui/ui_evidence_card.png | 証拠カード | playable |
| game/images/ui/ui_log_panel.png | ログパネル | playable |
| game/images/ui/ui_choice_button.png | 選択ボタン | playable |
| game/images/ui/ui_timeline_panel.png | タイムラインパネル | playable |
| game/images/ui/ui_alma_panel.png | ALMAパネル | playable |
| game/images/ui/ui_menu_background.png | メニュー背景 | playable |
| game/images/ui/ui_deduction_background.png | 最終推理/証拠提示背景 | reference-polished |

## Icons

| File | Description | Status |
| --- | --- | --- |
| game/images/icons/icon_evidence_log.png | ログ証拠 | playable |
| game/images/icons/icon_evidence_suit.png | 宇宙服証拠 | playable |
| game/images/icons/icon_evidence_audio.png | 音声証拠 | playable |
| game/images/icons/icon_evidence_medical.png | 医療証拠 | playable |
| game/images/icons/icon_evidence_key.png | 鍵証拠 | playable |
| game/images/icons/icon_person.png | 人物 | playable |
| game/images/icons/icon_location.png | 場所 | playable |
| game/images/icons/icon_warning.png | 警告 | playable |

## Fonts

| File | Description | Status |
| --- | --- | --- |
| game/fonts/NotoSansJP-Regular.otf | 日本語本文用フォント / SIL OFL 1.1 | final |
| game/fonts/NotoSansJP-Bold.otf | 日本語名前欄・強調用フォント / SIL OFL 1.1 | final |

## BGM Candidates

| Use | Direction | Status |
| --- | --- | --- |
| プロローグ | 静かな降下、低いドローン、遠い通信音 | needed |
| 調査メニュー | 冷たい環境音、薄いパルス | needed |
| 酸素工房R-7 | 低い機械音、緊急感を抑えた緊張 | needed |
| 最終推理 | 心拍に近い低音、控えめな上昇感 | needed |
| True Ending | 冷たい夜明け、少しだけ暖かい和音 | needed |

## SE Candidates

| Use | Direction | Status |
| --- | --- | --- |
| 証拠入手 | 端末通知、短いシアン系UI音 | needed |
| ALMAログ表示 | 低いシステム起動音 | needed |
| 選択決定 | 控えめなクリック音 | needed |
| 不正解 | 警告音、短く乾いた音 | needed |
| エアロック | 圧力扉、空気音 | needed |
