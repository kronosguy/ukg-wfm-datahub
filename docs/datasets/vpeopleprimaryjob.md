# vPeoplePrimaryJob

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Primary Job in the Business Structure

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeoplePrimaryJob |
| Unique Identifier | personId,primaryOrgId,effectiveDate, expirationDate |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 13

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| primaryOrgPathTxt | STRING | Primary org structure locations concatenated into a string. |  |  |
| primaryOrgId | INT64 | Unique identifier of Primary Business Structure location of the employee associated with the transaction - Joins to Business Structure dimensions |  |  |
| effectiveDate | DATE | Primary job assignment effective date |  |  |
| expirationDate | DATE | Primary job assignment expiration date |  |  |
| primaryLaborString | STRING | Primary labor category entries concatenated into a string |  |  |
| primaryLaborEntryName1 | STRING | Labor Category 1 entry name associated with transaction |  |  |
| primaryLaborEntryName2 | STRING | Labor Category 2 entry name associated with transaction |  |  |
| primaryLaborEntryName3 | STRING | Labor Category 3 entry name associated with transaction |  |  |
| primaryLaborEntryName4 | STRING | Labor Category 4 entry name associated with transaction |  |  |
| primaryLaborEntryName5 | STRING | Labor Category 5 entry name associated with transaction |  |  |
| primaryLaborEntryName6 | STRING | Labor Category 6 entry name associated with transaction |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
