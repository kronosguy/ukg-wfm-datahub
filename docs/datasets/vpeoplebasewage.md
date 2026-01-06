# vPeopleBaseWage

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Base Wage Rates

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleBaseWage |
| Unique Identifier | personId,baseWageId,effectiveDate,expirationDate |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| hourlyRate | FLOAT64 | Wage amount | Confidential | BLANK |
| expirationDate | DATE | Date expires |  |  |
| effectiveDate | DATE | Date effective |  |  |
| baseWageId | INT64 | Base wage ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
