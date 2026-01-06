# vAccrualTransaction

**Group:** Detail Dataset → Accrual Detail Views

- Raw Accrual Transactions (Grants/Takings/Adjustments, etc).

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAccrualTransaction |
| Unique Identifier | accrualTransId |
| Source Pipeline | accrualTransaction (DR) |

## Columns

**Column count:** 69

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| originalDate | DATE | The original date of the accrual transaction. |  |  |
| endDate | DATE | The end date of the accrual transaction. |  |  |
| accrualCode | STRING | The AccrualCode object associated with the accrual transaction data. |  |  |
| typeStr | STRING | A string associated with the type of accrual transaction. |  |  |
| accrualCodeLanguage | STRING | Accrual code Language |  |  |
| accrualCodeId | INT64 | Accrual code ID |  |  |
| accrualCodeCountry | STRING | Accrual code Country |  |  |
| hoursAmount | FLOAT64 | Hours amount for totalized transaction |  |  |
| moneyAmount | FLOAT64 | The money amount of the accrual transaction. |  |  |
| daysAmount | FLOAT64 | Days amount for totalized transaction |  |  |
| originalHoursAmount | FLOAT64 | The original amount (in hours) of the accrual transaction. |  |  |
| originalMoneyAmount | FLOAT64 | The original money amount of the accrual transaction. |  |  |
| originalDaysAmount | FLOAT64 | The original amount (in days) of the accrual transaction. |  |  |
| grantHoursAmount | FLOAT64 | The grant amount (in hours) of the accrual transaction. |  |  |
| grantMoneyAmount | FLOAT64 | The grant money amount of the accrual transaction. |  |  |
| grantDaysAmount | FLOAT64 | The grant amount (in days) of the accrual transaction. |  |  |
| limitHoursAmount | FLOAT64 | The limit amount (in hours) of the accrual transaction. |  |  |
| limitMoneyAmount | FLOAT64 | The limit money amount of the accrual transaction. |  |  |
| limitDaysAmount | FLOAT64 | The limit amount (in days) of the accrual transaction. |  |  |
| carryForwardHoursAmount | FLOAT64 | The carry forward amount (in hours) of the accrual transaction. |  |  |
| carryForwardMoneyAmount | FLOAT64 | The carry forward money amount of the accrual transaction. |  |  |
| carryForwardDaysAmount | FLOAT64 | The carry forward amount (in days) of the accrual transaction. |  |  |
| probationHoursAmount | FLOAT64 | The probation amount (in hours) of the accrual transaction. |  |  |
| probationMoneyAmount | FLOAT64 | The probation money amount of the accrual transaction. |  |  |
| probationDaysAmount | FLOAT64 | The probation amount (in days) of the accrual transaction. |  |  |
| enteredOnDateTime | TIMESTAMP | The date and time the accrual transaction was entered. |  |  |
| updateDatetm | TIMESTAMP | The date and time of the update made to the accrual transaction. |  |  |
| type | STRING | The type of accrual transaction. i.e. "TAKEN", "GRANT", "ACCRUAL_RESET" |  |  |
| excluded | BOOLEAN | A Boolean indicator of whether or not the accrual transaction is excluded. |  |  |
| disqualified | BOOLEAN | A Boolean indicator of whether or not the accrual transaction is disqualified. |  |  |
| onProbation | BOOLEAN | A Boolean indicator of whether or not the accrual transaction is probationary. |  |  |
| suspended | BOOLEAN | A Boolean indicator of whether or not the accrual transaction is suspended. |  |  |
| fromTransition | BOOLEAN | A Boolean indicator of whether or not the accrual transaction is from transition. |  |  |
| spcededByReset | BOOLEAN | ** Do Not Use this value is not available or inaccurate ** A Boolean indicator of whether or not the accrual transaction is spcededbyreset. |  |  |
| accrualCodeAmountType | STRING | The amount type of the accrual code in this transaction. |  |  |
| editedBy | STRING | A reference to the person who updated the accrual transaction. | PII |  |
| editedById | INT64 | Edited by personId |  |  |
| dataSource | STRING | A reference to the data source, if one exists. Normally, this indicates that the context object came from a different source, such as a clock, device, or an external data source such as an import or interface. |  |  |
| dataSourceId | INT64 | Data source ID |  |  |
| oldFTEAmt | FLOAT64 | The old FTE amount of this accrual transaction. |  |  |
| newFTEAmt | FLOAT64 | The new FTE amount of this accrual transaction. |  |  |
| payCodeCombined | BOOLEAN | A Boolean indicator of whether or not the accrual transaction is a combined paycode. |  |  |
| payCodeExcusedAbsence | BOOLEAN | A Boolean indicator of whether or not the accrual transaction is a excused absence. |  |  |
| payCodeName | STRING | Pay code name |  |  |
| payCodeAddToTimecardTotal | INT64 | Pay code added to Timecard Total |  |  |
| payCodeWageAddition | FLOAT64 | Pay code wage addition amount |  |  |
| payCodeVisibleToUser | INT64 | Pay code visible to user |  |  |
| payCodeWageMultiplier | FLOAT64 | Indicates pay code multiplier of hours times base wage - 1 is regular, 1.5 is premium pay, etc |  |  |
| payCodeVisibleToTCSched | INT64 | Pay code visible to schedule total |  |  |
| payCodeEffectiveDate | DATE | Effective date of Pay Code |  |  |
| payCodeMoney | BOOLEAN | A Boolean indicator of whether or not the accrual transaction is money. |  |  |
| payCodeScheduleHoursType | STRING | Pay code scheduled hours type |  |  |
| payCodeVisibleToReports | INT64 | Pay code visible in Reports |  |  |
| payCodeType | STRING | Pay code type |  |  |
| payCodeId | INT64 | Pay code ID |  |  |
| payCodeTotals | BOOL | A Boolean indicator of whether or not the pay code is in totals |  |  |
| payCodeCheckAvailability | INT64 | Paycode Check Availability |  |  |
| payCodeShortName | STRING | Pay Code Short Name |  |  |
| payCodeAmountType | STRING | Pay Code Amount Type |  |  |
| toAccrualCode | STRING | Accrual Code |  |  |
| toAccrualCodeLanguage | STRING | Accrual Code Language |  |  |
| toAccrualCodeId | INT64 | Accrual Code ID |  |  |
| toAccrualCodeCountry | STRING | Accrual Code Country |  |  |
| toPersonId | INT64 | Person Id |  |  |
| accrualTransId | STRING | Accrual Transaction ID |  |  |
| systemGeneratedNum | INT64 | The system generated INT64 of this accrual transaction. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
