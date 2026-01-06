# vLkpHoursOfOperationOverrideDaily

**Group:** Detail Dataset → Hours of Operations Views

Daily Version Hours of Operation Override Defintions used for calculations in materialization process

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLkpHoursOfOperationOverrideDaily |
| Unique Identifier | partitionDate,hoursOfOperationOverrideId,startDate,endDate |
| Source Pipeline | getHoursOfOperationOverride (DR) |

## Columns

**Column count:** 13

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Calendar Date |  |  |
| hoursOfOperationOverrideId | INT64 | Hours of operation override Identifier |  |  |
| name | STRING | Hours of operation override name |  |  |
| version | INT64 | The version of hours of operation |  |  |
| description | STRING | Hours of operation override description |  |  |
| activeSwt | BOOL | A Boolean indicator of whether or not the override is active |  |  |
| unrestrictedEditSwt | BOOL | A Boolean indicator of whether or not an unrestricted edit is associated with Hours of Operation. Defaults to false. |  |  |
| startDate | DATE | The effective start date |  |  |
| endDate | DATE | The effective end date |  |  |
| closedSwt | BOOL | Boolean indicator of whether or not the hours of operation is closed |  |  |
| openTime | TIME | The opening time associated with an hours of operation item in ISO_LOCAL_TIME format (HH:mm:ss.SSS). |  |  |
| closeTime | TIME | The opening time associated with an hours of operation item in ISO_LOCAL_TIME format (HH:mm:ss.SSS). |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted into Data Hub – BigQuery |  |  |
