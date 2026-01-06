# vScheduleAuditShiftAuditsSegments

**Group:** Detail Dataset → Audit Detail Views

The list of segments of this availability ordered by start time.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleAuditShiftAuditsSegments |
| Unique Identifier | shiftId,shiftSegmentID,partitionDate,revisionId |
| Source Pipeline | scheduleAudit (CDC) |

## Columns

**Column count:** 58

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| shiftId | INT64 | The shift id (shiftId is used for the Shift Audit Counts) |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension personId for the employee who's schedule changed |  |  |
| auditLocalTimestamp | TIMESTAMP | The date and time that the revision was made in the Data Hub Integration user's home time zone. |  |  |
| auditTimestamp | TIMESTAMP | The date and time that the revision was made in Greenwich Mean Time (GMT). |  |  |
| auditType | STRING | The type of Audit Insert or Update |  |  |
| auditUser | STRING | The full name of the user who made the revision. | PII |  |
| revisionId | INT64 | The id of the this revision/audit record. |  |  |
| shiftSegmentId | INT64 | The shift segment id |  |  |
| startDateTime | TIMESTAMP | Shift Start Date Time |  |  |
| endDateTime | TIMESTAMP | Shift End Date Time |  |  |
| primaryWorkRule | STRING | Primary work rule name |  |  |
| primaryWorkRuleId | INT64 | Primary work rule id |  |  |
| primaryOrgId | INT64 | Unique identifier of Primary Business Structure location of the employee associated with the transaction - Joins to Business Structure dimensions |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| workRule | STRING | Work rule associated with this audit |  |  |
| workRuleId | INT64 | Work rule ID |  |  |
| shiftSegmentType | STRING | The type of the shift segment |  |  |
| shiftSegmentTypeId | INT64 | The ID of the shift segment type |  |  |
| segmentType | STRING | The segment type |  |  |
| segmentTypeId | INT64 | The segment type ID |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
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
| userEnteredLaborEntryName1 | STRING | Labor Category 1 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName2 | STRING | Labor Category 2 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName3 | STRING | Labor Category 3 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName4 | STRING | Labor Category 4 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName5 | STRING | Labor Category 5 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName6 | STRING | Labor Category 6 entry name associated with transaction  Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| userEnteredLaborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| primaryCostCenter | STRING | Primary cost center for employee associated with transaction |  |  |
| primaryCostCenterId | INT64 | Primary cost center ID - joins to cost center dimension |  |  |
| costCenter | STRING | Cost Center name |  |  |
| costCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension |  |  |
| transferOrgIdSwt | BOOLEAN | A Boolean indicator of whether or not the org job is transferred. |  |  |
| transferOrgString | STRING | An ordered, semi-colon separated list of Labor Category Entries and Cost Center. |  |  |
| userEnteredCostCenterSwt | BOOLEAN | A Boolean indicator of whether or not the cost center was entered by the user. |  |  |
| transferLaborCategoriesSwt | BOOLEAN | A Boolean indicator of whether or not the labor category is a transfer. |  |  |
| transferWorkruleSwt | BOOLEAN | A Boolean indicator of whether or not the work rule is a transfer. |  |  |
| userEnteredWorkruleSwt | BOOLEAN | A Boolean indicator of whether or not a work rule for this shift segment was entered by the user. |  |  |
| transferCostCenterSwt | BOOLEAN | A Boolean indicator of whether or not there is a transfer cost center for this shift segment. |  |  |
| userEnteredOrgSwt | BOOLEAN | A Boolean indicator of whether or not a business structure job was entered by the user. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
