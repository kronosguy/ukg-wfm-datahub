# vPayRulesAssignment

**Group:** Detail Dataset → Timekeeping Setup

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPayRulesAssignment |
| Unique Identifier | all fields |
| Source Pipeline | payRules (DR) |

## Columns

**Column count:** 18

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| payRuleId | INT64 | The ID of a pay rule join with vPayRules |  |  |
| assignWorkRuleName | STRING | Assigned work rule name |  |  |
| assignWorkRuleid | INT64 | Assigned work rule ID |  |  |
| sundaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Sunday. Defaults to TRUE. |  |  |
| mondaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Monday. Defaults to TRUE. |  |  |
| tuesdaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Tuesday. Defaults to TRUE. |  |  |
| wednesdaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Wednesday. Defaults to TRUE. |  |  |
| thursdaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Thursday. Defaults to TRUE. |  |  |
| fridaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Friday. Defaults to TRUE. |  |  |
| saturdaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Satruday. Defaults to TRUE. |  |  |
| unscheduledSwt | BOOLEAN | A Boolean indicator of whether or not unscheduled employees can qualify for an assignment shift. Defaults to TRUE. |  |  |
| orderNum | INT64 | The order number of the assignment rules that are assigned to a particular pay rule. |  |  |
| scheduleStartTime | INT64 | or scheduled employees to qualify for the assigned shift, their scheduled start times must be before the end time. for unscheduled employees to qualify for the assigned shift, their in-punches must be before the end time. end time in hh:mm am\|pm format. |  |  |
| scheduleEndTime | INT64 | The end time of a schedule closes the range of time that allows in-punches to link to an assigned schedule. |  |  |
| scheduledSwt | BOOLEAN | A Boolean indicator of whether or not scheduled employees can qualify for an assignment shift. Defaults to TRUE. |  |  |
| shiftMin | INT64 | The minimum shift length required for an employee to qualify for the assignment rule. Specify the length in hh:mm format. The default is 0:00 (no minimum is required to qualify). |  |  |
| shiftMax | INT64 | The maximum shift length allowed for an employee to qualify for the assignment rule. Specify the length in hh:mm format. The default is 99:59. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
