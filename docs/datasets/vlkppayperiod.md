# vLkpPayPeriod

**Group:** Detail Dataset → Pay Code/Period Detail Views

INTERNAL USE ONLY use dimPayPeriod in Summary Dataset
Contains payperiod data generated from transactional data with 5 pay periods in the future and 15 pay periods in the past.
This data is available in both lkpPayPeriod in the detail dataset and  dimPayPeriod in the summary dataset.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLkpPayPeriod |
| Unique Identifier | partitionDate,personId |
| Source Pipeline | getPayPeriod (DR) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Reference Date |  |  |
| personId | INT64 | Person ID linked to the pay period |  |  |
| PP_startDate | DATE | Pay period start date |  |  |
| PP_endDate | DATE | Pay period end date |  |  |
| PP_payPeriod | STRING | Pay period name - describes relative to current pay period |  |  |
| PP_payPeriodOffset | INT64 | Indicates number of pay periods in the past or future. |  |  |
