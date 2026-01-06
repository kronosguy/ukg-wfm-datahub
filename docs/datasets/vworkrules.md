# vWorkRules

**Group:** Detail Dataset → Timekeeping Setup

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vWorkRules |
| Unique Identifier | workRuleId |
| Source Pipeline | workRules (DR) |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| workRuleId | INT64 | Work Rule ID |  |  |
| workRule | STRING | Work Rule Name |  |  |
| effectiveWorkRuleId | INT64 | Effective date work rule id |  |  |
| effectiveDateTime | TIMESTAMP | Effective Date Time |  |  |
| expirationDateTime | TIMESTAMP | Expiration Date Time |  |  |
| deniedPayCodeId | INT64 | Denied paycode id |  |  |
| unapprovedPayCodeId | INT64 | Non approved paycode id |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
