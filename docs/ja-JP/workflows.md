## ワークフロー

### 1. 要件分析（`/vspec:new`）

- 生の要件を入力
- 前提・範囲・ルール・依存関係などの確認質問に回答
- `/specs/` にベースライン成果物（roles/terms/flows/scenarios/functions/dependencies/questions）を生成

### 2. 詳細 spec（`/vspec:detail`）

- `/specs/functions/*` を入力に、機能ごとの仕様を `/specs/details/<function_slug>/` に生成
- 目標：要件を実装可能な設計入力へ変換

### 3. 検証（`/vspec:verify`）

- 前提：`/specs/details/` が存在し空でない
- `/specs/models/*.md` と、`/scheme.yaml` の選択に従った実行可能プロトタイプを `/specs/prototypes/` に生成

### 4. 受入ケース（`/vspec:accept`）

- `/specs/acceptance/` に受入テストケースを生成

### 5. 自動テスト（`/vspec:append-test`）

- 受入ケースと既存テストスタックを読み、E2E/API/単体テストの最小セットを生成
- 注意：テスト実行は行わず、コード生成/追記のみ

### 6. 統合実装（`/vspec:impl`）

- specs/details/models/dependencies を読み、リポジトリの規約に沿った統合コードを生成

### 7. 見積・排期（`/vspec:plan`）

- 機能一覧とシナリオをもとに見積・排期（HTML）を生成

## インストール（skills.sh）

```bash
npx skills add visual-req/visual-spec --skill visual-spec-skill
```
