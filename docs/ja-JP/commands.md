## コマンド一覧

| コマンド | 目的 | 主な入力 | 主な出力 |
| --- | --- | --- | --- |
| `/vspec:new` | 生要件からベースライン spec を生成 | 要件テキスト + 対話 Q&A | `/specs/`（background/roles/terms/flows/scenarios/scenario_details/dependencies/functions/questions）+ `/docs/*` の初期化 |
| `/vspec:refine` | 追補資料を反映し、詳細と原型を同期更新 | `/docs/refine/*`（または引数）+ `/specs/background/original.md` + `/specs/details/` | `original.md` に追記（変更点 + 新口径）+ 影響範囲の `/specs/details/` と `/specs/prototypes/` 更新 |
| `/vspec:refine-q` | questions の回答を要件へ取り込み | `/specs/background/original.md` + `/specs/background/questions.md` | `original.md` に追記（採用項目 + 変更点 + 新口径） |
| `/vspec:detail` | 機能ごとの実装可能レベルの詳細 spec を生成 | `/specs/functions/*` + 関連成果物 | `/specs/details/<function_slug>/*` |
| `/vspec:verify` | モデルと実行可能プロトタイプを生成 | 既存 `/specs/`（functions + details + roles） | `/specs/models/*.md`、`/specs/prototypes/`（原型 + `scenario.html`） |
| `/vspec:accept` | 受入テストケースを生成 | functions/scenarios/details/roles/models | `/specs/acceptance/<function_slug>/acceptance_cases.md`、`/specs/acceptance/index.md` |
| `/vspec:append-test` | 自動テストコードを生成 | acceptance + リポジトリのテストスタック | 既存テストディレクトリ（なければ `/tests/`）に書き込み |
| `/vspec:impl` | バックエンド + フロントエンドの統合実装を生成 | specs/details/models/dependencies | 統合実装コード（API 契約、backend、frontend 連携） |
| `/vspec:upgrade` | 既存資料から specs を再生成/更新 | `/docs/current/file_list.md` + `/docs/legacy/*` + 既存 `original.md`（任意） | `/specs/` 更新 + `/scheme.yaml` に選定内容同期 |
| `/vspec:qc` | `/specs/` の品質チェック | 組み込み標準 + 任意 `domain_quality_standard.md` + 任意 `quality_standard.md` | `/specs/qc_report.md` |
| `/vspec:plan` | 見積とスケジュール | functions/roles/flows/dependencies/details | `/specs/plan/plan_estimate.md`、`/specs/plan/plan_schedule.html` |

## `/vspec:new`

- 使いどころ：情報が揃っていない段階で、レビュー可能な共通言語を素早く作る
- 主な出力：ステークホルダー、ロール、用語、フロー、シナリオ、機能一覧、未解決質問
- ディレクトリ初期化：`/docs/` とその配下（legacy/current/refine/templates/texts/assets）を作成

## `/vspec:detail`

- 使いどころ：設計・実装前に、各機能を実装可能な粒度まで落とし込む
- 主な出力：RBAC（コントロール単位）、データ権限、ロード/操作/バリデーション、状態遷移、ログ/通知、MQ、入出力、定期実行

## `/vspec:verify`

- 使いどころ：詳細が揃った後、モデルと画面形状を早期に検証し認識齟齬を減らす
- 前提：`/specs/details/` が存在し空でないこと

## `/vspec:append-test`

- 使いどころ：受入ケースを、実行可能な自動テストへ落とす
- 注意：このコマンドはテストコードの生成/追記のみ（テスト実行はしない）
