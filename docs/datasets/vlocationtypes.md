# vLocationTypes

**Group:** Detail Dataset → Org Structure Detail Views

- Contains the location (node) type information

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLocationTypes |
| Unique Identifier | id |
| Source Pipeline | getBusinessStructure (DR) |

## Columns

**Column count:** 14

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| id | INT64 | LocationType ID |  |  |
| name | STRING | Location Type Name |  |  |
| description | STRING | Location Type Description |  |  |
| hierarchyOrder | INT64 | The hierarchical order of a node type. |  |  |
| contextId | INT64 | The context ID of a node type |  |  |
| contextName | STRING | The context name of a node type |  |  |
| effectiveDate | DATE | The effective date of a node type in ISO_LOCAL_DATE format (YYYY-MM-DD). |  |  |
| expirationDate | DATE | The expiration date of a node type in ISO_LOCAL_DATE format (YYYY-MM-DD). |  |  |
| lastRevision | BOOLEAN | A Boolean indicator of whether or not this is a node type's last revision. |  |  |
| firstRevision | BOOLEAN | A Boolean indicator of whether or not this is a node type's first revision. |  |  |
| goldDataSwt | BOOLEAN | A Boolean indicator of whether or not this is gold data |  |  |
| persistentId | STRING | The persistent ID of a node type. |  |  |
| updatedDateTime | DATETIME | The date and time of the most recent update to a node type in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
