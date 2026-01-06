# vPeopleGroupAssignment

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Schedule Group Assignments

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleGroupAssignment |
| Unique Identifier | personId,groupId,effectiveDate, expirationDate |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| groupId | INT64 | Group ID |  |  |
| groupName | STRING | Group Name |  |  |
| expirationDate | DATE | Expiration Date |  |  |
| effectiveDate | DATE | Effective Date |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
