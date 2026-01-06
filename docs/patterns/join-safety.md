# Join Safety (Cardinality Control)

## The problem
Most reporting bugs are join bugs:
- many-to-many joins inflate hours
- non-unique dimensions duplicate facts
- “current attributes” overwrite historical reality

## Minimum checks before trusting a join
- Does the dimension have **1 row per key**?
- Did row count change unexpectedly after joining?
- Did totals change without business logic changing?

## Best practice
- Join summary facts to conformed dimensions
- Only join detail tables when you can prove the grain matches
