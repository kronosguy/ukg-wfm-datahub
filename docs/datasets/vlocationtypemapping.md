# vLocationTypeMapping

**Group:** Detail Dataset → Org Structure Detail Views

- Contains the location type mapping data as configure in Configuration Portal

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLocationTypeMapping |
| Unique Identifier | locationTypeId |
| Source Pipeline |  |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| locationTypeId | INT64 | LocationType ID |  |  |
| locationTypeName | STRING | Location Type Name |  |  |
| locationTypeDescription | STRING | Location Type Description |  |  |
| locationTypeCategory | STRING | Location Type Category |  |  |
| locationTypeOrder | INT64 | Location Type Order |  |  |
| mappingId | INT64 | Mapping ID used to define the orgBreaks in vDimBusinessStructure and vKronosDaySummary |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
