# vAssignmentCustomDatesEntries

**Group:** Detail Dataset → Assignment Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAssignmentCustomDatesEntries |
| Unique Identifier |  |
| Source Pipeline | peoplePositions (CDC) |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | id of the employee to which that particular position is assigned |  |  |
| assignmentId | INT64 | id of a particular assignment |  |  |
| customDateTypeId | INT64 | Type of the custom date field added in an assignment |  |  |
| dateName | STRING | Name of the custom date fields |  |  |
| defaultDate | DATE | Default value for the custom date |  |  |
| description | STRING | Description of the custom date |  |  |
| overrideDate | DATE | Date to be overriden in custom date |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
