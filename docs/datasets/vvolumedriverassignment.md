# vVolumeDriverAssignment

**Group:** Detail Dataset → Forecasting Detail Views

orgid to Site orgid mapping

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vVolumeDriverAssignment |
| Unique Identifier | siteOrgId,orgId,volumeDriverId |
| Source Pipeline | volumeDriverAssignment (DR) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| siteOrgId | INT64 | Site orgId -  joins to Business Structure Dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| posLabel | STRING | The label of a Volume Driver. |  |  |
| posLabelId | INT64 | The label ID of a Volume Driver Assignment. |  |  |
| volumeDriverId | INT64 | The ID of the Volume Driver. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| volumeDriver | STRING | The Name of  the Volume Driver. (derived from volumeDrivers.volumeDriver for slowly changing dimensions) |  |  |
