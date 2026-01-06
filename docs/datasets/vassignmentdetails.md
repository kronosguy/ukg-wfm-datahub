# vAssignmentDetails

**Group:** Detail Dataset → Assignment Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAssignmentDetails |
| Unique Identifier |  |
| Source Pipeline | peoplePositions (CDC) |

## Columns

**Column count:** 17

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | id of the employee to which that particular position is assigned |  |  |
| assignmentId | INT64 | id of a particular assignment |  |  |
| assignmentName | STRING | Captures the name of the particular assignment |  |  |
| assignmentExemptStatusSwt | BOOLEAN | Boolean indicator of whether an assignment is exempt or not |  |  |
| assignmentExternalId | STRING | External Id of an assignment |  |  |
| assignmentHireDate | DATE | ID of the accrual profile that is assigned to a position |  |  |
| assignmentReportsToManager | STRING | Name of the accrual profile that is assigned to a position |  |  |
| supervisorId | INT64 | ID of the cascading profile that is assigned to a position |  |  |
| supervisorPersonNumber | STRING | Name of the cascading profile that is assigned to a position |  |  |
| seniorityDate | DATE | date of hire of an employee on a particular assignment |  |  |
| accrualProfileId | INT64 | ID of the shift template profile that is assigned to a position |  |  |
| accrualProfileName | STRING | Name of the shift template profile that is assigned to a position. |  |  |
| cascadingProfileId | INT64 | Date of seniority on an assignment |  |  |
| cascadingProfileName | STRING | Employee id of the reporting manager/supervisor of the particular position |  |  |
| professionalShiftCodeId | INT64 | Person number i.e. id of the manager/supervisor |  |  |
| professionalShiftCodeName | STRING | Name of the reporting manager at a particular position |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
