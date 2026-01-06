# vScheduleDayLock

**Group:** Detail Dataset → Schedule Detail Views

- Indicates the person/dates that have had the schedule "locked" by a manager.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleDayLock |
| Unique Identifier | partitionDate,personId |
| Source Pipeline | schedule (CDC) |

## Columns

**Column count:** 10

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| dayLockId | INT64 | Schedule Day Lock ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| startDateTime | DATETIME | Schedule start date time |  |  |
| endDateTime | DATETIME | Schedule end date time |  |  |
| deletedSwt | BOOLEAN | The Boolean flag indicating the day lock deleted status (read-only). |  |  |
| postedSwt | BOOLEAN | The Boolean flag  that the system generated this day lock. |  |  |
| generatedSwt | BOOLEAN | The Boolean indicating that the system generated this day lock. |  |  |
| version | INT64 | Unix timestamp that logs the date/time of change |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
