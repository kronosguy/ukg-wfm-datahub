# vLkpHoursOfOperationDaily

**Group:** Detail Dataset → Hours of Operations Views

Daily Version Hours of Operation Defintions used for calculations in materialization process

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLkpHoursOfOperationDaily |
| Unique Identifier | partitionDate,hoursOfOperationId,startDate,endDate,weekDay |
| Source Pipeline | getHoursOfOperation (DR) |

## Columns

**Column count:** 14

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Calendar Date |  |  |
| hoursOfOperationId | INT64 | Hours of operation Identifier |  |  |
| name | STRING | Name of hours operation object |  |  |
| version | INT64 | The version of hours of operation |  |  |
| description | STRING | Hours of operation description |  |  |
| unrestrictedEditSwt | BOOL | A Boolean indicator of whether or not an unrestricted edit is associated with Hours of Operation. Defaults to false. |  |  |
| startDate | DATE | The effective start date |  |  |
| endDate | DATE | The effective end date |  |  |
| closedSwt | BOOL | Boolean indicator of whether or not the hours of operation is closed |  |  |
| openTime | TIME | The opening time associated with an hours of operation item in ISO_LOCAL_TIME format (HH:mm:ss.SSS). |  |  |
| closeTime | TIME | The close  time associated with an hours of operation item in ISO_LOCAL_TIME format (HH:mm:ss.SSS). |  |  |
| holidaySwt | BOOL | Boolean indicator of whether or not the hours of operation is closed |  |  |
| weekDay | STRING | The day of the week for the hours of operation |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted into Data Hub – BigQuery |  |  |
