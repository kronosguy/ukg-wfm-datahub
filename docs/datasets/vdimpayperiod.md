# vDimPayPeriod

**Group:** Summary Dataset → Dimension Views

Contains the 15 previous and 5 future pay periods for the current assigned person pay rule

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vDimPayPeriod |
| Unique Identifier | partitionDate,personId |
| Source Pipeline | getPayPeriod (DR) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Reference date |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| PP_startDate | DATE | Pay period start date |  |  |
| PP_endDate | DATE | Pay period end date |  |  |
| PP_payPeriod | STRING | Symbolic Time Period |  |  |
| PP_payPeriodOffset | INT64 | Number of pay periods in the future or past |  |  |
