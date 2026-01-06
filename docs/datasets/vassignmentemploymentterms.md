# vAssignmentEmploymentTerms

**Group:** Detail Dataset → Assignment Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAssignmentEmploymentTerms |
| Unique Identifier |  |
| Source Pipeline | peoplePositions (CDC) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | id of the employee to which that particular position is assigned |  |  |
| assignmentId | INT64 | id of a particular assignment |  |  |
| employmentTermId | INT64 | id of the employment term assigned in a particular position |  |  |
| name | STRING | name of the particular employment term |  |  |
| effectiveDate | DATE | date when a specific employment term becomes effective. |  |  |
| expirationDate | DATE | date when a specific employment term expires. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
