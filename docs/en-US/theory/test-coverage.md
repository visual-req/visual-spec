## Test Coverage

This page explains common coverage metrics, what they do and do not guarantee, and why “100% coverage” can still miss important logic.

### 1) Statement coverage

Definition: the percentage of executable statements that were executed.

Notes:
- Good at finding code that never runs, but it does not guarantee each decision outcome was validated.
- With branching logic, 100% statement coverage can still miss important branch outcomes.

### 2) Branch coverage

Definition: for each decision point (`if`, `switch`, etc.), each outcome (True/False or each `case`) is executed at least once.

Notes:
- Stronger than statement coverage for finding unexecuted branches.
- With compound conditions (`A && B`, `A || B`), branch coverage does not prove that each atomic condition meaningfully affects outcomes.

### 3) Condition coverage

Definition: each atomic condition inside a compound expression (e.g. `A`, `B`) takes both True and False at least once.

Notes:
- Focuses on flipping each atomic condition, but it does not guarantee all decision outcomes are covered.
- Commonly reviewed together with branch coverage.

### 4) Condition/branch coverage

Definition: both of the following hold:
- Branch coverage (each decision’s outcomes are covered)
- Condition coverage (each atomic condition flips to True and False)

Notes:
- A practical baseline for business validations implemented as compound conditions.
- Still not the same as path coverage (not all combinations / paths are guaranteed).

### 5) Path coverage

Definition: coverage of feasible execution paths from entry to exit (considering combinations of branches).

Notes:
- Theoretical strongest, but the number of paths can grow exponentially with branches/loops.
- In practice, teams usually cover critical paths + high-risk branches + boundary cases rather than enumerating all paths.

---

## Example: different “coverage” on the same code

Example code:

```ts
export function canSubmit(isDraft: boolean, hasPermission: boolean, quotaOk: boolean) {
  if (isDraft && hasPermission) {
    if (quotaOk) return true;
    return false;
  }
  return false;
}
```

Decisions:
- Decision 1: `isDraft && hasPermission`
- Decision 2: `quotaOk`

### A) A minimal set that achieves 100% branch coverage (illustrative)

| Case | isDraft | hasPermission | quotaOk | Expected | What it covers |
| --- | --- | --- | --- | --- | --- |
| T1 | true | true | true | true | Decision1=True, Decision2=True |
| T2 | true | true | false | false | Decision2=False |
| T3 | false | true | (n/a) | false | Decision1=False (short-circuit) |

This set typically achieves:
- High statement coverage
- Branch coverage for both decisions (True/False covered)

But it can still miss:
- `isDraft=true, hasPermission=false` (still Decision1=False, but different business meaning)

### B) Making condition coverage meaningful: flip the atomic conditions

Add one more case:

| Case | isDraft | hasPermission | quotaOk | Expected | What it covers |
| --- | --- | --- | --- | --- | --- |
| T4 | true | false | (n/a) | false | Flips hasPermission=False (short-circuit) |

This moves closer to condition/branch coverage: decision outcomes are covered, and atomic conditions are explicitly flipped.

### C) Why full path coverage is rarely achievable

As more decisions are added (states, permissions, external dependency switches), feasible paths explode. A better practical strategy is:
- Use scenarios as the backbone (critical paths)
- Split risky branches (auth/validation/errors/concurrency/idempotency) into independent cases
- Use matrices (decision/judgment) to make combinations explicit, then pick a minimal covering set
