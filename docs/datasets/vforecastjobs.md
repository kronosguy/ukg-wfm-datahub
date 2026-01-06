# vForecastJobs

**Group:** Detail Dataset → Forecasting Detail Views

A list of forecast job org ids

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vForecastJobs |
| Unique Identifier | orgId |
| Source Pipeline | getForecastJobs (DR) |

## Columns

**Column count:** 2

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
