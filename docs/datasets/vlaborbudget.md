# vLaborBudget

**Group:** Detail Dataset → Budget Detail Views

Customer's budgeted amounts for labor costs and hours. Separate rows for budgeted hours and budgeted costs.

- labor budget -  (COST and HOURS) daily by Job(org)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborBudget |
| Unique Identifier | partitionDate,orgId,laborTypeId |
| Source Pipeline | laborBudget (DR) |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| currencyId | INT64 | currency id |  |  |
| currency | STRING | If amount is cost type then currency code. (e.g. USD) |  |  |
| dailyAmount | FLOAT | Budgeted labor amount, can be budgeted hours or budgeted wages. |  |  |
| laborTypeId | INT64 | labor type id |  |  |
| laborTypeName | STRING | HOURS or COST |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
