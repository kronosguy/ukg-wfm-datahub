# vAssignmentFullTimeEquivalencies

**Group:** Detail Dataset → Assignment Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAssignmentFullTimeEquivalencies |
| Unique Identifier |  |
| Source Pipeline | peoplePositions (CDC) |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | id of the employee to which that particular position is assigned |  |  |
| assignmentId | INT64 | id of a particular assignment |  |  |
| effectiveDate | DATE | Effective date of a position full time equivalency |  |  |
| expirationDate | DATE | Employee standard hours of a position full time equivalency |  |  |
| employeeStandardHours | FLOAT | Expiration date of a position full time equivalency |  |  |
| fullTimePercentage | FLOAT | Full time percentage of a position full time equivalency |  |  |
| fullTimeStandardHours | FLOAT | Full time Hours of a position full time equivalency |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
