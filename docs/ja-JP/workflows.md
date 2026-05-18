## ワークフロー

[English](../en-US/workflows.md) | [中文](../zh-CN/workflows.md) | [日本語](../ja-JP/workflows.md)

### 全体フロー図

![visual-spec ワークフロー概要](../assets/ja-JP/visual-spec-workflow.svg)

### 1. 要件分析（[/vspec:new](../../README.md#commands)）

- 生の要件を入力
- 前提・範囲・ルール・依存関係などの確認質問に回答
- `/specs/` にベースライン成果物（roles/terms/flows/scenarios/functions/dependencies/questions）を生成
- 質問への回答（HTML、推奨）：
  - [/vspec:new](../../README.md#commands) は対話式 Q&A ページを生成：`/specs/background/question_and_answer.html`
  - HTML を開き、以下を選択：
    - `/specs/background/original.md`
    - `/specs/background/questions.md`
  - フォームで回答し保存して md に反映（ブラウザが File System Access API に対応していれば直接上書き、未対応ならダウンロードして手動で置換）

### 2. 追加質問（[/vspec:more-q](../../README.md#commands)）

- 質問が不足している、または要件が変わって追加確認が必要な場合に使う
- 入力：`/specs/background/questions.md`（無い場合は先に [/vspec:new](../../README.md#commands)）
- 出力：`/specs/background/questions.md` に追記（追加質問 + 回答手順）
- 質問への回答（HTML、推奨）：
  - [/vspec:more-q](../../README.md#commands) は同じ Q&A ページを更新/生成：`/specs/background/question_and_answer.html`
  - HTML を開き、追加された質問に回答して保存し、最後に [/vspec:refine-q](../../README.md#commands) を実行

### 3. 回答の取り込み（[/vspec:refine-q](../../README.md#commands)）

- `questions.md` に記入した回答を要件口径へ取り込む
- 入力：回答済みの `/specs/background/questions.md` + `original.md`
- 出力：`/specs/background/original.md` へ追記（採用項目 + 変更点 + 最新口径）

### 4. 追補の適用（[/vspec:refine](../../README.md#commands)）

- 実装中の追加情報/明確化を反映し、口径と下流成果物を同期する
- 入力：
  - 既定：`/docs/refine/*`（`file_list.md` があれば優先）
  - 任意：コマンド引数で指定したファイル/ディレクトリ
- 前提：`/specs/details/` が存在し空でない
- 出力：`original.md` へ追記 + 影響する `/specs/details/` と `/specs/prototypes/` を更新（`/specs/backend/` が存在する場合は backend も同期更新）

### 5. 詳細 spec（[/vspec:detail](../../README.md#commands)）

- `/specs/functions/*` を入力に、機能ごとの仕様を `/specs/details/<function_slug>/` に生成
- 目標：要件を実装可能な設計入力へ変換
- 追加出力：`/specs/details/reader.html`（左にディレクトリツリー、右に Markdown レンダリング。PlantUML は図としてレンダリング）

### 6. Word 要約ドキュメント（[/vspec:doc](../../README.md#commands)）

- 既存成果物を集約してレビュー/回覧/保管用の Word 文書を生成する
- 入力：既存の `/specs/**`（original/functions/details/models/flows など。存在するものを読む）
- 出力：`/docs/current/requirement_detail.docx`（Word で開ける `.docx`、単一 HTML）
- 注意：この Word は要約用（直接編集しない）。修正は対応する markdown を更新し、[/vspec:doc](../../README.md#commands) を再実行して再生成する

### 7. 検証（[/vspec:verify](../../README.md#commands)）

- 前提：`/specs/details/` が存在し空でない
- `/specs/models/*.md` と、`/scheme.yaml` の選択に従った実行可能プロトタイプを `/specs/prototypes/` に生成

### 8. 受入ケース（[/vspec:accept](../../README.md#commands)）

- JSON の受入ケースを生成：`/test/验收用例/acceptance_cases.json`
- `/test/testcase_reader.html` で生成した JSON を閲覧

### 8.1 単体/結合テストケース（[/vspec:i-test](../../README.md#commands)）

- JSON のテストケースを生成：
  - `/test/单元测试/unit_test_cases.json`
  - `/test/集成测试/integration_test_cases.json`
- 重点：CRUD を Query/Create/Edit/Detail/Delete に分割し、検証/権限/分岐は独立ケースとして生成

### 8.2 Playwright スクリプト（[/vspec:script](../../README.md#commands)）

- Playwright スクリプトを生成：`/test/playwright/`

### 9. 自動テスト（[/vspec:append-test](../../README.md#commands)）

- 受入ケースと既存テストスタックを読み、E2E/API/単体テストの最小セットを生成
- 注意：テスト実行は行わず、コード生成/追記のみ

### 10. 統合実装（[/vspec:impl](../../README.md#commands)）

- specs/details/models/dependencies を読み、リポジトリの規約に沿った統合コードを生成

### 11. 品質チェック（[/vspec:qc](../../README.md#commands)）

- `/specs/` 配下の成果物を品質チェックし、`/specs/qc_report.md` を生成

### 12. 見積・排期（[/vspec:plan](../../README.md#commands)）

- 機能一覧とシナリオをもとに見積・排期（HTML）を生成

### 13. アップグレード/改修（[/vspec:upgrade](../../README.md#commands)）

- `/docs/` 配下の資料（legacy/current）に基づき、[/vspec:new](../../README.md#commands) と同様の構造で `/specs/` を再生成/更新
- 入口：`/docs/current/file_list.md`（無ければテンプレを生成）

### 14. MRD（[/vspec:mrd](../../README.md#commands)）

- 市場/競合/ユーザー/プロダクト設計の分析パックを生成し、`/docs/market/` に書き出す

## インストール（skills.sh）

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```
