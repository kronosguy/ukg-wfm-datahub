# vLkpBusinessStructureAllDesc

**Group:** Detail Dataset → Org Structure Detail Views

A hierarchical business structure that shows the parent/child relationship for each org INTERNAL USE ONLY utilized by several materialized Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLkpBusinessStructureAllDesc |
| Unique Identifier |  |
| Source Pipeline | getBusinessStructure (DR) |

## Columns

**Column count:** 9

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgLevelDiffNumber | INT64 | Difference between Top Most Level of Org and Current Org as defined in location Type Mapping |  |  |
| parentOrgTypeId | INT64 | The orgType Id of the parent |  |  |
| parentOrgTypeName | STRING | The orgType Name of the parent |  |  |
| parentLocationCategory | STRING | The parent location category |  |  |
| parentOrgId | INT64 | The orgId of the parent |  |  |
| orgTypeId | INT64 | The orgType Id |  |  |
| orgTypeName | STRING | The orgType Name |  |  |
| locationCategory | STRING | Category, Department, or Site,   used for Forecasting (Retail) |  |  |
| orgId | INT64 | Self related orgId |  |  |
