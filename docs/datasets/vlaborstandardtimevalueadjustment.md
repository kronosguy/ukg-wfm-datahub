# vLaborStandardTimeValueAdjustment

**Group:** Detail Dataset → Forecasting Detail Views

Labor Standards Setup Configuration (Time Value > Labor Standard Adjustment)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborStandardTimeValueAdjustment |
| Unique Identifier | effectiveVersionId,laborStandardId |
| Source Pipeline | laborStandard (DR) |

## Columns

**Column count:** 10

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| effectiveVersionId | INT64 | Effective Version ID |  |  |
| laborStandardId | INT64 | The ID of an effective labor standard version. |  |  |
| effectiveDate | DATE | Labor Standard effective start date |  |  |
| expirationDate | DATE | Labor Standard effective end date |  |  |
| disableSwt | BOOLEAN | A Boolean indicator of whether or not to disable the effective version of the labor standard. |  |  |
| laborStdAdjBlankTreatedAsZeroSwt | BOOLEAN | A Boolean indicator of whether or not to treat blank value as zero |  |  |
| operation | STRING |  |  |  |
| adjustmentDriverId | INT64 | Adjustment Driver ID |  |  |
| adjustmentDriver | STRING | Adjustment Driver Name |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted or updated in Data Hub - BigQuery |  |  |
