# vHoursOfOperationAssignOverride

**Group:** Detail Dataset → Hours of Operations Views

The orgs assigned to the hours of operation override

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHoursOfOperationAssignOverride |
| Unique Identifier | hoursOfOperationOverrideId,orgId |
| Source Pipeline | hoursOfOperationAssignOverride (DR) |

## Columns

**Column count:** 4

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgId | INT64 | Organization Identifier |  |  |
| hoursOfOperationOverrideId | INT64 | Hours of operation Identifier |  |  |
| inheritedSwt | BOOL | Boolean indicator of whether or not the hours of operation is inherited from parent location |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted into Data Hub – BigQuery |  |  |
