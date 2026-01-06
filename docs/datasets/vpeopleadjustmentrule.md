# vPeopleAdjustmentRule

**Group:** Detail Dataset → People Detail Views

Captures Effective Dated Adjustment Rule assigned to person record

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleAdjustmentRule |
| Unique Identifier | personId,adjustmentRuleId,effectiveDate,expirationDate |
| Source Pipeline | peopleAdjustmentRule (CDC) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| adjustmentRuleId | INT64 | Unique Identifier for Adjustment Rule |  |  |
| adjustmentRule | STRING | Adjustment Rule Description |  |  |
| personId | INT64 | Primary Key  - Should be used for all joins to detail fact Views. Not the Person Id in Dimensions |  |  |
| effectiveDate | DATE | Effective Date |  |  |
| expirationDate | DATE | Expiration Date |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
