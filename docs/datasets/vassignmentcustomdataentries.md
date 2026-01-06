# vAssignmentCustomDataEntries

**Group:** Detail Dataset → Assignment Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAssignmentCustomDataEntries |
| Unique Identifier |  |
| Source Pipeline | peoplePositions (CDC) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | id of the employee to which that particular position is assigned |  |  |
| assignmentId | INT64 | id of a particular assignment |  |  |
| customDataType | STRING | Type of the custom data field added in an assignment |  |  |
| customDataTypeId | INT64 | id of such custom data fields |  |  |
| customText | STRING | Any text to be stored in the custom field |  |  |
| updateDtm | DATETIME |  |  |  |
