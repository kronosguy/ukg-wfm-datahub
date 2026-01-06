# vPeople

**Group:** Detail Dataset → People Detail Views

- One record for each employee - Data in this view is CURRENTLY EFFECTIVE

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeople |
| Unique Identifier | personId |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 110

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| snapShotDate | DATE | This is the date the last time the view was refreshed and that is what this data is effective as of. |  |  |
| exceptionPresentSwt | BOOLEAN | Does the employee have an exception on there people record? True/False |  |  |
| personId | INT64 | Primary Key  - Should be used for all joins to detail fact Views. Not the Person Id in Dimensions |  |  |
| personNumber | STRING | Friendly Person Number as configured in WFD. | PII |  |
| firstName | STRING | Employee first name | PII | Random Name |
| middleName | STRING | Employee middle name | PII | Random Name |
| lastName | STRING | Employee last name | PII | Random Name |
| timeZone | STRING | Time zone assigned to person |  |  |
| timeZoneId | INT64 | Time zone ID |  |  |
| userName | STRING | User name | PII | Random Name |
| isEmployeeSwt | BOOLEAN | Indicates if person is employee |  |  |
| isManagerSwt | BOOLEAN | Indicates if person is manager |  |  |
| hourlyRate | FLOAT64 | Hours wage | Confidential |  |
| hireDate | DATE | Data employee was hired |  |  |
| seniorityDate | DATE | Seniority Date |  |  |
| empCurrencyCode | STRING | Currency code assigned to employee |  |  |
| userCurrencyCode | STRING | User currency code |  |  |
| wageProfile | STRING | Wage profile assigned |  |  |
| payRuleName | STRING | Assigned pay rule name |  |  |
| workRuleId | INT64 | Work Rule ID |  |  |
| managerSignoffThruDate | DATE | Data through which employee's timecards have been signed off by their manager |  |  |
| payrollLockoutThruDate | DATE | Date payroll lockout through |  |  |
| supervisorPersonNumber | STRING | Supervisor person number |  |  |
| supervisorPersonId | INT64 | Supervisor person ID Used to join to people dimension |  |  |
| supervisorFullName | STRING | Supervisor full name | PII |  |
| employmentTerm | STRING | Employment term |  | Random Name |
| availabilityPattern | STRING | Availability pattern |  |  |
| expectedDailyHours | FLOAT64 | Expected hours per day |  |  |
| useMASwt | BOOLEAN | User Multiple Assignments Switch |  |  |
| deletedSwt | BOOLEAN | Indicates deleted. |  |  |
| assignPersonOvertimeSwt | BOOLEAN | Assign person overtime switch |  |  |
| expectedByPayPeriodHours | FLOAT64 | Expected hours per pay period |  |  |
| hyperfindProfile | STRING | The Hyperfind profile associated with a Scheduling extension. |  |  |
| useMultipleAssignmentsSwt | BOOLEAN | User Multiple Assignments Switch |  |  |
| professionalTransferOrganizationSet | STRING | Professional transfer organizational set |  |  |
| managerAccessEmployeeGroup | STRING | Employee group assigned for manager access |  |  |
| managerTransferOrganizationSet | STRING | Org transfer set assigned |  |  |
| jobTransferSet | STRING | Job transfer set assigned |  |  |
| workerType | STRING | Worker type - full time, part time, etc |  |  |
| hasPersonalOvertimeSwt | BOOLEAN | A Boolean indicator of whether or not the entity has personal overtime. |  |  |
| managerAccessSet | STRING | Manager access set |  |  |
| groupSchedule | STRING | The group schedule associated with a Scheduling extension. Person Record > Scheduling > Manager Role-Scheduler > Schedule Group Profile |  |  |
| schedulePattern | STRING | The schedule pattern associated with a Scheduling extension.Person Record > Scheduling > Manager Role-Scheduler > Pattern Template Profile |  |  |
| scheduleGroup | STRING | The schedule group associated with a Scheduling extensio Person Record > Scheduling > Scheduler > Group Assignment |  |  |
| expectedWeeklyHours | FLOAT64 | Expected hours per week |  |  |
| hasKmailNotificationDeliverySwt | BOOLEAN | Indicates if employee has Kmail delivery |  |  |
| learnPath | STRING | Learning path |  |  |
| lockoutResetDateTime | TIMESTAMP | date time for lockout reset |  |  |
| primaryLaborCategory | STRING | Primary labor category entries concatentated. |  |  |
| primaryLaborEntryName1 | STRING | Labor Category 1 entry name associated with transaction |  |  |
| primaryLaborEntryName2 | STRING | Labor Category 2 entry name associated with transaction |  |  |
| primaryLaborEntryName3 | STRING | Labor Category 3 entry name associated with transaction |  |  |
| primaryLaborEntryName4 | STRING | Labor Category 4 entry name associated with transaction |  |  |
| primaryLaborEntryName5 | STRING | Labor Category 5 entry name associated with transaction |  |  |
| primaryLaborEntryName6 | STRING | Labor Category 6 entry name associated with transaction |  |  |
| primaryOrgPathTxt | STRING | Concatentated org path information |  |  |
| employmentStatus | STRING | Employment status of employee: Active, Inactive, Terminated |  |  |
| accountStatus | STRING | Current account status |  |  |
| logonProfile | STRING | logon profile |  |  |
| processManagerProfile | STRING | Assigned process manager profile |  |  |
| authenticationType | STRING | Authentication type - basic, federated |  |  |
| localeProfile | STRING | Locale profile assigned |  | BLANK |
| accountLockedSwt | BOOLEAN | Indicates if user account is locked |  |  |
| usingShiftLabelSwt | BOOLEAN | Using shift label switch |  |  |
| usesTwelveHourFormatSwt | BOOLEAN | Uses twelve hour format switch |  |  |
| calendarProfile | STRING | employee calendar profile |  |  |
| summaryViewProfile | STRING | Summary view profile |  |  |
| schedulePeriod | STRING | Schedule Period |  |  |
| preferenceProfile | STRING | Assigned preference profile |  |  |
| externalURLProfile | STRING | Assigned external url profile |  |  |
| staffSchedulerProfile | STRING | Staff scheduler profile |  |  |
| accessProfile | STRING | Access profile assigned to employee |  |  |
| accessProfileId | INT64 | Access profile ID |  |  |
| notificationProfile | STRING | Assigned notification profile |  |  |
| reportName | STRING | Report name |  |  |
| sseWorkRuleProfile | STRING | This is Work Rule Profile under the Employee Role |  |  |
| workRuleProfile | STRING | This is Work Rule Profile under the Manager Role - General |  |  |
| timeEntryType | STRING | Time entry type: Hourly view, project view |  |  |
| payCodeProfile | STRING | Assigned paycode profile |  |  |
| sseLaborLevelTransferset | STRING | This is Labor Level Transfer under the Employee Role |  |  |
| sseLaborCategoryProfile | STRING | This is Labor Category Profile under the Employee Role |  |  |
| canApproveOvertimeSwt | BOOLEAN | Can approve overtime |  |  |
| laborLevelTransferset | STRING | labor category transfer set |  |  |
| shiftCode | STRING | Shift Code |  |  |
| ssePayCode | STRING | This is Pay Code Edits Profile under the Employee Role |  |  |
| canTransferSwt | BOOLEAN | Can be transferred to different jobs |  |  |
| payCodeViewProfile | STRING | Assigned paycode view profile |  |  |
| laborCategoryProfile | STRING | Labor category profile |  |  |
| processEmployeeProfile | STRING | Assigned process employee profile |  |  |
| mfaRequiredSwt | BOOLEAN | Multi-factor authentication required switch |  |  |
| passwordUpdateRequiredSwt | BOOLEAN | A Boolean indicator of whether or not an updated password is required |  |  |
| requirePassChangeSwt | BOOLEAN | A Boolean indicator of whether or not to require a password change |  |  |
| fullName | STRING | Employee full name | PII |  |
| shortName | STRING | Short Name | PII | Random |
| romanizedFullName | STRING | Romanized Full Name | PII | Random |
| phoneticFullName | STRING | Phonetic full name | PII | Random |
| passwordUpdatedDateTime | TIMESTAMP | Date user password was most recently updated |  |  |
| restrictedUserSwt | BOOLEAN | Restricted User switch |  |  |
| consecutiveBadLogons | INT64 | Count of incorrect logins |  |  |
| birthDate | DATE | date of birth | Confidential | Random |
| delegateProfile | STRING | Delegate profile |  |  |
| badgeNumber | STRING | badge number | PII | Blank |
| fingerRequiredSwt | BOOLEAN | Indicateds if finger required |  |  |
| deviceGroup | STRING | Device Group assigned to employee |  |  |
| fullTimeStandardHoursQuantity | FLOAT64 | Standard full time hours for employee |  |  |
| fullTimeEquivalencyPercent | FLOAT64 | FTE percent |  |  |
| employeeStandardHoursQuantity | FLOAT64 | Standard hours |  |  |
| accrualProfileName | STRING | Accrual profile assigned to employee |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| workRuleName | STRING | Work rule name |  |  |
