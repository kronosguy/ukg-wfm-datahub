# vCustomDriverValues

**Group:** Detail Dataset → Forecasting Detail Views

Daily Custom (Labor) Driver values by business structure, 1 row per custom driver/date.  All custom drivers are in this view.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vCustomDriverValues |
| Unique Identifier | orgId,partitionDate,cstmDriverId |
| Source Pipeline | customDriverValues (DR) |

## Columns

**Column count:** 9

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| amount | FLOAT64 | Custom driver amount |  |  |
| cstmDriver | STRING | Driver name |  |  |
| cstmDriverId | INT64 | Driver ID |  |  |
| currency | STRING | Currency name |  |  |
| currencyId | INT64 | Currency ID |  |  |
| version | INT64 | Unix timestamp that logs the date/time of change |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
