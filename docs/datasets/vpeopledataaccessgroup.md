# vPeopleDataAccessGroup

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Manager "Generic Data Access Profile" assignments.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleDataAccessGroup |
| Unique Identifier | personId,dataAccessGroupId,effectiveDate,expirationDate |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 10

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| expirationDate | DATE | Expiration date |  |  |
| effectiveDate | DATE | Effective Date |  |  |
| dataAccessGroupRoleId | INT64 | Data Access group rold ID |  |  |
| dataAccessGroupId | INT64 | Data Access group ID |  |  |
| defaultSwt | BOOLEAN | Default switch indicator |  |  |
| dataAccessGroupRole | STRING | Data Access Group role |  |  |
| dataAccessGroup | STRING | Data access group |  |  |
| assignDAGID | INT64 | Data access group assignment ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
