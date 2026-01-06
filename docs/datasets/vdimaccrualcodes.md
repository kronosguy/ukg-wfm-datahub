# vDimAccrualCodes

**Group:** Summary Dataset → Dimension Views

Contains a list of accrual code types

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vDimAccrualCodes |
| Unique Identifier | Acc_AccrualCodeId |
| Source Pipeline |  |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| Acc_AccrualCodeId | INT64 | The ID of an accrual code. |  |  |
| Acc_AccrualCode | STRING | The name of an accrual code. |  |  |
| Acc_ShortName | STRING | The short name of an accrual code. |  |  |
| Acc_TypeId | INT64 | The ID of an accrual code type. |  |  |
| Acc_TypeName | STRING | The name of an accrual code type. |  |  |
| Acc_HoursPerDayInSeconds | INT64 | The hours per day (in seconds) associated with an accrual code. |  |  |
| Acc_AllowEditSwt | BOOLEAN | A Boolean indicator of whether or not an accrual code is ediview. |  |  |
