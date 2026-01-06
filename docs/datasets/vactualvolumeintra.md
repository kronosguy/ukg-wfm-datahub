# vActualVolumeIntra

**Group:** Detail Dataset → Forecasting Detail Views

Use this view instead of the view since this will display at the lowest business structure node
Actual Volume by Site (eventually will be at the Category Level) (Retail Forecasting) 15 Min Grain Note: Includes only currently active orgs

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vActualVolumeIntra |
| Unique Identifier | partitionDate,orgId,volumeDriverId,posLabelId,startTime,endTime |
| Source Pipeline | actualVolume (DR) |

## Columns

**Column count:** 12

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| amount | FLOAT64 | Actual volume amount |  |  |
| volumeDriver | STRING | Volume driver amount is assigned to (Sales, traffic, units, etc) |  |  |
| volumeDriverId | INT64 | Volume Driver ID |  |  |
| posLabel | STRING | Point of sale label |  |  |
| posLabelId | INT64 | Point of sale label ID |  |  |
| startTime | TIME | Start date time of 15 minute span that the volume amount was recorded |  |  |
| endTime | TIME | End date time of 15 minute span that the volume amount was recorded |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| linkedCategoryType | STRING | a string value Primary or Secondary identifying how the org was defined in Dimensions.  This field can used to filter on the org you wish to include in your totals. |  |  |
| includeSummarySwt | BOOLEAN | determines which nodes will appear vKronosDaySummary .  It’s based on linked_category_configuration |  |  |
