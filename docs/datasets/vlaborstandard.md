# vLaborStandard

**Group:** Detail Dataset → Forecasting Detail Views

Labor Standards Setup Configuration

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborStandard |
| Unique Identifier | laborStandardId |
| Source Pipeline | laborStandard (DR) |

## Columns

**Column count:** 12

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| laborStandardId | INT64 | The ID of an effective labor standard version. |  |  |
| laborStandardName | STRING | The name of an effective labor standard version. |  |  |
| laborStandardDescription | STRING | The description of a labor standard. |  |  |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not a labor standard is active. |  |  |
| version | INT64 | The version of a labor standard. |  |  |
| genericDepartmentId | INT64 | Generic Department ID |  |  |
| genericDepartmentName | STRING | Generic Department Name |  |  |
| siteId | INT64 | Site ID associated with the Labor Standard |  |  |
| sitePathTxt | STRING | Site Name associated with the Labor Standard |  |  |
| siteEffectiveDate | DATE | The effective date of site |  |  |
| storeSpecificSwt | BOOLEAN | A Boolean indicator of whether or not a labor task is store-specific. |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted or updated in Data Hub - BigQuery |  |  |
