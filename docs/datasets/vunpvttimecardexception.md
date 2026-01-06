# vUnpvtTimecardException

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtTimecardException |
| Unique Identifier | partitionDate,personId,orgId |
| Source Pipeline |  |

## Columns

**Column count:** 75

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| veryEarlyInExcCnt | INT64 | Very Early In Count |  |  |
| veryEarlyInExcUnreviewedCnt | INT64 | Very Early In Unreviewd |  |  |
| veryEarlyInExcViolationInHrs | FLOAT64 | Very Early In Violation Hours |  |  |
| veryEarlyInExcOverLimitInHrs | FLOAT64 | Very Early In Overlimit Hours |  |  |
| veryEarlyInExcViolationInCosts | FLOAT64 | Very Early In Violation Cost |  |  |
| earlyInExcCnt | INT64 | Early In Count |  |  |
| earlyInExcUnreviewed_Cnt | INT64 | Early In Unreviewd |  |  |
| earlyInExcViolationInHrs | FLOAT64 | Early In Violation Hours |  |  |
| earlyInExcOverLimitInHrs | FLOAT64 | Early In Overlimit Hours |  |  |
| earlyInExcViolationInCosts | FLOAT64 | Early In Violation Cost |  |  |
| lateInExcCnt | INT64 | Late In Count |  |  |
| lateInExcUnreviewed_Cnt | INT64 | Late In  Unreviewed Count |  |  |
| lateInExcViolationInHrs | FLOAT64 | Late In Violation Hours |  |  |
| lateInExcOverLimitInHrs | FLOAT64 | Late Over Limit Hours |  |  |
| earlyOutExcCnt | INT64 | Early Out Count |  |  |
| earlyOutExcUnreviewed_Cnt | INT64 | Early Out Unreviewd Count |  |  |
| earlyOutExcViolationInHrs | FLOAT64 | Early Out Violation Hours |  |  |
| earlyOutExcOverLimitInHrs | FLOAT64 | Early Out Overlimit Hours |  |  |
| lateOutExcCnt | INT64 | Late Out Count |  |  |
| lateOutExcUnreviewed_Cnt | INT64 | Late Out Unreviewd Count |  |  |
| lateOutExcViolationInHrs | FLOAT64 | Late Out Violation Hours |  |  |
| lateOutExcOverLimitInHrs | FLOAT64 | Late Out Overlimit Hours |  |  |
| lateOutExcViolationInCosts | FLOAT64 | Late Out Violation Costs |  |  |
| veryLateOutExcCnt | INT64 | Very Late In Count |  |  |
| veryLateOutExcUnreviewed_Cnt | INT64 | Very Late In Unreviewd |  |  |
| veryLateOutExcViolationInHrs | FLOAT64 | Very Late In Violation Hours |  |  |
| veryLateOutExcOverLimitInHrs | FLOAT64 | Very Late In Overlimit Hours |  |  |
| veryLateOutExcViolationInCosts | FLOAT64 | Very Late In Violation Cost |  |  |
| shortShiftExcCnt | INT64 | Short Shift Count |  |  |
| shortShiftExcCntUnreviewed_Cnt | INT64 | Short Shift Unreviewd Count |  |  |
| shortShiftExcCntViolationInHrs | FLOAT64 | Short Shift Violation Hours |  |  |
| shortShiftExcCntOverLimitInHrs | FLOAT64 | Shor Shift Overlimit Hours |  |  |
| longShiftExcCnt | INT64 | Long Shift Count |  |  |
| longShiftExcCntUnreviewed_Cnt | INT64 | Long Shift Unreviewd Count |  |  |
| longShiftExcCntViolationInHrs | FLOAT64 | Long Shift Violation Hours |  |  |
| longShiftExcCntOverLimitInHrs | FLOAT64 | Long Shift Overlimit Hours |  |  |
| shorBreakExcCnt | INT64 | Short Break Count |  |  |
| shorBreakExcUnreviewed_Cnt | INT64 | Short Break Unreviewd Count |  |  |
| shorBreakExcViolationInHrs | FLOAT64 | Short Break Violation Hours |  |  |
| shorBreakExcOverLimitInHrs | FLOAT64 | Shor Break Overlimit Hours |  |  |
| shorBreakExcOverLimitInCosts | FLOAT64 | Shor Break Overlimit Cost |  |  |
| shortTotalBreakExcCnt | INT64 | Short Total Break Count |  |  |
| shortTotalBreakExcUnreviewed_Cnt | INT64 | Short Total Break Unreviewd Count |  |  |
| shortTotalBreakExcViolationInHrs | FLOAT64 | Short Total Break Violation Hours |  |  |
| shortTotalBreakExcOverLimitInHrs | FLOAT64 | Shor Total Break Overlimit Hours |  |  |
| shortTotalBreakExcOverLimitInCosts | FLOAT64 | Shor Total Break Overlimit Cost |  |  |
| longBreakExcCnt | INT64 | Long Break Count |  |  |
| longBreakExcCntUnreviewed_Cnt | INT64 | Long Break Unreviewd Count |  |  |
| longBreakExcCntViolationInHrs | FLOAT64 | Long Break Violation Hours |  |  |
| longBreakExcCntOverLimitInHrs | FLOAT64 | Long Break Overlimit Hours |  |  |
| longTotalBreakExcCnt | INT64 | Long Total Break Count |  |  |
| longTotalBreakExcCntUnreviewed_Cnt | INT64 | Long Total Break Unreviewd Count |  |  |
| longTotalBreakExcCntViolationInHrs | FLOAT64 | Long Total Break Violation Hours |  |  |
| longTotalBreakExcCntOverLimitInHrs | FLOAT64 | Long Total Break Overlimit Hours |  |  |
| excusedAbsenceExcCnt | INT64 | Excused Absence Count |  |  |
| excusedAbsenceExcViolationInHrs | FLOAT64 | Excuse Absenc Violation Hours |  |  |
| unexcusedAbsenceExcCnt | INT64 | Unexcused Absence Count |  |  |
| unexcusedAbsenceExcViolationInHrs | FLOAT64 | Unexcused Absence Violation Hours |  |  |
| unscheduledExcCnt | INT64 | Unscheduled Unreviewed Count |  |  |
| unscheduledExcUnreviewed_Cnt | INT64 | Unscheduled Count |  |  |
| missedOutPunchExcCnt | INT64 | Missed Out Punch Count |  |  |
| missedInPunchExcCnt | INT64 | Missed In Punch Count |  |  |
| bonusAppliedExcCnt | INT64 | Bonus Applied Count |  |  |
| bonusAppliedExcUnreviewed_Cnt | INT64 | Bonus Applied Unreviewd Count |  |  |
| cancelledDeductionExcCnt | INT64 | Cancelled Deduction Count |  |  |
| holidayScheduleViolationExcCnt | INT64 | Holidaty Schedule Violation Count |  |  |
| breakOutSequenceExcCnt | INT64 | Break Out Sequenct Count |  |  |
| breakOutSequenceExcUnreviewed_Cnt | INT64 | Break Out Sequenct Unreviewd Count |  |  |
| minimumDaysEmployedViolationExcCnt | INT64 | Minimun Days Employed Violation Count |  |  |
| minimumDaysActiveViolationExcCnt | INT64 | Minimun Days Active Violation Count |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| currencyExchangeRates | STRING | a string value that contains the available currency and exchange rate needed for calculations |  |  |
