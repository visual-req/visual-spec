## 测试覆盖率（Test Coverage）

本页用于解释常见覆盖率指标的含义、差异与局限，并用同一个代码样例说明：达到某类覆盖率并不等价于“逻辑都测到了”。

### 1) 指令覆盖（Statement Coverage）

定义：被执行到的“可执行语句/指令”占比。

要点：
- 能发现“代码根本没跑到”的死路径，但无法保证每个分支都被验证。
- 对包含 `if/else` 的逻辑，指令覆盖 100% 仍可能漏掉某些分支组合。

### 2) 分支覆盖（Branch Coverage）

定义：每个判定点（例如 `if`、`switch`）的每个分支（True/False 或 case）是否至少执行过一次。

要点：
- 比指令覆盖更能发现“某分支从未执行”的问题。
- 对复合条件（`A && B`、`A || B`），分支覆盖仍可能无法证明每个子条件的取值影响被验证。

### 3) 条件覆盖（Condition Coverage）

定义：复合条件表达式中的每个原子条件（例如 `A`、`B`）是否分别取到过 True 与 False。

要点：
- 关注每个子条件是否被“翻转”过，但不保证整条判定分支的 True/False 都覆盖。
- 常见做法是配合分支覆盖一起看。

### 4) 条件分支覆盖（Condition/Branch Coverage）

定义：同时满足：
- 分支覆盖（每个判定点 True/False 都跑过）
- 条件覆盖（每个原子条件 True/False 都跑过）

要点：
- 在复合条件常见的业务校验里，条件分支覆盖是更实用的基线。
- 仍不等于路径覆盖（所有组合路径都被验证）。

### 5) 路径覆盖（Path Coverage）

定义：从入口到出口的“可行执行路径”覆盖情况（考虑分支组合）。

要点：
- 理论上最强，但在存在多个分支/循环时路径数量可能指数增长，往往不可完全穷举。
- 实务上通常以“关键路径 + 高风险分支 + 边界条件”替代全路径穷举。

---

## 示例：同一段代码下，不同覆盖率意味着什么

示例代码：

```ts
export function canSubmit(isDraft: boolean, hasPermission: boolean, quotaOk: boolean) {
  if (isDraft && hasPermission) {
    if (quotaOk) return true;
    return false;
  }
  return false;
}
```

其中：
- 判定点 1：`isDraft && hasPermission`
- 判定点 2：`quotaOk`

### A) 达到 100% 分支覆盖的最小用例集（示意）

| 用例 | isDraft | hasPermission | quotaOk | 期望 | 覆盖说明 |
| --- | --- | --- | --- | --- | --- |
| T1 | true | true | true | true | 命中判定点1=True，判定点2=True |
| T2 | true | true | false | false | 命中判定点2=False |
| T3 | false | true | (无关) | false | 命中判定点1=False（短路） |

这组用例通常能达到：
- 指令覆盖：高（几乎全跑到）
- 分支覆盖：判定点 1/2 的 True/False 都覆盖

但它仍可能遗漏：
- `isDraft=true, hasPermission=false` 的情况（同为判定点1=False，但业务语义可能不同）

### B) 让条件覆盖更有意义：补齐子条件翻转

为了让原子条件都取到 True/False，增加一条：

| 用例 | isDraft | hasPermission | quotaOk | 期望 | 覆盖说明 |
| --- | --- | --- | --- | --- | --- |
| T4 | true | false | (无关) | false | 翻转 hasPermission=False（短路） |

这会更接近条件分支覆盖：既有分支 True/False，又让子条件取值变化被验证。

### C) 为什么“路径覆盖”很难完全做满

如果再加入更多判定点（例如状态机、权限维度、外部依赖开关），可行路径会迅速膨胀。实务上更推荐：
- 以场景为主线（关键路径）
- 把高风险分支（权限/校验/异常/并发/幂等）拆成独立用例
- 用判定矩阵/决策矩阵把条件组合显式化，再选择最小覆盖集
