# vPeopleExternalIdentifiers

**Group:** Detail Dataset → People Detail Views

- Non-Effective Dated - External ID (EEID Information) - Added with WFD v8  & DH - 7.2.1

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleExternalIdentifiers |
| Unique Identifier | personId,identifierType |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 4

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| identifierType | STRING | External ID type:  PRO_EEID is for Ulti-Pro |  |  |
| identifierValue | STRING | External ID value |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
