---
name: "visual-spec-skill"
description: "生要件を分析して visual spec と成果物を生成します。ユーザーが /vspec:new で分析を開始する時、または /vspec:verify でモデル/プロトタイプを生成する時に利用します。"
---

# Visual Spec Skill（日本語）

ユーザー入力に基づいて visual spec を分析し、短い要件メモをレビュー可能な構造化成果物へ変換します。

## 利用シーン

以下の状況で利用します：
- ビジネス側の要件説明が非常に簡略で、仕様化に必要な情報が欠けている
- ユーザーが `/vspec:new` を実行して新しい要件分析フローを開始する

## この Skill が定義すること

- シナリオ駆動のファシリテーションで詳細を補完する
- データモデルを設計する
- 補完した詳細に基づき UI モック/原型を生成する
- 業務ロジック詳細を可視化/構造化して出力する

## Commands

### `/vspec:new`

新しい要件分析セッションを開始します。

言語：
- `/scheme.yaml` の `selected.language` を読み取る（`en`、`zh-CN`、`ja`。欠落/不正なら `en`）
- コマンド引数または入力で `lang=<en|zh-CN|ja>` が明示された場合、その値を今回の実行に採用し、`selected.language` も更新する（該当フィールドのみ更新）
- `selected.language=en` の場合、`/specs/background/original.md` の見出しは必ず英語に統一し、非英語の見出しは以下へ正規化する：
  `# Raw Requirement`, `# Summary`, `# Business Context`, `# Core Features`, `# Pages & Interactions`, `# Data Model`, `# Business Logic`, `# Risks & Assumptions`, `# Open Questions`

Flow:
0. `/docs/` の存在を保証し、サブフォルダを作成する：
   - `/docs/legacy/`
   - `/docs/current/`
   - `/docs/refine/`
   - `/docs/dependencies/`
   - `/docs/change/` は作成しない（廃止）
0.2 ユーザーが引数に `lang=<en|zh-CN|ja>` を渡した場合、`/scheme.yaml` `selected.language` をその値へ更新する（該当フィールドのみ更新、その他のフィールド/フォーマットは保持）
0.5 ユーザーが早期に調整できるようにプロジェクト制約を作成する（既存なら上書きしない）：
   - `/scheme.yaml` が無ければ既定値（原型スタック選定 + catalog）で作成
   - `/prototype_ui_convention.md` が無ければ作成（`/scheme.yaml` と同階層）
1. ユーザーへ原始要件の入力を依頼する
2. ユーザーが Enter を押した入力を raw requirement として扱う
3. `prompts/vspec_new/background.md` を読み込む
4. プロンプトに従い要件を分析し、業務背景を拡張する
5. raw requirement と背景分析を `/specs/background/original.md` に書き込む
6. Open Questions セクションの質問にユーザーが回答するよう促す（見出しは選択言語に従う）
7. ユーザー回答後、`prompts/vspec_new/stakeholders.md` を読み込みステークホルダーを分析
8. 結果を `/specs/background/stakeholder.md`（markdown 表）へ書き込む
9. `prompts/vspec_new/roles.md` を読み込み、直接ユーザーの役割とタスクを分析
10. 結果を `/specs/background/roles.md` へ書き込む
11. `prompts/vspec_new/terms.md` を読み込み、用語と定義を抽出
12. 結果を `/specs/background/terms.md`（markdown 表）へ書き込む
13. `prompts/vspec_new/flows.md` を読み込み、業務フローを分析して PlantUML 泳道図を生成
14. 図を `/specs/flows/*.puml` に書き込む
15. `prompts/vspec_new/scenarios.md` を読み込み、ノード組合せでシナリオを列挙
16. 結果を `/specs/background/scenarios.md`（markdown 表）へ書き込む
17. `prompts/vspec_new/details_pre_post.md` を読み込み、ノードごとの詳細フォルダを作成し `pre_post.md` を生成
18. `prompts/vspec_new/details_constraints.md` を読み込み、`constraints.md` を生成
19. `prompts/vspec_new/details_variations.md` を読み込み、`variations.md` を生成
20. `prompts/vspec_new/details_boundaries.md` を読み込み、`boundaries.md` を生成
21. `prompts/vspec_new/details_symmetry.md` を読み込み、`symmetry.md` を生成
22. ノード別出力が `/specs/background/scenario_details/` に書き込まれていることを保証
23. `prompts/vspec_new/dependencies.md` を読み込み、外部依存システムを分析
24. 結果を `/specs/background/dependencies.md` へ書き込む
25. `prompts/vspec_new/functions.md` を読み込み、モジュール/外部依存ごとに機能一覧を生成
26. `/specs/functions/` に書き込む
27. `prompts/vspec_new/questions.md` を読み込み、質問一覧と必要資料を生成
28. `/specs/background/questions.md`（markdown リスト）に書き込む
29. `prompts/harness/post_new_verify.md` を読み込み、functions と scenario_details の完備性を検証（ログイン/設定/マスタ/承認など）。問題が出た場合は問題一覧を表示して停止
30. 構造化した分析結果を返し、次の設計ステップへ進む

