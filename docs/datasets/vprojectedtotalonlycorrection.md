# vProjectedTotalOnlyCorrection

**Group:** Detail Dataset → Totals Detail Views

- Same as projectedTotal, but only INCLUDES the "Historical Corrections"

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vProjectedTotalOnlyCorrection |
| Unique Identifier | personId,partitionDate, signedOffSwt, amountType (nullable), wages (nullable), hoursAmount (nullable), daysAmount (nullable), combined pay codeswt (nullable), payCode (nullable), payCodeId (nullable), wageMultiplier (nullable), payPeriodWeek (nullable), payPeriodNumber (nullable), , laborTransferSwt, wageAddition, orgTransferSwt, orgId, isFromCorrectionSwt, costCenterId (nullable), uniqueId, laborEntryName1 (nullable), laborEntryName2 (nullable), laborEntryName3 (nullable), laborEntryName4 (nullable), laborEntryName5 (nullable), laborEntryName6 (nullable), laborEntryDesc1 (nullable), laborEntryDesc2 (nullable), laborEntryDesc3 (nullable), laborEntryDesc4 (nullable), laborEntryDesc5 (nullable), laborEntryDesc6 (nullable),updateDtm, costCenter (nullable) |
| Source Pipeline | timecardMetrics (CDC) |

## Columns

**Column count:** 42

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| signedOffSwt | BOOLEAN | Indicates that timecard is signed off for the date of the transaction ** Do Not Use this value is not available or inaccurate ** |  |  |
| amountType | STRING | Indicates if the pay code unit type of the amount paid was hours, money, or days |  |  |
| wages | FLOAT64 | Wage amount for totalized transaction |  |  |
| wagesCurrencyCode | STRING | Wages Currency Code |  |  |
| hoursAmount | FLOAT64 | Hours amount for totalized transaction |  |  |
| daysAmount | FLOAT64 | Days amount for totalized transaction |  |  |
| combined pay codeswt | BOOLEAN | Indicates if amount is associated with a combined pay code |  |  |
| payCode | STRING | Name of the pay code transactions are charged to - joins to pay code dimension |  |  |
| payCodeId | INT64 | Unique identifier of a pay code. Joins to pay code dimension |  |  |
| wageMultiplier | FLOAT64 | Indicates pay code multiplier of hours times base wage - 1 is regular, 1.5 is premium pay, etc |  |  |
| payPeriodWeek | INT64 | ** Do Not Use this value is not available or inaccurate ** |  |  |
| payPeriodNumber | INT64 | ** Do Not Use this value is not available or inaccurate ** |  |  |
| laborTransferSwt | BOOLEAN | Indicates if the transaction has a labortransfer |  |  |
| wageAddition | FLOAT64 | Pay code wage addition amount |  |  |
| orgTransferSwt | BOOLEAN | Indicates if transaction has a business structure transfer |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| isFromCorrectionSwt | BOOLEAN | Indicates if the transaction is from a historical correction Note: this value is not consistent for combined pay codes |  |  |
| costCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension |  |  |
| uniqueId | STRING | Unique Identifier |  |  |
| assignmentId | INT64 |  |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc1 | STRING | Labor Category 1 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName2 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc2 | STRING | Labor Category 2 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName3 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc3 | STRING | Labor Category 3 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName4 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc4 | STRING | Labor Category 4 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName5 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc5 | STRING | Labor Category 5 entry description associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName6 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) Note: after DH Release 8.1 only view will have this value |  |  |
| laborEntryDesc6 | STRING | Labor Category 6 entry description associated with transaction (applies to labor category transfer) |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| costCenter | STRING | Cost Center name |  |  |
| laborEntryOrdinal1 | INT64 | labor category entry ordinal position 1 |  |  |
| laborEntryOrdinal2 | INT64 | labor category entry ordinal position 2 |  |  |
| laborEntryOrdinal3 | INT64 | labor category entry ordinal position 3 |  |  |
| laborEntryOrdinal4 | INT64 | labor category entry ordinal position 4 |  |  |
| laborEntryOrdinal5 | INT64 | labor category entry ordinal position 5 |  |  |
| laborEntryOrdinal6 | INT64 | labor category entry ordinal position 6 |  |  |
