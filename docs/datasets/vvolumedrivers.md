# vVolumeDrivers

**Group:** Detail Dataset → Forecasting Detail Views

Distinct list of volume drivers as configured in WFD.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vVolumeDrivers |
| Unique Identifier | volumeDriverId |
| Source Pipeline | getVolumeDrivers (DR) |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| volumeDriverId | INT64 | Volume Driver ID |  |  |
| volumeDriver | STRING | Volume Driver Name |  |  |
| dependent | BOOLEAN | A Boolean indicator of whether or not a Volume Driver depends on some other Volume Driver. |  |  |
| currency | BOOLEAN | A Boolean indicator of whether or not a Volume Driver is currency-related |  |  |
| decimalPosition | INT64 | The precision of numeric values in the Volume Driver. |  |  |
| rowNumber | INT64 | The order of the Volume Driver among other Drivers. |  |  |
| version | INT64 | The version of a Volume Driver. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
