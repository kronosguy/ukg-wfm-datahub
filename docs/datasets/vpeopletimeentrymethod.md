# vPeopleTimeEntryMethod

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Time Entry Method from WFD (Ie, Timecard or Project View)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleTimeEntryMethod |
| Unique Identifier | personId,assignTimeEntryId |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| timeEntryTypeId | INT64 | Time entry type ID |  |  |
| timeEntryType | STRING | Time entry type |  |  |
| expirationDate | DATE | Assignment expiration date |  |  |
| effectiveDate | DATE | Assignent effective date |  |  |
| assignTimeEntryId | INT64 | Time entry assignment ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
