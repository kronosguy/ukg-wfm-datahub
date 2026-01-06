# vLaborForecastLimits

**Group:** Detail Dataset → Forecasting Detail Views

The labor forecast limits, which include minimum and maximum labor coverage requirements for jobs and job rounding factors

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborForecastLimits |
| Unique Identifier | laborForecastLimitId,effectiveStartDate,effectiveEndDate,poaTypeId,jobId |
| Source Pipeline | laborForecastLimits (DR) |

## Columns

**Column count:** 25

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| laborForecastLimitId | INT64 | The unique ID of a labor forecast limit. |  |  |
| laborForecastLimitName | STRING | The unique name of a labor forecast limit. |  |  |
| laborForecastLimitDesc | STRING | The description of a labor forecast limit. |  |  |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not a labor forecast limit is active. |  |  |
| version | INT64 | The version of a labor forecast limit. |  |  |
| jobId | INT64 | The forecasted job ID |  |  |
| jobName | STRING | The forecasted job Name |  |  |
| withinLaborPeriodSwt | BOOLEAN | A Boolean indicator of whether or not a labor forecast limit assignment is within a labor period. |  |  |
| effectiveStartDate | DATE | The effective start date of a local date span in ISO_LOCAL_DATE format (YYYY-MM-DD). |  |  |
| effectiveEndDate | DATE | The effective end date of the local date span in ISO_LOCAL_DATE format (YYYY-MM-DD). |  |  |
| weekDayId | INT64 | The weekday ID |  |  |
| weekDayName | STRING | The weekday Name |  |  |
| startTime | TIME | The start time of a labor forecast limit item, from 00:00 to 23:45. The value must be a multiple of 15. |  |  |
| endTime | TIME | The end time of a labor forecast limit item, from 00:00 to 23:45. The value must be a multiple of 15. |  |  |
| rounding | FLOAT | The value of a round up headcount threshold. The possible values are: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]. |  |  |
| minHeadCount | INT64 | The maximum value of a headcount, from 0 to 9999. |  |  |
| minHeadCount | INT64 | The minimum value of a headcount, from 0 to 9999. |  |  |
| poaTypeId | INT64 | The poaType ID |  |  |
| poaTypeName | STRING | The poaType Name |  |  |
| offSetMinQty | INT64 | The period offset in minutes, from -720 to 720. The value must be a multiple of 15. |  |  |
| durationMinQty | INT64 | The period duration in minutes, from 0 to 720. The value must be a multiple of 15. |  |  |
| optimizeMinHeadCountSwt | BOOLEAN | A Boolean indicator of whether or not the optimize minimum head count feature is enabled. |  |  |
| fatigueFactor | FLOAT | The value of a fatigue factor expressed as a percent, from 0 to 100. |  |  |
| breakFactor | FLOAT | The value of a break factor expressed as a percent, from 0 to 100. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
