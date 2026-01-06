# vUnpvtTimecardAudit

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtTimecardAudit |
| Unique Identifier | auditUniqueId |
| Source Pipeline | timecardAudit (DR) |

## Columns

**Column count:** 24

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Person ID for whom the audit was made |  |  |
| auditUniqueId | STRING | Unique Identifier for Timecard Audit |  |  |
| auditRevisionPersonId | INT64 | Person ID of the person who made the audit |  |  |
| auditPaycodeId | INT64 | ID of the paycode edit |  |  |
| auditTransferCostCenter | STRING | Transfer Cost Center Name (at the time of transaction) |  |  |
| auditTransferLaborEntryName1 | STRING | Transfer Labor Category Name 1 (at the time of transaction) |  |  |
| auditTransferLaborEntryName2 | STRING | Transfer Labor Category Name 2 (at the time of transaction) |  |  |
| auditTransferLaborEntryName3 | STRING | Transfer Labor Category Name 3 (at the time of transaction) |  |  |
| auditTransferLaborEntryName4 | STRING | Transfer Labor Category Name 4 (at the time of transaction) |  |  |
| auditTransferLaborEntryName5 | STRING | Transfer Labor Category Name 5 (at the time of transaction) |  |  |
| auditTransferLaborEntryName6 | STRING | Transfer Labor Category Name 6 (at the time of transaction) |  |  |
| paycodeCnt | INT64 | AuditType = paycode edit |  |  |
| managerApproveAddCnt | INT64 | Audit Type = manager approval and revision type = add |  |  |
| managerApproveDelCnt | INT64 | Audit Type = manager approval and revision type = delete |  |  |
| employeeApproveAddCnt | INT64 | Audit Type = employee approval and revision type = add |  |  |
| employeeApproveDelCnt | INT64 | Audit Type = employee approval and revision type = delete |  |  |
| approvalSwt | INT64 | Is the timecard approved |  |  |
| selfEditCnt | INT64 | Timecard edit by employee |  |  |
| managerEditCnt | INT64 | Timecard edit by manager |  |  |
| historicalCorrectionCnt | INT64 | Historical correction count |  |  |
| signOffAddCnt | INT64 | Audit Type = sign of and revision type = add |  |  |
| signOffDelCnt | INT64 | Audit Type = sign of and revision type = delete |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
