# vSecOrgMatrix

**Group:** Detail Dataset → Org Structure Detail Views

- Security view used in UserAuthorized Views to restrict access to data at a row level based on the Employee Group assigned in Dimension as of Current Date.  Note this only applied business structure  security and does not support labor category security.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vSecOrgMatrix |
| Unique Identifier | orgId,personId,employeeGroupId |
| Source Pipeline | secOrgMatrix (DR) |
| Scrubbing | DO NOT LOAD |

## Columns

**Column count:** 9

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| emailAddress | STRING | Employee's email address | PII |  |
| employeeGroupId | INT64 | Employee Group ID  join to vEmployeeGroups |  |  |
| employeeGroupName | STRING | Employee Group Name |  |  |
| locationSetName | STRING | The name of the location set |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| proExternalId | STRING | Pro external identifier |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| userCurrencyDisplayPreference | STRING | - the default currency as defined in Dimensions for the employee |  |  |
