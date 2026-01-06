# Accrual Health Monitor

## Business question
Are accrual balances and transactions behaving correctly, and where are we at risk?

## Recommended grains
- Dashboard: **person-day** or **person-period**
- Drill-through: **transaction-event**

## Required decisions
- As-of date rule (calendar vs pay period close)
- Which accrual codes are in scope
- How to treat adjustments and payouts

## Data strategy
- Use balances for monitoring
- Use transactions for explanations (why a balance changed)

## Cost-safe filters
- Bound by recent periods (example: last 3–6 months) unless auditing
- Partition filters required

## Validation checklist
- Sample employees with known adjustments
- Compare to UI balances for an as-of date
- Verify transaction totals reconcile to balance changes

## Common gotchas
- payout logic and partial payouts can change balances
- negative balance protections or policy rules alter outcomes
- late adjustments can backfill older periods