### `/vspec:refine`

`/docs/refine/` の追補資料（またはコマンド引数で指定されたファイル/ディレクトリ）に基づき、要件を追補して更新します。

Flow:
0. `/specs/details/` が存在し非空であることを確認。欠ける場合は停止し、先に `/vspec:detail` を実行するよう促す
1. refine 入力を読む：
   - 引数があれば、それらを refine 入力ソース（ファイル/ディレクトリ）として扱う
   - 引数がなければ `/docs/refine/` を読む（`/docs/refine/file_list.md` があれば優先、なければファイル名順）
2. `prompts/vspec_refine/refine.md` が無い場合は即時停止し何もしない
3. `prompts/vspec_refine/refine.md` を読み込み、追補を適用し、口径を更新し、影響成果物を更新する
4. 結果を `/specs/background/original.md` に追記し、影響する `/specs/details/` と `/specs/prototypes/` を同期更新する

主な流れ：
1. `/specs/details/` が存在し非空であること（前提条件）
回答済みの質問に基づき要件を更新します。

Flow:
1. `/specs/background/questions.md` が無い場合は即時停止し何もしない
2. 未回答/保留の質問が無い場合は即時停止し何もしない
3. `/specs/background/questions.md` を読み、回答済みの項目を抽出
4. `prompts/vspec_refine/refine_q.md` を読み込み、回答を口径へマージ
5. 結果を `/specs/background/original.md` に追記
6. `/specs/background/questions.md` を更新し、本実行で「回答済みとして扱った項目」をマークする：
   - 回答とステータスを `<mark>...</mark>` で囲み、視認性を上げる（フィールド名は選択言語に従う）
3. `prompts/vspec_refine/refine.md` に従い、`/specs/background/original.md` へ追記し、必要な成果物を更新

### `/vspec:refine-q`
追加の確認質問を生成し、`/specs/background/questions.md` に追記します。

Flow:
1. `/specs/background/questions.md` が無い場合は停止し、先に `/vspec:new` を実行するよう促す
2. `prompts/vspec_more_q/more_q.md` を読み込み、追加質問を生成（重複排除・番号継続）
3. 新規項目のみを `/specs/background/questions.md` に追記（既存項目は書き換えない）
4. ユーザーが回答し、その後 `/vspec:refine-q` を実行するための明確な指示を出す
`/specs/background/questions.md` に記入された回答を要件へ取り込み、口径を更新します。

### `/vspec:more-q`
機能一覧に基づき要件詳細を展開します。

言語：
- `/scheme.yaml` `selected.language` を読み取る（`en`、`zh-CN`、`ja`。欠落/不正なら `en`）
- `/specs/` 配下に生成する仕様文書は、見出し/表/フィールド説明/ステータス/ボタン/メッセージ等を含め、必ず選択言語で統一する

Flow:
1. `/specs/functions/*` から機能一覧を読む
   - `/specs/functions/` 配下のすべてのファイルの全行を必ず走査する（core.md のみは不可）
