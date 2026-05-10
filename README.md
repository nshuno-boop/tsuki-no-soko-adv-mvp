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
  tools/
    generate_placeholder_assets.py
```

## 素材生成方法

Pythonで仮素材を生成します。

```powershell
python tools/generate_placeholder_assets.py
```

Pillowが使える場合は、ラベル付きの仮背景・仮立ち絵・仮UI・仮アイコンを生成します。Pillowが使えない場合も、Python標準ライブラリのみで最低限のPNGを生成するフォールバックがあります。

この作業環境ではPATH上の `python` が見つからないため、Codex付属Pythonで生成確認しました。

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
4. 背景・立ち絵の本素材化
5. BGM/SE追加
6. GitHub remote追加とpush
