# tsuki-no-soko-adv-mvp

推理ADV『月の底で、息をする』Ren'Py 8系MVPプロトタイプ。

2056年の月面南極都市《白環市》、通称「シロワ」を舞台に、証拠品入手・聞き込み・最終推理・エンディング分岐までを仮素材で確認するためのプロジェクトです。

## プロジェクト概要

- ジャンル: 推理ADV
- 想定規模: 2〜3時間の個人開発向けMVP
- 主人公: 佐伯澪、地球から来た監査官
- 舞台: 月面南極都市《白環市》、会話上の通称は「シロワ」
- 事件: 生命維持主任・檜山徹が酸素工房R-7の緊急減圧で死亡
- 真相: ALMAを改ざんしたのではなく、ALMAに偽の現実を見せた偽装殺人

## 現在の実装状況

- 現在の開発フェーズ: Phase 5 / Alpha Polish
- Alpha版バージョン: `v0.5-alpha`
- 証拠品IDベースのカタログ管理
- `add_evidence(id)` による証拠入手
- 章番号・章タイトルの進行管理
- 証拠品一覧スクリーン
- 人物メモスクリーン
- 聞き込み対象選択スクリーン
- ALMAログ風スクリーン
- 証拠提示式の最終推理
- 正解・不正解・ヒント表示
- True / Normal / Bad Ending 分岐
- 事件タイムライン画面
- 複数証拠提示式の推理問題
- Phase 4時点では、実機でプロローグから3エンディングまで通しプレイ可能であることを確認済み
- Phase 5変更後の再通しプレイは未確認

## Phase 2で追加した内容

- 固有名詞を改訂版へ更新
- 背景、立ち絵、UI、アイコン、CG、音声用フォルダを追加
- `tools/generate_placeholder_assets.py` で仮PNG素材を自動生成
- `game/images.rpy` にRen'Py画像定義を追加
- `script.rpy` に背景・立ち絵・ALMAログ表示を追加
- 証拠品データにカテゴリ、関連人物、関連施設、アイコンを追加
- `docs/ART_DIRECTION.md` にアートディレクションを追加
- `docs/IMAGE_PROMPTS.md` に完成素材向けプロンプト集を追加
- `docs/ASSET_MANIFEST.md` に素材管理表を追加

## Phase 3で追加した内容

- GitHub remote `origin` を設定済み
- `main` ブランチをGitHubへpush済み
- プロローグからエンディングまで進める「通しプレイMVP」構造を追加
- 章構成を以下に整理
  - プロローグ：シロワへようこそ
  - 第1章：息が止まった夜
  - 第2章：アルマは嘘をつかない
  - 第3章：影井戸の数字
  - 第4章：白兎は外へ出なかった
  - 最終章：だれのための空
  - エンディング
- 必須証拠15点を実装
- 章ごとの目的表示 `current_objective` を追加
- 聞き込み対象6名に、初回・追加・核心の会話段階を追加
- 最終推理9問と、人物指摘問題を追加
- True / Normal / Bad Ending の条件を整理
- Ren'Pyなしでも使える整合性チェック `tools/check_project_integrity.py` を追加
- プレイテスト用チェックリスト `docs/PLAYTEST_CHECKLIST.md` を追加

## Phase 4で追加した内容

- MVP表示基準を1280x720に統一
- 仮背景PNGを1280x720、仮立ち絵・ALMA画像を520x760で再生成
- 章タイトル表示の重複を避け、UIでは `chapter_title` のみを表示
- 証拠入手状態を `evidence_unlocked` に一本化し、`acquired` フィールドを削除
- 調査ハブから開ける「事件タイムライン」画面を追加
- Q3/Q4/Q6/Q8を複数証拠提示式に変更
- 最終推理後の短いリザルト表示を追加
- True Endingにノア、徹の監査ファイル、ALMAの最終記録を追加
- 開発者用 `label debug_menu` を追加
- GitHub Actionsの静的チェック `.github/workflows/static-check.yml` を追加
- `tools/check_project_integrity.py` にscreen / label / jump / call / 旧称 / acquired残存チェックを追加

## Hotfix: 日本語フォントと仮素材

