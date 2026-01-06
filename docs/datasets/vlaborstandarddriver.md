# vLaborStandardDriver

**Group:** Detail Dataset → Forecasting Detail Views

Labor Standards Setup Configuration (Labor Driver)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborStandardDriver |
| Unique Identifier | effectiveVersionId,laborStandardId |
| Source Pipeline | laborStandard (DR) |

## Columns

**Column count:** 15

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| effectiveVersionId | INT64 | Effective Version ID |  |  |
| laborStandardId | INT64 | The ID of an effective labor standard version. |  |  |
| effectiveDate | DATE | Labor Standard effective start date |  |  |
| expirationDate | DATE | Labor Standard effective end date |  |  |
| disableSwt | BOOLEAN | A Boolean indicator of whether or not to disable the effective version of the labor standard. |  |  |
| laborDriverType | STRING | The type of labor standard driver settings. i.e. VARIABLE_VOLUME VARIABLE_CUSTOM FIXED_FREQUENCY FIXED_FREQUENCY_BY_DAILY_VOLUME FIXED_STATIC_DRIVER |  |  |
| lookBackDays | INT64 | The number of days to look back. For the VARIABLE_CUSTOM type, valid values are 0, 1, 2, 3, 4, 5, 6, and 7. For the VARIABLE_VOLUME type, valid values are 0, 1, 2, and 3. |  |  |
| frequencyUnit | STRING | The frequency interval. The Frequency Interval i.e. PER_PERIOD PER_HOUR PER_DAY PER_WEEK |  |  |
| frequency | FLOAT | The number of times per interval, a positive value the maximum of which is 9999999999.99999. |  |  |
| applicationFactor | FLOAT | The number of items for application factor, a positive value the maximum of which is 9999999999.99999. |  |  |
| genericCategoryId | INT64 | Generic Category ID |  |  |
| genericCategoryName | STRING | Generic Category Name |  |  |
| volumeDriverId | INT64 | Volume Driver ID |  |  |
| volumeDriver | STRING | Volume Driver Name |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted or updated in Data Hub - BigQuery |  |  |
