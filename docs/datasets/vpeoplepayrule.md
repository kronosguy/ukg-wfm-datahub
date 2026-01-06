# vPeoplePayRule

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Payrule Assignments

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeoplePayRule |
| Unique Identifier | personId,payRuleId,payRuleAssignmentId,effectiveDate,expirationDate |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 9

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| workRuleName | STRING | Work Rule Name |  |  |
| payRuleName | STRING | Pay rule name |  |  |
| workRuleId | INT64 | Work Rule ID |  |  |
| payRuleAssignmentId | INT64 | Pay rule assignment ID |  |  |
| payRuleId | INT64 | Pay rule ID |  |  |
| expirationDate | DATE | Pay rule assignment expiration date |  |  |
| effectiveDate | DATE | Pay rule assignment effective date |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
