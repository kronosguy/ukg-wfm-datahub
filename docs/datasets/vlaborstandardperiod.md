# vLaborStandardPeriod

**Group:** Detail Dataset → Forecasting Detail Views

Labor Standards Setup Configuration (Period)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborStandardPeriod |
| Unique Identifier | effectiveVersionId,laborStandardId |
| Source Pipeline | laborStandard (DR) |

## Columns

**Column count:** 23

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| effectiveVersionId | INT64 | Effective Version ID |  |  |
| laborStandardId | INT64 | The ID of an effective labor standard version. |  |  |
| effectiveDate | DATE | Labor Standard effective start date |  |  |
| expirationDate | DATE | Labor Standard effective end date |  |  |
| disableSwt | BOOLEAN | A Boolean indicator of whether or not to disable the effective version of the labor standard. |  |  |
| distributionType | STRING | The type of labor standard distribution if distributed by traffic pattern. Valid values include POA and HOO. POA corresponds to 'compressed' and HOO to 'truncate'. This setting allows you to compress or truncate traffic pattern distribution. |  |  |
| remainderDistribution | STRING | The type indicating how to evenly distribute the remaining labor. ROUNDING: use the standard labor distribution algorithm. LEFT: spread the remaining labor to the left. RIGHT: spread the remaining labor to the right. |  |  |
| volumerDriverId | INT64 | Volume Driver ID |  |  |
| volumerDriver | STRING | Volume Driver Name |  |  |
| genericCategoryId | INT64 | Generic Category ID |  |  |
| genericCategoryName | STRING | Generic Category Name |  |  |
| distributeByTrafficPatternSwt | BOOLEAN | A Boolean indicator of whether or not to distribute labor by traffic pattern. If false, labor is distributed evenly. This property is optional. The default value is false. |  |  |
| accumulateDriverSwt | BOOLEAN | A Boolean indicator of whether or not to accumulate the volume driver. |  |  |
| overRidePoaSwt | BOOLEAN | A Boolean indicator of whether or not to override the period. |  |  |
| applicationType | STRING | The type indicating the way labor is distributed throughout the day. ABSOLUTE: labor period times are specific. HOO: labor periods are defined by the hours of operation for the department or site. HOO_CLOSE: start labor after the store closes. HOO_OPEN: start labor after the store opens. |  |  |
| lagSwt | BOOLEAN | A Boolean indicator of whether or not to start labor distribution after the labor period. When false, labor distribution starts before the labor period. If no value is passed, labor distribution is the same as the selected labor period. |  |  |
| offSetMin | INT64 | The amount of time in minutes of distributing labor in relation to the defined labor period from 0 to 480. The number must be a multiple of 15. |  |  |
| startTime | TIME | The start time of a period element, from 00:00 to 23:45. The value must be a multiple of 15. |  |  |
| endTime | TIME | The end time of a period element, from 00:00 to 23:45. The value must be a multiple of 15. |  |  |
| offsetDuration | INT64 | The period duration in minutes, from 0 to 720. The value must be a multiple of 15. |  |  |
| offsetMinutes | INT64 | The period offset in minutes, from -705 to 720. The value must be a multiple of 15. |  |  |
| dayOfWeek | STRING | The day of the week. The default is EVERY_DAY. I.e. MONDAY TUESDAY WEDNESDAY THURSDAY FRIDAY SATURDAY SUNDAY EVERY_DAY [Default] |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted or updated in Data Hub - BigQuery |  |  |
