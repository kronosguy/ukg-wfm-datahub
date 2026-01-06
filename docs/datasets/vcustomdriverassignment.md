# vCustomDriverAssignment

**Group:** Detail Dataset → Forecasting Detail Views

Custom Drivers assigned to Business Structure nodes. (Sourced from WFD)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vCustomDriverAssignment |
| Unique Identifier | orgId,cstmDriverId |
| Source Pipeline | customDriverAssignment (DR) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| cstmDriverId | INT64 | Custom Driver ID |  |  |
| name | STRING | Name of custom driver |  |  |
| currency | BOOLEAN | Indicates if amount is a currency amount |  |  |
| decimalPosition | INT64 | Decimal position |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
