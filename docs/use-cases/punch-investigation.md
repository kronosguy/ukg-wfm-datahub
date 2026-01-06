# Punch Investigation (Timekeeping)

## Business question
What happened with a punch/shift, and what changes were made?

## Recommended grains
- Investigation: **punch-event** and **edit/audit-event**
- Summary (optional): **person-day**

## Data strategy
- Start with the narrowest scope: person + date window
- Use audit/change history to explain “why it looks different now”

## Cost-safe filters
- Always filter by:
  - person
  - narrow date range
- Never run wide scans for investigations

## Validation checklist
- Confirm timestamps and time zone assumptions
- Confirm sequence of edits matches expected history

## Common gotchas
- multiple punches in short windows (duplicates, device retries)
- edits that re-interpret spans/segments
- backfills rewriting historical facts
