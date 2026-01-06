# vForecastWeeks

**Group:** Detail Dataset → Forecasting Detail Views

Identifies the week start date for every business structure node, for forecasting...

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vForecastWeeks |
| Unique Identifier | orgId |
| Source Pipeline | getForecastWeeks (DR) |

## Columns

**Column count:** 3

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| weekStartDay | INT64 | Indicates day of week the forecast week starts |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
