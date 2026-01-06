# Validation Checklist (Before You Publish)

## Always do these
- confirm grain (what one row represents)
- confirm unique keys for each joined table
- compare row counts before/after joins
- check for null join keys
- reconcile to a known sample (small group of employees/time windows)

## When comparing to the UKG UI
Mismatch causes to consider:
- worked vs home org
- calendar vs pay period vs fiscal period
- late edits/backfills
- mapping changes (reclassification)
