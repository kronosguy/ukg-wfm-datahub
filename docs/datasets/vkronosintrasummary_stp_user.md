# vKronosIntraSummary_STP_User

**Group:** Summary Dataset → Traffic Pattern Volume Forecast (M_TrafPatVolFcst)

Same as vKronosIntraSummary_STP. plus row level security driven by users email address

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vKronosIntraSummary_STP_User |
| Unique Identifier |  |
| Source Pipeline |  |

## Columns

**Column count:** 10

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| STPName | STRING | Symbolic Time Period Name |  |  |
| STPDates | DATE | Symbolic Time Period Date |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| emailAddress | STRING | Employee's email address | PII |  |
| employeeGroupId | INT64 | Employee Group ID  join to vEmployeeGroups |  |  |
| employeeGroupName | STRING | Employee Group Name |  |  |
| locationSetName | STRING | The name of the location set |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| proExternalId | STRING | Pro external identifier |  |  |
| userCurrencyDisplayPreference | STRING | - the default currency as defined in Dimensions for the employee |  |  |
