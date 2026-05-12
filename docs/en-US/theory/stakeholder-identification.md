## Stakeholder identification thinking

[English](../../en-US/theory/stakeholder-identification.md) | [中文](../../zh-CN/theory/stakeholder-identification.md) | [日本語](../../ja-JP/theory/stakeholder-identification.md)

The goal is not to list role names, but to identify who drives decisions, who uses the system, who owns constraints (data/compliance/finance/risk), who operates/monitors, and who is impacted by changes.

### 1) Identify stakeholders by value chain

- Requesters: who initiates the goal/problem
- Users: operators, approvers, managers
- Support functions: customer support, operations, data, finance, risk, legal, IT ops
- Impacted parties: upstream/downstream collaborators, external partners, end beneficiaries

### 2) Identify stakeholders by permissions and data

- Who can view/change/export/approve/close what
- Who needs auditability and accountability

### 3) Identify stakeholders by failure/compensation paths

- Who handles failed cases, reversals/refunds, reconciliation issues
- Who responds to alerts and owns SLAs

### 4) Identify stakeholders by lifecycle milestones

- Review stakeholders: decision makers for scope and prototype acceptance
- Release stakeholders: training, operations cutover, migration, rollout strategy

### Where it lands in `/vspec:new`

- Capture stakeholders/roles in baseline artifacts
- Turn “who decides what” into explicit open questions and a decision list
