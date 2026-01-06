# vLkpLinkedCategoryConfig

**Group:** Detail Dataset → Forecasting Detail Views

Pivoted version of vLinkedCategory used to perform downstream calculations

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLkpLinkedCategoryConfig |
| Unique Identifier | orgId,volumeDriverId |
| Source Pipeline | linkedCategory (DR) |

## Columns

**Column count:** 4

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| volumeDriverId | INT64 | The ID of the Volume Driver. |  |  |
| linkedCategoryType | STRING | a string value Primary or Secondary identifying how the org was defined in Dimensions.  This field can used to filter on the org you wish to include in your totals |  |  |
| includeSummarySwt | BOOLEAN | a boolean that is based on the linked_category_configuration if true the org will be included and false it will not |  |  |
