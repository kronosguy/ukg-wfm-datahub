# vEssTimeOffApprovalPeriod

**Group:** Detail Dataset → Employee Self Service Detail Views

- Time Off Request Approval Period

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssTimeOffApprovalPeriod |
| Unique Identifier | essTimeOffId,partitionDate,personId,approvalPeriodId |
| Source Pipeline | essTimeOff (DR) |

## Columns

**Column count:** 12

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essTimeOffId | INT64 | time off request id |  |  |
| partitionDate | DATE | The start date of the request |  |  |
| personId | INT64 | The employee ID of the initiator of  time off request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| approvalPeriodId | INT64 | Approval period the ID for the time-off period |  |  |
| startDate | DATE | Approval period start date of the time-off period; in ISO_LOCAL_DATE format (YYYY-MM-DD). |  |  |
| endDate | DATE | Approval period the end date of the time-off period; in ISO_LOCAL_DATE format (YYYY-MM-DD). |  |  |
| startTime | TIME | Approval period start time of the time-off period; in ISO_LOCAL_TIME format (HH:mm:ss.SSS). |  |  |
| duration | FLOAT64 | Approval period the duration requested as time off; in hours. |  |  |
| payCodeId | INT64 | Approval period the pay code ID for the time-off period. |  |  |
| payCodeName | STRING | Approval period the pay code name for the time-off period. |  |  |
| symbolicAmountName | STRING | Approval period symbolic qualifier for the time-off period: full day, half day, first half day, second half day, or hours. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
