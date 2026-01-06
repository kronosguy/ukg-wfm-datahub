# vHcaVolumeDetail

**Group:** Detail Dataset → Healthcare Productivity

Volume Detail provides work unit totals at the procedure code level for raw and weighted volume quantities that are based on the posting and service dates. Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaVolumeDetail |
| Unique Identifier | partitionDate,workunitId,procedureId |
| Source Pipeline | hcaVolumeDetail (CDC) |

## Columns

**Column count:** 11

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of the volume detail - use to join to date dimension |  |  |
| serviceDate | DATE | Service date |  |  |
| workunitId | INT64 | The ID of the work unit |  |  |
| procedureId | INT64 | The ID of the procedure |  |  |
| hcaVolmetricPostDate | DATE | Post Date |  |  |
| hcaVolmetricRawVolume | FLOAT | Raw volume provided by customer volume import integrations |  |  |
| hcaVolmetricAllocatedVolume | FLOAT | Weighted volume based on raw volume and weighting |  |  |
| coreProcedureCode | STRING | Procedure Code |  |  |
| coreProcedureDesc | STRING | Procedure Description |  |  |
| corePatientType | STRING | Patient Type |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
