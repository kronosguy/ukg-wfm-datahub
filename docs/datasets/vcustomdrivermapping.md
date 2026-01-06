# vCustomDriverMapping

**Group:** Detail Dataset → Forecasting Detail Views

Maps WFD custom Driver Ids to user defined mapping Ids (1-25) - Sourced from the Vision Admin Website.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vCustomDriverMapping |
| Unique Identifier | cstmDriverId,mappingId |
| Source Pipeline | volumeDriverAssignment (DR) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| cstmDriverId | INT64 | Custom Driver ID |  |  |
| mappingId | INT64 | Mapping ID - determines column custom driver amounts are loaded to |  |  |
| customDriverName | STRING | Custom Driver Name |  |  |
| customDriverCurrency | STRING | Indicates if custom driver is currency amount |  |  |
| customDriverDecPos | INT64 | Decimal position |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
