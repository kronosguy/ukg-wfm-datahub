# vUnpvtLaborBudget

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtLaborBudget |
| Unique Identifier | partitionDate,orgId |
| Source Pipeline |  |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| currency | STRING | Curency Type |  |  |
| currencyId | INT64 | Currency ID |  |  |
| lbrBdgt_Hours | FLOAT64 | Labor Budget Hours |  |  |
| lbrBdgt_Cost | FLOAT64 | Labor Budget Cost |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| currencyExchangeRates | STRING | a string value that contains the available currency and exchange rate needed for calculations |  |  |
