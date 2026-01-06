# vLinkedCategory

**Group:** Detail Dataset → Forecasting Detail Views

Dimensions primary and secondary linked categories

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLinkedCategory |
| Unique Identifier | All fields |
| Source Pipeline | linkedCategory (DR) |

## Columns

**Column count:** 9

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| primaryLinkedCategoryOrgId | INTEGER | Unique ID of Business Structure location for the Primary Category Org ID - joins to Business Structure Dimension |  |  |
| secondaryLinkedCategoryOrgId | INTEGER | Unique ID of Business Structure location for the Secondary Category Org ID - joins to Business Structure Dimension |  |  |
| volumeDriverId | INTEGER | The ID of the Volume Driver. |  |  |
| volumeDriver | STRING | The Name of  the Volume Driver. (derived from volumeDrivers.volumeDriver for slowly changing dimensions) |  |  |
| actionTypeId | INTEGER | Action Type ID  ** not used by Data Hub |  |  |
| actionType | STRING | A reference to an action type object. ** not used by Data Hub |  |  |
| effectiveDate | DATE | The effective date |  |  |
| version | INTEGER | The current version of a volume driver action. ** not used by Data Hub |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
