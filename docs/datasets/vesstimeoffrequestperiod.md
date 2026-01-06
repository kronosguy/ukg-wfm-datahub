# vEssTimeOffRequestPeriod

**Group:** Detail Dataset → Employee Self Service Detail Views

- Time Off Request Period

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEssTimeOffRequestPeriod |
| Unique Identifier | essTimeOffId,periodId,partitionDate,personId |
| Source Pipeline | essTimeOff (DR) |

## Columns

**Column count:** 12

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| essTimeOffId | INT64 | time off request id |  |  |
| partitionDate | DATE | The start date of the request |  |  |
| personId | INT64 | The employee ID of the initiator of  time off request, which is an ID that uniquely identifies an employee.This is not a person number. |  |  |
| periodId | INT64 | The ID for the time-off period. |  |  |
| startDate | DATE | The start date of the time-off period; in ISO_LOCAL_DATE format (YYYY-MM-DD). |  |  |
| endDate | DATE | The end date of the time-off period; in ISO_LOCAL_DATE format (YYYY-MM-DD). |  |  |
| startTime | TIME | Start time of the time-off period; in ISO_LOCAL_TIME format (HH:mm:ss.SSS). |  |  |
| duration | FLOAT64 | The duration requested as time off; in hours. |  |  |
| payCodeId | INT64 | The pay code ID for the time-off period. |  |  |
| payCodeName | STRING | The pay code qualifier for the time-off period. |  |  |
| symbolicAmountName | STRING | Symbolic amount for the time-off period: full day, half day, first half day, second half day, or hours. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
