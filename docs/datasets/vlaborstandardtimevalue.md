# vLaborStandardTimeValue

**Group:** Detail Dataset → Forecasting Detail Views

Labor Standards Setup Configuration (Time Value)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborStandardTimeValue |
| Unique Identifier | effectiveVersionId,laborStandardId |
| Source Pipeline | laborStandard (DR) |

## Columns

**Column count:** 16

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| effectiveVersionId | INT64 | Effective Version ID |  |  |
| laborStandardId | INT64 | The ID of an effective labor standard version. |  |  |
| effectiveDate | DATE | Labor Standard effective start date |  |  |
| expirationDate | DATE | Labor Standard effective end date |  |  |
| disableSwt | BOOLEAN | A Boolean indicator of whether or not to disable the effective version of the labor standard. |  |  |
| timeUnit | STRING | The unit of time representing fixed time values. i.e. HOURS MINUTES SECONDS |  |  |
| frequencyUnit | STRING | The unit of time representing frequency i.e. .PER_PERIOD PER_HOUR PER_DAY PER_WEEK |  |  |
| timeValueAmt | FLOAT | The time the action takes for fixed time values. |  |  |
| timeValueScaledSwt | BOOLEAN | A Boolean indicator of whether or not the time value is scaled. When false, it is fixed. |  |  |
| volumeDriverId | INT64 | Volume Driver ID |  |  |
| volumeDriver | STRING | Volume Driver Name |  |  |
| secondaryVolumeDriverId | INT64 | Secondary Volume Driver ID |  |  |
| secondaryVolumeDriver | STRING | Secondary Volume Driver Name |  |  |
| genericCategoryId | INT64 | Generic Category ID |  |  |
| genericCategoryName | STRING | Generic Category Name |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted or updated in Data Hub - BigQuery |  |  |
