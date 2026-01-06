# vPeopleJobTransfer

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Job Transfer profiles

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleJobTransfer |
| Unique Identifier | personId,effectiveDate,expirationDate |
| Source Pipeline |  |

## Columns

**Column count:** 11

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| professionalTransferOrganizationSet | STRING | Employee Job Transfer Set |  |  |
| managerTransferOrganizationSetId | INT64 | Manager Job Transfer Set ID |  |  |
| managerAccessEmployeeGroupId | INT64 | Manager |  |  |
| professionalTransferOrganizationSetId | INT64 | Employee Job Transfer Set ID |  |  |
| managerAccessEmployeeGroup | STRING | Manager employee group access |  |  |
| expirationDate | DATE | Expiration Date of Job Transfer |  |  |
| managerTransferOrganizationSet | STRING | Manager Job Transfer Set |  |  |
| jobTransferSet | STRING | Job Transfer Set |  |  |
| effectiveDate | DATE | Effective Date of Job Transfer |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
