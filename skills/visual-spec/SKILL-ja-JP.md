---
name: "visual-spec"
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
- `/scheme.yaml` の `selected.language` を読む（`en`、`zh`、`ja`。欠落/不正なら `en`。`zh-CN` は `zh` の別名として扱う）
- コマンド引数または入力で `lang=<...>` が明示された場合：
  - 単一言語：`lang=en|zh|ja`
  - 複数言語：`lang=zh,en`（先頭が文書既定言語。`selected.languages` に切替集合を保存）

Flow:
0. `/docs/` の存在を保証し、サブフォルダを作成：
   - `/docs/legacy/`
   - `/docs/current/`
   - `/docs/refine/`
   - `/docs/dependencies/`
   - `/docs/change/` は作成しない（廃止）
0.2 引数で `lang=...` が渡された場合、`/scheme.yaml` の `selected.language` と `selected.languages` を更新（該当フィールドのみ。その他のフィールド/フォーマットは保持）
0.5 早期に調整できるように制約ファイルを作成（既存なら上書きしない）：
   - `/scheme.yaml`（原型スタック選定 + catalog）
   - `/prototype_ui_convention.md`（`/scheme.yaml` と同階層）
1. ユーザーに原始要件の入力を依頼
2. 入力を raw requirement として扱う
3. `prompts/vspec_new/background.md` を読み込み、要件分析と背景補完を実行
4. `/specs/background/original.md` に書き込み
5. Open Questions/要確認事項の回答を促す（自己回答でも、AI の回答案→ユーザー確認でも可）
6. 以降、`prompts/vspec_new/*` に従い `/specs/` 配下の成果物を生成

### `/vspec:refine`

`/docs/refine/` の追補資料（またはコマンド引数で指定されたファイル/ディレクトリ）に基づき、要件を追補して更新します。

Flow:
0. `/specs/details/` が存在し非空であることを確認（欠ける場合は停止し `/vspec:detail` を促す）
1. refine 入力を読む（引数があれば優先、無ければ `/docs/refine/refine.md`）
2. `prompts/vspec_refine/refine.md` を読み込み、口径と影響成果物を更新
3. `/specs/background/original.md` に追記し、影響する `/specs/details/` と `/specs/prototypes/` を同期更新

### `/vspec:refine-q`

回答済みの質問に基づき要件を更新します。

Flow:
1. `/specs/background/questions.md` が無い場合は停止
2. 回答済み項目を抽出
3. `prompts/vspec_refine/refine_q.md` を読み込み、回答を口径へマージ
4. `/specs/background/original.md` に追記
5. `/specs/background/questions.md` を更新し、回答済みとして扱った項目を `<mark>...</mark>` で強調

### `/vspec:more-q`

追加の確認質問を生成し、`/specs/background/questions.md` に追記します（重複排除・番号継続）。

Flow:
1. `/specs/background/questions.md` が無い場合は停止（先に `/vspec:new` を促す）
2. `prompts/vspec_more_q/more_q.md` を読み込み、追加質問を生成
3. 新規項目のみを `questions.md` 末尾へ追記（既存は書き換えない）
4. ユーザーが回答し、その後 `/vspec:refine-q` を実行するための指示を出す

### `/vspec:detail`

機能一覧に基づき要件詳細を展開します（`/specs/details/` に生成）。各ステップの種別（端=Web/Mobile/Web+Mobile/Backend/Job）を判定し、対応するロジック詳細を必ず生成します（ロジックを省略しない）。あわせて、Markdown/PlantUML をレンダリングできる閲覧用 `index.html` を `/specs/details/index.html` に生成します。

### `/vspec:doc`

要件成果物（`/specs/**`）を集約し、Word で直接開ける単一ファイルの Word 文書（HTML 形式の `.doc`）を `/docs/current/requirement_detail.doc` に生成します。

### `/vspec:verify`

