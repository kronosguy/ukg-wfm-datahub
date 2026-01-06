# vHoursOfOperationOverride

**Group:** Detail Dataset → Hours of Operations Views

The Hours of Operation Override Definitions

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHoursOfOperationOverride |
| Unique Identifier | hoursOfOperationOverrideId,startDate,endDate |
| Source Pipeline | getHoursOfOperationOverride (DR) |

## Columns

**Column count:** 13

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| hoursOfOperationOverrideId | INT64 | Hours of operation override Identifier |  |  |
| name | STRING | Hours of operation override name |  |  |
| description | STRING | Hours of operation override description |  |  |
| version | INT64 | The version of hours of operation |  |  |
| activeSwt | BOOL | A Boolean indicator of whether or not the override is active |  |  |
| unrestrictedEditSwt | BOOL | A Boolean indicator of whether or not an unrestricted edit is associated with Hours of Operation. Defaults to false. |  |  |
| startDate | DATE | The effective start date |  |  |
| endDate | DATE | The effective end date |  |  |
| openTime | TIME | The opening time associated with an hours of operation item in ISO_LOCAL_TIME format (HH:mm:ss.SSS). |  |  |
| closeTime | TIME | The close  time associated with an hours of operation item in ISO_LOCAL_TIME format (HH:mm:ss.SSS). |  |  |
| reason | STRING | The Hours of Operation Override Reason |  |  |
| closedSwt | BOOL | Boolean indicator of whether or not the hours of operation is closed |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted into Data Hub – BigQuery |  |  |
