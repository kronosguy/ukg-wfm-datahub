# vAssignmentPayFromSchedules

**Group:** Detail Dataset → Assignment Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAssignmentPayFromSchedules |
| Unique Identifier |  |
| Source Pipeline | peoplePositions (CDC) |

## Columns

**Column count:** 11

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | id of the employee to which that particular position is assigned |  |  |
| assignmentId | INT64 | id of a particular assignment |  |  |
| cancelPFSOnHolidaysSwt | BOOLEAN | A Boolean indicator of whether or not to cancel Pay From Schedule on holidays. |  |  |
| effectiveDate | DATE | Start date from where the pay from schedules will start in an assignment |  |  |
| expirationDate | DATE | End date from where the pay from schedules will end in an assignment |  |  |
| overridePayRuleSwt | BOOLEAN | Boolean indicator of whether or not to override pay rules |  |  |
| payEditsFromScheduleSwt | BOOLEAN | Boolean indicator of whether or not to pay edits from schedule |  |  |
| payShiftFromScheduleSwt | BOOLEAN | Boolean indicator of whether or not to pay shifts from schedule. |  |  |
| paycodeTagId | INT64 | Id of the paycode tag |  |  |
| paycodeTag | STRING | Name of the paycode tag |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
