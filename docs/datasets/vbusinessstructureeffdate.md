# vBusinessStructureEffDate

**Group:** Detail Dataset → Org Structure Detail Views

Effective Dated Business Structure view

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vBusinessStructureEffDate |
| Unique Identifier | orgId,effectiveDate |
| Source Pipeline | getBusinessStructure (DR) |

## Columns

**Column count:** 12

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgId | INT64 | Primary Key (  Mimics behavior from ORG_IDS_ID in WFAN) DOES NOT contain all previous versions of the org path which are currently active.  - Should be used for all joins to detail fact Views. |  |  |
| parentOrgId | INT64 | Self relation to the orgId of the parent row |  |  |
| parentOrgName | STRING | Name value for parentOrgId |  |  |
| name | STRING | Name of the Org Node as entered in WFD (single value) |  |  |
| fullName | STRING | Full Name of the Org Node as entered in WFD (single value) |  |  |
| description | STRING | Description of the Org Node as entered in WFD (single value) |  |  |
| effectiveDate | DATE | Effective date of the current record (Should not be used for joins to prevent duplicates use filter like parttionDate >= effectiveDate and parttionDate < expirationDate) |  |  |
| expirationDate | DATE | Expiration date of the current record (Should not be used for joins to prevent duplicates use filter like parttionDate >= effectiveDate and parttionDate < expirationDate) |  |  |
| orgPathTxt | STRING | Full path in the business structure down to this node. |  |  |
| locationCategory | STRING | Category, Department, or Site,   used for Forecasting (Retail) |  |  |
| orgTypeName | STRING | Org Type(Name) in the Business Structure that this node is configured. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
