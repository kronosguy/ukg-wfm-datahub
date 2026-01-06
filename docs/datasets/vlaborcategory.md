# vLaborCategory

**Group:** Detail Dataset → Org Structure Detail Views

- Distinct list of all Labor Categories and Entries (WFD Configuration).

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborCategory |
| Unique Identifier | laborCategoryId,laborCategoryEntryId |
| Source Pipeline | getLaborCategory (DR) |

## Columns

**Column count:** 10

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| laborCategoryId | INT64 | Unique identifier of a labor category in WFD |  |  |
| laborCategoryQualifier | STRING | The name of a labor category object reference |  |  |
| laborCategoryName | STRING | Labor Category Name |  |  |
| laborCategorySortOrder | INT64 | Labor level sort order  i.e.1 = Labor , 2 = Labor Level 2 ... |  |  |
| laborCategoryEntryId | INT64 | The ID of a labor category entry. |  |  |
| laborCategoryEntryName | STRING | The name of a labor category entry. |  |  |
| laborCategoryEntryDescription | STRING | The description of a labor category entry. |  |  |
| inactive | BOOLEAN | A Boolean indicator of whether or not a labor category is inactive |  |  |
| version | INT64 | The current version of the entity. This is used to ensure that an entity is not updated with stale data. |  |  |
| updateDtm | STRING | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
