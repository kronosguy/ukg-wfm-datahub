# vLaborStandardTaskGroup

**Group:** Detail Dataset → Forecasting Detail Views

Labor Standards Task Group

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborStandardTaskGroup |
| Unique Identifier | taskGroupId,taskAssignmentId |
| Source Pipeline | laborStandardTaskGroup (DR) |

## Columns

**Column count:** 25

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| taskGroupId | INT64 | The ID of a labor task group. |  |  |
| taskGroupName | STRING | The name of a labor task group. |  |  |
| taskGroupDescription | STRING | The description of a labor task group. |  |  |
| effectiveDate | DATE | The effective start date |  |  |
| expirationDate | DATE | The effective end date |  |  |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not a labor task group is active. |  |  |
| version | INT64 | The version of a labor task to allow support for optimistic locking. |  |  |
| genericDepartmentId | INT64 | Generic Department ID |  |  |
| genericDepartmentName | STRING | Generic Department Name |  |  |
| siteId | INT64 | Site ID associated with the Labor Standard |  |  |
| sitePathTxt | STRING | Site Name associated with the Labor Standard |  |  |
| siteEffectiveDate | DATE | The effective date of site |  |  |
| storeSpecificSwt | BOOLEAN | A Boolean indicator of whether or not a labor task is store-specific. |  |  |
| combinedLaborDistributionId | INT64 | Combined Labor Distribution ID |  |  |
| combinedLaborDistributionName | STRING | Combined Labor Distribution Name |  |  |
| laborHourAllocationRule | STRING | A type indicating how to allocate labor hours. The default value is ACTUAL_DAY. ACTUAL_DAY: Labor hours are split as they fall across the day divide. START_DAY: All hours for the job are applied to the day on which the labor hours begin. END_DAY: All hours for the job are applied to the day on which the labor hours end. |  |  |
| skipBreaksInLaborSwt | BOOLEAN | A Boolean indicator of whether or not the Forecast Manager ignores breaks when it calculates labor hours for a given day when there are gaps of a specified duration in the labor requirements on either side of the day divide. |  |  |
| maximumBreakDuration | INT64 | The number of minutes that defines a break in labor from 0 to 120. The number must be a multiple of 15. |  |  |
| breakPlacementWindow | INT64 | A window (in minutes) on each side of the day divide. Any gap in labor with a start day and end day that falls within this window and meets the maximum break duration is ignored. For example, if you define the window to be 60 minutes, then the window extends from one hour before the day divide to one hour after the day divide. The numerical value of this window represents minutes and can be 0 to 360. The value must be a multiple of 15 and greater than or equal to the maximum break duration. |  |  |
| orgJobAssignmentAsOfDate | DATE | The effective date for jobs resolving |  |  |
| orgJobAssignmentId | INT64 | Org Job Assignment orgId |  |  |
| orgJobAssignmentPathTxt | STRING | Org Job Assignment orgpathtxt |  |  |
| taskAssignmentId | INT64 | Task Assignment ID |  |  |
| taskAssignmentName | STRING | Task Assignment Name |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted or updated in Data Hub - BigQuery |  |  |