2. 可能なら関連成果物を読む：`/specs/background/*`、`/specs/flows/*.puml`、`/specs/background/scenario_details/`、`/specs/background/roles.md`、既存の `/specs/models/*.md`（あれば）
3. 各機能（ページ/非ページ）について、関与する詳細成果物を先に判定し、必要なものだけ生成する（非関与部分の空文書を生成しない）
   - カバレッジ要件：走査した全行について、最低でも `rbac.md` と `data_permission.md` を生成できなければならない。できない場合は明示的エラーで停止（黙ってスキップしない）
   - 常に生成する基礎文書：
     - `rbac.md`：ページ領域/コントロールまで落とした RBAC
     - `data_permission.md`：データ権限ルールとスコープ
   - ページ機能のみ：
     - `page_load.md`：ロード
      - `interaction.md`：インタラクション
     - `validation_matrix.md`：バリデーション行列（submit/save/approve/reject/cancel/change 等の送信系がある場合のみ）
     - `post_submit_check.md`：送信後チェック（送信がある場合）
     - `post_submit_processing.md`：送信後処理（送信がある場合）
     - `post_submit_navigation.md`：送信後遷移（送信がある場合）
   - 条件付き（関与するときのみ）：
     - `logging_matrix.md`：操作/監査ログ（変更履歴保持、監査、否認防止が必要な場合のみ）
     - `decision_matrix.md`：状態ごとの操作可否（ステータスマシンがあり、操作が状態/ロールで変わる場合）
     - `notification_matrix.md`：通知（通知要件がある場合）
     - `mq.md`：MQ/イベント設計（非同期イベント/キュー/クロスシステムがある場合）
     - `file_import.md`：インポート（要件がある場合）
     - `file_export.md`：エクスポート（要件がある場合）
     - `formula.md`：計算式/指標口径（計算がある場合）
     - `expression_tree.md`：式木（多段分岐がある場合、HTML）
    - `code_rules.md`：番号/コード生成（必要な場合）
    - `payment.md`：決済/返金/精算/対帳（必要な場合）
    - `auth.md`：非 SSO のアカウント/パスワード（必要な場合）
    - `judgemental_matrix.md`：判定行列（2+要素の多因子分岐がある場合）
   - モジュール単位（最大 1 回、関与時のみ）：
     - `timeline.md`：時間軸（有効期限/締切/跨日等がフロー判断に影響する場合）
      - `state_machine.md`：状態一覧 + 遷移 + PlantUML（機能単位ではなく全体）
     - `nfp.md`：非機能要件（全体）
     - `cron_job.md`：定期実行（全体）
4. 関与して生成した文書のみを書き込む：
   - 機能単位：`/specs/details/<module_slug>/<logic_type>/<function_slug>.(md|html)`
   - モジュール単位：`/specs/details/<module_slug>/<logic_type>/<module_slug>.(md|html)`
既存の `questions.md` に追加の質問を生成して追記します（重複排除・番号継続）。追記後、回答手順を明示してユーザーに回答を促します。

### `/vspec:detail`
モデルと実行可能プロトタイプを生成して検証します。

言語：
- `/scheme.yaml` `selected.language` を読み取る（`en`、`zh-CN`、`ja`。欠落/不正なら `en`）
- `/specs/models/` とプロトタイプ UI 文言は選択言語で統一する

Flow:
0. `/specs/details/` が存在し非空であることを確認。欠ける場合は停止し、`/vspec:detail` を先に実行するようメッセージを出す
1. `/specs/background/questions.md` が存在し、未回答が残っている場合は、先に回答するよう促す（スキップは許容するが、未回答が残らないようにする）
2. `prompts/vspec_verify/model.md` を読み込みデータモデルを生成
3. `/specs/models/*.md` に書き込む
4. functions/details/models/roles に基づき、実行可能プロトタイプを生成（スタックは `/scheme.yaml` で選定。無ければ既定で自動作成）
   - `prompts/vspec_verify/prototype.md` を使用（`scheme.yaml` 遵守、html-only は不可）
5. `/specs/prototypes/` に書き込む
6. `prompts/harness/post_verify_stack_verify.md` でプロトタイプのスタック一致を検証。不一致があれば問題一覧を表示し停止
7. `prompts/vspec_verify/validation.md` でシナリオ検証ページを生成
8. `/specs/prototypes/` に書き込み、`scenario.html` をエントリとして提供
9. `prompts/vspec_verify/entries.md` でエントリページを生成し `/specs/prototypes/entries.html` に書き込む（メニュー/ヘッダーからはリンクしない）
10. `prompts/harness/post_verify_mobile_selection_check.md` でモバイルのデータ選択 UI を検証。不一致があれば停止
11. `prompts/harness/post_verify_price_format_check.md` で価格表示フォーマットを検証。不一致があれば停止
12. `prompts/harness/post_verify_click_check.md` でクリック無反応を検出。問題があれば停止
13. `prompts/harness/post_verify_verify.md` で原型の完備性を検証。問題があれば停止
機能一覧（`/specs/functions/*`）を入力に、各機能の詳細仕様（`/specs/details/`）を生成します。

