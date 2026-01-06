# vPayCodeMapping

**Group:** Detail Dataset → Pay Code/Period Detail Views

- Imported Mapping of paycodes to pay categories.  Used in summary level Views.  Must be imported using the standard process and requires it is kept up to date when new paycodes are added.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPayCodeMapping |
| Unique Identifier | payCodeId |
| Source Pipeline | Sourced from Config Portal (DR) |

## Columns

**Column count:** 25

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| payCodeId | INT64 | Unique identifier of a pay code. Joins to pay code dimension |  |  |
| payCodeName | STRING | Pay code name |  |  |
| payCodeType | STRING | Pay code type i.e. Regular, Combined, Duration etc. |  |  |
| payCategory | STRING | Pay Category i.e. Regular, Overtime, Absence or Other |  |  |
| absenceCategory | STRING | Planned or Unplanned Absence |  |  |
| isCoreSwt | BOOLEAN | A Boolean indicator of whether or not the pay code is Core |  |  |
| isProductiveSwt | BOOLEAN | A Boolean indicator of whether or not the pay code is Productive |  |  |
| isPaidSwt | BOOLEAN | A Boolean indicator of whether or not the pay code is Paid |  |  |
| isOTNetDownSwt | BOOLEAN | A Boolean indicator of whether or not the pay code is Net Down Overtime |  |  |
| isTrainingSwt | BOOLEAN | A Boolean indicator of whether or not the pay code is Training |  |  |
| isMealPenalty | BOOLEAN | A Boolean indicator of whether or not the pay code is Meal Penalty |  |  |
| isHoliday | BOOLEAN | A Boolean indicator of whether or not the pay code is Holiday |  |  |
| isOnCall | BOOLEAN | A Boolean indicator of whether or not the pay code is On Call |  |  |
| isCallBack | BOOLEAN | A Boolean indicator of whether or not the pay code is Callback |  |  |
| userDefined1 | STRING | User defined field |  |  |
| userDefined2 | STRING | User defined field |  |  |
| userDefined3 | STRING | User defined field |  |  |
| userDefined4 | STRING | User defined field |  |  |
| userDefined5 | STRING | User defined field |  |  |
| userDefined6 | STRING | User defined field |  |  |
| userDefined7 | STRING | User defined field |  |  |
| userDefined8 | STRING | User defined field |  |  |
| userDefined9 | STRING | User defined field |  |  |
| userDefined10 | STRING | User defined field |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
