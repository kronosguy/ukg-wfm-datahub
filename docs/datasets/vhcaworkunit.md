# vHcaWorkUnit

**Group:** Detail Dataset → Healthcare Productivity

One row for each work unit.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaWorkUnit |
| Unique Identifier | workUnitId |
| Source Pipeline | hcaWorkUnits (CDC) |

## Columns

**Column count:** 14

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| workUnitId | INT64 | The ID of the work unit |  |  |
| workUnitCode | STRING | Work Unit Code |  |  |
| workUnitName | STRING | Work Unit Name |  |  |
| caregiverSwt | INT64 | Work Unit Caregiver Switch |  |  |
| workWeekFTEHours | FLOAT | FTE Hours in Work Week |  |  |
| serviceLine | STRING | Work Unit Service Line |  |  |
| unitOfService | STRING | Work Unit Unit of Service |  |  |
| payRuleId | INT64 | The ID of a pay rule join with vPayRules |  |  |
| payRuleName | STRING | Pay Rule Name |  |  |
| workUnitTypeId | INT64 | The ID of the work unit type |  |  |
| workUnitTypeName | STRING | Work Unit Type Name |  |  |
| workGroupId | INT64 | The ID of the work group |  |  |
| workGroupName | STRING | Work Group Name |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