### `/vspec:verify`
既存プロトタイプ上に Survey（アンケート）一式（Web 管理 + モバイル回答）を生成します。

Flow:
0. `/specs/prototypes/` が無い/空の場合は停止し、先に `/vspec:verify` を実行するよう促す
1. `/specs/functions/*`、`/specs/details/`、`/specs/models/*.md`、`/specs/background/roles.md`、`/specs/background/dependencies.md`、`/scheme.yaml` を読む（あれば）
2. `prompts/vspec_verify/prototype_survey.md` を読み込み、ページ/ルート/モックデータを生成/更新
3. Survey 関連の差分のみを書き込み、原型が動作する状態を保つ
モデル（`/specs/models/`）と実行可能プロトタイプ（`/specs/prototypes/`）を生成して素早く検証します。

### `/vspec:proto-survey`
既存プロトタイプ上に非 SSO の認証/アカウント機能（Web + モバイル）を生成します。

Flow:
0. `/specs/prototypes/` が無い/空の場合は停止し、先に `/vspec:verify` を実行するよう促す
1. `/specs/functions/*`、`/specs/details/`、`/specs/background/roles.md`、`/specs/background/dependencies.md`、`/scheme.yaml` を読む（あれば）
2. `prompts/vspec_verify/prototype_auth.md` を読み込み、ページ/ルート/セッションモック/ガードを生成/更新
3. auth 関連の差分のみを書き込み、原型が動作する状態を保つ
既存プロトタイプ上にアンケート機能一式（Web 管理 + モバイル回答）を追加生成します。

### `/vspec:proto-auth`
`/specs/` 配下の成果物を品質チェックします。

Note: Pro 版ではより広範なチェック（例：プロトタイプ/実装の post-run 検証）をサポートします（有償）。

言語：
- `/scheme.yaml` `selected.language` を読み取る（`en`、`zh-CN`、`ja`。欠落/不正なら `en`）
- QC レポート `/specs/qc_report.md` は選択言語で統一する

Flow:
1. `prompts/vspec_qc/quality_standard.md` の内蔵基準を読む
2. プロジェクト `qc/` 配下に錯題本がある場合、プロジェクトルート `quality_standard.md` を生成/更新する
3. プロジェクトルート `quality_standard.md` が存在する場合、補足/上書き基準としてマージする
4. `prompts/vspec_qc/qc.md` を読み込み、非適合チェックリストを生成する
5. `/specs/qc_report.md` に書き込む
既存プロトタイプ上に非 SSO の認証/アカウント機能（Web + モバイル）を追加生成します。

### `/vspec:qc`
受入テストケースを生成します。

言語：
- `/scheme.yaml` `selected.language` を読み取る（`en`、`zh-CN`、`ja`。欠落/不正なら `en`）
- `/specs/acceptance/` 配下の文書は選択言語で統一する

Flow:
1. `/specs/functions/*`、`/specs/background/scenarios.md`、`/specs/background/scenario_details/`、`/specs/background/roles.md`、`/specs/models/*.md` を読む
2. `prompts/vspec_accept/accept.md` を読み込み、主フロー/例外/境界/権限/データ範囲をカバーする受入ケースを生成
3. `/specs/acceptance/` に書き込み（機能ごとにサブフォルダ）、`/specs/acceptance/index.md` を生成
`/specs/` 配下の成果物を、内蔵品質基準（`prompts/vspec_qc/quality_standard.md`）等に基づいて品質チェックし、`/specs/qc_report.md` を出力します。

### `/vspec:accept`
受入ケースと仕様に基づき、自動テストコードを生成します。

言語：
- `/scheme.yaml` `selected.language` を読み取る（`en`、`zh-CN`、`ja`。欠落/不正なら `en`）
- テストケースのタイトル/説明は可能な限り選択言語に合わせる

