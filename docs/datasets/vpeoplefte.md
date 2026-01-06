# vPeopleFTE

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Full Time Equivelency

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleFTE |
| Unique Identifier | personId,fullTimeEquivalencyId |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| fullTimeStandardHoursQuantity | FLOAT64 | Full time standard hours quantity |  |  |
| fullTimeEquivalencyPercent | FLOAT64 | Full time equivalency percent |  |  |
| fullTimeEquivalencyId | INT64 | Full time equivalency ID |  |  |
| expirationDate | DATE | Expiration date |  |  |
| employeeStandardHoursQuantity | FLOAT64 | Employee standard hours quantity |  |  |
| effectiveDate | DATE | Effective date |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
