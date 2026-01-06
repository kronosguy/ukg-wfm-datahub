# vActualVolume

**Group:** Detail Dataset → Forecasting Detail Views

- Actual Volume by Site (eventually will be at the Category Level) (Retail Forecasting) Note: Includes only currently active orgs

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vActualVolume |
| Unique Identifier | partitionDate,orgId,volumeDriverId,posLabelId |
| Source Pipeline | actualVolume (DR) |

## Columns

**Column count:** 10

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| dailyAmount | FLOAT64 | Actual volume amount |  |  |
| volumeDriver | STRING | Volume driver amount is assigned to (Sales, traffic, units, etc) |  |  |
| volumeDriverId | INT64 | Volume Driver ID |  |  |
| posLabel | STRING | Point of sale label |  |  |
| posLabelId | INT64 | Point of sale label ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| linkedCategoryType | STRING | a string value Primary or Secondary identifying how the org was defined in Dimensions.  This field can used to filter on the org you wish to include in your totals. |  |  |
| includeSummarySwt | BOOLEAN | determines which nodes will appear vKronosDaySummary .  It’s based on linked_category_configuration |  |  |
