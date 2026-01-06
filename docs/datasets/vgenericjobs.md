# vGenericJobs

**Group:** Detail Dataset → Org Structure Detail Views

- The jobs attached to locations on the business structure that represent locations where employees actually perform those jobs.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vGenericJobs |
| Unique Identifier | id,effectiveDate |
| Source Pipeline | genericJobs (DR) |

## Columns

**Column count:** 13

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| id | INT64 | Unique Identifier for a generic job |  |  |
| name | STRING | The short name of a generic job. |  |  |
| fullName | STRING | The full name of a generic job. |  |  |
| description | STRING | The description of a generic job.Despite location behavior if null passed on update then empty string will be set. |  |  |
| effectiveDate | DATE | The effective date of a generic job. |  |  |
| expirationDate | DATE | The expiration date of a generic job. |  |  |
| displayOrder | STRING | The display order of a generic job. |  |  |
| code | STRING | The code of a generic job. |  |  |
| lastRevision | BOOLEAN | A Boolean indicator of whether or not this is the generic job's first revision. |  |  |
| firstRevision | BOOLEAN | A Boolean indicator of whether or not this is the generic job's last revision. |  |  |
| persistentId | STRING | The persistent ID of a generic job. |  |  |
| updatedDateTime | DATETIME | The last updated time of a generic job. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
