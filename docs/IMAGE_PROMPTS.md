# IMAGE PROMPTS

将来の本素材制作や画像生成AI向けのプロンプト集。既存作品名、特定作家名、既存キャラクター名は使わない。

## 共通ネガティブ指定

No existing anime, movie, game, celebrity, or known character references. No direct imitation of a specific artist. Avoid excessive cyberpunk neon, fantasy city design, full glass dome moon city, unreadable UI, overdesigned costumes, glossy toy-like surfaces.

## VN用共通構図

- 背景は下部テキストボックス領域を暗く潰しすぎず、左右に立ち絵を置いても主要モチーフが隠れない構図にする。
- 中央には調査対象や奥行きの焦点を置き、左右端は人物表示用の余白を残す。
- キャラクター立ち絵は同一キャラ内で顔・体格・服の比率を固定し、transparent PNG、足元または腰位置のアンカーを揃える。
- キャラクター生成時は、既存キャラとの差別化を明示する。顔型、目の形、髪型、姿勢、シルエット、職能小物を変え、色替えや近い美形顔に寄せない。
- ALMA UIは no eyes, no mouth, no mascot, no humanoid assistant avatar を必ず入れる。

## 背景プロンプト

| ファイル名 | 用途 | 推奨サイズ | プロンプト |
| --- | --- | --- | --- |
| bg_lander_interior.png | 月面降下船内部 | 1920x1080 | A grounded near-future lunar lander interior in 2056, compact cockpit, worn control panels, pale cyan status lights, cold navy shadows, practical industrial design, subtle signs of human use, visual novel background, no characters. |
| bg_shirowa_hab_ring.png | シロワ中央居住環 | 1920x1080 | Central habitation ring of a lunar south pole city called Shirowa, clean but lived-in corridors, handrails, maintenance tape, small personal items, cool gray and cyan palette, believable corporate-managed moon city, visual novel background. |
| bg_core.png | コア | 1920x1080 | AI operations core for a lunar city, server columns, monitoring walls, calm cyan interface glow, precise functional layout, no humanoid AI, quiet tension, dark navy and white, visual novel investigation background. |
| bg_oxygen_workshop_r7.png | 酸素工房R-7 | 1920x1080 | Oxygen processing workshop R-7 in a lunar city, industrial tanks, pressure doors, warning stripes, emergency decompression aftermath, cold light, practical machinery, subtle damage, mystery ADV background. |
| bg_outer_port.png | 外口 | 1920x1080 | EVA outer port airlock, spacesuit racks, pressure warning signs, heavy sealed doors, moon dust traces, cold blue-gray lighting, boundary between breathable city and vacuum, visual novel background. |
| bg_medbay.png | 医療室 | 1920x1080 | Lunar city medical bay, compact examination room, sterile white and blue surfaces, worn equipment, charts for low-gravity born residents, soft but tired atmosphere, visual novel background. |
| bg_sena_office.png | セナ執務室 | 1920x1080 | Office of the representative of Shirowa, restrained corporate lunar design, city operation screens, water resource maps, low warm desk light against cold blue city lighting, tense quiet mood, visual novel background. |
| bg_dawn_window.png | 夜明けの窓 | 1920x1080 | Observation window on the moon, edge of lunar dawn, cold regolith outside, faint earthlight, quiet hope, functional interior frame, no glass dome city, visual novel ending background. |
| bg_shadow_well.png | 影井戸 | 1920x1080 | Permanently shadowed lunar mining pit, water ice extraction site, dark industrial shafts, hazard lights, cables, frost, harsh practical worksite, lonely and dangerous atmosphere, visual novel background. |

## キャラクタープロンプト

