# vTimecardHistoricalCorrection

**Group:** Detail Dataset → Timecard Detail Views

- Historical Corrections(not the resulting totals)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTimecardHistoricalCorrection |
| Unique Identifier | historicalCorrectionId |
| Source Pipeline | timecard (CDC) |

## Columns

**Column count:** 32

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| historicalCorrectionId | INT64 | The ID of the historical correction. |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension The date to which a historical correction applies in |  |  |
| originalDate | DATE | The historical date of the historical correction in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| workRule | STRING | The work rule associated with a timestamp context. |  |  |
| workRuleId | INT64 | The work rule ID |  |  |
| includeInTotalsSwt | BOOLEAN | Specifies whether the total for the historical correction is included for the apply date. |  |  |
| isPendingSwt | BOOLEAN | A Boolean indicator of whether or not the historical correction is in a pending (not saved) state. |  |  |
| isAgedSwt | BOOLEAN | A Boolean indicator of whether or not the apply date of the historical correction is on or before the signoff through date. |  |  |
| durationInHours | FLOAT64 | The duration (in hours) after the historical correction. |  |  |
| durationInDays | FLOAT64 | The duration (in days) after the historical correction. |  |  |
| wages | FLOAT64 | The wage amount (as a decimal value representing money) of the historical correction. |  |  |
| moneyAmount | FLOAT64 | The amount (as a decimal value representing money) of the historical correction. |  |  |
| originalMoneyAmount | FLOAT64 | The amount (as a decimal value representing money) prior to the historical correction. |  |  |
| originalDurationInHours | FLOAT64 | The duration (in hours) prior to the historical correction. |  |  |
| originalDurationInDays | FLOAT64 | The duration (in days) prior to the historical correction. |  |  |
| dataSource | STRING | A reference to the data source, if one exists, related to a historical correction. |  |  |
| dataSourceId | INT64 | Data source ID |  |  |
| payCode | STRING | Name of the pay code transactions are charged to - joins to pay code dimension |  |  |
| payCodeId | INT64 | Unique identifier of a pay code. Joins to pay code dimension |  |  |
| wagePayCode | STRING | A reference to the wage pay code associated with a historical correction. |  |  |
| wagePayCodeId | INT64 | Unique identifier of a pay code. Joins to pay code dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| costCenter | STRING | Cost Center name |  |  |
| costCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension |  |  |
| userEnteredLaborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName2 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName3 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName4 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName5 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| userEnteredLaborEntryName6 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
