# vPeopleBadge

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Badge Numbers

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleBadge |
| Unique Identifier | personId,badgeAssignmentId,effectiveDate,expirationDate |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| startTime | TIME | Start time |  |  |
| expirationDate | DATE | Date badge expires |  |  |
| endTime | TIME | End time |  |  |
| effectiveDate | DATE | Date badge is effective |  |  |
| badgeNumber | STRING | Badge number | PII | BLANK |
| badgeAssignmentId | INT64 | Badge assignment ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
