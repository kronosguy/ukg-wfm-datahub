# vAssignmentHrPositionCodes

**Group:** Detail Dataset → Assignment Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAssignmentHrPositionCodes |
| Unique Identifier |  |
| Source Pipeline | peoplePositions (CDC) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | id of the employee to which that particular position is assigned |  |  |
| assignmentId | INT64 | id of a particular assignment |  |  |
| hrPositionCodeId | INT64 | Id of the HR position code |  |  |
| name | STRING | Name of the HR position code |  |  |
| startDate | DATE | start date of a date range associated with an HR position code |  |  |
| endDate | DATE | end date of a date range associated with an HR position code |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
