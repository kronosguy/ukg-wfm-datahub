# vHoursOfOperation

**Group:** Detail Dataset → Hours of Operations Views

The Hours of Operation Definitions

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHoursOfOperation |
| Unique Identifier | hoursOfOperationId,startDate,endDate,weekDayQualifier |
| Source Pipeline | getHoursOfOperation (DR) |

## Columns

**Column count:** 14

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| hoursOfOperationId | INT64 | Hours of operation Identifier |  |  |
| name | STRING | Name of hours operation object |  |  |
| version | INT64 | The version of hours of operation |  |  |
| activeSwt | BOOL | A Boolean indicator of whether or not Hours of Operation object is active. |  |  |
| description | STRING | Describes the hours of operation |  |  |
| unrestrictedEditSwt | BOOL | A Boolean indicator of whether or not an unrestricted edit is associated with Hours of Operation. Defaults to false. |  |  |
| startDate | DATE | The effective start date |  |  |
| endDate | DATE | The effective end date |  |  |
| closedSwt | BOOL | Boolean indicator of whether or not the hours of operation is closed |  |  |
| openTime | TIME | The opening time associated with an hours of operation item in ISO_LOCAL_TIME format (HH:mm:ss.SSS). |  |  |
| closeTime | TIME | The close  time associated with an hours of operation item in ISO_LOCAL_TIME format (HH:mm:ss.SSS). |  |  |
| holidaySwt | BOOL | Boolean indicator of whether or not the hours of operation is closed |  |  |
| weekDayQualifier | STRING | The day of the week for the hours of operation |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted into Data Hub – BigQuery |  |  |
