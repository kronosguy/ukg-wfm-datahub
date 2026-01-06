# Partition and Date Filters (Cost-Safe Queries)

## Why this exists
BigQuery bills by data scanned. Unbounded queries are expensive and slow.

## Rules
- Always filter by date/partition as early as possible
- Only select needed columns (avoid `SELECT *`)
- Aggregate early when building KPIs

## Practical defaults
- Dashboards: last 90–400 days (depending on need)
- Investigations: narrow windows (days, not years)

## Validation habit
If a query surprises you with cost/latency, it usually lacks a bounded time filter.
