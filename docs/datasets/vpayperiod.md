# vPayPeriod

**Group:** Detail Dataset → Pay Code/Period Detail Views

This view/view only contains information for the current pay period - dimPayPeriod in the summary dataset is a better source for reporting by pay period.

- payperiod  (like current, next, last etc)  spans for each payruleid

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPayPeriod |
| Unique Identifier | payRuleId,periodType |
| Source Pipeline | getPayPeriod (DR) |

## Columns

**Column count:** 21

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| payRuleId | INT64 | Unique identifier of the pay rule that the pay period is associated with. |  |  |
| periodType | STRING | Pay period type i.e. Current, Previous or Next |  |  |
| payPeriodType | STRING | Pay period configuration type Days, Hours, etc. |  |  |
| spanStartDate | DATE | Span start date |  |  |
| spanStartDateTime | TIMESTAMP | Span start date time |  |  |
| spanEndDate | DATE | Span end date |  |  |
| spanEndDateTime | TIMESTAMP | Span end date time |  |  |
| spanDurationZeroSw | BOOLEAN | Boolean indicate of whether or not the span duration is zero |  |  |
| spanDurationNegativeSw | BOOLEAN | Boolean indicate of whether or not the span duration is negative |  |  |
| spanDurationUnits | STRING | Span duration unit types |  |  |
| spanDurationNano | INT64 | Span duration in nano seconds |  |  |
| spanDurationSeconds | INT64 | Span duration in seconds |  |  |
| spanPeriodNegativeSw | BOOLEAN | Boolean indicate of whether or not the span period is negative |  |  |
| spanPeriodZeroSw | BOOLEAN | Boolean indicate of whether or not the span period is zero |  |  |
| spanPeriodUnits | STRING | Span period unit type i.e. YEARS,MONTHS,DAYS |  |  |
| spanPeriodChronologyId | STRING | Span period chronology id |  |  |
| spanPeriodChronologyCalendarType | STRING | Span period chronology calender type i.e. iso8601 |  |  |
| spanPeriodDays | INT64 | Number of days in span period |  |  |
| spanPeriodMonths | INT64 | Number of months in span period |  |  |
| spanPeriodYears | INT64 | Number of years in span period |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
