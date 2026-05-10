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

## 通しプレイMVPの状態

現在のMVPは、仮背景・仮立ち絵・テキストのみで以下を確認できます。

- 事件発生
- 証拠入手
- 聞き込み
- 証拠不足警告
- 最終推理
- 3種類のエンディング分岐

本格的な演出、BGM/SE、本素材、長い会話分岐は未実装です。

## ファイル構成

```text
tsuki-no-soko-adv-mvp/
  game/
    audio/
      bgm/
      se/
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
    ASSET_MANIFEST.md
    IMAGE_PROMPTS.md
    PLAYTEST_CHECKLIST.md
  tools/
    check_project_integrity.py
    generate_placeholder_assets.py
  .github/
    workflows/
      static-check.yml
```

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

Pillowが使える場合は、ラベル付きの仮背景・仮立ち絵・仮UI・仮アイコンを生成します。Pillowが使えない場合も、Python標準ライブラリのみで最低限のPNGを生成するフォールバックがあります。

この作業環境ではPATH上の `python` が見つからないため、Codex付属Pythonで生成確認しました。

## 整合性チェック

Ren'Py本体がない環境でも、最低限のファイル・画像・証拠ID・名称体系を確認できます。

```powershell
python tools/check_project_integrity.py
```

このチェックはRen'Py構文を完全に解析するものではありません。最終確認にはRen'Py Launcherでの起動と `renpy lint` が必要です。

## 推理UX

事件タイムライン画面では、時刻、出来事、説明、関連証拠を確認できます。関連証拠が未入手の場合は「未入手の関連証拠あり」と表示されます。

最終推理では、単一証拠提示に加えて複数証拠提示があります。複数証拠問題では、必要な証拠だけを過不足なく選ぶ必要があります。True EndingにはQ6、Q8、Q9の正解が必須です。

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

- Ren'Py Launcherでの起動確認
- `renpy lint`
- UI画像をRen'PyのFrame背景として使ったときの見た目
- すべての聞き込みから最終推理までの通しプレイ
- セーブ・ロード・バックログなど標準UIとの見た目の整合

## 次にやること

1. Ren'Py本体での起動確認
2. `renpy lint`
3. 推理パートの通しプレイ
4. 誤字脱字修正
5. 各キャラの会話量増加
6. UIの文字量調整
7. BGM/SE追加
8. 背景・立ち絵の本素材化
