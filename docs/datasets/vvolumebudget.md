# vVolumeBudget

**Group:** Detail Dataset → Budget Detail Views

Customer's budgeted volumes.
- volume budget - daily by category

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vVolumeBudget |
| Unique Identifier | partitionDate,orgId,volumeDriverId |
| Source Pipeline | volumeBudget (DR) |

## Columns

**Column count:** 10

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| currency | STRING | If amount is cost type then currency code. (e.g. USD) |  |  |
| currencyId | INT64 | currency id |  |  |
| dailyAmount | FLOAT | Budgeted volume amount, can be budgeted hours or budgeted wages. |  |  |
| volumeDriver | STRING | The ID of the Volume Driver. |  |  |
| volumeDriverId | INT64 | The Name of  the Volume Driver. (derived from volumeDrivers.volumeDriver for slowly changing dimensions) |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| linkedCategoryType | STRING | a string value Primary or Secondary identifying how the org was defined in Dimensions.  This field can used to filter on the org you wish to include in your totals. |  |  |
| includeSummarySwt | BOOLEAN | determines which nodes will appear vKronosDaySummary .  It’s based on linked_category_configuration |  |  |