- Ren'Py標準フォントでは日本語グリフが不足し、文字が四角の豆腐表示になることがあります。
- 日本語表示には `game/fonts/NotoSansJP-Regular.otf` が必要です。
- 名前欄などの強調用に `game/fonts/NotoSansJP-Bold.otf` も同梱しています。
- フォント設定はCSSではなく、Ren'Pyの `.rpy` ファイルで行います。このプロジェクトでは `game/font_config.rpy` に `gui.text_font`、`gui.interface_text_font`、`gui.language = "japanese-normal"`、各style設定をまとめています。
- OS付属フォント、たとえば Meiryo、MS Gothic、Yu Gothic はリポジトリに含めない方針です。
- 文字が四角に化ける場合は、フォントファイル未配置または `game/font_config.rpy` の設定ミスを確認してください。
- 仮素材はプレイ確認用であり、最終素材ではありません。Phase 4 Hotfixでは、画像内の大きな英字ラベルを削除し、背景・立ち絵・ALMA表示を雰囲気確認に耐える控えめなプレースホルダーへ寄せています。

## Phase 5で追加した内容

- プロローグ、第1章、第2章、第4章、最終章、エンディングの地の文と会話を軽く補強
- 第1章から第4章までの章末に短い「調査まとめ」を追加
- 聞き込み会話に、セナ、ルカ、アカリ、ノア、ジンの感情が見える台詞を追加
- 最終推理9問の問題文、ヒント、正解・不正解メッセージを自然な文に調整
- 調査ハブに「おすすめ行動」を1行表示
- 人物メモに「現在の印象」を追加
- 証拠品一覧で重要証拠が分かるように表示を追加
- `config.version` を `v0.5-alpha` に更新
- Alpha向けの `docs/ALPHA_GOALS.md` と `docs/CREDITS.md` を追加
- Phase 5品質監査の結果を `docs/PHASE5_REVIEW_REPORT.md` に追加

## 通しプレイMVPの状態

現在のMVPは、仮背景・仮立ち絵・テキストのみで以下を確認できます。

- 事件発生
- 証拠入手
- 聞き込み
- 証拠不足警告
- 最終推理
- 3種類のエンディング分岐

Phase 4時点では実機で最後までプレイ可能であることを確認済みです。Phase 5の文章・UI微調整後は、再度の通しプレイ確認が必要です。本格的な演出、BGM/SE、本素材、長い会話分岐は未実装です。

## ファイル構成

```text
tsuki-no-soko-adv-mvp/
  game/
    audio/
      bgm/
      se/
    fonts/
      NotoSansJP-Regular.otf
      NotoSansJP-Bold.otf
    images/
      bg/
      chars/
      cg/
      icons/
      ui/
    characters.rpy
    evidence.rpy
    images.rpy
    options.rpy
    screens.rpy
    script.rpy
  docs/
    ART_DIRECTION.md
    ALPHA_GOALS.md
    ASSET_MANIFEST.md
    CREDITS.md
    FONT_LICENSE.md
    IMAGE_PROMPTS.md
    PLAYTEST_CHECKLIST.md
    PHASE5_REVIEW_REPORT.md
  tools/
    check_project_integrity.py
    generate_placeholder_assets.py
  Start_TsukiNoSoko_ADV_MVP.cmd
  .github/
    workflows/
      static-check.yml
```

## ローカル起動ショートカット

Windowsでは、ルートにある `Start_TsukiNoSoko_ADV_MVP.cmd` からRen'Py SDKを探して起動します。デスクトップショートカットを作っている場合も、このcmdを呼び出す想定です。

Ren'Py SDKを移動した場合は、cmd内のSDK探索パスを確認してください。

## 画面サイズ

MVPでは1280x720を基準にしています。

- 背景: 1280x720
- 立ち絵・ALMA表示: 520x760
- 本素材化時は16:9を維持すれば、1920x1080などへ差し替え可能です。

## 素材生成方法

Pythonで仮素材を生成します。

```powershell
python tools/generate_placeholder_assets.py
```

Pillowが使える場合は、プレイ確認用の仮背景・仮立ち絵・仮UI・仮アイコンを生成します。Pillowが使えない場合も、Python標準ライブラリのみで最低限のPNGを生成するフォールバックがあります。

この作業環境ではPATH上の `python` が見つからないため、Codex付属Pythonで生成確認しました。

