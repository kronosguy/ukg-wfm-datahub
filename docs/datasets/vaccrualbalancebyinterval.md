# vAccrualBalanceByInterval

**Group:** Detail Dataset → Accrual Detail Views

Containis the vested, probation, earned, granted, taken and planned accruals as of the balance date

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAccrualBalanceByInterval |
| Unique Identifier | partitionDate,uniqueId |
| Source Pipeline | accrualBalance (DR) |

## Columns

**Column count:** 28

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Depending on the INTERVAL selected the partition date could be weekly, monthly or pay period end date. This is "as of a specific date." Note : Only one value is permitted. The available options are:   "Weekly-Monday",   "Weekly-Tuesday",   "Weekly-Wednesday",   "Weekly-Thursday",   "Weekly-Friday",   "Weekly-Saturday",   "Weekly-Sunday",   "Monthly-Begin",   "Monthly-End",   "Pay-Period-End" For example, if "Weekly-Monday", is selected, the partitionDate will reference any date that falls on a Monday. This is date as of which all the other metrics and attributes in this view are calculated. |  |  |
| personId | INT64 | Person Identifier |  |  |
| accrualCodeId | INT64 | Accrual Code Identifier |  |  |
| currencyCode | STRING | Currency code for the amounts . Currency code for the current, probation, planned, pending, taking, earned or available amounts. |  |  |
| currentBalVestedDays | FLOAT | Vested refers to balances earned or otherwise accrued. Vested Balance Days as of the partitionDate. In this example if the partiotionDate is 8/22, Vested Days as of 8/22. |  |  |
| currentBalVestedHrs | FLOAT | Vested Balance Hours as of the partitionDate. In this example if the partiotionDate is 8/22,  Vested hours as of 8/22. |  |  |
| currentBalVestedAmt | FLOAT | Vested Balance Amount as of the partitionDate. In this example if the partiotionDate is 8/22,  Vested amount as of 8/22. |  |  |
| currentBalProbationDays | FLOAT | Accrued balances Days  for Probation type accrual code. Balances in Days |  |  |
| currentBalProbationHrs | FLOAT | Accrued balances hours for Probation type accrual code. Balances in Hours |  |  |
| currentBalProbationAmt | FLOAT | Accrued balances  amounts for Probation type accrual code. Balances in Amounts |  |  |
| availableBalDays | FLOAT | Balance or remainig days as of the partition date  In this example currentBalVestedDays as of 8/22,  minus the plannedTakingDays as 8/22 , minus the takingToDateDays as of 8/22. |  |  |
| availableBalHrs | FLOAT | Balance or remainig hours as of the partition date |  |  |
| availableBalAmt | FLOAT | Balance or remainig amount as of the partition date |  |  |
| earnedToDateDays | FLOAT | The number of days earned as of the partitionDate. If using an  accrual policy which involves for example accruing vacation for every day or hour worked, then earned will be the days of vacation accrued as of the partitionDate |  |  |
| earnedToDateHrs | FLOAT | The number of hours earned as of the partitionDate |  |  |
| earnedToDateAmt | FLOAT | The amount earned as of the partitionDate. |  |  |
| pendingGrantDays | FLOAT | Days which will accrue after the partitionDate. For example vacation days earned after 8/22 are considered as Pending as of 8/22. |  |  |
| pendingGrantHrs | FLOAT | Hours which will accrue after the partitionDate. |  |  |
| pendingGrantAmt | FLOAT | Amounts which will accrue after the partitionDate. |  |  |
| plannedTakingDays | FLOAT | Days scheduled to be taken or used after the current partition date. For example, vacation days that are  scheduled to be taken after current partion date, 8/22. These are considered to be planned but not yet taken. |  |  |
| plannedTakingHrs | FLOAT | Hours scheduled to be taken or used after the current partition date. |  |  |
| plannedTakingAmt | FLOAT | Amounts scheduled to be taken or used after the current partition date. |  |  |
| takingToDateDays | FLOAT | Days already taken or used as of the current partition date. For example, vacation days before current partion date, 8/22. |  |  |
| takingToDateHrs | FLOAT | Hours already taken or used as of the current partition date. |  |  |
| takingToDateAmt | FLOAT | Amounts already taken or used as of the current partition date. |  |  |
| uniqueId | STRING | Concatenation of Employee ID and Accrual Code. This will uniquely identify each record |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| accrualCode | STRING | The name of an accrual code. |  |  |
