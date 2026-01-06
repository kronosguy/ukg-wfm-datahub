# vLkpHoursOfOperationAssign

**Group:** Detail Dataset → Hours of Operations Views

Daily Version Hours of Operation Assignment used for calculations in materialization process

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLkpHoursOfOperationAssign |
| Unique Identifier | partitionDate,hoursOfOperationId,orgId,startDate,endDate |
| Source Pipeline | hoursOfOperationAssign (DR) |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Calendar date |  |  |
| orgId | INTEGER | Organization Identifier |  |  |
| hoursOfOperationId | INTEGER | Hours of operation Identifier |  |  |
| startDate | DATE | Hours of Operation Start Date |  |  |
| endDate | DATE | Hours of Operation End Date |  |  |
| inheritedSwt | BOOLEAN | Boolean indicator of whether or not the hours of operation is inherited from parent location |  |  |
| allowOverlappingOverrideSwt | BOOLEAN | Boolean indicator of whether or not the hours of operation is allowed to overlap |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted into Data Hub – BigQuery |  |  |