## 整合性チェック

Ren'Py本体がない環境でも、最低限のファイル・画像・証拠ID・名称体系を確認できます。

```powershell
python tools/check_project_integrity.py
```

このチェックはRen'Py構文を完全に解析するものではありません。最終確認にはRen'Py Launcherでの起動と `renpy lint` が必要です。

## 推理UX

事件タイムライン画面では、時刻、出来事、説明を確認できます。関連証拠の入手状態に応じた段階表示は、Beta向けの改善候補として `docs/PHASE5_REVIEW_REPORT.md` に記録しています。

第3章の調査ハブでは、左カラムに6人の聞き込み対象を固定表示します。第4章へ進むには4人以上への初回聞き込みが必要で、条件未達時は不足人数と未聞き込み対象を表示します。

最終推理では、単一証拠提示に加えて複数証拠提示があります。複数証拠問題では、必要な証拠だけを過不足なく選ぶ必要があります。True EndingにはQ6、Q8、Q9の正解が必須です。

最終推理中は「調査に戻る」から第5章の調査ハブへ戻れます。証拠不足のまま進む場合は、空の証拠選択で止まらずBad Endingへ分岐します。

途中セーブやデバッグジャンプで証拠品の入手状態だけが欠けた場合に備え、第3章以降のハブ到達時にストーリー上入手済みであるべき証拠を自動同期します。

## 開発者用デバッグ導線

`label debug_menu` を追加しています。`config.developer` がTrueのときだけ使用する開発用導線です。

- すべての証拠を入手
- 重要証拠だけ入手
- 第3章 / 第5章 / 最終推理へジャンプ
- True / Normal / Bad Endingへジャンプ

通常プレイ用の導線ではありません。

## GitHub Actions

push / pull_request で静的チェックが走ります。

- Pillowをインストール
- 仮素材を再生成
- `tools/check_project_integrity.py` を実行
- Pythonスクリプトを `py_compile`

Ren'Py本体の導入はCIに含めていません。Ren'Py Launcherでの手動確認は引き続き必要です。

## GitHub

git remote は以下のURLで設定済みです。

```text
origin https://github.com/nshuno-boop/tsuki-no-soko-adv-mvp.git
```

## Ren'Pyでの確認方法

Ren'Py Launcherからこのフォルダをプロジェクトとして追加し、起動してください。

この環境ではRen'Py本体コマンドがPATHにない可能性があります。その場合、ここでは `renpy lint` ではなく、Python構文チェック、ファイル存在確認、Ren'Py構文の目視確認を行います。

## 未確認事項

- Phase 5変更後の通しプレイ再確認
- セーブ・ロード・バックログなど標準UIとの見た目の整合
- タイトル画面などRen'Py標準UIとの細部の統一

## 次にやること

1. Phase 5変更後の通しプレイ
2. 誤字脱字修正
3. 各キャラの会話量の微調整
4. UIの文字量調整
5. BGM/SE追加
6. 背景・立ち絵の本素材化
7. 演出強化
8. Beta前の最終調整

## Phase 6 Playable Art Pass

Phase 6では、通しプレイの没入感を上げるため、主要な仮素材を本素材寄りの playable art に更新しました。

Reference Polishでは、提示された生成画像をビジュアル基準として、澪の立ち絵、タイトル背景、調査/推理系の背景、UIフレーム、証拠アイコンを再ブラッシュアップしました。単純な仮図形ではなく、実際のプレイ画面で「読ませる」密度と質感に寄せています。

- 背景9点を1920x1080の月面都市ビジュアルへ更新
- 主要立ち絵差分とALMA差分を透明PNGとして更新
- タイトル背景、タイトルロゴ、会話UI、選択肢、証拠カード、ログ/タイムライン/ALMAパネルを更新
- R-7事故、徹の監査ファイル、白兎3号検証、True Ending夜明けのCGを追加
- `game/images.rpy` で背景とCGを1280x720表示へスケール
- `tools/generate_placeholder_assets.py` は既存PNGを上書きせず、欠損補完用に変更

まだBGM/SE、標準セーブ/ロード/設定画面の専用化、最終手描き素材化は未完了です。次は実機スクリーンショット確認、BGM/SEプレースホルダー、Beta前の本磨きを行います。
