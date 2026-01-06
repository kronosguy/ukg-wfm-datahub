# vPayRules

**Group:** Detail Dataset → Timekeeping Setup

- The pay rule allows you to define and manage rules that control how time and attendance information is processed for each employee.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPayRules |
| Unique Identifier | payRuleId,effectivePayRulesId,effectiveDate,holidayId (nullable), orderNum  (nullable), extensionProcessorsId, extensionProcessorsName |
| Source Pipeline | payRules (DR) |

## Columns

**Column count:** 57

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| payRuleId | INT64 | The ID of a pay rule. |  |  |
| payRuleName | STRING | The name of a pay rule. The name can be up to 32 characters long, is case insensitive, and must be unique. |  |  |
| persistentId | STRING | The persistent ID of a pay rule. |  |  |
| workRuleTransferSwt | BOOLEAN | A Boolean indicator of whether or not the work rule transfers option is enabled for this effective pay rule. When this option is enabled, any work rule transfer that was entered is allowed to continue until a new transaction (employee punch, timecard edit, or group edit) is entered. |  |  |
| cancelPFSOnHolidaySwt | BOOLEAN | A Boolean indicator of whether or not paying scheduled shifts and scheduled edits is canceled on a day that happens to be a holiday |  |  |
| correctionsApplyDate | INT64 | The apply date for corrections. Valid values are: 1:'today', 2:'first day of the current pay period', 3:'last day of the current pay period', 4:'first day of the previous pay period', 5:'last day of the previous pay period'. |  |  |
| cancelPFSEditsOnlyOnHolidaySwt | BOOLEAN | A Boolean indicator of whether or not only scheduled edits are canceled on a day that happens to be a holiday |  |  |
| applyOnlySwt | BOOLEAN | A Boolean indicator that functions in conjunction with payfromschedule. When payfromschedule is equal to true and applyonly is equal to false |  |  |
| fixedRuleId | INT64 | Fixed Rule ID |  |  |
| fixedRuleName | STRING | The name of the associated fixed rule that identifies constant pay policies that are assigned to employees. |  |  |
| effectiveDate | DATE | The effective date span of this pay rule version |  |  |
| costCenterLaborCategoryAndJobTransferSwt | BOOLEAN | A Boolean indicator of whether or not labor account and job transfers are enabled for this effective pay rule. |  |  |
| extensionProcessorsId | INT64 | A list of extension processor IDs |  |  |
| extensionProcessorsName | STRING | A list of extension processor names. |  |  |
| approvedAccntNotificationId | INT64 | The id of the generic notification which is used to notify managers assigned to this pay rule of changes to approved account totals. |  |  |
| approvedAccntNotificationName | STRING | The name of the generic notification which is used to notify managers assigned to this pay rule of changes to approved account totals. |  |  |
| sequenceRuleId | INT64 | The name of the associated processing order rule that defines the order in which accumulated hour types are processed. |  |  |
| sequenceRuleNAme | STRING | sequence rule name |  |  |
| holidaySelectedSwt | BOOLEAN | A Boolean indicator of whether or not the holiday indicated by holidayname is selected for this pay rule. |  |  |
| holidayId | INT64 | The ID of the associated holiday. |  |  |
| holidayName | STRING | The name of the associated holiday. |  |  |
| creditRulesId | INT64 | Credit Rules ID |  |  |
| creditRulesName | STRING | The names of one or more holiday credit rules associated with the pay rule. |  |  |
| managerApprovalRestrictionRuleId | INT64 | A reference to the manager approval restriction rule. |  |  |
| managerApprovalRestrictionRuleName | STRING | manager approval restriction rule name |  |  |
| prepopulateProjectSwt | BOOLEAN | A Boolean indicator of whether or not project prepopulation is enabled for this effective pay rule. When this option is enabled, a project view timecard is prepopulated with the transfer accounts that were used in the previous pay period. |  |  |
| cancelPFSShiftsOnlyOnHolidaySwt | BOOLEAN | A Boolean indicator of whether or not only scheduled shifts are canceled on a day that happens to be a holiday. |  |  |
| payFromScheduleSwt | BOOLEAN | A Boolean indicator that functions in conjunction with applyonly. When payfromschedule is equal to true and applyonly is equal to false, the behavior corresponds to when apply scheduled edits is equal to always and apply scheduled shifts is equal to never. |  |  |
| effectivePayRulesId | INT64 | The id of the pay rule |  |  |
| effectivePayRulesName | STRING | The name of the pay rule. The name is case-insensitive and must be unique. |  |  |
| updateThisVersionSwt | BOOLEAN | A Boolean indicator of whether or not to update the current version of a pay rule. |  |  |
| terminalRuleId | INT64 | The name of the associated punch interpretation rule that determines when punches link to schedules and when data collection devices accept and reject punches. |  |  |
| terminalRuleName | STRING | terminal rule name |  |  |
| enableEditsAfter | INT64 | Enable edits after sign-off: -1 indicates 'enable edits after the lock is removed manually or by payroll interface'. 0, ö, 999 indicate the amount of hours to enable edits after the end of the pay period. |  |  |
| transferRegularHomeSwt | BOOLEAN | A Boolean indicator of whether or not regular home transfers are enabled for this effective pay rule. |  |  |
| scheduleTotal | BOOLEAN | A Boolean indicator of whether or not the projected totals are calculated and stored. Schedule totals are calculated and stored regardless of this setting. |  |  |
| holidayCreditRuleId | INT64 | Holiday Credit Rule ID |  |  |
| holidayCreditRuleName | STRING | The name of the associated holiday credit rule that determines if an employee is eligible to receive holiday credits and the amount of holiday credits the employee can receive. |  |  |
| workRuleId | INT64 | The name of the associated work rule that identifies the work rule that interprets and calculates employee time. |  |  |
| qualifiedSignOffRuleId | INT64 | The name of the associated qualified sign-off rule that restricts a manager's ability to signoff if specific conditions are not met. |  |  |
| qualifiedSignOffRuleName | STRING | qualified sign off rule name |  |  |
| assignWorkRuleid | INT64 | Assignment Workrule ID |  |  |
| sundaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Sunday. Defaults to TRUE. |  |  |
| mondaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Monday. Defaults to TRUE. |  |  |
| tuesdaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Tuesday. Defaults to TRUE. |  |  |
| wednesdaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Wednesday. Defaults to TRUE. |  |  |
| thursdaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Thursday. Defaults to TRUE. |  |  |
| fridaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Friday. Defaults to TRUE. |  |  |
| saturdaySwt | BOOLEAN | A Boolean indicator of whether or not the assignment rule is enabled for Saturday. Defaults to TRUE. |  |  |
| unscheduledSwt | BOOLEAN | A Boolean indicator of whether or not unscheduled employees can qualify for an assignment shift. Defaults to TRUE. |  |  |
| orderNum | INT64 | An order number associated with processing work orders that can be configured in a pay rule. |  |  |
| scheduledSwt | BOOLEAN | A Boolean indicator of whether or not scheduled employees can qualify for an assignment shift. Defaults to TRUE. |  |  |
| scheduleStartTime | INT64 | for scheduled employees to qualify for the assigned shift, their scheduled start times must be before the end time. for unscheduled employees to qualify for the assigned shift, their in-punches must be before the end time. end time in hh:mm am\|pm format. |  |  |
| scheduleEndTime | INT64 | The end time of a schedule closes the range of time that allows in-punches to link to an assigned schedule. For scheduled employees to qualify for the assigned shift, their scheduled start times must be before the end time. For unscheduled employees to qualify for the assigned shift, their in-punches must be before the end time. The end time is in hh:mm am\|pm format. |  |  |
| shiftMin | INT64 | The minimum shift length required for an employee to qualify for the assignment rule. Specify the length in hh:mm format. The default is 0:00 (no minimum is required to qualify). |  |  |
| shiftMax | INT64 | The maximum shift length allowed for an employee to qualify for the assignment rule. Specify the length in hh:mm format. The default is 99:59. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
