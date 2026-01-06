# vScheduleHoliday

**Group:** Detail Dataset → Schedule Detail Views

- lists the person/dates where exists a scheduled holiday. NOTE: the holidays are tied to the employee's pay rule and the holidays associated with that pay rule

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleHoliday |
| Unique Identifier | holidayId,partitionDate,personId |
| Source Pipeline | schedule (CDC) |

## Columns

**Column count:** 12

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| holidayId | INT64 | Holiday ID |  |  |
| partitionDate | DATE | Represents date of availability - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| holiday | STRING | Holiday name |  |  |
| startDateTime | DATETIME | Schedule start date time |  |  |
| endDateTime | DATETIME | Schedule end date time |  |  |
| generatedSwt | BOOLEAN | The Boolean indicating that the system generated this holiday |  |  |
| lockedSwt | BOOLEAN | The Boolean flag  that the holiday is locked |  |  |
| deletedSwt | BOOLEAN | The Boolean flag indicating the day lock deleted status (read-only). |  |  |
| postedSwt | BOOLEAN | The Boolean indicating that the holiday is posted |  |  |
| version | INT64 | Unix timestamp that logs the date/time of change |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
