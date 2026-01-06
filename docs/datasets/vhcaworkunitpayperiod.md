# vHcaWorkUnitPayPeriod

**Group:** Detail Dataset → Healthcare Productivity

One row for each pay period associated with a work unit from the pay rule assigned to the work unit.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaWorkUnitPayPeriod |
| Unique Identifier | partitionDate,workunitId |
| Source Pipeline | hcaWorkUnitPayPeriod (DR) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of daily productivity metric - use to join to date dimension |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
| PP_startDate | DATE | Pay Period start date |  |  |
| PP_endDate | DATE | Pay Period end date |  |  |
| PP_payPeriod | STRING | Pay Period name |  |  |
| PP_payPeriodOffset | INT64 | Number of pay period back or forward from current pay period |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
