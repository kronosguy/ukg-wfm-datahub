# vKronosIntraSummary_User

**Group:** Summary Dataset → Traffic Pattern Volume Forecast (M_TrafPatVolFcst)

Same as vKronosIntraSummary. plus row level security driven by users email address

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vKronosIntraSummary_User |
| Unique Identifier |  |
| Source Pipeline |  |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| emailAddress | STRING | Employee's email address | PII |  |
| employeeGroupId | INT64 | Employee Group ID  join to vEmployeeGroups |  |  |
| employeeGroupName | STRING | Employee Group Name |  |  |
| locationSetName | STRING | The name of the location set |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| proExternalId | STRING | Pro external identifier |  |  |
| userCurrencyDisplayPreference | STRING | - the default currency as defined in Dimensions for the employee |  |  |
