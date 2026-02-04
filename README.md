# UKG Pro WFM Data Hub & BigQuery Reporting Guide

> **Status**: ACTIVE // **Owner**: KRONOS_GUY // **Ecosystem**: BigQuery + UKG Pro WFM

This repository serves as the definitive guide for engineers and analysts architecting a data warehouse solution for UKG Pro WFM (formerly Dimensions). It covers the critical "gotchas" of the Data Hub schema, proven join patterns, and how to turn raw API dumps into actionable workforce intelligence.

---

## 🏗️ 1. Core Architecture & Domains

The Data Hub schema is **highly normalized**, which is great for storage but painful for reporting if you don't understand the "Grain".

### The "Big 4" Domains

| Domain | Primary Key (Grain) | Use Case | BQ Partition Strat |
| :--- | :--- | :--- | :--- |
| **PUNCHES** | `punch_id` | Time & Attendance accuracy, missing punches, overtime risk. | `partition by DATE(punch_dt)` |
| **SCHEDULES** | `shift_segment_id` | Planned vs Actual, coverage gaps, adherence. | `partition by DATE(start_dt)` |
| **PERSONS** | `person_id` (SCD Type 2*) | Employee demographics, home org, active status. | `partition by ingestion_date` |
| **JOBS** | `job_id` | Job titles, pay codes, labor categories. | Snapshot (Slow Changing) |

> **⚠️ WARNING**: `person_id` is NOT unique over time if you are handling history! The API often returns snapshots. In BigQuery, always `QUALIFY ROW_NUMBER() OVER (PARTITION BY person_id ORDER BY effective_date DESC) = 1` to get the *current* state, unless doing point-in-time reporting.


---

## 🚦 Phase 0: The "Wish I Knew" List

> **"DataHub unlocks powerful analytics, but it isn’t real‑time."**

Before you write a single line of SQL, internalize these 6 lessons from real-world implementations:

1.  **Expect Latency**: ~4h within UKG + downstream landing = **5–6h delay** to your warehouse.
2.  **CDC ≠ Everything**: Attendance/Setup data (Business Structure, Pay Rules) are often **Full Loads**. Treat them as snapshots.
3.  **Windows Matter**: Default is 30 days back / 7 days forward. Modifying this impacts volume, cost, and runtime aggressively.
4.  **Follow the Masterbook**: The Data Dictionary is your absolute source of truth for pipelines and keys.
5.  **Sequence or Suffer**: Refresh pipelines in the dependency order (Setup -> Person -> Transaction) to avoid referential breaks.
6.  **Know your GCP**: *Enterprise* = You own the GCP project. *Premium* = UKG owns it. This dictates your access level.

---

## 🔗 2. The Golden Join Rules

Joining UKG data incorrectly leads to **fan-out** (duplicate hours) or **data loss**.

### Rule #1: The Worked vs. Home Org Dilemma
*   **Home Org**: Where the employee *belongs* (HR hierarchy). Found in `PERSON_JOB_ASSIGNMENT`.
*   **Worked Org**: Where the shift *occurred*. Found in `PUNCH_DTL` or `SCHEDULE_SEGMENT`.

**SQL Pattern for Labor Costing:**
```sql
SELECT
  p.person_number,
  -- If transfer exists, use it. Else fall back to home job.
  COALESCE(punch.transfer_job_id, assign.primary_job_id) as cost_job_id,
  punch.duration_hours
FROM \`ukg_raw.punches\` punch
LEFT JOIN \`ukg_raw.person_assignment\` assign
  ON punch.person_id = assign.person_id
  AND punch.apply_date BETWEEN assign.eff_start AND assign.eff_end
```

### Rule #2: One Shift, Many Segments
A single "Shift" (e.g., 9am - 5pm) is often split into multiple rows in `SCHEDULE_SEGMENT` due to:
1.  Transfers (9-12 in Dept A, 1-5 in Dept B)
2.  Breaks
3.  Pay Code changes

**Aggregation Key:**
Always aggregate by `full_shift_id` if you just want "Shift Counts", but stick to `segment_id` for "Hours Calculations".

---

## ⚡ 3. Troubleshooting Common Issues

### "My hours don't match the Timecard"
1.  **Check for Historical Corrections**: UKG allows retro-edits. Did your ETL capture the *update* or just the insert?
    *   *Fix*: Implement a `merge` strategy in BigQuery using `last_modified_timestamp`.
2.  **UTC vs Local Time**: Data Hub exports in UTC.
    *   *Fix*: Always convert using the `location_timezone` table before summing hours for a "Tuesday" report.

### "Duplicate Person Rows"
*   **Cause**: Employee changed jobs mid-pay-period.
*   **Fix**: You must handle Slowly Changing Dimensions (SCD). Join on `person_id` AND `date between effective_start and effective_end`.

---

## 🛡️ 4. Best Practices: "Good Data Leads Data"

1.  **Never trust `null`**: UKG often emits explicit nulls for "no change". Coalesce heavily.
2.  **Validate Totals**: Build a "Control Tower" view that compares `SUM(daily_hours)` from your BQ warehouse against the `payroll_summary_api` every morning.
    *   *Alert Threshold*: > 0.1% variance = STOP THE PIPELINE.
3.  **Tags are life**: Use the `comment_codes` array in punches to identify "System Generated" vs "Manager Edited" punches. This detects edited timecards.

---
**Maintained by**: @KronosGuy
