# Schedule vs Worked Variance

## Business question
How far off are we from plan (scheduled) vs reality (worked), and where?

## Recommended grains
- Dashboard: **org-day**
- Drill-through: **person-day** and/or **shift-segment**

## Required decisions (non-negotiable)
- Worked org vs home org for attribution
- Calendar vs pay period for trend grouping
- Whether to include:
  - on-call
  - call-back
  - premium hours
  - unscheduled worked time

## Data strategy
- Use **schedule summary** for planned hours
- Use **worked summary/totals** for actual hours
- Only use detail tables for explanations (late punches, edits, call-ins)

## Cost-safe filters
- Bound the window (example: rolling 90–180 days for operations; 400 days for year lookback)
- Partition/date filters are required

## Validation checklist
- Sample a week and a pay period
- Pick a small set of employees
- Reconcile scheduled hours and worked hours to a known reference sample
- Confirm joins do not inflate totals (cardinality checks)

## Common gotchas
- schedule can change after the fact (edits/coverage adjustments)
- worked time can change due to late edits/backfills
- attribution shifts if you mix home org slices with worked-hour facts
