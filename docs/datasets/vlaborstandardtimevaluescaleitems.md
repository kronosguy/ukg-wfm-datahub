# vLaborStandardTimeValueScaleItems

**Group:** Detail Dataset → Forecasting Detail Views

Labor Standards Setup Configuration (Time Value > Saled Time Values)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborStandardTimeValueScaleItems |
| Unique Identifier | effectiveVersionId,laborStandardId |
| Source Pipeline | laborStandard (DR) |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| effectiveVersionId | INT64 | Effective Version ID |  |  |
| laborStandardId | INT64 | The ID of an effective labor standard version. |  |  |
| effectiveDate | DATE | Labor Standard effective start date |  |  |
| expirationDate | DATE | Labor Standard effective end date |  |  |
| disableSwt | BOOLEAN | A Boolean indicator of whether or not to disable the effective version of the labor standard. |  |  |
| timeValue | FLOAT | The time value in minutes, a positive value less than 9999999999.99999. |  |  |
| forecastValue | FLOAT | The volume threshold in minutes, a positive value less than 9999999999.99999. |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted or updated in Data Hub - BigQuery |  |  |
