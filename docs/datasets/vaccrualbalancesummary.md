# vAccrualBalanceSummary

**Group:** Summary Dataset → Transactional Views

Containis the vested, probation, earned, granted, taken and planned accruals as of the balance date

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAccrualBalanceSummary |
| Unique Identifier | Date_BalanceAsOfDate,Person_personId,Acc_AccrualCodeId, CNCY_DisplayPreference |
| Source Pipeline | accrualBalance (DR) |

## Columns

**Column count:** 120

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| CNCY_DisplayPreference | STRING | a string value that contains that is used in where clause which shows the results in the desired currency |  |  |
| Date_BalanceAsOfDate | DATE | Accrual Balance as of Date |  |  |
| M_Acc_CurrentBalVested_Days | FLOAT | Vested refers to balances earned or otherwise accrued. Vested Balance Days as of the partitionDate. In this example if the partiotionDate is 8/22, Vested Days as of 8/22. |  |  |
| M_Acc_CurrentBalVested_Hrs | FLOAT | Vested Balance Hours as of the partitionDate. In this example if the partiotionDate is 8/22,  Vested hours as of 8/22. |  |  |
| M_Acc_CurrentBalVested_Amt | FLOAT | Vested Balance Amount as of the partitionDate. In this example if the partiotionDate is 8/22,  Vested amount as of 8/22. |  |  |
| M_Acc_CurrentBalProbation_Days | FLOAT | Accrued balances Days  for Probation type accrual code. Balances in Days |  |  |
| M_Acc_CurrentBalProbation_Hrs | FLOAT | Accrued balances hours for Probation type accrual code. Balances in Hours |  |  |
| M_Acc_CurrentBalProbation_Amt | FLOAT | Accrued balances  amounts for Probation type accrual code. Balances in Amounts |  |  |
| M_Acc_AvailableBal_Days | FLOAT | Balance or remainig days as of the partition date  In this example currentBalVestedDays as of 8/22,  minus the plannedTakingDays as 8/22 , minus the takingToDateDays as of 8/22. |  |  |
| M_Acc_AvailableBal_Hrs | FLOAT | Balance or remainig hours as of the partition date |  |  |
| M_Acc_AvailableBal_Amt | FLOAT | Balance or remainig amount as of the partition date |  |  |
| M_Acc_EarnedToDate_Days | FLOAT | The number of days earned as of the partitionDate. If using an  accrual policy which involves for example accruing vacation for every day or hour worked, then earned will be the days of vacation accrued as of the partitionDate |  |  |
| M_Acc_EarnedToDate_Hrs | FLOAT | The number of hours earned as of the partitionDate |  |  |
| M_Acc_EarnedToDate_Amt | FLOAT | The amount earned as of the partitionDate. |  |  |
| M_Acc_PendingGrant_Days | FLOAT | Days which will accrue after the partitionDate. For example vacation days earned after 8/22 are considered as Pending as of 8/22. |  |  |
| M_Acc_PendingGrant_Hrs | FLOAT | Hours which will accrue after the partitionDate. |  |  |
| M_Acc_PendingGrant_Amt | FLOAT | Amounts which will accrue after the partitionDate. |  |  |
| M_Acc_PlannedTaking_Days | FLOAT | Days scheduled to be taken or used after the current partition date. For example, vacation days that are  scheduled to be taken after current partion date, 8/22. These are considered to be planned but not yet taken. |  |  |
| M_Acc_PlannedTaking_Hrs | FLOAT | Hours scheduled to be taken or used after the current partition date. |  |  |
| M_Acc_PlannedTaking_Amt | FLOAT | Amounts scheduled to be taken or used after the current partition date. |  |  |
| M_Acc_TakingToDate_Days | FLOAT | Days already taken or used as of the current partition date. For example, vacation days before current partion date, 8/22. |  |  |
| M_Acc_TakingToDate_Hrs | FLOAT | Hours already taken or used as of the current partition date. |  |  |
| M_Acc_TakingToDate_Amt | FLOAT | Amounts already taken or used as of the current partition date. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| CC_CostCenter | STRING | Cost Center Name |  |  |
| Acc_AccrualCodeId | INT64 | The ID of an accrual code. |  |  |
| Acc_AccrualCode | STRING | The name of an accrual code. |  |  |
| Acc_ShortName | STRING | The short name of an accrual code. |  |  |
| Acc_TypeId | INT64 | The ID of an accrual code type. |  |  |
| Acc_TypeName | STRING | The name of an accrual code type. |  |  |
| Acc_HoursPerDayInSeconds | INT64 | The hours per day (in seconds) associated with an accrual code. |  |  |
| Acc_AllowEditSwt | BOOLEAN | A Boolean indicator of whether or not an accrual code is ediview. |  |  |
| Person_personId | INT64 | Person ID |  |  |
| Person_PersonNumber | STRING | Person Number | PII |  |
| Person_FullName | STRING | Full Name | PII |  |
| Person_IsEmployeeSwt | BOOLEAN | Boolean indicator whether or not this person is a employee |  |  |
| Person_IsManagerSwt | BOOLEAN | Boolean indicator whether or not this person is a manager |  |  |
| Person_HourlyRate | FLOAT | Hourly Rate | Confidential |  |
| Person_HireDate | DATE | Hire Date |  |  |
| Person_SeniorityDate | DATE | Seniority Date |  |  |
| Person_SupervisorPersonNumber | STRING | Supervisor Person Nunber | PII |  |
| Person_SupervisorFullName | STRING | Supervisor Name | PII |  |
| Person_EmploymentTerm | STRING | Employment Term |  |  |
| Person_WorkerType | STRING | Worker Type |  |  |
| Person_ExpectedDailyHours | FLOAT | Expected Daily Hours |  |  |
| Person_PrimaryLaborCategory | STRING | PRO External Identifier |  |  |
| Person_PrimaryLaborEntryName1 | STRING | Primary Labor Category |  |  |
| Person_PrimaryLaborEntryName2 | STRING | Primary Labor Entry Name 1 |  |  |
| Person_PrimaryLaborEntryName3 | STRING | Primary Labor Entry Name 2 |  |  |
| Person_PrimaryLaborEntryName4 | STRING | Primary Labor Entry Name 3 |  |  |
| Person_PrimaryLaborEntryName5 | STRING | Primary Labor Entry Name 4 |  |  |
| Person_PrimaryLaborEntryName6 | STRING | Primary Labor Entry Name 5 |  |  |
| Person_primaryOrgPathTxt | STRING | Primary Labor Entry Name 6 |  |  |
| Person_employmentStatus | STRING | Employment Status |  |  |
| Person_timeEntryType | STRING | Time entry type |  |  |
| Person_shiftCode | STRING | Shift Code |  |  |
| Person_birthDate | DATE | Birth date | Confidential |  |
| Person_fullTimeStandardHoursQuantity | FLOAT | FT Standard Hours Qty |  |  |
| Person_FullTimeEquivalencyPercent | FLOAT | FTE Percent |  |  |
| Person_ProExternalId | STRING | Primary Org Path |  |  |
| Person_contactData | STRING | Contact information | PII |  |
| Person_zipCode | STRING | Zip Code | PII |  |
| Person_state | STRING | State | PII |  |
| Person_city | STRING | City | PII |  |
| Person_country | STRING | Country | PII |  |
| BusPri_primaryOrgId | INT64 | Primary Org Id |  |  |
| BusPri_PrimaryOrgName | STRING | Primary Org Name |  |  |
| BusPri_primaryOrgFullName | STRING | Primary Org Full Name |  |  |
| BusPri_primaryOrgDescription | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak0 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak1 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak2 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak3 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak4 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak5 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak6 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak7 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak8 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak9 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak10 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak11 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak12 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak13 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak14 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak15 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak16 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak17 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak18 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak19 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| BusPri_primaryOrgBreak20 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Person_CustomText1 | STRING | Custom Text | PII |  |
| Person_CustomText2 | STRING | Custom Text | PII |  |
| Person_CustomText3 | STRING | Custom Text | PII |  |
| Person_CustomText4 | STRING | Custom Text | PII |  |
| Person_CustomText5 | STRING | Custom Text | PII |  |
| Person_CustomText6 | STRING | Custom Text | PII |  |
| Person_CustomText7 | STRING | Custom Text | PII |  |
| Person_CustomText8 | STRING | Custom Text | PII |  |
| Person_CustomText9 | STRING | Custom Text | PII |  |
| Person_CustomText10 | STRING | Custom Text | PII |  |
| Person_CustomText11 | STRING | Custom Text | PII |  |
| Person_CustomText12 | STRING | Custom Text | PII |  |
| Person_CustomText13 | STRING | Custom Text | PII |  |
| Person_CustomText14 | STRING | Custom Text | PII |  |
| Person_CustomText15 | STRING | Custom Text | PII |  |
| Person_CustomText16 | STRING | Custom Text | PII |  |
| Person_CustomText17 | STRING | Custom Text | PII |  |
| Person_CustomText18 | STRING | Custom Text | PII |  |
| Person_CustomText19 | STRING | Custom Text | PII |  |
| Person_CustomText20 | STRING | Custom Text | PII |  |
| Person_CustomText21 | STRING | Custom Text | PII |  |
| Person_CustomText22 | STRING | Custom Text | PII |  |
| Person_CustomText23 | STRING | Custom Text | PII |  |
| Person_CustomText24 | STRING | Custom Text | PII |  |
| Person_CustomText25 | STRING | Custom Text | PII |  |
| Person_CustomText26 | STRING | Custom Text | PII |  |
| Person_CustomText27 | STRING | Custom Text | PII |  |
| Person_CustomText28 | STRING | Custom Text | PII |  |
| Person_CustomText29 | STRING | Custom Text | PII |  |
| Person_CustomText30 | STRING | Custom Text | PII |  |
