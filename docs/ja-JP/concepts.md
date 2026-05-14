## 設計原則

[English](../en-US/concepts.md) | [中文](../zh-CN/concepts.md) | [日本語](../ja-JP/concepts.md)

以下の 7 原則は visual-spec の設計信条です。コマンドの振る舞い、成果物の構造、レビューのしやすさはすべてこの原則に従って設計されています。原則を理解すると、なぜ前段で情報を埋める必要があるのか、各出力が実装・受入・変更同期にどう効くのかが読み解けます。

### 1. 成果物で合意する

- 核心思想：会話をレビュー可能な成果物に固定し、記憶ではなく証拠で合意する
- 何を解決する：結論が漂流する／レビューが抽象的になる／時間と人が変わると文脈が失われる
- visual-spec での現れ方：
  - [/vspec:new](../../README.md#commands) が `/specs/` に基礎成果物（ロール/用語/flows/シナリオ/機能一覧/未解決事項など）を作る
  - [/vspec:verify](../../README.md#commands) がレビュー可能な実行可能成果物（`/specs/models/`、`/specs/prototypes/`）へ落とす
  - [/vspec:detail](../../README.md#commands) と [/vspec:accept](../../README.md#commands) が実装可能・受入可能な仕様へ接続する

### 2. シナリオ駆動で分解する（機能の羅列ではない）

- 核心思想：機能リストではなく、ユーザーシナリオ/ノード連鎖で要件を分解する
- 何を解決する：主経路だけの仕様、ロールバック/例外の抜け、検証不能な曖昧仕様
- visual-spec での現れ方：
  - [/vspec:new](../../README.md#commands) が flows とシナリオ集合（主経路 + ロールバック）を出し、未解決事項も明示する
  - [/vspec:accept](../../README.md#commands) がシナリオを受入ケース（`/specs/acceptance/`）へ変換し、「実行可能な操作 + 検証可能な期待結果」を固定する

### 3. RBAC とデータ権限を先に設計する

- 核心思想：権限は後付けではなく、原型と詳細仕様の前提として先に設計する
- 何を解決する：画面は見えるが操作できない／データ可視範囲が曖昧で越権や誤操作が起きる
- visual-spec での現れ方：
  - [/vspec:verify](../../README.md#commands) がロール別ダッシュボード原型でロール差分を早期にレビューできるようにする（`/specs/prototypes/`）
  - [/vspec:detail](../../README.md#commands) が RBAC を領域/コントロール単位まで落とし、データ権限を独立に設計してから合成する（`/specs/details/`）

### 4. 実装に落ちる詳細にする

- 核心思想：挙動をチェックリスト/表/マトリクスで表現し、実装入力として直接使える形にする
- 何を解決する：「送信後は何が起きる？」「どの項目をどう検証する？」といった反復確認と漏れ
- visual-spec での現れ方：
  - [/vspec:detail](../../README.md#commands) がロード/操作/送信後挙動を表で、検証/ログ/通知をマトリクスで表現する（`/specs/details/`）
  - [/vspec:impl](../../README.md#commands) がリポジトリの技術スタック/規約に沿った実装入力を整形する

### 5. 一貫性と観測性をデフォルトにする

- 核心思想：信頼性と観測性を「要件の一部」として扱い、最後に埋めない
- 何を解決する：リトライ/DLQ/補償などが場当たりで不整合になる／trace/audit/alert がなく障害解析できない
- visual-spec での現れ方：
  - [/vspec:detail](../../README.md#commands) が外部依存、MQ、失敗時戦略、冪等、補償などを明示する（`/specs/details/`）
  - [/vspec:qc](../../README.md#commands) が欠落と矛盾をチェック可能なルールとして露出する（`/specs/qc_report.*`）

### 6. 受入 → 自動化 → 統合

- 核心思想：受入を共通言語にし、可能な限り自動化し、統合可能な入力へ接続する
- 何を解決する：正しいがテストできない要件／自動化の導入コストが高く運用されない
- visual-spec での現れ方：
  - [/vspec:accept](../../README.md#commands) が受入ケース（`/specs/acceptance/`）を作る
  - [/vspec:append-test](../../README.md#commands) が既存のテストフレームワーク/ディレクトリ規約を優先して保守負担を下げる
  - [/vspec:impl](../../README.md#commands) が最小差分でレビュー可能かつ E2E で動く統合入力を志向する

### 7. 変更しやすい要件

- 核心思想：要件は進化する。canonical な源泉を 1 つにし、派生成果物を同期する
- 何を解決する：変更後に原型/用例/仕様が漂流する／変更の根拠が追えない／下流の基準が割れる
- visual-spec での現れ方：
  - [/vspec:refine](../../README.md#commands) が canonical requirement を更新し、影響範囲の成果物を同期する
  - [/vspec:qc](../../README.md#commands) が変更後の新しい欠落/矛盾を素早く露出する

### 原則の協調関係

1. 成果物で合意する（1）が合意形成の方式と分層構造を決める  
2. シナリオ駆動（2）+ 権限優先（3）が曖昧さを前段で消し、レビューを具体化する  
3. 実装に落ちる詳細（4）+ 一貫性/観測性（5）が「交付可能な仕様」の基準を与える  
4. 受入→自動化→統合（6）+ 変更しやすい要件（7）がデリバリーと長期進化の閉ループを作る

### 早見表（原則 → コマンド → 成果物）

| 原則 | 注目コマンド | 主要成果物 |
| --- | --- | --- |
| 1. 成果物で合意する | [/vspec:new](../../README.md#commands)、[/vspec:verify](../../README.md#commands) | `/specs/`、`/specs/models/`、`/specs/prototypes/` |
| 2. シナリオ駆動で分解する | [/vspec:new](../../README.md#commands)、[/vspec:accept](../../README.md#commands) | `/specs/`（flows/scenarios/functions）、`/specs/acceptance/` |
| 3. RBAC とデータ権限を先に設計する | [/vspec:verify](../../README.md#commands)、[/vspec:detail](../../README.md#commands) | `/specs/prototypes/`、`/specs/details/` |
| 4. 実装に落ちる詳細にする | [/vspec:detail](../../README.md#commands)、[/vspec:impl](../../README.md#commands) | `/specs/details/`、`/specs/backend/`（有効時） |
| 5. 一貫性と観測性をデフォルトにする | [/vspec:detail](../../README.md#commands)、[/vspec:qc](../../README.md#commands) | `/specs/details/`、`/specs/qc_report.*` |
| 6. 受入→自動化→統合 | [/vspec:accept](../../README.md#commands)、[/vspec:append-test](../../README.md#commands)、[/vspec:impl](../../README.md#commands) | `/specs/acceptance/`、テストディレクトリまたは `/tests/` |
| 7. 変更しやすい要件 | [/vspec:refine](../../README.md#commands)、[/vspec:qc](../../README.md#commands) | canonical requirement（例：`original.md`）+ 影響する `/specs/` 成果物 |
