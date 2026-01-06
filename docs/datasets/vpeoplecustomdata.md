# vPeopleCustomData

**Group:** Detail Dataset → People Detail Views

- Non-Effective Dated - Custom Data Fields as seen on "Additional Information" in WFD.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleCustomData |
| Unique Identifier | personId,customDataTypeId |
| Source Pipeline | people (CDC) |
| Scrubbing | DO NOT LOAD |

## Columns

**Column count:** 5

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| customDataTypeId | INT64 | Data type ID |  |  |
| customText | STRING | Custom data value | PII | BLANK |
| customDataType | STRING | Custom data type | PII | BLANK |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
