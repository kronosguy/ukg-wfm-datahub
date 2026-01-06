# vFiscalCalendar

**Group:** Detail Dataset → Date/Time Detail Views

- Imported Fiscal Calendar (1), must be imported thru the standard process and will only represent the dates imported(caution on joins outside of the date range)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vFiscalCalendar |
| Unique Identifier | date |
| Source Pipeline | This is loaded via uploading a file to Data Hub Director. The fiscal calendar is loaded into DHD and then pushed to the fiscalCalendar view. |

## Columns

**Column count:** 10

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| date | DATE | Date that fiscal calendar date values are assigned to |  |  |
| fsclDayOfYear | INT64 | Fiscal day of year - generally should be 1-365 with day 1 being the first day of the year |  |  |
| fsclMonthOfYearName | STRING | Fiscal Month of year name - Name assigned to a fiscal month |  |  |
| fsclMonthOfYearNbr | INT64 | Fiscal Month of year number - Number assigned to a fiscal month |  |  |
| fsclQtrOfYearName | STRING | Fiscal Quarter of year name - Name assigned to a fiscal quarter |  |  |
| fsclQtrOfYearNbr | INT64 | Fiscal quarter of year number - number assigned to a fiscal quarter |  |  |
| fsclWeekOfYear | INT64 | Fiscal week of year number - generally should be 1-53 |  |  |
| fsclYear | INT64 | Fiscal Year - fiscal year that the date falls in |  |  |
| monthHours | FLOAT64 | Not used |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
