# vEmployeeGroups

**Group:** Detail Dataset → Org Structure Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vEmployeeGroups |
| Unique Identifier | employeeGroupId |
| Source Pipeline | employeeGroups (DR) |

## Columns

**Column count:** 16

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| employeeGroupName | STRING | Employee Grouip Name |  |  |
| employeeGroupId | INT64 | Employee Group ID |  |  |
| locationSetName | STRING | The name of the location set |  |  |
| locationSetId | INT64 | The ID of a location set. |  |  |
| includeAllEnabled | BOOLEAN | A Boolean indicator of whether or not to include all enabled locations. |  |  |
| typeId | INT64 | The type ID of a location set type. |  |  |
| goldData | BOOLEAN | A Boolean indicator of whether or not an org map group is gold data. Org map groups are also known as business structure location sets. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| orgList | RECORD (REPEATED) | Nested list of orgIds |  |  |
| orgId | INT64 | Unique identifier of Primary Business Structure location |  |  |
| orgPathTxt | STRING | Org structure locations concatenated into a string. |  |  |
| allLocations | BOOLEAN | SBS Tenants only - include all locations below this level |  |  |
| locationId | INT64 | SBS Tenants only - The location ID of the org object. |  |  |
| locationName | STRING | SBS Tenants only - The location name of the org object. |  |  |
| locationTypeId | INT64 | SBS Tenants only - The location type ID of the org object. |  |  |
| locationTypeName | STRING | SBS Tenants only - The location type name of the org object. |  |  |
