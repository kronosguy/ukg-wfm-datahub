# vSchedulePost

**Group:** Detail Dataset → Schedule Post Detail Views

Schedule Postings by org

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vSchedulePost |
| Unique Identifier | All fields |
| Source Pipeline | schedulePost (DR) |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents the schedule date associated with the posting.  i.e. a Cashier Job Posting to work on 07/05 - 07/09 the partitionDates reflect the schedule Dates |  |  |
| orgId | INT64 | The orgId for the posted job |  |  |
| postUserName | STRING | User name of person who posted the job |  |  |
| postedSwt | BOOLEAN | If job is posted the value is True and False if the job in unposted |  |  |
| postPersonId | INT64 | Person ID of the person who posted the job |  |  |
| postOnDtm | TIMESTAMP | Date and time job was posted |  |  |
| deletedSwt | BOOLEAN | True if the job was posted and subsequently unposted |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