モデル（`/specs/models/`）と実行可能プロトタイプ（`/specs/prototypes/`）を生成して検証します。

### `/vspec:qc`

`/specs/` 配下の成果物を品質チェックし、`/specs/qc_report.md` を生成します。

### `/vspec:accept`

受入テストケースを `/specs/acceptance/` に生成します。

### `/vspec:append-test`

受入ケースと既存テストスタックをもとに、自動テストコードを生成します（テスト実行はしない）。

### `/vspec:impl`

仕様に基づき、統合実装コード（API 契約、backend、frontend 連携）を `/specs/` 配下に生成します。

### `/vspec:upgrade`

`/docs/` 配下の資料（legacy/current）に基づき、`/vspec:new` と同様の構造で `/specs/` を再生成/更新します。あわせて、`/docs/legacy/` 配下（サブディレクトリ含む）を再帰的にスキャンし、原資料として取り込みます。

### `/vspec:plan`

ストーリーマップで分解し、見積（SP）と排期（HTML）を生成します。

### `/vspec:mrd`

MRD（市場/競合/ユーザー/プロダクト設計）分析パックを生成し、`/docs/market/` に書き出します。

## Prompt Files

- `prompts/vspec_new/background.md`
- `prompts/vspec_new/stakeholders.md`
- `prompts/vspec_new/roles.md`
- `prompts/vspec_new/terms.md`
- `prompts/vspec_new/flows.md`
- `prompts/vspec_new/scenarios.md`
- `prompts/vspec_new/details_pre_post.md`
- `prompts/vspec_new/details_constraints.md`
- `prompts/vspec_new/details_variations.md`
- `prompts/vspec_new/details_boundaries.md`
- `prompts/vspec_new/details_symmetry.md`
- `prompts/vspec_new/dependencies.md`
- `prompts/vspec_new/functions.md`
- `prompts/vspec_new/questions.md`
- `prompts/vspec_more_q/more_q.md`
- `prompts/vspec_mrd/mrd.md`
- `prompts/vspec_refine/refine.md`
- `prompts/vspec_refine/refine_q.md`
- `prompts/vspec_doc/doc.md`
- `prompts/vspec_verify/model.md`
- `prompts/vspec_verify/prototype.md`
- `prompts/vspec_verify/validation.md`
- `prompts/vspec_detail/rbac.md`
- `prompts/vspec_detail/data_permission.md`
- `prompts/vspec_detail/page_load.md`
- `prompts/vspec_detail/interaction.md`
- `prompts/vspec_detail/index.md`
- `prompts/vspec_detail/index.html`
- `prompts/vspec_detail/timeline.md`
- `prompts/vspec_detail/formula.md`
- `prompts/vspec_detail/expression_tree.md`
- `prompts/vspec_detail/code_rules.md`
- `prompts/vspec_detail/judgemental_matrix.md`
- `prompts/vspec_detail/validation_matrix.md`
- `prompts/vspec_detail/post_submit_check.md`
- `prompts/vspec_detail/post_submit_processing.md`
- `prompts/vspec_detail/post_submit_navigation.md`
- `prompts/vspec_detail/mq.md`
- `prompts/vspec_detail/service_logic.md`
- `prompts/vspec_detail/job_logic.md`
- `prompts/vspec_detail/logging_matrix.md`
- `prompts/vspec_detail/notification_matrix.md`
- `prompts/vspec_detail/nfp.md`
- `prompts/vspec_detail/file_import.md`
- `prompts/vspec_detail/file_export.md`
- `prompts/vspec_detail/cron_job.md`
- `prompts/vspec_accept/accept.md`
- `prompts/vspec_test/test.md`
- `prompts/vspec_impl/implement.md`
- `prompts/vspec_upgrade/upgrade.md`
- `prompts/vspec_plan/estimate.md`
- `prompts/vspec_plan/schedule.md`
- `prompts/vspec_qc/qc.md`
- `prompts/vspec_qc/quality_standard.md`
