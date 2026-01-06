# vDimPeople

**Group:** Summary Dataset → Dimension Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vDimPeople |
| Unique Identifier | Person_personId |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 88

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
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
| Person_ProExternalId | INT64 | PRO External Identifier |  |  |
| Person_PrimaryLaborCategory | STRING | Primary Labor Category |  |  |
| Person_PrimaryLaborEntryName1 | STRING | Primary Labor Entry Name 1 |  |  |
| Person_PrimaryLaborEntryName2 | STRING | Primary Labor Entry Name 2 |  |  |
| Person_PrimaryLaborEntryName3 | STRING | Primary Labor Entry Name 3 |  |  |
| Person_PrimaryLaborEntryName4 | STRING | Primary Labor Entry Name 4 |  |  |
| Person_PrimaryLaborEntryName5 | STRING | Primary Labor Entry Name 5 |  |  |
| Person_PrimaryLaborEntryName6 | STRING | Primary Labor Entry Name 6 |  |  |
| Person_employmentStatus | STRING | Employment Status |  |  |
| Person_timeEntryType | STRING | Time entry type |  |  |
| Person_shiftCode | STRING | Shift Code |  |  |
| Person_birthDate | DATE | Birth date | Confidential |  |
| Person_fullTimeStandardHoursQuantity | FLOAT | FT Standard Hours Qty |  |  |
| Person_FullTimeEquivalencyPercent | FLOAT | FTE Percent |  |  |
| Person_primaryOrgPathTxt | STRING | Primary Org Path |  |  |
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