| キャラ | 用途 | 推奨サイズ | プロンプト |
| --- | --- | --- | --- |
| 佐伯澪 | 立ち絵 | 900x1400 transparent PNG | Young Earth audit officer, practical inspection jacket, calm but inexperienced, neat short-to-medium dark hair, subtle tired eyes, grounded near-future lunar mystery ADV character sprite, simple readable silhouette. Expressions: neutral, thinking, surprised, pained. |
| 雨宮セナ | 立ち絵 | 900x1400 transparent PNG | Representative of Shirowa lunar city, early-to-mid 30s, soft oval face, tired gentle amber-brown eyes with slightly downturned corners, long warm chestnut-brown hair partly tied back with loose side strands, refined ivory/taupe civic coat over muted teal high-collar dress, subtle amber administrative accents, calm public face with hidden pressure. Must not look like a recolor of Mio; change face shape, eye shape, hairstyle, silhouette, and outfit role. Expressions: neutral, smile, calm, shaken, broken. |
| 檜山徹 | 立ち絵 | 900x1400 transparent PNG | Life support chief, honest exhausted engineer, utility uniform, signs of long work in oxygen systems, kind eyes, recorded-message variant, grounded design. Expressions: neutral, tired, gentle, recording. |
| 北条リツ | 立ち絵 | 900x1400 transparent PNG | ALMA systems engineer, distinct from Mio: angular narrow face, thin tired eyes, rectangular glasses, short ash-gray/blue-gray undercut pixie hair, forward-hunched nervous posture, slate technical jumpsuit, utility vest, wrist terminal, cable probe, tool pouch, cyan diagnostic accents. More engineer than investigator, not a black-haired bob, not a tablet-holding Mio silhouette. Expressions: neutral, anxious, angry, relieved. |
| ルカ・ナディム | 立ち絵 | 900x1400 transparent PNG | Mining chief from the Shadow Well, rugged lunar workwear, dust marks, direct gaze, sarcastic posture, practical safety gear. Expressions: neutral, sarcastic, angry, sad. |
| 白石アカリ | 立ち絵 | 900x1400 transparent PNG | Medical chief caring for moon-born residents, clean medical coat over practical clothes, calm fatigue, gentle but firm expression, pale blue-white palette. Expressions: neutral, doctor, worried. |
| 雨宮ノア | 立ち絵 | 900x1400 transparent PNG | Girl born on the moon, slightly rebellious, light utility hoodie, small personal charm, fragile strength, not overly cute, grounded sci-fi design. Expressions: neutral, rebellious, tears, smile. |
| 鷹峰ジン | 立ち絵 | 900x1400 transparent PNG | Corporate PR and legal officer for Selene Resource Development, clean suit adapted for lunar city, polished smile, controlled posture, subtle corporate orange-gray accent. Expressions: neutral, business smile, irritated, defeated. |
| ALMA UI | UI波形 | 900x1400 transparent PNG | Non-humanoid AI management interface, cyan waveform, status rings, calm system panel, no face, no human body, functional city operations UI. States: idle, alert, speaking. |

## UI素材プロンプト

| ファイル名 | 用途 | 推奨サイズ | プロンプト |
| --- | --- | --- | --- |
| ui_textbox.png | テキストボックス | 1100x230 | Dark navy visual novel textbox, thin cyan lines, clean readable futuristic lunar city interface, slight transparency, no text. |
| ui_nameplate.png | 名前表示 | 420x90 | Compact dark nameplate UI, cyan accent line, practical operations terminal feel, no text. |
| ui_evidence_card.png | 証拠カード | 760x420 | Evidence card panel for mystery ADV, dark navy, amber highlight, clear information hierarchy, no text. |
| ui_log_panel.png | ログ画面 | 900x520 | ALMA system log panel, dark terminal UI, cyan grid lines, practical and readable, no text. |
| ui_choice_button.png | 選択ボタン | 760x120 | Wide choice button panel, dark gray-blue, cyan hover-like border, clear readable visual novel UI, no text. |
| ui_timeline_panel.png | タイムライン | 900x320 | Investigation timeline panel, dark lunar operations UI, violet-cyan accents, no text. |
| ui_alma_panel.png | ALMAパネル | 900x520 | AI operations panel, cyan waveform motif, dark background, non-humanoid, no text. |

## アイコン素材プロンプト

