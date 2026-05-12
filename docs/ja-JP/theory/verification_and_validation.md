## Verification & Validation：検証と妥当性確認の閉ループ

[English](../../en-US/theory/verification_and_validation.md) | [中文](../../zh-CN/theory/verification_and_validation.md) | [日本語](../../ja-JP/theory/verification_and_validation.md)

visual-spec では、Verification（仕様として正しいか）と Validation（作るべきものか）は別の問題です。必要な証拠とレビュー方法が異なります。

### 2 つの違い

- Verification：仕様が整合し、漏れがなく、実装可能で、テスト可能で、追跡可能か
- Validation：ユーザー価値と目的に合い、シナリオが end-to-end で成立するか

### visual-spec における V&V の流れ

1. 範囲と共通言語の確立（`/vspec:new`）
   - 役割、用語、シナリオ、フロー、機能一覧、依存、要確認事項
2. 実装可能粒度への仕様化（`/vspec:detail`）
   - 追跡可能な詳細仕様を作る
3. Validation（`/vspec:verify` + 関係者レビュー）
   - 実行可能プロトタイプとシナリオ入口で、期待どおりに動くかを確認する
   - 「レビューと確定」で対象シナリオ範囲を明確化し、今回のレビュー/受入で何を確認するかを確定する
4. Verification（`/vspec:qc`）
   - ルールベースで漏れ/矛盾/テスト不能/追跡不足を洗い出す
5. 閉ループ（`/vspec:refine`）
   - レビュー結論と QC の修正点を refine 入力に落とし、下流成果物を同期更新し、再検証する

### なぜ V と V を分けるのか

- 証拠が違う：Validation は動作の証拠、Verification は整合性とテスト可能性の証拠が必要
- レビュアーが違う：業務側はシナリオ/プロトタイプでズレを見つけやすく、開発/QA は仕様と可測性で欠落を見つけやすい
- 結論が実行可能になる：対象範囲を切り、refine で反映することで、フィードバックが追跡可能な作業に変わる
