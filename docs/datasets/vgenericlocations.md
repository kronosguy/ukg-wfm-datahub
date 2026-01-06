# vGenericLocations

**Group:** Detail Dataset → Org Structure Detail Views

- Generic Locations can be a physical location (Operating Room or Mail Room) or a logistical unit that is not a physical location (Support, Administration, a Home Care Unit). Note: for Simplified Business Structure Customers Only

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vGenericLocations |
| Unique Identifier | id |
| Source Pipeline |  |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| id | INT64 | Unique Identifier for a generic location. |  |  |
| persistentId | STRING | The persistent ID of a generic location. |  |  |
| name | STRING | The short name of a generic location. |  |  |
| fullName | STRING | The full name of a generic location. |  |  |
| orgId | INT64 | The organization id associated with the generic location |  |  |
| orgName | STRING | The organization name associated with the generic location |  |  |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not a generic location is active. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