| ファイル名 | 用途 | 推奨サイズ | プロンプト |
| --- | --- | --- | --- |
| icon_evidence_log.png | ログ証拠 | 256x256 | Minimal evidence log icon, dark navy tile, cyan terminal lines, no text, readable at small size. |
| icon_evidence_suit.png | 宇宙服証拠 | 256x256 | Minimal spacesuit evidence icon, white suit silhouette, cyan outline, dark lunar UI tile, no text. |
| icon_evidence_audio.png | 音声証拠 | 256x256 | Minimal audio waveform evidence icon, cyan waveform and amber marker, dark tile, no text. |
| icon_evidence_medical.png | 医療証拠 | 256x256 | Minimal medical record evidence icon, clean cross-like form without real-world logo, blue-white palette, no text. |
| icon_evidence_key.png | 権限証拠 | 256x256 | Minimal admin key evidence icon, access token shape, cyan and amber accents, no text. |
| icon_person.png | 人物 | 256x256 | Minimal person profile icon, neutral silhouette, dark navy tile, cyan line, no text. |
| icon_location.png | 場所 | 256x256 | Minimal location marker icon for lunar city investigation, cyan map pin, dark tile, no text. |
| icon_warning.png | 警告 | 256x256 | Minimal warning icon, amber triangle, dark navy tile, clean functional UI, no text. |

## ファイル名対応表

背景、立ち絵、ALMA、UI、アイコンの現在のファイル名は `docs/ASSET_MANIFEST.md` を正とする。

## Phase 6 Playable Art Prompt Notes

Phase 6では、実際のPNGアセットを生成して組み込んだ。今後さらにAI画像生成や外部制作へ渡す場合は、以下を基準にする。

Reference Polishでは、生成済みの画面モックを基準に、澪の監査官デザイン、タイトル/調査ハブ/最終推理の情報密度、透明パネルUIの質感を強化した。以後の追加生成では、この方向をanchorとして扱う。

### 共通スタイル

- Japanese mystery visual novel, late-2050s lunar city, clean but lived-in, restrained near-future design.
- Cold navy, blue-gray, white, pale cyan, limited amber warning lights.
- Not cyberpunk, not neon-heavy, not toy-like, no large embedded labels.
- Keep the lower 30 percent readable for dialogue UI.
- Keep left and right sides calm enough for character sprites.

### Background anchors

- Lander interior: cramped cockpit, moon ridge outside, transport labels, quiet arrival tension.
- Shirowa hab ring: residential railings, repair tape, personal traces, human life inside a closed city.
- Core: ALMA operation wall, server rings, waveform panels, silent machine intelligence.
- Oxygen workshop R-7: oxygen tanks, pressure doors, frost, warning amber and muted red.
- Outer port: suit racks, airlock, moon dust, subtle footprints, cold white-blue lighting.
- Medbay: tired medical equipment, low-gravity child charts, soft clinical light.
- Sena office: orderly corporate room, water/resource map, warm desk light, quiet pressure.
- Dawn window: thin lunar dawn, large window frame, distant light, restrained hope.
- Shadow well: mining shaft, cables, frost, powder, deep vertical darkness.

### Character anchors

- Mio: young Earth auditor, clean audit jacket, observant, slightly stiff.
- Sena: city representative, distinct from Mio by face shape, downturned amber eyes, long chestnut hair, ivory civic coat, tired responsibility, controlled collapse.
- Toru: life-support engineer, practical workwear, sincere and exhausted.
- Ritsu: ALMA engineer, angular face, short ash-gray undercut, glasses, nervous honesty, cable probe, wrist terminal, blue technical accents.
- Luka: mining worker, dusty utility clothing, sarcasm with warmth.
- Akari: doctor, calm and tired, distinct from Mio/Sena/Ritsu by soft rounded face, gray-green eyes, pale warm silver-brown low side bun, no glasses, blue-gray scrubs, pale blue-lined medical coat, scanner, and compact diagnostic tablet.
- Noah: lunar-born youth, defensive softness, lightweight utility hoodie.
- Jin: corporate legal PR, neat suit, warm-gray and orange corporate accents.
- ALMA: non-human interface, ring/waveform/light state, never mascot-like.

### Phase 6.2 Akari / Dialogue UI Notes

- Akari sprites should keep a softer medical silhouette: rounded face, low side bun, clinical scrubs, and a scanner. Avoid black bob hair, tablet-holding audit poses, civic-representative robes, or ALMA engineer glasses.
- Dialogue textbox art should favor a dense readable navy surface. Decorative brackets, dotted guide lines, and highly transparent fills must stay outside the main text-safe area.
