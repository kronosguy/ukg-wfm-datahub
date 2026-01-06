# vAssignmentScheduleGroups

**Group:** Detail Dataset → Assignment Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAssignmentScheduleGroups |
| Unique Identifier |  |
| Source Pipeline | peoplePositions (CDC) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | id of the employee to which that particular position is assigned |  |  |
| assignmentId | INT64 | id of a particular assignment |  |  |
| scheduleGroupId | INT64 | id of the schedule group assigned in a particular position |  |  |
| name | STRING | name of the particular schedule group |  |  |
| effectiveDate | DATE | date when a specific schedule group becomes effective. |  |  |
| expirationDate | DATE | date when a specific schedule group expires. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
