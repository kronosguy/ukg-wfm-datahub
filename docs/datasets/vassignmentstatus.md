# vAssignmentStatus

**Group:** Detail Dataset → Assignment Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAssignmentStatus |
| Unique Identifier |  |
| Source Pipeline | peoplePositions (CDC) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | id of the employee to which that particular position is assigned |  |  |
| assignmentId | INT64 | id of a particular assignment |  |  |
| employmentStatus | STRING | Represents the start date of a defined period during where different positions can have different status |  |  |
| employmentStatusTypeId | INT64 | Represents the status of a particular assignment in that timeframe if position is ACTIVE, INACTIVE or TERMINATED |  |  |
| effectiveDate | DATE | id of the status of a position |  |  |
| expirationDate | DATE | Represents the end date of a of that particular timeframe. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
