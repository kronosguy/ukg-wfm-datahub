# vHoursOfOperationAssign

**Group:** Detail Dataset → Hours of Operations Views

The orgs assigned to the hours of operation

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHoursOfOperationAssign |
| Unique Identifier | hoursOfOperationId,orgId |
| Source Pipeline | hoursOfOperationAssign (DR) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgId | INT64 | Organization Identifier |  |  |
| hoursOfOperationId | INT64 | Hours of operation Identifier |  |  |
| startDate | DATE | The effective start date |  |  |
| endDate | DATE | The effective end date |  |  |
| inheritedSwt | BOOL | Boolean indicator of whether or not the hours of operation is inherited from parent location |  |  |
| allowOverlappingOverrideSwt | BOOL | Boolean indicator of whether or not the hours of operation is allowed to overlap |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted into Data Hub – BigQuery |  |  |
