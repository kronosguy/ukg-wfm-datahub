# vLaborCategories

**Group:** Detail Dataset → Org Structure Detail Views

- Distinct list of all Labor Categories (WFD Configuration).

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborCategories |
| Unique Identifier | laborCategoryId |
| Source Pipeline | laborCategories (DR) |

## Columns

**Column count:** 10

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| laborCategoryId | INT64 | Unique identifier of a labor category in WFD |  |  |
| laborCategorySortOrder | INT64 | Labor level sort order  i.e.1 = Labor , 2 = Labor Level 2 ... |  |  |
| laborCategoryName | STRING | Labor Category Name |  |  |
| laborCategoryAbbrev | STRING | Labor Category Abbreviation |  |  |
| minNameLength | INT64 | Minimum name length |  |  |
| maxNameLength | INT64 | Maximum name length |  |  |
| version | INT64 | The current version of the entity. This is used to ensure that an entity is not updated with stale data. |  |  |
| inactive | BOOLEAN | A Boolean indicator of whether or not a labor category is inactive |  |  |
| persistentId | STRING | Persistent ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
