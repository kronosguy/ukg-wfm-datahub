# vDimBusinessStructure

**Group:** Summary Dataset → Dimension Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vDimBusinessStructure |
| Unique Identifier | Bus_orgId |
| Source Pipeline | getBusinessStructure (DR) |

## Columns

**Column count:** 65

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| Bus_orgId | INT64 | Primary Key (  Mimics behavior from ORG_IDS_ID in WFAN) DOES NOT contain all previous versions of the org path which are currently active.  - Should be used for all joins to detail fact Views. |  |  |
| Bus_orgName | STRING | Name of the Org Node as entered in WFD (single value) |  |  |
| Bus_orgFullName | STRING | Full Name of the Org Node as entered in WFD (single value) |  |  |
| Bus_orgDescription | STRING | Description of the Org Node as entered in WFD (single value) |  |  |
| Bus_orgEffectiveDate | DATE | Effective date of the current record (Should not be used for joins) |  |  |
| Bus_orgExpirationDate | DATE | Expiration date of the current record (Should not be used for joins) |  |  |
| Bus_orgTypeId | INT64 | Org Type(ID) in the Business Structure that this node is configured. |  |  |
| Bus_orgTypeName | STRING | Org Type(Name) in the Business Structure that this node is configured. |  |  |
| Bus_orgPathTxt | STRING | Full path in the business structure down to this node. |  |  |
| Bus_orgContextName | STRING | Can only be ORG or FORECAST |  |  |
| Bus_orgLocationCategory | STRING | Category, Department, or Site,   used for Forecasting (Retail) |  |  |
| Bus_orgBreak0 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration.  This is ALWAYS the CATEGORY level of the business structure (For Volume Only) |  |  |
| Bus_orgBreak1 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration.  This is ALWAYS the JOB level of the business structure |  |  |
| Bus_orgBreak2 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak3 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak4 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak5 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak6 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak7 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak8 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak9 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak10 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak11 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak12 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak13 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak14 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak15 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak16 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak17 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak18 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak19 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak20 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak21 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak22 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak23 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak24 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak25 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak0Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration.  This is ALWAYS the CATEGORY level of the business structure (For Volume Only) |  |  |
| Bus_orgBreak1Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration.  This is ALWAYS the JOB level of the business structure |  |  |
| Bus_orgBreak2Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak3Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak4Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak5Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak6Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak7Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak8Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak9Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak10Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak11Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak12Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak13Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak14Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak15Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak16Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak17Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak18Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak19Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak20Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak21Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak22Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak23Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak24Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_orgBreak25Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| Bus_directWorkPercent | INT64 | Percentage of Work Hours considered to be direct.  Can be found in Dimensions Business Structure at the Job level called Direct Work Allocation |  |  |
| Bus_indirectWorkPercent | INT64 | Percentage of Work Hours considered to be indirect.  Can be found in Dimensions Business Structure at the Job level called Indirect Work Allocation |  |  |
