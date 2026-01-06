# vDimHoursOfOperation

**Group:** Summary Dataset → Dimension Views

Hours of Operation by Org and Date at the 15 minute grain

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vDimHoursOfOperation |
| Unique Identifier | HROP_orgId,HROP_partitionDate, HROP_timeQtr24H |
| Source Pipeline |  |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| HROP_orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| HROP_partitionDate | DATE | Represents the calendar date |  |  |
| HROP_timeQtr24H | TIME | Quarter of 24h |  |  |
| HROP_openTime | TIME | Location open time |  |  |
| HROP_closeTime | TIME | Location close time |  |  |
| HROP_openSwt | BOOLEAN | A boolean indicator whether the location is open.  If TRUE its open during this segment |  |  |
| HROP_overRideSwt | BOOLEAN | A boolean indicator whether the hours of operation is derived from an override |  |  |
| HROP_categoryIds | INT64 (NESTED) | A nested list of category ids associated with department |  |  |
