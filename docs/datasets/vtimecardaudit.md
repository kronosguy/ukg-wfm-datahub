# vTimecardAudit

**Group:** Detail Dataset → Audit Detail Views

This view provides timecaard audit details

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTimecardAudit |
| Unique Identifier | auditUniqueId |
| Source Pipeline | timecardAudit (DR) |

## Columns

**Column count:** 51

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| auditId | INT64 | Audit ID (this value can be joined to the ids in the Timecard views i.e.vTimecardPunch.punchId = vTimecardAudit.auditId, vTimecardPayCodeEdit.payCodeEditId =  vTimecardAudit.auditId, vTimecardException.exceptionId = vTimecardAudit.auditId |  |  |
| auditUniqueId | STRING | Unique Identifier for Timecard Audit |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Person ID for whom the audit was made |  |  |
| personNumber | STRING | Person Number for whom the auidt was amde |  |  |
| orgId | INT64 | Org ID of the approved worked job |  |  |
| auditTimeStamp | DATETIME | Date and time when timecard audit was made |  |  |
| auditType | STRING | The type of timecard entity that was edited i.e. Punch, paycode edit |  |  |
| auditPaycodeId | INT64 | ID of the paycode edit |  |  |
| auditPaycodeName | STRING | Paycode name |  |  |
| auditAmountDays | FLOAT | Paycode Edit Duration (Days) |  |  |
| auditAmountHours | FLOAT | Paycode Edit Duration (Hours) |  |  |
| auditAmountMoney | FLOAT | Paycode Edit Amount (Money) |  |  |
| auditTransferWorkruleId | INT64 | Work Rule ID of the transfer |  |  |
| auditTransferWorkrule | STRING | Work Rule Name of the transfer |  |  |
| transferOrgId | INT64 | Job ID of the transfer |  |  |
| auditTransferLaborEntryName1 | STRING | Transfer Labor Category Name 1 (at the time of transaction) |  |  |
| auditTransferLaborEntryName2 | STRING | Transfer Labor Category Name 2 (at the time of transaction) |  |  |
| auditTransferLaborEntryName3 | STRING | Transfer Labor Category Name 3 (at the time of transaction) |  |  |
| auditTransferLaborEntryName4 | STRING | Transfer Labor Category Name 4 (at the time of transaction) |  |  |
| auditTransferLaborEntryName5 | STRING | Transfer Labor Category Name 5 (at the time of transaction) |  |  |
| auditTransferLaborEntryName6 | STRING | Transfer Labor Category Name 6 (at the time of transaction) |  |  |
| auditTransferCostCenter | STRING | Transfer Cost Center Name (at the time of transaction) |  |  |
| tkauditPunchOverride | STRING | Punch Override Type (i.e. In Punch, Out Punch) |  |  |
| auditCommentText | STRING | Punch Comment Text |  |  |
| auditNoteText | STRING | Punch Note Text |  |  |
| auditDatasource | STRING | Source of the Timecard Audit (i,e, Timecard Editor, Group Edit) |  |  |
| auditDatasourceIpAddress | STRING | IP Addres of the data source |  |  |
| auditDelegatePersonId | INT64 | Employee ID of the Delegator or Proxied User |  |  |
| auditRevisionId | INT64 | Timecard Audit Revision ID |  |  |
| auditRevisionDatetime | DATETIME | The date and time the audit was made (i.e. if this was a punch it would be the punch date time or sign-off/approval the date time it was made) |  |  |
| auditChangeRequestStatus | STRING | Status of the Timecard Change Request |  |  |
| auditRevisionType | STRING | Audit Revision Type (i.e. Add, Edit, Delete) |  |  |
| auditRevisionPersonId | INT64 | Person ID of the person who made the audit |  |  |
| auditRevisionUserPersonNumber | STRING | Person Number of the person who made the audit |  |  |
| auditOriginalDate | DATE | The date of the original transaction modified by a historical correction |  |  |
| tkauditPunchCancelDeduct | STRING | Cancel Deduction Indicator |  |  |
| tkauditPunchCancelWorkRuleTransfer | STRING | Work Rule Transfer Indicator |  |  |
| tkauditPunchHasComments | STRING | Comment Indicator |  |  |
| tkauditPunchCommentNoteId | INT64 | Comment Note ID |  |  |
| tkauditPunchCommentHasNote | STRING | Note Indicator |  |  |
| tkauditPunchCommentPunchId | INT64 | Associated Punch ID can be joined to timecardPunch with partitionDate and personId |  |  |
| tkauditPunchCommentUpdateDateTime | DATETIME | Comment Update Date Time |  |  |
| tkauditPunchDeleted | STRING | Punch Deleted Indicator |  |  |
| tkauditPunchExceptionResolve | INT64 | Resolved Exception Indicator |  |  |
| tkauditPunchTime | DATETIME | Punch Date Time |  |  |
| tkauditPunchEnteredOnTime | DATETIME | Punch Entered Date Time |  |  |
| tkauditPunchUpdateTime | DATETIME | Punch Update Date Time |  |  |
| auditApplication | STRING | The application… browser, mobile app … and the device used when connecting with the system |  |  |
| auditAppId | STRING | Audit Application ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
