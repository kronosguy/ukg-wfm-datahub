# vScheduleAuditPayCodeEditAudits

**Group:** Detail Dataset → Audit Detail Views

This view provides schedule audit details related to scheduled pay code edits.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleAuditPayCodeEditAudits |
| Unique Identifier | payCodeEditsId,partitionDate,revisionId |
| Source Pipeline | scheduleAudit (CDC) |

## Columns

**Column count:** 91

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| payCodeEditsId | INT64 | The ID for the relationship between the pay code edit and schedule. |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| auditLocalTimestamp | TIMESTAMP | The date and time that the revision was made in the user's home time zone |  |  |
| auditTimestamp | TIMESTAMP | Timestamp for the schedule change |  |  |
| auditType | STRING | The type of this revision. |  |  |
| auditUser | STRING | The full name of the user who made the revision. | PII |  |
| revisionId | INT64 | The id of the this revision/audit record. |  |  |
| startDate | DATE | The shift start date |  |  |
| endDate | DATE | The shift end date |  |  |
| startTime | TIME | The inclusive start time of the pay code edit |  |  |
| endTime | TIME | The shift end time |  |  |
| payCode | STRING | Name of the pay code transactions are charged to - joins to pay code dimension |  |  |
| payCodeId | INT64 | Unique identifier of a pay code. Joins to pay code dimension |  |  |
| durationInTime | INT64 | The duration in seconds of a pay code edit. |  |  |
| durationInDays | FLOAT | The duration in days of a pay code edit. |  |  |
| overrideAccrualAmount | FLOAT | The number of accrual days that a pay code edit overrides. |  |  |
| moneyAmount | FLOAT | The amount (as a decimal value representing money) of the pay code edit. |  |  |
| primaryOrgId | INT64 | Unique identifier of Primary Business Structure location of the employee associated with the transaction - Joins to Business Structure dimensions |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryName2 | STRING | Labor Category 2 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryName3 | STRING | Labor Category 3 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryName4 | STRING | Labor Category 4 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryName5 | STRING | Labor Category 5 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryName6 | STRING | Labor Category 6 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| transferLaborEntryName1 | STRING | Labor Category Transfer 1 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| transferLaborEntryName2 | STRING | Labor Category Transfer 2 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| transferLaborEntryName3 | STRING | Labor Category Transfer 3 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| transferLaborEntryName4 | STRING | Labor Category Transfer 4 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| transferLaborEntryName5 | STRING | Labor Category Transfer 5 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| transferLaborEntryName6 | STRING | Labor Category Transfer 6 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| transferLaborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| transferLaborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| transferLaborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| transferLaborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| transferLaborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| transferLaborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName2 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName3 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName4 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName5 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName6 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| primaryLaborEntryName1 | STRING | Labor Category 1 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| primaryLaborEntryName2 | STRING | Labor Category 2 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| primaryLaborEntryName3 | STRING | Labor Category 3 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| primaryLaborEntryName4 | STRING | Labor Category 4 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| primaryLaborEntryName5 | STRING | Labor Category 5 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| primaryLaborEntryName6 | STRING | Labor Category 6 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| primaryLaborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| primaryLaborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| primaryLaborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| primaryLaborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| primaryLaborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| primaryLaborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| symbolicValue | STRING | A reference to the symbolic value used to create this pay code edit segment. |  |  |
| symbolicValueId | INT64 | The id for the the symbolic value |  |  |
| primaryCostCenter | STRING | Primary cost center for employee associated with transaction |  |  |
| primaryCostCenterId | INT64 | Primary cost center ID - joins to cost center dimension |  |  |
| overrideAccrual | BOOLEAN | A Boolean indicator of whether or not to override the accrual amount associated with a pay code edit. |  |  |
| costCenter | STRING | Cost Center name |  |  |
| costCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension |  |  |
| transferOrgJobSwt | BOOLEAN | A Boolean indicator of whether or not the business structure job is a transfer. |  |  |
| transferCostCenterSwt | BOOLEAN | A Boolean indicator of whether or not there is a transfer cost center for this shift segment. |  |  |
| transferLaborCategoriesSwt | BOOLEAN | A Boolean indicator of whether or not there is a labor category transfer  for this shift segment. |  |  |
| generatedSwt | BOOLEAN | A Boolean indicator of whether or not the shift was generated by the Scheduling engine. |  |  |
| deletedSwt | BOOLEAN | Shift deleted switch |  |  |
| lockedSwt | BOOLEAN | A Boolean indicator of whether or not a pay code edit is locked. |  |  |
| postedSwt | BOOLEAN | The pay code edit posted status. |  |  |
| userEnteredOrgJobSwt | BOOLEAN | A Boolean indicator of whether or not a business structure job was entered by the user. |  |  |
| userEnteredCostCenterSwt | BOOLEAN | A Boolean indicator of whether or not a cost center was entered by the user for this shift segment. |  |  |
| version | INT64 | Unix timestamp that logs the date/time of change |  |  |
| postedNotificationPendingSwt | BOOLEAN | A boolean indicator of whether or not the notification to the employee of the posted pay code edit is pending. |  |  |
| postedNotifiedSwt | BOOLEAN | A boolean indicator of whether or not the  employee has received notification pay code edit |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| auditUserId | INT64 | person id for audit user (Note: column added in 7.3.3) |  |  |
| auditUserPersonNumber | STRING | person number for audit user (Note: column added in 7.3.3) | PII |  |
| auditUserName | STRING | person name for audit user (Note: column added in 7.3.3) | PII |  |
