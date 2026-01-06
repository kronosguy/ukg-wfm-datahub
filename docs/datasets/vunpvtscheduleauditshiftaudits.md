# vUnpvtScheduleAuditShiftAudits

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtScheduleAuditShiftAudits |
| Unique Identifier | partitionDate,orgId,personId |
| Source Pipeline | scheduleAudit (CDC) |

## Columns

**Column count:** 26

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| costCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName2 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName3 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName4 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName5 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName6 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) |  |  |
| shiftAuditCnt | INT64 | Count distinct where shift audit type = "Update" and deleted_swt = False |  |  |
| shiftAuditCntBeforePost | INT64 | Count distinct of shift audit revisions where posted switch is false |  |  |
| shiftAuditCntAfterPost | INT64 | Count distinct of shift audit revisions where posted switch is true |  |  |
| shiftAuditInsertCnt | INT64 | Count distinct where shift audit type = "Insert" |  |  |
| shiftAuditDeleteCnt | INT64 | Count distinct where shift deleted_swt = True |  |  |
| shiftAuditChangeCnt | INT64 | Count distinct where shift audit type = "Update" and deleted_swt = False |  |  |
| shiftAuditRetroCnt | INT64 | Count distinct where AuditLocalTimestamp > ShiftStartDTM. |  |  |
| shiftAuditNoticeVioltnCnt | INT64 | Count distinct of shift audits whereViolation DTM > AuditLocalTimestamp  > ShiftStartDTM     (Offset from start of shift) i.e. Setting = 2hrs Shift 8am to 5pm Count only where AuditLocalTimestamp   is between 6am and 8am |  |  |
| schdShiftCnt | INT64 | Count distinct of scheduled shifts |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| laborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
