# vBusinessStructure

**Group:** Detail Dataset → Org Structure Detail Views

- One Row for every unique path in the business structure, only contains completely end dated(does not have a current version), currently effective, or future(where there is no current version)

NOTE: If new Location Types are added,  the orgBreak% columns need to be mapped in the Admin Panel.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vBusinessStructure |
| Unique Identifier | orgId |
| Source Pipeline | getBusinessStructure (DR) |

## Columns

**Column count:** 86

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgId | INT64 | Primary Key (  Mimics behavior from ORG_IDS_ID in WFAN) DOES NOT contain all previous versions of the org path which are currently active.  - Should be used for all joins to detail fact Views. |  |  |
| parentOrgId | INT64 | Self relation to the orgId of the parent row |  |  |
| parentOrgName | STRING | Name value for parentOrgId |  |  |
| name | STRING | Name of the Org Node as entered in WFD (single value) |  |  |
| fullName | STRING | Full Name of the Org Node as entered in WFD (single value) |  |  |
| description | STRING | Description of the Org Node as entered in WFD (single value) |  |  |
| effectiveDate | DATE | Effective date of the current record (Should not be used for joins) |  |  |
| expirationDate | DATE | Expiration date of the current record (Should not be used for joins) |  |  |
| firstRevision | BOOLEAN | Is this the first revision of this org node. - True/False |  |  |
| lastRevision | BOOLEAN | Is this the last revision of this org node. - True/False |  |  |
| transferable | BOOLEAN | Is this the org node transferable (as configured in WFD). - True/False |  |  |
| orgTypeId | INT64 | Org Type(ID) in the Business Structure that this node is configured. |  |  |
| orgTypeName | STRING | Org Type(Name) in the Business Structure that this node is configured. |  |  |
| orgPathTxt | STRING | Full path in the business structure down to this node. |  |  |
| contextId | INT64 | Unique Identifier for Context |  |  |
| contextName | STRING | Can only be ORG or FORECAST |  |  |
| locationCategory | STRING | Category, Department, or Site,   used for Forecasting (Retail) |  |  |
| orgBreak0 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak1 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak2 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak3 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak4 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak5 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak6 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak7 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak8 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak9 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak10 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak11 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak12 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak13 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak14 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak15 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak16 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak17 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak18 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak19 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak20 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak21 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak22 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak23 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak24 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak25 | STRING | Name of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak0Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak1Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak2Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak3Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak4Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak5Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak6Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak7Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak8Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak9Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak10Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak11Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak12Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak13Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak14Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak15Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak16Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak17Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak18Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak19Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak20Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak21Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak22Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak23Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak24Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| orgBreak25Desc | STRING | Description of Business Structure Location based on Location type mappings in Data Hub configuration. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| addressBreak | STRING | The address associated with a node. |  |  |
| genericJobId | INT64 | A reference to the type of a generic job. |  |  |
| genericJobName | STRING | Generic Job Name |  |  |
| timezoneId | INT64 | The timezone associated with a node. |  |  |
| timezoneBreakName | STRING | The timezone name associated with a node. |  |  |
| currencyId | INT64 | A reference to the explicit currency associated with a node. |  |  |
| currencyBreakName | STRING | Currency name |  |  |
| costCenterId | INT64 | The cost center associated with a node. |  |  |
| persistentId | STRING | The PersistentId of an org map node. |  |  |
| indirectWorkPercent | FLOAT | The indirect work allocation associated with a node. |  |  |
| color | STRING | The color of an org map node. Only job nodes can have a color. |  |  |
| externalId | STRING | The external ID of an org map node. If no value is passed during an update, the previous value remains in effect and is taken from the revision with the most recent effective date. |  |  |
| directWorkPercent | FLOAT | The direct work allocation associated with a node. |  |  |
| costCenterBreakName | STRING | Cost center name |  |  |
| genericLocationId | INT64 | A reference to the type of a generic location. |  |  |
| genericLocationName | STRING | Generic Location Name |  |  |
