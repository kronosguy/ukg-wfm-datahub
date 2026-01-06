# vLaborStandardTask

**Group:** Detail Dataset → Forecasting Detail Views

Labor Standards Task

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborStandardTask |
| Unique Identifier | taskId,laborStandardId |
| Source Pipeline | laborStandardTask (DR) |

## Columns

**Column count:** 21

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| taskId | INT64 | The ID of a labor task. |  |  |
| taskName | STRING | The name of a labor task |  |  |
| taskDescription | STRING | The description of a labor task. |  |  |
| effectiveDate | DATE | The effective start date |  |  |
| expirationDate | DATE | The effective end date |  |  |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not a labor task is active. |  |  |
| version | INT64 | The version of a labor task to allow support for optimistic locking. |  |  |
| genericDepartmentId | INT64 | Generic Department ID |  |  |
| genericDepartmentName | STRING | Generic Department Name |  |  |
| siteId | INT64 | Site ID associated with the Labor Standard |  |  |
| sitePathTxt | STRING | Site Name associated with the Labor Standard |  |  |
| siteEffectiveDate | DATE | The effective date of site |  |  |
| storeSpecificSwt | BOOLEAN | A Boolean indicator of whether or not a labor task is store-specific. |  |  |
| combinedLaborDistributionId | INT64 | Combined Labor Distribution ID |  |  |
| combinedLaborDistributionName | STRING | Combined Labor Distribution Name |  |  |
| timeDependentSwt | BOOLEAN | A Boolean indicator of whether or not a effective labor task is time-dependent. |  |  |
| allocateExtraLaborBeforeTrafficSwt | BOOLEAN | A Boolean indicator of whether or not to allocate extra labor before traffic. (true) before traffic starts, then after traffic ends (false) after traffic ends, then before traffic starts |  |  |
| selectedForCombinedDistributionSwt | BOOLEAN | A Boolean indicator of whether or not a labor standard is included in a combined distribution. |  |  |
| laborStandardId | INT64 | The ID of an effective labor standard version. |  |  |
| laborStandardName | STRING | The name of an effective labor standard version. |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted or updated in Data Hub - BigQuery |  |  |
