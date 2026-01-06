# vPeopleCostCenter

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Cost Center

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleCostCenter |
| Unique Identifier | personId,costCenterId,effectiveDate,expirationDate |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| costCenterId | INT64 | Cost Center ID |  |  |
| costCenterName | STRING | Cost Center Name |  |  |
| costCenterNumber | STRING | Cost Center Number |  |  |
| effectiveDate | DATE | Cost Center Effective Date |  |  |
| expirationDate | DATE | Cost Center Expiration Date |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
