# vAssignmentJobTransfers

**Group:** Detail Dataset → Assignment Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAssignmentJobTransfers |
| Unique Identifier |  |
| Source Pipeline | peoplePositions (CDC) |

## Columns

**Column count:** 16

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | id of the employee to which that particular position is assigned |  |  |
| assignmentId | INT64 | id of a particular assignment |  |  |
| effectiveDate | DATE | Effective date of a particular job transfer |  |  |
| empMgrTransferOrganizationSet | STRING | Name of the employee manager transfer organization set in a particular assignment |  |  |
| empMgrTransferOrganizationSetId | INT64 | ID of an employee manager transfer organization set. |  |  |
| expirationDate | DATE | Expiration date of a particular job transfer |  |  |
| jobTransferSet | STRING | Name of the job transfer set |  |  |
| managerAccessOrganizationSet | STRING | Name of the manager access organization set |  |  |
| managerAccessOrganizationSetId | INT64 | Id of the manager access organization set |  |  |
| managerTransferOrganizationSet | STRING | Name of the manager transfer organization set |  |  |
| managerTransferOrganizationSetId | INT64 | Id of the manager transfer organization set |  |  |
| professionalTransferOrganizationSet | STRING | Name of a professional transfer organization set |  |  |
| professionalTransferOrganizationSetId | INT64 | ID of a professional transfer organization set |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| managerAccessEmployeeGroup | STRING | Name of a manager access employee group |  |  |
| managerAccessEmployeeGroupId | INT64 | ID of a manager access employee group |  |  |
