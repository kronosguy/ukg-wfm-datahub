# vPeopleLicense

**Group:** Detail Dataset → People Detail Views

- Non-Effective Dated - WFD License Assignments

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleLicense |
| Unique Identifier | personId,licenseId,licenseType |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| licenseTypeName | STRING | License Type Name |  |  |
| licenseType | STRING | License Type |  |  |
| licenseId | INT64 | License ID |  |  |
| activeSwt | BOOLEAN | License active switch |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