Flow:
1. `/specs/acceptance/`、`/specs/functions/*`、`/specs/details/` を読み、リポジトリの既存テストフレームワークを検出する
2. `prompts/vspec_test/test.md` を読み込み、既存フレームワーク/規約に沿ったテストを生成する
3. テストコードを既存テストディレクトリ（無ければ `/tests/`）に書き込み、既存スクリプトで動作可能な形にする
4. `prompts/harness/post_append_test_coverage_check.md` でカバレッジ十分性を検証。問題があれば続行
5. 問題がある場合は、不足項目に絞って `/vspec:append-test` をもう 1 回実行し、再度チェックする
6. 2 回目でも問題が残る場合、問題一覧を表示して停止
7. 本コマンドはテスト生成/追加のみを行い、テストコマンドの実行はしない
受入テストケースを `/specs/acceptance/` に生成します。

### `/vspec:append-test`
仕様に基づき、フロント/バック統合コードを生成します。

Flow:
1. `/specs/functions/*`、`/specs/details/`、`/specs/models/*.md`、`/specs/background/dependencies.md` を読み、既存スタックと規約を検出する
2. `prompts/vspec_impl/implement.md` を読み込み、backend-first で実装：`/specs/backend/` に実行可能な backend を生成し、その後 frontend 連携を生成する
3. 変更は `/specs/` 配下のみに書き込み、差分を最小化してレビュー可能にする（backend は `/specs/backend/`、原型 frontend は `/specs/prototypes/`）
4. `prompts/harness/post_impl_verify.md` で backend の MVC 構造とテストカバレッジを検証。問題があれば停止
受入ケースと既存テストスタックをもとに、自動テストコードを生成します（テスト実行はしない）。

### `/vspec:impl`
`/docs/` 配下の資料（legacy/new inputs）に基づき、`/vspec:new` と同じ構造で `/specs/` を再生成/更新します。

言語：
- `/scheme.yaml` `selected.language` を読み取る（`en`、`zh-CN`、`ja`。欠落/不正なら `en`）
- 再生成される `/specs/**` は選択言語で統一する

Flow:
1. `/docs/current/file_list.md` の存在を保証。無ければ入力リストテンプレートを生成
2. `/docs/current/file_list.md` を読み、列挙された `/docs/` 配下のソース（`legacy/current`、必要に応じ `templates/texts/assets`）を順に読み、構造化情報（機能、依存、UI、ロール/権限、技術仕様）を抽出
3. `/specs/background/original.md` があれば現行口径として差分（継承/新規/変更/廃止）の基線にする
4. `prompts/vspec_upgrade/upgrade.md` を読み込み、`/specs/` を生成/更新（`/vspec:new` の出力規約を再利用）
5. 抽出した技術仕様を `/scheme.yaml` に同期し、`/vspec:verify` と `/vspec:impl` で利用できるようにする
仕様成果物をもとに、統合実装コード（API 契約、backend、frontend 連携）を `/specs/` 配下に生成します。

### `/vspec:upgrade`
ストーリーマップで分解し、見積と排期を生成します。

言語：
- `/scheme.yaml` `selected.language` を読み取る（`en`、`zh-CN`、`ja`。欠落/不正なら `en`）
- `/specs/plan/plan_estimate.md` と `/specs/plan/plan_schedule.html` は選択言語で統一する

Flow:
1. `/specs/functions/*`、`/specs/background/roles.md`、`/specs/background/scenarios.md`、`/specs/details/`、`/specs/background/dependencies.md` を読む
2. `prompts/vspec_plan/estimate.md` を読み込み、機能一覧に合わせて見積を生成
3. `/specs/plan/plan_estimate.md` に書き込む
4. `prompts/vspec_plan/schedule.md` を読み込み、排期とデリバリーマップを生成
5. `/specs/plan/plan_schedule.html` に書き込む
`/docs/legacy` と `/docs/current` の資料をもとに、`/vspec:new` と同様の構造で `/specs/` を再生成/更新します。

### `/vspec:plan`
MRD（市場/競合/ユーザー/プロダクト設計）分析パックを生成します。

