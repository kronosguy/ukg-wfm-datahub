# vPayRulesHoliday

**Group:** Detail Dataset → Timekeeping Setup

- A list of holidays that give holiday credits to the employees who are assigned to this pay rule.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPayRulesHoliday |
| Unique Identifier | payRuleId,ifnull(holidayName,"") |
| Source Pipeline | payRules (DR) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| payRuleId | INT64 | The ID of a pay rule join with vPayRules |  |  |
| holidaySelectedSwt | BOOLEAN | A Boolean indicator of whether or not the holiday indicated by holidayname is selected for this pay rule |  |  |
| holidayId | INT64 | The id of the associated holiday. |  |  |
| holidayName | STRING | The name of the associated holiday. |  |  |
| creditRulesId | INT64 | Credit Rule Id |  |  |
| creditRulesName | STRING | The names of one or more holiday credit rules associated with the pay rule. |  |  |
