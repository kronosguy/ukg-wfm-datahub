# KPI Contract (Template)

A KPI contract is the single source of truth for what a metric means.

## KPI Name
**<KPI_NAME>**

## Business definition
What this KPI measures in plain English.

## Intended audience
Who uses it and why.

## Grain
What one row represents (examples: org-day, person-day, pay-period-person).

## Source domain(s)
Which domain(s) this KPI comes from (Totals, Timecard, Schedule, etc.)

## Included / excluded logic
- Included pay codes / categories:
- Excluded pay codes / categories:
- Premium handling:
- Rounding rules (if any):

## Org logic
- Worked org vs home org:
- Org rollup rules:

## Date logic
- Calendar vs pay period vs fiscal:
- Time zone considerations (if applicable):

## Filters (cost-safe defaults)
- Default lookback window:
- Required partition/date filters:

## Validation method
How to validate with a sample set (what to compare against, how many people, what range).

## Known limitations
Where this KPI does not apply or may differ from UI behavior.

## Owner
Person/team who owns the definition.

## Change log
- YYYY-MM-DD: what changed and why