Flow:
1. `/docs/market/` の存在を保証
2. 利用可能な成果物を読む：`/specs/background/original.md`、`/specs/background/roles.md`、`/specs/background/terms.md`、`/specs/background/scenarios.md`、`/specs/flows/*.puml`、`/specs/background/dependencies.md`、`/specs/functions/*`（あれば）
3. `prompts/vspec_mrd/mrd.md` を読み込む
4. 次のファイルへ書き込む：
   - `/docs/market/market.md`
   - `/docs/market/competitors.md`
   - `/docs/market/users.md`
   - `/docs/market/product_design.md`

## Prompt Files

- `prompts/vspec_new/background.md`：`/vspec:new` で raw requirement を受け取った直後に使うプロンプト
- `prompts/vspec_new/stakeholders.md`：ユーザーが `待确认问题` に回答した後、`/specs/background/stakeholder.md` を生成するためのプロンプト
- `prompts/vspec_new/roles.md`：`/specs/background/roles.md` を生成するためのプロンプト
- `prompts/vspec_new/terms.md`：`/specs/background/terms.md` を生成するためのプロンプト
- `prompts/vspec_new/flows.md`：`/specs/flows/*.puml` を生成するためのプロンプト
- `prompts/vspec_new/scenarios.md`：`/specs/background/scenarios.md` を生成するためのプロンプト
- `prompts/vspec_new/details_pre_post.md`：ノード単位の `pre_post.md` を生成するためのプロンプト
- `prompts/vspec_new/details_constraints.md`：ノード単位の `constraints.md` を生成するためのプロンプト
- `prompts/vspec_new/details_variations.md`：ノード単位の `variations.md` を生成するためのプロンプト
- `prompts/vspec_new/details_boundaries.md`：ノード単位の `boundaries.md` を生成するためのプロンプト
- `prompts/vspec_new/details_symmetry.md`：ノード単位の `symmetry.md` を生成するためのプロンプト
- `prompts/vspec_new/dependencies.md`：`/specs/background/dependencies.md` を生成するためのプロンプト
- `prompts/vspec_new/functions.md`：`/specs/functions/` を生成するためのプロンプト
- `prompts/vspec_new/questions.md`：`/specs/background/questions.md` を生成するためのプロンプト
- `prompts/vspec_more_q/more_q.md`：`/vspec:more-q` で `questions.md` に追加質問を追記するためのプロンプト
- `prompts/vspec_mrd/mrd.md`：`/vspec:mrd` で `/docs/market/` 配下に市場/競合/ユーザー/設計文書を生成するためのプロンプト
- `prompts/vspec_refine/refine.md`：`/vspec:refine` のプロンプト
- `prompts/vspec_refine/refine_q.md`：`/vspec:refine-q` のプロンプト
- `prompts/vspec_verify/model.md`：`/vspec:verify` で `/specs/models/*.md` を生成するためのプロンプト
- `prompts/vspec_verify/prototype.md`：`/vspec:verify` でスタック選定済み原型を生成するためのプロンプト（`scheme.yaml` 必須）
- `prompts/vspec_verify/validation.md`：`/vspec:verify` で `scenario.html` を生成するためのプロンプト
- `prompts/vspec_detail/rbac.md`：`/vspec:detail` で RBAC を生成するためのプロンプト
- `prompts/vspec_detail/data_permission.md`：`/vspec:detail` でデータ権限を生成するためのプロンプト
- `prompts/vspec_detail/page_load.md`：`/vspec:detail` でロード仕様を生成するためのプロンプト
- `prompts/vspec_detail/interaction.md`：`/vspec:detail` でインタラクション仕様を生成するためのプロンプト
- `prompts/vspec_detail/timeline.md`：`/vspec:detail` で時間軸 HTML を生成するためのプロンプト
- `prompts/vspec_detail/formula.md`：`/vspec:detail` で計算式を生成するためのプロンプト
- `prompts/vspec_detail/expression_tree.md`：`/vspec:detail` で式木 HTML を生成するためのプロンプト
- `prompts/vspec_detail/code_rules.md`：`/vspec:detail` で番号/コード生成規則を生成するためのプロンプト
- `prompts/vspec_detail/judgemental_matrix.md`：`/vspec:detail` で判定行列を生成するためのプロンプト
- `prompts/vspec_detail/validation_matrix.md`：`/vspec:detail` でバリデーション行列を生成するためのプロンプト
- `prompts/vspec_detail/post_submit_check.md`：`/vspec:detail` で送信後チェックを生成するためのプロンプト
- `prompts/vspec_detail/post_submit_processing.md`：`/vspec:detail` で送信後処理を生成するためのプロンプト
- `prompts/vspec_detail/post_submit_navigation.md`：`/vspec:detail` で送信後遷移を生成するためのプロンプト
- `prompts/vspec_detail/mq.md`：`/vspec:detail` で MQ 設計を生成するためのプロンプト
- `prompts/vspec_detail/logging_matrix.md`：`/vspec:detail` でログ行列を生成するためのプロンプト
- `prompts/vspec_detail/notification_matrix.md`：`/vspec:detail` で通知行列を生成するためのプロンプト
- `prompts/vspec_detail/nfp.md`：`/vspec:detail` で非機能要件を生成するためのプロンプト
- `prompts/vspec_detail/file_import.md`：`/vspec:detail` でインポート仕様を生成するためのプロンプト
- `prompts/vspec_detail/file_export.md`：`/vspec:detail` でエクスポート仕様を生成するためのプロンプト
- `prompts/vspec_detail/cron_job.md`：`/vspec:detail` で定期実行を生成するためのプロンプト
- `prompts/vspec_accept/accept.md`：`/vspec:accept` で受入ケースを生成するためのプロンプト
- `prompts/vspec_test/test.md`：`/vspec:append-test` で自動テストを生成するためのプロンプト
- `prompts/vspec_impl/implement.md`：`/vspec:impl` で統合実装を生成するためのプロンプト
- `prompts/vspec_upgrade/upgrade.md`：`/vspec:upgrade` で upgraded specs を生成するためのプロンプト
- `prompts/vspec_plan/estimate.md`：`/vspec:plan` で見積を生成するためのプロンプト
- `prompts/vspec_plan/schedule.md`：`/vspec:plan` で排期 HTML を生成するためのプロンプト
- `prompts/vspec_qc/qc.md`：`/vspec:qc` で QC レポートを生成するためのプロンプト
- `prompts/vspec_qc/quality_standard.md`：`/vspec:qc` が使用する内蔵品質基準

