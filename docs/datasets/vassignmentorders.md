# vAssignmentOrders

**Group:** Detail Dataset → Assignment Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAssignmentOrders |
| Unique Identifier |  |
| Source Pipeline | peoplePositions (CDC) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | id of the employee to which that particular position is assigned |  |  |
| assignmentId | INT64 | id of a particular assignment |  |  |
| assignmentOrder | INT64 | Represents the start date of a defined period during which one or more positions are present |  |  |
| effectiveDate | DATE | Represents the end date of a of that particular timeframe. |  |  |
| expirationDate | DATE | Represents whether a particular position is primary in that time range. |  |  |
| isPrimarySwt | BOOLEAN | Order number of a particular position in that timeframe |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
