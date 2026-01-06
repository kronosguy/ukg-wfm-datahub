# vAssignmentLaborAccounts

**Group:** Detail Dataset → Assignment Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAssignmentLaborAccounts |
| Unique Identifier |  |
| Source Pipeline | peoplePositions (CDC) |

## Columns

**Column count:** 10

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | id of the employee to which that particular position is assigned |  |  |
| assignmentId | INT64 | id of a particular assignment |  |  |
| assignmentJob | STRING | date when a particular labour account becomes effective in a position |  |  |
| assignmentLaborCategory | STRING | date when a specific labour account expires and employee will no longer be on that |  |  |
| assignmentLaborCategoryId | INT64 | name of the job assigned in a particular assignment |  |  |
| assignmentOrganizationId | INT64 | name of the labor category assigned in a particular job account |  |  |
| effectiveDate | DATE | id of that particular labor category |  |  |
| expirationDate | DATE | Business structure (org) ID associated with a job account |  |  |
| effDatedCostCenterEntries | STRING | json with details of cost centers associated with a primary job account. "List<CostCenterDataExtension> CostCenterDataExtension : costCenter costCenterDescription costCenterId effectiveDate expirationDate" |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