## 推奨ワークフロー

1. Skill をインストールする
2. `/vspec:new` を実行する
3. ユーザーに原始要件を入力してもらい、Enter を待つ
4. `prompts/vspec_new/background.md` を読み込み、要件分析を開始する
5. `待确认问题` にユーザーが回答するよう促す
6. `prompts/vspec_new/stakeholders.md` を読み込み、`/specs/background/stakeholder.md` を生成
7. `prompts/vspec_new/roles.md` を読み込み、`/specs/background/roles.md` を生成
8. `prompts/vspec_new/terms.md` を読み込み、`/specs/background/terms.md` を生成
9. `prompts/vspec_new/flows.md` を読み込み、`/specs/flows/*.puml` を生成
10. `prompts/vspec_new/scenarios.md` を読み込み、`/specs/background/scenarios.md` を生成
11. `prompts/vspec_new/details_pre_post.md` を読み込み、ノード単位の `pre_post.md` を生成
12. `prompts/vspec_new/details_constraints.md` を読み込み、`constraints.md` を生成
13. `prompts/vspec_new/details_variations.md` を読み込み、`variations.md` を生成
14. `prompts/vspec_new/details_boundaries.md` を読み込み、`boundaries.md` を生成
15. `prompts/vspec_new/details_symmetry.md` を読み込み、`symmetry.md` を生成
16. `prompts/vspec_new/dependencies.md` を読み込み、`/specs/background/dependencies.md` を生成
17. `prompts/vspec_new/functions.md` を読み込み、`/specs/functions/` を生成
18. `prompts/vspec_new/questions.md` を読み込み、`/specs/background/questions.md` を生成
19. 生成された分析手順に従ってプロジェクトを継続する

## 出力ゴール

- 業務目的とコアユーザーシナリオを明確化する
- 主要ロール、ページ/モジュール、インタラクションフローを特定する
- エンティティと主要フィールドを抽出する
- 次の設計ステップへ進むための要件ドラフトを生成する
